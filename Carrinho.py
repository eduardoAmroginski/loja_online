from Roupa import Roupa
from Eletronico import Eletronico
from Alimento import Alimento # Importando a nova classe do Desafio 6

import os
import time
import json


class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
    

    def adicionar_produto(self, novo_produto):
        # Verifica se o produto já existe no carrinho
        for item in self.itens:
            if item["produto"].nome == novo_produto.nome:
                item["quantidade"] += 1
                print(f"🛒 Mais um '{novo_produto.nome}' adicionado. (Qtd: {item['quantidade']})")
                return
        
        # Se não existir, adiciona com quantidade 1
        self.itens.append({"produto": novo_produto, "quantidade": 1})
        print(f"🛒 '{novo_produto.nome}' adicionado ao carrinho.")
    
    def exibir_resumo(self):
        print("\n--- RESUMO DO CARRINHO ---")
        total = 0
        for item in self.itens:
            obj_produto = item["produto"]
            qtd = item["quantidade"]
            
            # Chama o método polimórfico
            obj_produto.exibir_detalhes()
            print(f"   ↳ Quantidade: {qtd} | Subtotal: R$ {obj_produto.get_preco() * qtd}")
            
            total += (obj_produto.get_preco() * qtd)
            
        print(f"💰 TOTAL A PAGAR: R$ {total}")


# =======================================================
    # MÉTODOS PRIVADOS (Encapsulamento da Lógica de Remoção)
    # =======================================================
    
    def _encontrar_item_por_nome(self, nome_busca):
        """Busca o item no carrinho ignorando maiúsculas e espaços."""
        busca_formatada = nome_busca.strip().lower()
        for item in self.itens:
            if item["produto"].nome.strip().lower() == busca_formatada:
                return item
        return None


    def _obter_quantidade_para_remover(self, qtd_atual):
        """Garante que o usuário digite uma quantidade válida (Loop de Validação)."""
        while True:
            try:
                qtd_remover = int(input(f"Quantas unidades deseja remover? (1 a {qtd_atual}): "))
                if 1 <= qtd_remover <= qtd_atual:
                    return qtd_remover
                else:
                    print(f"⚠️ Por favor, digite um valor entre 1 e {qtd_atual}.")
            except ValueError:
                print("⚠️ Erro: Digite um número inteiro válido.")


    def _aplicar_remocao(self, item, qtd_remover):
        """Aplica a regra de negócio para atualizar o dicionário ou remover da lista."""
        obj_produto = item["produto"]
        qtd_atual = item["quantidade"]
        
        if qtd_remover == qtd_atual:
            # Se a quantidade a remover for igual à do carrinho, remove o registro inteiro
            self.itens.remove(item)
            if qtd_atual == 1:
                print(f"❌ O produto '{obj_produto.nome}' foi removido do carrinho.")
            else:
                print(f"❌ Todas as {qtd_atual} unidades de '{obj_produto.nome}' foram removidas.")
        else:
            # Se for menor, apenas atualiza o valor no dicionário
            item["quantidade"] -= qtd_remover
            print(f"📉 {qtd_remover} unidade(s) de '{obj_produto.nome}' removida(s). Restam {item['quantidade']}.")


    # =======================================================
    # MÉTODO PÚBLICO (Orquestrador)
    # =======================================================
    
    def remover_produto(self, nome_busca):
        """Método principal que o 'main.py' enxerga e chama."""
        
        # 1. Busca o item (delega para o método privado)
        item_encontrado = self._encontrar_item_por_nome(nome_busca)
        
        if not item_encontrado:
            print(f"⚠️ Produto '{nome_busca}' não encontrado no carrinho.")
            return

        obj_produto = item_encontrado["produto"]
        qtd_atual = item_encontrado["quantidade"]

        # 2. Decide a ação baseada na quantidade
        if qtd_atual == 1:
            # Se tem apenas 1, já manda remover direto sem perguntar
            self._aplicar_remocao(item_encontrado, 1)
        else:
            # Se tem mais de 1, orquestra as perguntas e depois remove
            print(f"📦 Você tem {qtd_atual} unidades de '{obj_produto.nome}' no carrinho.")
            qtd_remover = self._obter_quantidade_para_remover(qtd_atual)
            self._aplicar_remocao(item_encontrado, qtd_remover)

    
    def salvar_carrinho(self, arquivo="carrinho.json"):
        dados_para_salvar = []
        
        for item in self.itens:
            produto = item["produto"] # Assumindo a estrutura do Desafio 7
            
            # Criando um dicionário com os dados brutos
            dicionario_produto = {
                "classe": produto.__class__.__name__, # Descobre se é Roupa, Eletronico, etc.
                "nome": produto.nome,
                "preco": produto.get_preco(),
                "quantidade": item["quantidade"],
                # getattr pega o atributo se ele existir, se não, retorna None
                "tamanho": getattr(produto, "tamanho", None),
                "voltagem": getattr(produto, "voltagem", None)
            }
            dados_para_salvar.append(dicionario_produto)
            
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)
        print("💾 Carrinho salvo com sucesso no disco!")


    def carregar_carrinho(self, arquivo="carrinho.json"):
        if not os.path.exists(arquivo):
            return # Se não existir arquivo, apenas ignora
            
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados_carregados = json.load(f)
            
        self.itens.clear() # Esvazia o carrinho atual
        
        # A magia de reconstruir os objetos (Deserialização)
        for dado in dados_carregados:
            if dado["classe"] == "Roupa":
                novo_obj = Roupa(dado["nome"], dado["preco"], dado["tamanho"])
            elif dado["classe"] == "Eletronico":
                novo_obj = Eletronico(dado["nome"], dado["preco"], dado["voltagem"])
            elif dado["classe"] == "Alimento":
                novo_obj = Alimento(dado["nome"], dado["preco"], dado["data_validade"])
            
            # Adiciona de volta à lista com a quantidade salva
            self.itens.append({"produto": novo_obj, "quantidade": dado["quantidade"]})
            
        print("📂 Carrinho restaurado da última sessão!")