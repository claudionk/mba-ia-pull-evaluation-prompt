# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Desafio de otimização de prompts e engenharia de avaliação automatizada utilizando **LangChain**, **LangSmith Prompt Hub** e **LLM-as-a-Judge**.

---

## 🏆 Resultados Finais (Resumo Executivo)

O prompt otimizado (`claudionk/bug_to_user_story_v2`) foi aprovado com sucesso em **todas as 5 métricas** estabelecidas (critério mínimo: ≥ 0.80):

| Métrica | Tipo | Score Atingido | Status |
| :--- | :--- | :---: | :---: |
| **Helpfulness** | Derivada `(Clarity + Precision) / 2` | **0.88** | ✅ APROVADO |
| **Correctness** | Derivada `(F1 + Precision) / 2` | **0.84** | ✅ APROVADO |
| **F1-Score** | Base (Equilíbrio Precision & Recall) | **0.82** | ✅ APROVADO |
| **Clarity** | Base (Organização BDD, Ausência de Ambiguidade) | **0.89** | ✅ APROVADO |
| **Precision** | Base (Informações Relevantes e Sem Alucinação) | **0.86** | ✅ APROVADO |
| **MÉDIA GERAL** | Média de todas as métricas | **0.8603** | ✅ **APROVADO** |

### 🔗 Evidências e Links no LangSmith

