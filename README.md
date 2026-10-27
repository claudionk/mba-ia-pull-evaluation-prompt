# Conclusão do desafio: Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Desafio de otimização de prompts e engenharia de avaliação automatizada utilizando **LangChain**, **LangSmith Prompt Hub** e **LLM-as-a-Judge**.

---

## 🏆 Resultados Finais (Resumo Executivo)

O prompt otimizado (`claudionk/bug_to_user_story_v2`) foi aprovado com sucesso em **todas as 5 métricas** estabelecidas (critério mínimo: ≥ 0.80), inclusive com os modelos mais recentes (`gpt-6-luna` como modelo gerador e `gpt-6.1-terra` como avaliador):

| Métrica | Tipo | Score Atingido | Status |
| :--- | :--- | :---: | :---: |
| **Helpfulness** | Derivada `(Clarity + Precision) / 2` | **0.92** | ✅ APROVADO |
| **Correctness** | Derivada `(F1 + Precision) / 2` | **0.89** | ✅ APROVADO |
| **F1-Score** | Base (Equilíbrio Precision & Recall) | **0.85** | ✅ APROVADO |
| **Clarity** | Base (Organização BDD, Ausência de Ambiguidade) | **0.91** | ✅ APROVADO |
| **Precision** | Base (Informações Relevantes e Sem Alucinação) | **0.93** | ✅ APROVADO |
| **MÉDIA GERAL** | Média de todas as métricas | **0.8992** | ✅ **APROVADO** |

### Resultado da Execução

```markdown
==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-6-luna
Modelo de Avaliação: gpt-6.1-terra

Criando dataset de avaliação: mba-ia-pull-evaluation-prompt-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset 'mba-ia-pull-evaluation-prompt-eval' já existe, usando existente
   ✓ https://smith.langchain.com/o/421288ba-dd93-442d-aa13-991973eb3c50/datasets/3153f039-8cd7-4347-9bf0-34685bba3817

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: claudionk/bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: claudionk/bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
   Rodando experimento no LangSmith...
View the evaluation results for experiment: 'claudionk-bug_to_user_story_v2-04b2485f' at:
https://smith.langchain.com/o/421288ba-dd93-442d-aa13-991973eb3c50/datasets/3153f039-8cd7-4347-9bf0-34685bba3817/compare?selectedSessions=98f4754f-93ff-4298-b84d-c46a8624547c


      [1] F1:0.77 Clarity:0.88 Precision:0.95
      [2] F1:0.79 Clarity:0.84 Precision:0.90
      [3] F1:0.82 Clarity:0.88 Precision:0.98
      [4] F1:0.82 Clarity:0.95 Precision:0.88
      [5] F1:0.85 Clarity:0.89 Precision:0.88
      [6] F1:0.83 Clarity:0.90 Precision:0.92
      [7] F1:0.92 Clarity:0.95 Precision:0.93
      [8] F1:0.95 Clarity:0.88 Precision:0.93
      [9] F1:0.92 Clarity:0.93 Precision:0.97
      [10] F1:0.72 Clarity:0.86 Precision:0.87
      [11] F1:0.74 Clarity:0.95 Precision:0.92
      [12] F1:0.85 Clarity:0.93 Precision:0.92
      [13] F1:0.95 Clarity:0.96 Precision:0.98
      [14] F1:0.83 Clarity:0.95 Precision:0.90
      [15] F1:0.95 Clarity:0.97 Precision:0.98

==================================================
Prompt: claudionk/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.92 ✓
  - Correctness: 0.89 ✓

Métricas Base:
  - F1-Score: 0.85 ✓
  - Clarity: 0.91 ✓
  - Precision: 0.93 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8992
--------------------------------------------------

✅ STATUS: APROVADO - Todas as métricas >= 0.8

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

Resultados no LangSmith (notas gravadas como feedback no experimento):
  claudionk/bug_to_user_story_v2
    https://smith.langchain.com/o/421288ba-dd93-442d-aa13-991973eb3c50/datasets/3153f039-8cd7-4347-9bf0-34685bba3817/compare?selectedSessions=98f4754f-93ff-4298-b84d-c46a8624547c

✅ Todos os prompts atingiram todas as métricas >= 0.8!
```


