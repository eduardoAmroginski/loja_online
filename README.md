# 🛒 Loja Online - Prática Guiada de POO em Python

Este projeto é um simulador de E-commerce de terminal desenvolvido para consolidar os 4 pilares da **Programação Orientada a Objetos (POO)**: Encapsulamento, Herança, Polimorfismo e Abstração.

## 📂 Estrutura do Projeto

O sistema foi modularizado para seguir as melhores práticas de desenvolvimento, separando responsabilidades em arquivos distintos:

* `Produto.py`: Contém a classe base `Produto`, demonstrando o **Encapsulamento** (proteção de atributos como o preço e métodos de acesso).
* `Roupa.py`: Especialização de `Produto` (Demonstra **Herança** e **Polimorfismo**).
* `Eletronico.py`: Especialização de `Produto` (Demonstra **Herança** e **Polimorfismo**).
* `Carrinho.py`: Classe `CarrinhoDeCompras` que interage com os produtos e calcula totais (Demonstra **Composição**).
* `main.py`: O arquivo principal (Entry Point) que contém o menu interativo e a execução do programa.

## 🚀 Como Executar

Certifique-se de ter o Python 3 instalado na sua máquina. Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

## 🎯 Desafios e Melhorias Futuras (Checklist do Aluno)

Se você já terminou a versão base do projeto, aqui estão algumas missões para elevar o nível do seu código! Marque os itens conforme for completando:

### Nível 1: Melhorias na Experiência do Usuário (UX no Terminal)

- [ ] **Limpar o Terminal:** A tela do console pode ficar muito poluída. Importe a biblioteca `os` e crie uma função para limpar a tela a cada nova opção escolhida (`os.system('cls' if os.name == 'nt' else 'clear')`).
- [ ] **Pausa para Leitura:** Após exibir o resumo do carrinho ou adicionar um produto, o menu reaparece imediatamente. Adicione um `input("\nPressione ENTER para continuar...")` ou use a biblioteca `time` (`time.sleep(2)`) para dar tempo ao usuário de ler as mensagens.
- [ ] **Validações Robustas (Tratamento de Exceções):** O que acontece se o usuário digitar letras quando o sistema pedir a voltagem de um eletrônico? Adicione blocos `try/except` mais avançados e loops `while` para forçar o usuário a digitar o valor correto antes de prosseguir.

### Nível 2: Limpeza e Organização de Código (Refatoração)

- [ ] **Separar a Lógica do `main()`:** O arquivo principal está ficando com muitos `if/elif`. Crie funções separadas para cada ação. Exemplo: crie uma função `def cadastrar_roupa(carrinho):` e chame-a dentro do `if opcao == '1':`. Isso deixa o `main()` muito mais limpo e profissional.
- [ ] **Tratamento de Strings:** Ao remover um produto, o nome precisa ser exato. Melhore a busca utilizando métodos de string como `.strip()` e `.lower()` para que "Camiseta" e " camiseta " sejam reconhecidos como o mesmo produto.

### Nível 3: Novas Regras de Negócio (Evoluindo o E-commerce)

- [ ] **Novas Categorias de Produtos:** A loja cresceu! Crie novas classes que herdem de `Produto` (ex: `Alimento`, `Livro`). Adicione atributos exclusivos (como data de validade para Alimentos ou autor para Livros) e sobrescreva o método de exibir detalhes para mostrar essas informações com o Polimorfismo. Não se esqueça de adicionar as opções no menu interativo!
- [ ] **Gerenciamento de Quantidades:** Atualmente, se você comprar duas TVs iguais, elas aparecem como dois itens separados na lista. Modifique o carrinho para agrupar itens iguais e adicionar um atributo de `quantidade` a eles.
- [ ] **Identificadores Únicos (IDs):** Remover produtos pelo nome pode dar problema se houver dois produtos chamados "Camiseta". Importe a biblioteca `uuid` e gere um ID único para cada `Produto` no momento de sua criação (`__init__`). Atualize o método de remoção para buscar pelo ID.
- [ ] **Validação no Construtor:** Em `Produto`, não permita que um produto seja criado com preço negativo. Lance um erro (`raise ValueError`) dentro do `__init__` se isso acontecer.

### Nível 4: O "Boss" Final - Persistência de Dados

- [ ] **Salvar e Carregar em JSON:** Quando fechamos o programa, perdemos tudo que estava no carrinho! Pesquise sobre a biblioteca `json` nativa do Python.
  - [ ] Crie um método `salvar_carrinho()` que converte seus objetos em dicionários e os salva em um arquivo `carrinho.json`.
  - [ ] Crie um método `carregar_carrinho()` que, ao iniciar o programa, verifica se existe um `carrinho.json` e recria os objetos automaticamente!

---

*Bons estudos e mãos à obra!* 🛠️💻