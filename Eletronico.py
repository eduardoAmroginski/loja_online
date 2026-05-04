from Produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

    def exibir_detalhes(self):
        print(f"🔌 Eletrônico: {self.nome} ({self.voltagem}V) | Preço: {self.get_preco()}€")