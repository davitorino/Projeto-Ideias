# Projeto-Ideias: Sorteador e Banco de Ideias em Python (Tkinter)

Aplicação desktop com interface gráfica (GUI) para cadastrar, gerenciar e sortear ideias do que fazer. Desenvolvida como exercício prático de **Python**, **lógica de programação**, **programação orientada a objetos** e **versionamento com Git/GitHub**.

## Funcionalidades

- Sortear uma ideia aleatória a partir do banco cadastrado
- Gerenciar o banco de ideias em uma janela secundária (CRUD completo):
  - **Adicionar** novas ideias
  - **Listar** todas as ideias em um componente com barra de rolagem
  - **Editar** uma ideia selecionada
  - **Remover** uma ideia selecionada
- Persistência automática dos dados em arquivo JSON
- Carga de um conjunto de ideias padrão na primeira execução

## Tecnologias e conceitos aplicados

**Linguagem e bibliotecas (standard library)**
- **Python 3**
- **`tkinter`**: construção da interface gráfica, com os módulos `ttk` (widgets temáticos), `messagebox` (alertas e avisos) e `simpledialog` (caixas de entrada de texto)
- **`json`**: serialização e desserialização de dados (`json.load` e `json.dump`, com `ensure_ascii=False` e `indent=4` para preservar acentuação e legibilidade)
- **`random`**: seleção aleatória de itens com `random.choice()`
- **`os`**: verificação da existência do arquivo de dados com `os.path.exists()`

**Programação e arquitetura**
- **Programação orientada a objetos (POO)**: aplicação estruturada na classe `BancoDeIdeiasApp`, com construtor `__init__` e métodos com responsabilidades separadas
- **Programação orientada a eventos**: interação baseada em *callbacks* nos botões, via parâmetro `command`
- **Funções aninhadas (closures)**: funções `add`, `edit` e `remove` com acesso ao estado da janela onde são definidas
- **Gerenciamento de janelas**: janela principal (`Tk`) e secundária modal (`Toplevel`, `transient` e `grab_set`)
- **Persistência de dados em arquivo**: leitura e escrita com *context manager* (`with open(...)`) e codificação UTF-8
- **Tratamento de exceções**: bloco `try/except` na leitura do arquivo, com *fallback* para as ideias padrão em caso de arquivo ausente ou corrompido
- **Validação de entradas**: uso de `.strip()` e verificação de texto vazio antes de salvar
- **Constantes de módulo** e **guard clause** `if __name__ == "__main__"` para definir o ponto de entrada
- **Estruturas de dados**: manipulação de listas (`append`, `del`, acesso por índice)
- **Estilização de interface**: tema `clam` do `ttk.Style` e personalização de widgets

**Ferramentas**
- **Git e GitHub**: versionamento, `commit`, `push` e repositório remoto
- **Visual Studio Code**
- **Markdown** para a documentação

## Estrutura do projeto

```
Projeto-Ideias/
├── ideias.py      # Código principal da aplicação
├── ideias.json    # Gerado automaticamente ao salvar as ideias
├── .gitignore     # Arquivos ignorados pelo Git
└── README.md      # Documentação do projeto
```

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado (o Tkinter já acompanha a instalação padrão no Windows).

```bash
git clone https://github.com/davitorino/Projeto-Ideias.git
cd Projeto-Ideias
python ideias.py
```

## Próximos passos

- [ ] Confirmação antes de remover uma ideia
- [ ] Tratamento de exceções mais específico (`json.JSONDecodeError`, `OSError`)
- [ ] Busca e filtro de ideias
- [ ] Categorias de ideias
- [ ] Testes automatizados (`unittest` ou `pytest`)
- [ ] Empacotamento como executável (`PyInstaller`)

## Objetivo de aprendizado

Primeiro projeto de desenvolvimento, criado para consolidar fundamentos de programação em Python: modularização, orientação a objetos, manipulação de bibliotecas, persistência de dados, construção de interfaces gráficas e fluxo de trabalho com Git e GitHub.

## Autor

**davitorino**
[GitHub](https://github.com/davitorino)
