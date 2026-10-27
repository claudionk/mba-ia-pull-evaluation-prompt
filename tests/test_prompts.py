"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"


def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestPrompts:
    @pytest.fixture
    def prompt_data(self):
        """Carrega e retorna os dados do prompt v2."""
        data = load_prompts(str(PROMPT_FILE))
        assert "bug_to_user_story_v2" in data, "Chave 'bug_to_user_story_v2' não encontrada no YAML"
        return data["bug_to_user_story_v2"]

    def test_prompt_has_system_prompt(self, prompt_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "system_prompt" in prompt_data, "Campo 'system_prompt' não encontrado"
        system_prompt = prompt_data.get("system_prompt", "").strip()
        assert len(system_prompt) > 0, "system_prompt está vazio"

    def test_prompt_has_role_definition(self, prompt_data):
        """Verifica se o prompt define uma persona (ex: 'Você é um Product Manager')."""
        system_prompt = prompt_data.get("system_prompt", "").lower()
        role_keywords = ["você é", "product manager", "tech lead", "persona", "especialista"]
        assert any(keyword in system_prompt for keyword in role_keywords), (
            "system_prompt deve definir uma persona clara (ex: Product Manager/Tech Lead)"
        )

    def test_prompt_mentions_format(self, prompt_data):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        system_prompt = prompt_data.get("system_prompt", "")
        has_user_story_format = "como" in system_prompt.lower() and "quero" in system_prompt.lower()
        has_acceptance_criteria = "critérios de aceitação" in system_prompt.lower() or "critérios" in system_prompt.lower()
        has_markdown = "markdown" in system_prompt.lower() or "---" in system_prompt or "#" in system_prompt

        assert (has_user_story_format or has_acceptance_criteria) and has_markdown, (
            "Prompt deve mencionar ou estruturar formato Markdown e formato padrão de User Story"
        )

    def test_prompt_has_few_shot_examples(self, prompt_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        system_prompt = prompt_data.get("system_prompt", "")
        has_examples = "exemplo" in system_prompt.lower() or "few-shot" in system_prompt.lower()
        has_sample_cases = "relato" in system_prompt.lower() and "critérios de aceitação" in system_prompt.lower()
        assert has_examples and has_sample_cases, (
            "system_prompt deve conter exemplos claros de entrada/saída (Few-shot)"
        )

    def test_prompt_no_todos(self, prompt_data):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        system_prompt = prompt_data.get("system_prompt", "")
        user_prompt = prompt_data.get("user_prompt", "")
        description = prompt_data.get("description", "")

        assert "[TODO]" not in system_prompt, "system_prompt contém [TODO]"
        assert "TODO" not in system_prompt, "system_prompt contém TODO"
        assert "[TODO]" not in user_prompt, "user_prompt contém [TODO]"
        assert "[TODO]" not in description, "description contém [TODO]"

    def test_minimum_techniques(self, prompt_data):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        assert "techniques_applied" in prompt_data, "Campo 'techniques_applied' não encontrado nos metadados"
        techniques = prompt_data.get("techniques_applied", [])
        assert isinstance(techniques, list), "'techniques_applied' deve ser uma lista"
        assert len(techniques) >= 2, f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}"


@pytest.mark.parametrize(
    ("model_name", "expected_temperature"),
    [
        ("gpt-6.1-terra", 1),
        ("gpt-5", 1),
        ("o3-mini", 1),
        ("gpt-4o", 0),
    ],
)
def test_openai_model_temperature_compatibility(monkeypatch, model_name, expected_temperature):
    """Usa a temperatura padrão nos modelos OpenAI que não aceitam customização."""
    from utils import get_llm

    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    llm = get_llm(model=model_name, temperature=0)

    assert llm.temperature == expected_temperature


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
