class CarrinhoDeCompras:
    def __init__(self):
        # O carrinho nasce vazio!
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print(f"🛒 {produto.nome} foi adicionado ao carrinho.")

    def exibir_resumo(self):
        print("\n--- RESUMO DO CARRINHO ---")
        total = 0
        for item in self.itens:
            # Polimorfismo em ação! Não importa se é roupa ou eletrônico.
            item.exibir_detalhes()
            total += item.get_preco()
        print(f"💰 TOTAL A PAGAR: R$ {total}")
        print("--------------------------\n")

    # ==========================================
    # 🚨 GABARITO: DESAFIO 1 (A Remoção) 🚨
    # ==========================================
    def remover_produto(self, nome_do_produto):
        for produto in self.itens:
            if produto.nome == nome_do_produto:
                self.itens.remove(produto)
                print(f"❌ O produto '{nome_do_produto}' foi removido do carrinho.")
                return # Encerra o loop após encontrar e remover
        print(f"⚠️ Produto '{nome_do_produto}' não encontrado no carrinho.")