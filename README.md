# Boas-vindas ao projeto Algorithms!

Projeto feito durante o curso de desenvolvimento web na trybe.

## Habilidades:
  
- Lógica;

- Capacidade de interpretação de problemas;

- Capacidade de interpretação de um código legado;

- Capacidade de otimizar a resolução de problemas e;

- Resolver problemas/Otimizar algoritmos sob pressão.

<details>
  <summary><strong>🗓 Data de Entrega</strong></summary><br />
  
  * Este projeto é `individual`;
  * São `2` dias de projeto;
  * Data para entrega final do projeto: `07/09/2022 14:00`.

</details>

# Desenvolvimento
<details>
  <summary>
    <h3>
      Antes de começar a desenvolver
    </h3>
  </summary>

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:mabiiak/algorithms.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd algorithms`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `master`

  - Verifique que você está na branch `master`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `master`
    - Exemplo: `git checkout master`
  - Crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-de-usuario-nome-do-projeto`
    - Exemplo: `git checkout -b nome-algorithms`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'descrição'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin nome-algorithms`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/mabiiak/algorithms/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/mabiiak/algorithms/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

## Requisitos

## 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

    ✅ 1.1 - Retorne a quantidade de estudantes presentes para uma entrada específica;

    ✅ 1.2 - Retorne `None` se em `permanence_period` houver alguma entrada inválida;

    ✅ 1.3 - Retorne `None` se  `target_time` recebe um valor vazio;

    ✅ 1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear.

## 2 - Palíndromos (Recursividade)

    ✅ 2.1 - Retorne `True` se a palavra passada por parâmetro for um palíndromo;

    ✅ 2.2 - Retorne `False` se a palavra passada por parâmetro não for um palíndromo;

    ✅ 2.3 - Retorne `False` se nenhuma palavra for passada por parâmetro.

## 3 - Anagramas (Algoritmo de ordenação)

    ✅ 3.1 - Retorne `True` se as palavras passadas por parâmetro forem anagramas;

    ✅ 3.2 - Retorne `False` se as palavras passadas por parâmetro não forem anagramas;

    ✅ 3.3 - Retorne `False` se alguma das palavras passadas por parâmetro for uma string vazia;

    ✅ 3.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica.

    ✅ 3.5 - Retorne `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas.

# Bônus

## 4 - Encontrando números repetidos (Algoritmo de busca)

    ✅ 4.1 - Retorne o número repetivo se a função receber como parâmetro uma lista com números repetidos;

    ✅ 4.2 - Retorne `False` se a função não receber nenhum parâmetro;

    ✅ 4.3 - Retorne `False` se a função receber como parâmetro uma string;

    ✅ 4.4 - Retorne `False` se a função receber como parâmetro uma lista sem números repetidos;

    ✅ 4.5 - Retorne `False` se a função receber como parâmetro apenas um valor;

    ✅ 4.6 - Retorne `False` se a função receber como parâmetro um número negativo;

    ✅ 4.7 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica.

## 5 - Palíndromos (Iteratividade)

    ✅ 5.1 - Retorne `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa;

    ✅ 5.2 - Retorne `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa;

    ✅ 5.3 - Retorne `False` se nenhuma palavra for passada como parâmetro, executando uma função iterativa ;

    ✅ 5.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear.

