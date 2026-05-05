import uuid


class Produto:
    def __init__(self, nome, preco):
        if preco < 0:
            raise ValueError("Erro Crítico: O preço de um produto não pode ser negativo!")
            
        self.id = str(uuid.uuid4()) # Gera um ID único aleatório
        self.nome = nome
        self._preco = preco
    
    
    def get_preco(self):
        return self._preco


    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R$ {self._preco}")
