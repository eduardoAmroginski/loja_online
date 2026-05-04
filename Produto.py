class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        # O _ tranca o atributo! Ninguém pode mexer de fora.
        self._preco = preco

    def get_preco(self):
        return self._preco

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: {self._preco}€")

    # ==========================================
    # 🚨 GABARITO: DESAFIO 2 (Desconto Seguro) 🚨
    # ==========================================
    def aplicar_desconto(self, percentagem):
        if 0 <= percentagem <= 100:
            valor_desconto = self._preco * (percentagem / 100)
            self._preco -= valor_desconto
            print(f"✅ Desconto de {percentagem}% aplicado com sucesso no produto {self.nome}!")
        else:
            print("❌ Desconto inválido!")