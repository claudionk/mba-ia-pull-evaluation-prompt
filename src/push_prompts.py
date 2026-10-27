"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

DICAS DE IMPLEMENTAÇÃO:

- O push é feito pelo cliente do LangSmith:

      from langsmith import Client
      from langchain_core.prompts import ChatPromptTemplate

      client = Client()
      prompt = ChatPromptTemplate.from_messages([
          ("system", system_prompt),
          ("user", user_prompt),
      ])
      url = client.push_prompt(
          f"{username}/bug_to_user_story_v2",
          object=prompt,
          is_public=True,
          description="...",
          tags=[...],
      )

- `username` vem de USERNAME_LANGSMITH_HUB no .env e precisa ser o seu handle
  do Hub. Se você ainda não tem um handle, veja as instruções no .env.example.

- A variável do template precisa ser {bug_report}, que é a chave de entrada
  usada no dataset de avaliação.

- Use `load_yaml` de utils.py para ler o arquivo .yml.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header, validate_prompt_structure

load_dotenv()

# Fix para problemas de encoding no Windows, que podem gerar erros de UnicodeEncodeError
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
        

def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt.

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    is_valid, errors = validate_prompt_structure(prompt_data)

    user_prompt = prompt_data.get("user_prompt", "")
    if "{bug_report}" not in user_prompt and "{bug_report}" not in prompt_data.get("system_prompt", ""):
        errors.append("Variável de template '{bug_report}' não encontrada no prompt")
        is_valid = False

    return is_valid, errors


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt (ex: handle/bug_to_user_story_v2)
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        print(f"Fazendo push do prompt '{prompt_name}' para o LangSmith Hub...")
        client = Client()

        prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_data["system_prompt"]),
            ("user", prompt_data["user_prompt"]),
        ])

        description = prompt_data.get("description", "Prompt otimizado para Bug to User Story")
        tags = prompt_data.get("tags", [])

        url = client.push_prompt(
            prompt_name,
            object=prompt,
            is_public=True,
            description=description,
            tags=tags,
        )

        print("✓ Prompt publicado com sucesso no LangSmith Hub!")
        print(f"  URL: {url}")
        return True

    except Exception as e:
        print(f"❌ Erro ao fazer push do prompt: {e}")
        return False


def main():
    """Função principal"""
    print_section_header("PUSH DO PROMPT OTIMIZADO PARA O LANGSMITH HUB")

    required_vars = ["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]
    if not check_env_vars(required_vars):
        return 1

    prompt_file = "prompts/bug_to_user_story_v2.yml"
    data = load_yaml(prompt_file)
    if not data:
        print(f"❌ Não foi possível carregar {prompt_file}")
        return 1

    prompt_key = "bug_to_user_story_v2"
    prompt_data = data.get(prompt_key, data)

    print(f"Validando estrutura de '{prompt_key}'...")
    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print("❌ Validação do prompt falhou com os seguintes erros:")
        for err in errors:
            print(f"   - {err}")
        return 1
    print("✓ Estrutura do prompt validada com sucesso!")

    username = os.getenv("USERNAME_LANGSMITH_HUB", "").strip()
    prompt_name = f"{username}/bug_to_user_story_v2"

    success = push_prompt_to_langsmith(prompt_name, prompt_data)
    if success:
        print("\nPróximos passos:")
        print("1. Valide os testes: pytest tests/test_prompts.py")
        print("2. Execute a avaliação: python src/evaluate.py")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