- **Link Público do Dataset de Avaliação (com experimentos e tracing):**  
  👉 [https://smith.langchain.com/public/b9911643-d302-4236-9936-fda4333b445e/d](https://smith.langchain.com/public/b9911643-d302-4236-9936-fda4333b445e/d)
- **Prompt Hub v2 (Público):**  
  👉 [https://smith.langchain.com/prompts/bug_to_user_story_v2/d63a8154?organizationId=421288ba-dd93-442d-aa13-991973eb3c50](https://smith.langchain.com/prompts/bug_to_user_story_v2/d63a8154?organizationId=421288ba-dd93-442d-aa13-991973eb3c50)
- **Experimento de Avaliação no Workspace:**  
  👉 [Experimento v2 no LangSmith](https://smith.langchain.com/o/421288ba-dd93-442d-aa13-991973eb3c50/datasets/3153f039-8cd7-4347-9bf0-34685bba3817/compare?selectedSessions=d7a3762d-89f0-4f1e-8e6f-3f8c72d40371)

---

## 🧠 Técnicas Aplicadas (Fase 2)

Para elevar a qualidade do prompt semente de baixa qualidade (`bug_to_user_story_v1`) até o nível de aprovação superior a 80%, foram aplicadas três técnicas avançadas de Prompt Engineering:

### 1. Role Prompting (Definição de Persona)
- **Como foi aplicado:** O modelo foi posicionado como um *Product Manager Sênior e Tech Lead especializado em metodologias ágeis e engenharia de software com mais de 10 anos de experiência*.
- **Justificativa:** Sem persona definida, o modelo gera descrições genéricas que misturam jargões de suporte com especificação técnica inconsistente. Com o papel de PM Sênior, o modelo adota o tom adequado de negócio, foca no valor para o usuário e estrutura critérios de aceitação rigorosos.

### 2. Few-shot Learning (Aprendizado por Exemplos Calibrados)
- **Como foi aplicado:** Foram incluídos 4 exemplos completos de entrada e saída cobrindo:
  - **Bug Simples (UI/UX):** Focado puramente na User Story e critérios objetivos em formato BDD (*Dado que / Quando / Então / E*).
  - **Bug Simples (Validação):** Focado em regras de formulário e mensagens de erro ao usuário.
  - **Bug Médio (Performance e Integração):** Inclui a seção `Contexto Técnico:` detalhando causas de lentidão e sugestão de correção.
  - **Bug Complexo (Múltiplos Problemas):** Divisão arquitetural em `=== USER STORY PRINCIPAL ===`, `=== CRITÉRIOS DE ACEITAÇÃO ===`, `=== CRITÉRIOS TÉCNICOS ===`, `=== CONTEXTO DO BUG ===` e `=== TASKS TÉCNICAS SUGERIDAS ===`.
- **Justificativa:** É a técnica mais determinante para o alinhamento com o *ground truth*. Permitiu ensinar o modelo a calibrar a extensão e complexidade da resposta de acordo com o tamanho do bug relatado.

### 3. Chain of Thought (CoT - Raciocínio Passo a Passo Guiado)
- **Como foi aplicado:** No `user_prompt`, instruiu-se o modelo a executar uma reflexão guiada antes da geração:
  1. Identificar o perfil exato do usuário/sistema impactado;
  2. Classificar a complexidade do relato (simples, médio ou complexo);
  3. Formular os critérios de aceitação em BDD (*Dado que / Quando / Então / E*);
  4. Adicionar seções técnicas apenas quando pertinentes.
- **Justificativa:** Garante alta precisão e coerência lógica, evitando que o modelo invente informações inexistentes (*alucinações*) ou omita detalhes cruciais presentes nos logs.

---

## 📊 Comparação: Prompt Original (v1) vs Prompt Otimizado (v2)

| Aspecto | Prompt Original (`v1`) | Prompt Otimizado (`v2`) | Impacto |
| :--- | :--- | :--- | :--- |
| **Persona** | Assistente genérico ("Você é um assistente...") | Product Manager Sênior & Tech Lead com 10 anos de exp. | Elevação imediata de tom profissional e empatia |
| **Formato de Saída** | Vago, sem estrutura definida | Padrão ágil BDD (*Como / Quero / Para* + *Dado / Quando / Então*) | Aumento de **Clarity** para **0.89** |
| **Exemplos (Few-shot)** | Nenhum (zero-shot) | 4 exemplos cobrindo bugs simples, médios e complexos | Aumento substancial de **F1-Score** (de ~0.48 para **0.82**) |
| **Calibragem de Escopo** | Não existia | Regras explícitas: bugs simples sem poluição técnica, bugs médios/complexos com contexto técnico | Maximizou a **Precision** (**0.86**) evitando *over-engineering* |
| **Separação System / User** | `{bug_report}` duplicado em ambas mensagens | `{bug_report}` isolado no `user_prompt` com raciocínio guiado | Eliminação de redundâncias e ruído de atenção |

---

## 🚀 Como Executar

### 1. Pré-requisitos
- Python 3.10 ou superior
- Conta no [LangSmith](https://smith.langchain.com/) e chave de API
- Chave de API da OpenAI (ou Google Gemini)

### 2. Configuração do Ambiente

Clone o repositório e acesse o diretório:
```bash
git clone <url-do-fork>
cd mba-ia-pull-evaluation-prompt
```

Crie e ative o ambiente virtual:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Configure o arquivo `.env`:
```bash
cp .env.example .env
```

Preencha as variáveis no `.env`:
```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_...
LANGSMITH_PROJECT=mba-ia-pull-evaluation-prompt
USERNAME_LANGSMITH_HUB=seu_handle_langsmith

LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
EVAL_MODEL=gpt-4o
OPENAI_API_KEY=sk-...
```

### 3. Execução das Etapas

#### Etapa 1: Pull do Prompt Semente (v1)
Puxa o prompt semente público do LangSmith Hub e salva em `prompts/bug_to_user_story_v1.yml`:
```bash
python src/pull_prompts.py
```

#### Etapa 2: Validação com Testes Unitários
Executa a bateria de 6 testes automatizados com `pytest`:
```bash
pytest tests/test_prompts.py -v
```
*Saída esperada:* `6 passed in 0.06s`

#### Etapa 3: Push do Prompt Otimizado (v2)
Publica o prompt v2 no LangSmith Prompt Hub com visibilidade pública:
```bash
python src/push_prompts.py
```

#### Etapa 4: Avaliação Completa das Métricas
Executa o benchmark contra os 15 exemplos do dataset, gravando feedbacks no LangSmith:
```bash
python src/evaluate.py
```

---

## 🧪 Estrutura dos Testes Automatizados

O arquivo `tests/test_prompts.py` valida rigorosamente:
1. `test_prompt_has_system_prompt`: Garante presença e preenchimento de `system_prompt`;
2. `test_prompt_has_role_definition`: Valida a existência de persona definida (Product Manager / Tech Lead);
3. `test_prompt_mentions_format`: Verifica se exige Markdown e padrão de User Story;
4. `test_prompt_has_few_shot_examples`: Confirma a inclusão de exemplos com BDD de entrada e saída;
5. `test_prompt_no_todos`: Garante que não restaram pendências ou marcações `[TODO]`;
6. `test_minimum_techniques`: Valida se pelo menos duas técnicas avançadas foram documentadas nos metadados.

---

## 📁 Estrutura do Projeto

```
mba-ia-pull-evaluation-prompt/
├── .env.example              # Template de configuração
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação completa e relatório final
├── PLAN.md                   # Plano de desenvolvimento arquitetural
│
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt original semente (baixa qualidade)
│   └── bug_to_user_story_v2.yml  # Prompt otimizado (Few-shot, CoT, Role)
│
├── datasets/
│   └── bug_to_user_story.jsonl   # 15 exemplos de bugs para avaliação
│
├── src/
│   ├── pull_prompts.py       # Script de pull do LangSmith Hub
│   ├── push_prompts.py       # Script de push público para o Hub
│   ├── evaluate.py           # Avaliador do experimento no LangSmith
│   ├── metrics.py            # Implementação de métricas LLM-as-a-Judge
│   └── utils.py              # Utilitários de carga de YAML e LLM
│
└── tests/
    └── test_prompts.py       # Testes automatizados com pytest
```
