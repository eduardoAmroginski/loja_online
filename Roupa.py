from Produto import Produto

class Roupa(Produto):
    def __init__(self, nome, preco, tamanho):
        # Pedimos à classe Mãe para resolver o nome e o preço
        super().__init__(nome, preco)
        # Resolvemos a característica exclusiva da Roupa
        self.tamanho = tamanho

    def exibir_detalhes(self):
        # Usamos o get_preco() para conseguir ler o preço encapsulado!
        print(f"👕 Roupa: {self.nome} (Tamanho: {self.tamanho}) | Preço: {self.get_preco()}€")