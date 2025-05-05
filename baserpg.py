class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.itens = []

    def atacar(self, inimigo):
        print(f"{self.nome} ataca {inimigo.nome} e causa {self.ataque} de dano!")
        inimigo.vida -= self.ataque
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")

    def usar_item(self, item):
        print(f"{self.nome} usou o item {item.nome}")
        item.usar(self)

    def adicionar_item(self, item):
        self.itens.append(item)

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, recompensa):
        super().__init__(nome, vida, ataque)
        self.recompensa = recompensa

    def atacar(self, personagem):
        print(f"{self.nome} ataca {personagem.nome} e causa {self.ataque} de dano!")
        personagem.vida -= self.ataque
        if personagem.vida <= 0:
            print(f"{personagem.nome} foi derrotado!")

class Item:
    def __init__(self, nome):
        self.nome = nome

    def usar(self, personagem):
        pass  # Implementação padrão para itens (será sobrescrito em classes filhas)

class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome)
        self.dano = dano

    def usar(self, personagem):
        print(f"{personagem.nome} equipou a {self.nome} que causa {self.dano} de dano adicional!")
        personagem.ataque += self.dano

# Criando um personagem e um inimigo
heroi = Personagem("marquito", 100, 40)
inimigo = Inimigo("xaropinho", 1, 4, "Microfone")

# Criando uma arma e adicionando ao personagem
espada = Arma("fralda geriatrica", 40)
heroi.adicionar_item(espada)

# Usando a arma
heroi.usar_item(espada)

# O herói ataca o inimigo
heroi.atacar(inimigo)

# O inimigo contra-ataca
inimigo.atacar(heroi)

class Habilidade:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def usar(self, personagem, inimigo):
        print(f"{personagem.nome} usou a habilidade {self.nome}!")
        inimigo.vida -= self.dano
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado por {heroi.nome} com {self.nome}!")

# Criando uma habilidade
fogo_mental = Habilidade("Skin Barbie", 30)

# Usando a habilidade no inimigo
fogo_mental.usar(heroi, inimigo)
