from Produto import Produto

class Alimento(Produto):
    def __init__(self, nome, preco, data_validade):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    def exibir_detalhes(self):
        print(f"🍎 Alimento: {self.nome} (Validade: {self.data_validade}) | Preço: R$ {self.get_preco()}")