class Aves:
    def __init__(self):
        self.aves = []

    def criar_ave(self, nome, especie, peso):
        if type(nome) != str:
            raise ValueError("Nome não pode ser diferente de string!")
        nova_ave = {"nome": nome, "especie": especie, "peso": peso}
        self.aves.append(nova_ave)
        print(f"Ave {nome} criada com sucesso!")

    def atualizar_ave(self, nome, nova_especie, novo_peso):
        for ave in self.aves:
            if ave["nome"] == nome:
                ave["especie"] = nova_especie
                ave["peso"] = novo_peso
                print(f"Ave {nome} atualizada com sucesso!")

    def deletar_ave(self, nome):
        for ave in self.aves:
            if ave["nome"] == nome:
                self.aves.remove(ave)
                print(f"Ave {nome} removida com sucesso!")
                return
        print(f"Ave {nome} não encontrada.")

    def listar_aves(self):
        print("\nLista de Aves:")
        for ave in self.aves:
            print(f"Nome: {ave['nome']}, Espécie: {ave['especie']}, Peso: {ave['peso']} gramas")

# Exemplo de uso:
if __name__ == "__main__":
    viveiro = Aves()

    viveiro.criar_ave("Canarinho", "Passeriforme", 30)
    viveiro.criar_ave("Arara", "Psitacídeo", 1500)

    viveiro.listar_aves()

    viveiro.atualizar_ave("Canarinho", "Pardal", 35)

    viveiro.listar_aves()

    viveiro.deletar_ave("Arara")

    viveiro.listar_aves()