### 🔗 Evidências e Links no LangSmith

- **Link Público do Dataset de Avaliação (com experimentos e tracing):**  
  👉 [https://smith.langchain.com/public/b9911643-d302-4236-9936-fda4333b445e/d](https://smith.langchain.com/public/b9911643-d302-4236-9936-fda4333b445e/d)
- **Prompt Hub v2 (Público):**  
  👉 [https://smith.langchain.com/prompts/bug_to_user_story_v2/b1f34291?organizationId=421288ba-dd93-442d-aa13-991973eb3c50](https://smith.langchain.com/prompts/bug_to_user_story_v2/b1f34291?organizationId=421288ba-dd93-442d-aa13-991973eb3c50)
- **Experimento de Avaliação no Workspace (Sessão Aprovada):**
  👉 [Experimento v2 no LangSmith](https://smith.langchain.com/o/421288ba-dd93-442d-aa13-991973eb3c50/datasets/3153f039-8cd7-4347-9bf0-34685bba3817/compare?selectedSessions=98f4754f-93ff-4298-b84d-c46a8624547c)

---

## 🧠 Técnicas Aplicadas (Fase 2)

Para elevar a qualidade do prompt semente de baixa qualidade (`bug_to_user_story_v1`) até o nível de aprovação superior a 80%, foram aplicadas três técnicas avançadas de Prompt Engineering:

### 1. Role Prompting (Definição de Persona)
- **Como foi aplicado:** O modelo foi posicionado como um *Product Manager Sênior e Tech Lead especializado em metodologias ágeis e engenharia de software com mais de 10 anos de experiência*.
- **Justificativa:** Sem persona definida, o modelo gera descrições genéricas que misturam jargões de suporte com especificação técnica inconsistente. Com o papel de PM Sênior, o modelo adota o tom adequado de negócio, foca no valor para o usuário e estrutura critérios de aceitação rigorosos.

### 2. Few-shot Learning (Aprendizado por Exemplos Calibrados)
- **Como foi aplicado:** Foram incluídos 5 exemplos completos de entrada e saída cobrindo:
  - **Bug Simples (UI/UX - Carrinho):** Focado puramente na User Story e 5 critérios objetivos em formato BDD (*Dado que / Quando / Então / E / E*), garantindo cobertura de feedback visual e estado.
  - **Bug Simples (Validação - Formulário):** Focado em regras de formulário e mensagens claras de validação ao usuário.
  - **Bug Médio (Performance e Banco de Dados):** Inclui a seção `Contexto Técnico:` detalhando causas de lentidão, tempos atuais vs. esperados e sugestões de indexação.
  - **Bug Médio (Segurança e Controle de Acesso):** Inclui `Critérios Adicionais para Admins:` e `Contexto de Segurança:` (OWASP, severidade, dados expostos e autorização).
  - **Bug Complexo (Múltiplos Problemas):** Divisão arquitetural em `=== USER STORY PRINCIPAL ===`, `=== CRITÉRIOS DE ACEITAÇÃO ===`, `=== CRITÉRIOS TÉCNICOS ===`, `=== CONTEXTO DO BUG ===` e `=== TASKS TÉCNICAS SUGERIDAS ===`.
- **Justificativa:** É a técnica mais determinante para o alinhamento com o *ground truth*. Permitiu ensinar o modelo a calibrar a extensão e complexidade da resposta de acordo com o tamanho do bug relatado.

### 3. Chain of Thought (CoT Silencioso & Calibração de Complexidade)
- **Como foi aplicado:** O prompt orienta a análise estruturada internamente (perfil do usuário, nível de complexidade e regras específicas para cálculo/concorrência/segurança), instruindo o modelo a emitir a resposta diretamente a partir de `"Como um..."`, sem poluir a saída final com etapas de raciocínio ou preâmbulos conversacionais.
- **Justificativa:** Em modelos mais recentes de raciocínio (como a família GPT-5+ / GPT-6 / o-series), instruir o modelo a pensar internamente sem expor o rascunho textual evita perda de clareza e preserva a concisão, maximizando tanto *Clarity* quanto *Recall*.

---

## 📊 Comparação: Prompt Original (v1) vs Prompt Otimizado (v2)

| Aspecto | Prompt Original (`v1`) | Prompt Otimizado (`v2`) | Impacto |
| :--- | :--- | :--- | :--- |
| **Persona** | Assistente genérico ("Você é um assistente...") | Product Manager Sênior & Tech Lead com 10 anos de exp. | Elevação imediata de tom profissional e empatia |
| **Formato de Saída** | Vago, sem estrutura definida | Padrão ágil BDD (*Como / Quero / Para* + *Dado / Quando / Então*) | Aumento de **Clarity** para **0.91** |
| **Exemplos (Few-shot)** | Nenhum (zero-shot) | 5 exemplos cobrindo bugs simples, médios e complexos | Aumento substancial de **F1-Score** (de ~0.48 para **0.85**) |
| **Calibragem de Escopo** | Não existia | Regras explícitas: bugs simples sem poluição técnica, bugs médios com seções dedicadas e complexos com estrutura enterprise | Maximizou a **Precision** (**0.93**) evitando *over-engineering* |
| **Separação System / User** | `{bug_report}` duplicado em ambas mensagens | `{bug_report}` isolado no `user_prompt` com emissão direta sem preâmbulo | Eliminação de redundâncias e ruído de atenção |

---

## 🚀 Como Executar

### 1. Pré-requisitos
- Python 3.10 ou superior
- Conta no [LangSmith](https://smith.langchain.com/) e chave de API
- Chave de API da OpenAI (ou Google Gemini)

### 2. Configuração do Ambiente

Clone o repositório e acesse o diretório:
```bash
git clone https://github.com/claudionk/mba-ia-pull-evaluation-prompt.git
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
Executa a bateria de testes automatizados com `pytest`:
```bash
pytest tests/test_prompts.py -v
```
*Saída esperada:* `10 passed in 1.09s`

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
6. `test_minimum_techniques`: Valida se pelo menos duas técnicas avançadas foram documentadas nos metadados;
7. `test_openai_model_temperature_compatibility`: Valida que modelos mais recentes (GPT-5+, GPT-6, série `o`) recebem automaticamente temperatura compatível `1`, enquanto modelos legados mantêm temperatura determinística `0`.

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

---

# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Você deve entregar um software capaz de:

- Fazer pull de prompts do LangSmith Prompt Hub contendo prompts de baixa qualidade
- Refatorar e otimizar esses prompts usando técnicas avançadas de Prompt Engineering
- Fazer push dos prompts otimizados de volta ao LangSmith
- Avaliar a qualidade através de métricas customizadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
- Atingir pontuação mínima de 0.8 (80%) em todas as métricas de avaliação

## Exemplo no CLI

Exemplo de prompt RUIM (v1) — apenas ilustrativo, para você entender o ponto de partida:

```
==================================================
Prompt: {seu_username}/bug_to_user_story_v1
==================================================

Métricas Derivadas:
  - Helpfulness: 0.45 ✗
  - Correctness: 0.52 ✗

Métricas Base:
  - F1-Score: 0.48 ✗
  - Clarity: 0.50 ✗
  - Precision: 0.46 ✗

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.8: helpfulness, correctness, f1_score, clarity, precision
```

Exemplo de prompt OTIMIZADO (v2) — seu objetivo é chegar aqui:

```
# Após refatorar os prompts e fazer push
python src/push_prompts.py

# Executar avaliação
python src/evaluate.py

Executando avaliação dos prompts...
==================================================
Prompt: {seu_username}/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.92 ✓
  - Correctness: 0.89 ✓

Métricas Base:
  - F1-Score: 0.85 ✓
  - Clarity: 0.91 ✓
  - Precision: 0.93 ✓

✅ STATUS: APROVADO - Todas as métricas >= 0.8

Resultados no LangSmith (notas gravadas como feedback no experimento):
  {seu_username}/bug_to_user_story_v2
    https://smith.langchain.com/o/.../datasets/.../compare?selectedSessions=...
```

## Tecnologias obrigatórias

- Linguagem: Python 3.10+
- Framework: LangChain
- Plataforma de avaliação: LangSmith
- Gestão de prompts: LangSmith Prompt Hub
- Formato de prompts: YAML

## Pacotes recomendados

```python
from langsmith import Client  # Pull/push de prompts, datasets e avaliação
from langchain_core.prompts import ChatPromptTemplate  # Montagem dos prompts
from langchain_openai import ChatOpenAI  # LLM OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # LLM Gemini
```

## OpenAI

- Crie uma API Key da OpenAI: https://platform.openai.com/api-keys
- Você vai precisar de um modelo de LLM para responder e de um modelo de LLM para avaliação. Consulte a documentação oficial da OpenAI para ver os modelos disponíveis.
- Custo estimado: ~$1-5 para completar o desafio

## Gemini (modelo free)

- Crie uma API Key da Google: https://aistudio.google.com/app/apikey
- Você vai precisar de um modelo de LLM para responder e de um modelo de LLM para avaliação. Consulte a documentação oficial do Google para ver os modelos disponíveis.
- Os limites de requisições gratuitas mudam com frequência. Consulte os limites atuais na documentação oficial do Google.

## Escolha dos modelos

Este desafio não fixa modelos. Nomes e versões mudam com frequência e alguns são descontinuados, então faz parte do desafio consultar a documentação oficial do provedor que você escolher, ver quais modelos estão disponíveis no momento e selecionar os que atendem ao objetivo. Você pode usar o mesmo modelo para responder e para avaliar, ou um modelo mais capaz na avaliação.

Para compatibilidade, o código usa temperatura `1` nos modelos OpenAI das famílias GPT-5 ou posteriores e `o`, que não aceitam valores personalizados; nos demais modelos, mantém temperatura `0`.

## Handle do LangSmith Hub (seu username)

O LangSmith identifica os prompts que você publica por um **handle público**, no
formato `handle/nome_do_prompt`. Esse handle é o valor que vai em
`USERNAME_LANGSMITH_HUB` no `.env`.

Ele **não existe por padrão**: é criado no momento em que você torna um prompt
público pela primeira vez. Por isso, faça esta etapa antes de tentar o push:

1. Abra o LangSmith e vá em **Prompts**
2. Crie um prompt qualquer (pode ser de teste) ou abra um que você já tenha
3. Clique nos **três pontinhos** no canto superior direito, ao lado do botão **Playground**
4. Escolha **Make Public**
5. Na tela **Choose your public handle**, defina o seu handle

O handle é **definitivo** depois de confirmado, então escolha com calma. Feito
isso, ele aparece no endereço do prompt (`handle/nome_do_prompt`) e é esse valor
que você coloca no `.env`.

## Requisitos

### 1. Pull do Prompt inicial do LangSmith

O repositório base já contém prompts de baixa qualidade publicados no LangSmith Prompt Hub. Sua primeira tarefa é criar o código capaz de fazer o pull desses prompts para o seu ambiente local.

Tarefas:

- Criar seu handle do LangSmith Hub (ver a seção "Handle do LangSmith Hub" acima)
- Configurar suas credenciais do LangSmith no arquivo .env (conforme o arquivo .env.example)
- Implementar o script src/pull_prompts.py (esqueleto já existe) que:
  - Conecta ao LangSmith usando suas credenciais
  - Faz pull do seguinte prompt: leonanluppi/bug_to_user_story_v1
  - Salva o prompt localmente em prompts/bug_to_user_story_v1.yml

Atenção: o LangSmith bloqueia por padrão o pull de prompts identificados por
`owner/nome`, porque um prompt do Hub é um objeto LangChain serializado e pode vir
de terceiros. Para o prompt semente do desafio, passe `dangerously_pull_public_prompt=True`
no `client.pull_prompt(...)`.

### 2. Otimização do Prompt

Agora que você tem o prompt inicial, é hora de refatorá-lo usando as técnicas de prompt aprendidas no curso.

Tarefas:

- Analisar o prompt em prompts/bug_to_user_story_v1.yml
- Criar um novo arquivo prompts/bug_to_user_story_v2.yml com suas versões otimizadas
- Aplicar obrigatoriamente Few-shot Learning (exemplos claros de entrada/saída) e pelo menos uma das seguintes técnicas adicionais:
  - Chain of Thought (CoT): Instruir o modelo a "pensar passo a passo"
  - Tree of Thought: Explorar múltiplos caminhos de raciocínio
  - Skeleton of Thought: Estruturar a resposta em etapas claras
  - ReAct: Raciocínio + Ação para tarefas complexas
  - Role Prompting: Definir persona e contexto detalhado
- Documentar no README.md quais técnicas você escolheu e por quê

Requisitos do prompt otimizado:

- Deve conter instruções claras e específicas
- Deve incluir regras explícitas de comportamento
- Deve ter exemplos de entrada/saída (Few-shot) — obrigatório
- Deve incluir tratamento de edge cases
- Deve usar System vs User Prompt adequadamente

### 3. Push e Avaliação

Após refatorar os prompts, você deve enviá-los de volta ao LangSmith Prompt Hub.

Tarefas:

- Implementar o script src/push_prompts.py (esqueleto já existe) que:
  - Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
  - Faz push para o LangSmith com nomes versionados: {seu_username}/bug_to_user_story_v2
  - Adiciona metadados (tags, descrição, técnicas utilizadas)
- Executar o script e verificar no dashboard do LangSmith se os prompts foram publicados
- Deixá-lo público (`is_public=True` no push, ou pelo menu "Make Public" na interface)

Lembre-se de que `{seu_username}` é o handle do Hub, e ele só existe depois de você
ter tornado algum prompt público pelo menos uma vez.

### 4. Iteração

Espera-se 3-5 iterações.

- Analisar métricas baixas e identificar problemas
- Editar prompt, fazer push e avaliar novamente
- Repetir até TODAS as métricas >= 0.8

Cada execução do `src/evaluate.py` cria um **experimento** no LangSmith, ligado ao
dataset de avaliação. As 5 notas são gravadas como feedback em cada exemplo, o que
permite comparar suas iterações lado a lado no dashboard. Ao final, o script imprime
o link direto do experimento.

```
Critério de Aprovação:
- Helpfulness >= 0.8
- Correctness >= 0.8
- F1-Score >= 0.8
- Clarity >= 0.8
- Precision >= 0.8

MÉDIA das 5 métricas >= 0.8
```

IMPORTANTE: TODAS as 5 métricas devem estar >= 0.8, não apenas a média!

### 5. Testes de Validação

O que você deve fazer: Edite o arquivo tests/test_prompts.py e implemente, no mínimo, os 6 testes abaixo usando pytest:

- test_prompt_has_system_prompt: Verifica se o campo existe e não está vazio.
- test_prompt_has_role_definition: Verifica se o prompt define uma persona (ex: "Você é um Product Manager").
- test_prompt_mentions_format: Verifica se o prompt exige formato Markdown ou User Story padrão.
- test_prompt_has_few_shot_examples: Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot).
- test_prompt_no_todos: Garante que você não esqueceu nenhum [TODO] no texto.
- test_minimum_techniques: Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas.

Como validar:

```
pytest tests/test_prompts.py
```

## Estrutura obrigatória do projeto

Faça um fork do repositório base: https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt

```
mba-ia-pull-evaluation-prompt/
├── .env.example              # Template das variáveis de ambiente
├── requirements.txt          # Dependências Python
├── README.md                 # Sua documentação do processo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt inicial (já incluso)
│   └── bug_to_user_story_v2.yml  # Seu prompt otimizado (criar)
│
├── datasets/
│   └── bug_to_user_story.jsonl   # 15 exemplos de bugs (já incluso)
│
├── src/
│   ├── pull_prompts.py       # Pull do LangSmith (implementar)
│   ├── push_prompts.py       # Push ao LangSmith (implementar)
│   ├── evaluate.py           # Avaliação automática (pronto)
│   ├── metrics.py            # 5 métricas implementadas (pronto)
│   └── utils.py              # Funções auxiliares (pronto)
│
├── tests/
│   └── test_prompts.py       # Testes de validação (implementar)
```

O que você deve implementar:

- prompts/bug_to_user_story_v2.yml — Criar do zero com seu prompt otimizado
- src/pull_prompts.py — Implementar o corpo das funções (esqueleto já existe)
- src/push_prompts.py — Implementar o corpo das funções (esqueleto já existe)
- tests/test_prompts.py — Implementar os 6 testes de validação (esqueleto já existe)
- README.md — Documentar seu processo de otimização

O que já vem pronto (não alterar):

- src/evaluate.py — Script de avaliação completo (cria o experimento no LangSmith e grava as notas como feedback)
- src/metrics.py — 5 métricas implementadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
- src/utils.py — Funções auxiliares
- datasets/bug_to_user_story.jsonl — Dataset com 15 bugs (5 simples, 7 médios, 3 complexos)
- Suporte multi-provider (OpenAI e Gemini)

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ordem de execução

1. Executar pull dos prompts ruins

```
python src/pull_prompts.py
```

2. Refatorar prompts

Edite manualmente o arquivo prompts/bug_to_user_story_v2.yml aplicando as técnicas aprendidas no curso.

3. Fazer push dos prompts otimizados

```
python src/push_prompts.py
```

4. Executar avaliação

```
python src/evaluate.py
```

## Entregável

1. Repositório público no GitHub (fork do repositório base) contendo:

- Todo o código-fonte implementado
- Arquivo prompts/bug_to_user_story_v2.yml 100% preenchido e funcional
- Arquivo README.md atualizado

2. README.md deve conter:

A) Seção "Técnicas Aplicadas (Fase 2)":

- Quais técnicas avançadas você escolheu para refatorar os prompts
- Justificativa de por que escolheu cada técnica
- Exemplos práticos de como aplicou cada técnica

B) Seção "Resultados Finais":

- Link público do dataset de avaliação, com os experimentos (ver "Evidências no LangSmith")
- Screenshots das avaliações com as notas mínimas de 0.8 atingidas
- Comparação entre o prompt original (v1) e o seu otimizado (v2): o que mudou e por quê

C) Seção "Como Executar":

- Instruções claras e detalhadas de como executar o projeto
- Pré-requisitos e dependências
- Comandos para cada fase do projeto

3. Evidências no LangSmith:

- Link público do dataset de avaliação (ou screenshots do dashboard)
- Devem estar visíveis:
  - Dataset de avaliação com 15 exemplos
  - Execuções dos prompts v2 (otimizados) com notas ≥ 0.8
  - Tracing detalhado de pelo menos 3 exemplos

O link que o `src/evaluate.py` imprime ao final só abre para quem tem acesso ao seu
workspace. Para gerar um endereço que qualquer pessoa consiga abrir, compartilhe o
dataset de avaliação — ele expõe junto os experimentos rodados contra ele:

```python
from langsmith import Client

print(Client().share_dataset(dataset_name="<seu LANGSMITH_PROJECT>-eval")["url"])
```

Rode uma vez e guarde o endereço: ao compartilhar de novo, o link muda.

## Dicas Finais

- Lembre-se da importância da especificidade, contexto e persona ao refatorar prompts
- Use Few-shot Learning com 2-3 exemplos claros para melhorar drasticamente a performance
- Chain of Thought (CoT) é excelente para tarefas que exigem raciocínio complexo (como análise de bugs)
- Use o Tracing do LangSmith como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- Não altere os datasets de avaliação - apenas os prompts em prompts/bug_to_user_story_v2.yml
- Itere, itere, itere - é normal precisar de 3-5 iterações para atingir 0.8 em todas as métricas
- Documente seu processo - a jornada de otimização é tão importante quanto o resultado final