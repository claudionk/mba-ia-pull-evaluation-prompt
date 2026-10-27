"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull do prompt semente do desafio
3. Salva localmente em prompts/bug_to_user_story_v1.yml

DICAS DE IMPLEMENTAÇÃO:

- O pull é feito pelo cliente do LangSmith:

      from langsmith import Client
      client = Client()
      prompt = client.pull_prompt(
          "leonanluppi/bug_to_user_story_v1",
          dangerously_pull_public_prompt=True,
      )

- O parâmetro `dangerously_pull_public_prompt=True` é obrigatório sempre que o
  identificador tem dono explícito ("owner/nome"). O LangSmith bloqueia esse pull
  por padrão porque um prompt do Hub é um objeto LangChain serializado, que pode
  vir de terceiros. Aqui o prompt é o do desafio, então o risco é conhecido.

- O retorno é um ChatPromptTemplate. Para extrair o conteúdo das mensagens,
  use a serialização nativa do LangChain (`prompt.messages`, e o atributo
  `.prompt.template` de cada mensagem).

- Use `save_yaml` de utils.py para gravar o resultado no arquivo .yml.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

# Garantir encoding UTF-8 no stdout/stderr no Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def extract_template(message) -> str:
    """Extrai o template textual de uma mensagem de prompt do LangChain."""
    if hasattr(message, "prompt") and hasattr(message.prompt, "template"):
        return message.prompt.template
    if hasattr(message, "content"):
        return message.content
    return str(message)


def pull_prompts_from_langsmith() -> bool:
    """
    Conecta ao LangSmith, puxa o prompt leonanluppi/bug_to_user_story_v1
    e salva em prompts/bug_to_user_story_v1.yml.
    """
    print_section_header("PULL DO PROMPT SEMENTE DO LANGSMITH")

    required_vars = ["LANGSMITH_API_KEY"]
    if not check_env_vars(required_vars):
        return False

    seed_prompt_name = "leonanluppi/bug_to_user_story_v1"
    output_path = "prompts/bug_to_user_story_v1.yml"

    try:
        print(f"Puxando prompt '{seed_prompt_name}' do LangSmith Hub...")
        client = Client()
        prompt = client.pull_prompt(seed_prompt_name, dangerously_pull_public_prompt=True)
        print("✓ Prompt obtido com sucesso do LangSmith Hub!")

        system_prompt = ""
        user_prompt = ""

        for message in prompt.messages:
            template_text = extract_template(message)
            class_name = message.__class__.__name__.lower()
            msg_type = getattr(message, "type", "").lower()

            if "system" in class_name or "system" in msg_type:
                system_prompt = template_text
            elif "human" in class_name or "user" in class_name:
                user_prompt = template_text
            elif not system_prompt:
                system_prompt = template_text
            else:
                user_prompt = template_text

        prompt_data = {
            "bug_to_user_story_v1": {
                "description": "Prompt para converter relatos de bugs em User Stories",
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "version": "v1",
                "created_at": "2025-01-15",
                "tags": ["bug-analysis", "user-story", "product-management"],
            }
        }

        print(f"Salvando prompt em {output_path}...")
        success = save_yaml(prompt_data, output_path)
        if success:
            print(f"✓ Prompt salvo com sucesso em {output_path}")
            return True
        else:
            print(f"❌ Falha ao salvar prompt em {output_path}")
            return False

    except Exception as e:
        print(f"❌ Erro ao fazer pull do prompt: {e}")
        return False


def main():
    """Função principal"""
    success = pull_prompts_from_langsmith()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
