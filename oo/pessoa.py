class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nomes_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    cristina = Mutante(nome ='Cristina')
    carolina = Mulher(cristina, nome ='Carolina')
    print(Pessoa.cumprimentar(carolina))
    print(id(carolina))
    print(carolina.cumprimentar())
    print(carolina.nome)
    print(carolina.idade)
    for filho in carolina.filhos:
        print(filho.nome)
    carolina.sobrenome = 'Oliveira'
    del carolina.filhos
    carolina.olhos = 1
    del carolina.olhos
    print(carolina.__dict__)
    print(cristina.__dict__)
    print(Pessoa.olhos)
    print(carolina.olhos)
    print(cristina.olhos)
    print(id(Pessoa.olhos), id(carolina.olhos), id(cristina.olhos))
    print(Pessoa.metodo_estatico(), carolina.metodo_estatico())
    print(Pessoa.nomes_e_atributos_de_classe(), carolina.nomes_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(isinstance(cristina, Pessoa))
    print(isinstance(cristina, Mulher))
    print(carolina.olhos)
    print(cristina.cumprimentar())
    print(carolina.cumprimentar())