# 💡 Projeto-Ideias — Banco de Ideias em Python

Aplicação de linha de comando (CLI) para cadastrar, listar, sortear e editar ideias de projetos. Foi desenvolvida como exercício prático de **linguagem Python** e **lógica de programação**, com foco em estruturas de controle, manipulação de listas, entrada e saída de dados e uso de bibliotecas da biblioteca padrão.

## 📋 Funcionalidades

| Opção | Descrição |
|-------|-----------|
| 1 | Adicionar uma nova ideia |
| 2 | Listar todas as ideias cadastradas |
| 3 | Sortear uma ideia aleatória |
| 4 | Editar uma ideia existente |
| 5 | Sair do programa |

## 🛠️ Tecnologias e conceitos aplicados

- **Python 3**: linguagem principal do projeto.
- **Biblioteca `random`**: módulo da *standard library* importado com `import random`, usado para a seleção aleatória de itens da lista (opção "Sortear uma ideia").
- **Funções**: o código é organizado em funções com responsabilidades separadas, como `menu()`, que exibe as opções e retorna a escolha do usuário, e `main()`, que concentra o fluxo principal do programa.
- **Listas (`list`)**: estrutura de dados mutável usada para armazenar as ideias, com operações como `append()` para inserção e acesso por índice para edição.
- **Laço `while True`**: mantém o programa em execução contínua (*loop* de menu) até que o usuário escolha sair.
- **Estruturas condicionais (`if` / `elif` / `else`)**: controlam qual ação executar de acordo com a opção digitada.
- **Entrada de dados com `input()`**: captura o que o usuário digita no terminal.
- **Tratamento de strings com `.strip()`**: remove espaços em branco no início e no fim do texto digitado, evitando entradas vazias ou mal formatadas.
- **Validação de entrada**: verifica se o texto digitado não está vazio antes de salvar, e se a lista possui itens antes de listar ou sortear.
- **`enumerate()`**: percorre a lista gerando o índice junto com cada item, usado para numerar as ideias na listagem (`start=1`).
- **f-strings**: formatação de texto com variáveis embutidas, como `f"{i}. {ideia}"`.

## 📁 Estrutura do projeto

```
Projeto-Ideias/
├── ideias.py      # Código principal da aplicação
├── .gitignore     # Arquivos ignorados pelo Git
└── README.md      # Documentação do projeto
```

## ▶️ Como executar

**Pré-requisito:** ter o [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:
   ```bash
   git clone https://github.com/davitorino/Projeto-Ideias.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd Projeto-Ideias
   ```
3. Execute o programa:
   ```bash
   python ideias.py
   ```

## 🖥️ Exemplo de uso

```
=== BANCO DE IDEIAS ===
1. Adicionar nova ideia
2. Listar todas as ideias
3. Sortear uma ideia aleatória
4. Editar uma ideia
5. Sair
Escolha uma opção (1-5):
```

## 🚀 Próximos passos

Ideias para evoluir o projeto:

- [ ] Persistir as ideias em arquivo (`.txt`, `.json` ou `.csv`) para não perder os dados ao fechar o programa
- [ ] Adicionar a opção de remover ideias
- [ ] Tratar exceções com `try` / `except`
- [ ] Criar testes automatizados
- [ ] Migrar para banco de dados (SQLite)

## 🎯 Objetivo de aprendizado

Projeto criado para praticar fundamentos de programação em Python: modularização com funções, manipulação de estruturas de dados, controle de fluxo, uso de módulos da biblioteca padrão e versionamento de código com **Git** e **GitHub**.

## 👤 Autor

**davitorino**
[GitHub](https://github.com/davitorino)
