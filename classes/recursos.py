import random


class Personagem:

    def __init__(self, nome='', nivel=0, titulo='', vida=0):
        self.classe = None
        self._nome = nome
        self._nivel = nivel
        self.titulo = titulo
        self._vida = vida

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('nivel precisa ser numerico')
        self._nivel = valor

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    # titulos de cada class
    @property
    def titulos(self):
        if self.nivel < 10:
            self.titulo = 'Bloqueado'
        elif self.nivel < 20:
            self.titulo = 'Candidato a Mercenario'
        elif self.nivel < 26:
            self.titulo = 'Mercenario Iniciante'
        elif self.nivel < 36:
            self.titulo = 'Mercenario Pleno'
        elif self.nivel < 46:
            self.titulo = 'Mestre dos Mercenarios'
        return self.titulo

    # detalhes de cada classe
    '''def detalhes(self, classe='Unknown', vida=0):
        self.classe = classe
        self.vida = vida
        
        print(f'Classe: {self.classe}')
        print(f'Nome: {self.nome}', end=' ')
        print(f'Nivel: {self.nivel}', end=' ')
        print(f'Vida: {self.vida}', end=' ')'''


class Inimigo:
    def __init__(self, nome='', nivel=0, raca=''):
        self._nome = nome
        self._nivel = nivel
        self._classe = None
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        self._nivel = valor

    @property
    def raca(self):
        if self.nivel < 10:
            self._raca = 'Esqueleto'
        elif self.nivel < 20:
            raca_ale = random.choice(['Esqueleto', 'Bandido'])
            self._raca = raca_ale
        elif self.nivel < 30:
            raca_ale = random.choice(['Esqueleto', 'Bandido', 'Mercenario'])
            self._raca = raca_ale
        elif self.nivel < 40:
            raca_ale = random.choice(['Esqueleto', 'Bandido', 'Mercenario', 'Litch'])
            self._raca = raca_ale
        elif self.nivel < 45:
            raca_ale = random.choice(['Esqueleto', 'Bandido', 'Mercenario', 'Litch', 'Dragão'])
            self._raca = raca_ale
        return self._raca
