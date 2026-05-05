from Produto import Produto

class Roupa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def exibir_detalhes(self):
        print(f"👕 Roupa: {self.nome} (Tamanho: {self.tamanho}) | Preço: R$ {self.get_preco()}")

        