class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]


    def __len__(self):
        return len(self._programas)

home_aranhas = Filme('Homem Aranha no Aranhaverso', 2018, 120)
boris = Serie('Boris', 2007, 4)
lugar_silencioso = Filme('Um Lugar Silencioso', 2018, 90)
cuphead = Serie('Cuphead', 2022, 3)

home_aranhas.dar_likes()
home_aranhas.dar_likes()
home_aranhas.dar_likes()
boris.dar_likes()
boris.dar_likes()
lugar_silencioso.dar_likes()
lugar_silencioso.dar_likes()
cuphead.dar_likes()
cuphead.dar_likes()

listinha = [boris, home_aranhas, cuphead, lugar_silencioso]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')
