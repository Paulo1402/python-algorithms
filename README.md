# ❤️ Python Algorithms

Implementação de algoritmos comuns em entrevistas de programação utilizando Python.

Os algoritmos estão divididos entre três níveis de dificuldade:

- **Basic**: Algoritmos simples e diretos.
- **Intermediary**: Algoritmos mais complexos, que requerem um pouco mais de raciocínio.
- **Advanced**: Algoritmos complexos, que requerem um bom raciocínio e conhecimento avançado.

Dentro de cada nível, os algoritmos estão organizados por pacotes. Cada pacote contém um conjunto de arquivos, sendo:

- **README.md**: Descrição do pacote e dos algoritmos.
- **solution.py**: Solução do algoritmo.
- **imp.py**: Implementação do algoritmo.
- **test_imp.py**: Testes unitários para a implementação do algoritmo.

## ⭐ Como usar

Primeiramente, clone o repositório, ative o ambiente virtual e instale as dependências:

```bash
# Clone o repositório
git clone
cd python-algorithms

# Crie e ative o ambiente virtual
python -m venv .venv
. .venv/bin/activate

# Instale as dependências
pip install -r pyproject.toml
```

Na sequência, navegue até o diretório do algoritmo que deseja praticar e siga as instruções do arquivo `README.md`.

Para cada algoritmo, você encontrará uma descrição do problema, a solução e os testes unitários.

### ▶️ Implementação do algoritmo

A solução do algoritmo deve ser implementada em um arquivo chamado `imp.py`, na raíz do pacote do algoritmo
correspondente. A assinatura da função você encontrará no arquivo
`README.md`.

Caso queira visualizar uma possível solução para o algoritmo, consulte o arquivo `solution.py`.

### 🧪 Testes

Para executar os testes, utilize o comando:

```bash
ptw -- -k <nome_do_algoritmo>
```

#### Exemplo:

```bash
ptw -- -k sum_of_two_numbers

```

Esse comando irá executar os testes unitários para a implementação do algoritmo em modo `watch`, ou seja, sempre que
você alterar o código, os testes serão executados automaticamente.

Conforme você implementa a solução, os testes irão falhar. Quando todos os testes passarem, você terá implementado a
solução corretamente.

### Happy coding! 🚀



