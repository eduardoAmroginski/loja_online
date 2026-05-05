from Roupa import Roupa
from Eletronico import Eletronico
from Alimento import Alimento # Importando a nova classe do Desafio 6
from Carrinho import CarrinhoDeCompras

import os
import time

def limpar_tela():
    """Limpa o console de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Cria uma pausa dramática/útil para o usuário ler as mensagens."""
    input("\n[Pressione ENTER para continuar...]")

def exibir_menu():
    print("\n" + "="*45)
    print("🏪 MENU DA LOJA ONLINE 🏪".center(45))
    print("="*45)
    print("[ 1 ] 👕 Adicionar Roupa")
    print("[ 2 ] 🔌 Adicionar Eletrônico")
    print("[ 3 ] 🍎 Adicionar Alimento")
    print("[ 4 ] 🛒 Ver Resumo do Carrinho")
    print("[ 5 ] ❌ Remover Produto")
    print("[ 0 ] 🚪 Sair e Salvar")
    print("="*45)

def obter_preco_valido():
    """Força o usuário a digitar um número válido para o preço."""
    while True:
        try:
            valor = float(input("Preço: R$ "))
            if valor < 0:
                print("⚠️ O preço não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("⚠️ Erro: Por favor, digite um valor numérico válido (ex: 15.50).")

def cadastrar_roupa(carrinho):
    print("\n--- Cadastrando Roupa ---")
    nome = input("Nome da roupa: ")
    preco = obter_preco_valido() 
    tamanho = input("Tamanho (P/M/G): ")
    
    nova_roupa = Roupa(nome, preco, tamanho)
    carrinho.adicionar_produto(nova_roupa)

def cadastrar_eletronico(carrinho):
    print("\n--- Cadastrando Eletrônico ---")
    nome = input("Nome do eletrônico: ")
    # O try/except foi removido daqui pois a função obter_preco_valido já trata isso!
    preco = obter_preco_valido()
    voltagem = input("Voltagem (ex: 110V/220V): ")
    
    novo_eletronico = Eletronico(nome, preco, voltagem)
    carrinho.adicionar_produto(novo_eletronico)

def cadastrar_alimento(carrinho):
    print("\n--- Cadastrando Alimento ---")
    nome = input("Nome do alimento: ")
    preco = obter_preco_valido()
    validade = input("Data de validade (ex: 12/12/2026): ")
    
    novo_alimento = Alimento(nome, preco, validade)
    carrinho.adicionar_produto(novo_alimento)

def remover_produto_menu(carrinho):
    print("\n--- Removendo Produto ---")
    nome_remover = input("Digite o nome exato do produto a ser removido: ")
    carrinho.remover_produto(nome_remover)

def main():
    carrinho = CarrinhoDeCompras()
    
    # Tentativa de carregar o carrinho salvo anteriormente (Desafio 10)
    # Certifique-se de que o método carregar_carrinho() existe em CarrinhoDeCompras
    try:
        carrinho.carregar_carrinho()
    except AttributeError:
        pass # Ignora se o professor/aluno ainda não implementou o desafio 10

    print("\n🚀 Bem-vindo ao Sistema de Gestão de Loja!")
    pausar()

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("👉 Escolha uma opção: ")

        if opcao == "1":
            cadastrar_roupa(carrinho)
            pausar()
        
        elif opcao == "2":
            cadastrar_eletronico(carrinho)
            pausar()
            
        elif opcao == "3":
            cadastrar_alimento(carrinho)
            pausar()
            
        elif opcao == "4":
            carrinho.exibir_resumo()
            pausar()
            
        elif opcao == "5":
            remover_produto_menu(carrinho)
            pausar()
        
        elif opcao == "0":
            # Salva o carrinho no arquivo JSON antes de sair (Desafio 10)
            try:
                carrinho.salvar_carrinho()
            except AttributeError:
                pass
                
            print("\n👋 Encerrando o sistema. Até logo!\n")
            break
            
        else:
            print("\n⚠️ Opção inválida! Por favor, escolha um número de 0 a 5")
            pausar()

if __name__ == "__main__":
    main()