from Roupa import Roupa
from Eletronico import Eletronico
from Carrinho import CarrinhoDeCompras

def exibir_menu():
    """Função auxiliar para desenhar o menu na tela."""
    print("\n" + "="*45)
    print("🏪 MENU DA LOJA ONLINE 🏪".center(45))
    print("="*45)
    print("[ 1 ] 👕 Adicionar Roupa")
    print("[ 2 ] 🔌 Adicionar Eletrônico")
    print("[ 3 ] 🛒 Ver Resumo do Carrinho")
    print("[ 4 ] ❌ Remover Produto do Carrinho (Desafio 1)")
    print("[ 5 ] 🚪 Sair do Sistema")
    print("="*45)

def main():
    # Instanciando o carrinho vazio logo que o programa começa
    carrinho = CarrinhoDeCompras()
    
    print("\n🚀 Bem-vindo ao Sistema de Gestão da Loja!")

    while True:
        exibir_menu()
        opcao = input("👉 Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Cadastrando Roupa ---")
            nome = input("Nome da roupa: ")
            try:
                preco = float(input("Preço: R$"))
                tamanho = input("Tamanho (P/M/G): ")
                nova_roupa = Roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)
            except ValueError:
                print("⚠️ Erro: Por favor, digite um valor numérico válido para o preço.")

        elif opcao == '2':
            print("\n--- Cadastrando Eletrônico ---")
            nome = input("Nome do eletrônico: ")
            try:
                preco = float(input("Preço: R$"))
                voltagem = input("Voltagem (ex: 110V/220V): ")
                novo_eletronico = Eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
            except ValueError:
                print("⚠️ Erro: Por favor, digite um valor numérico válido para o preço.")

        elif opcao == '3':
            carrinho.exibir_resumo()

        elif opcao == '4':
            print("\n--- Removendo Produto ---")
            nome_remover = input("Digite o nome exato do produto a ser removido: ")
            carrinho.remover_produto(nome_remover)

        elif opcao == '5':
            print("\n👋 Encerrando o sistema. Até logo!\n")
            break

        else:
            print("\n⚠️ Opção inválida! Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()