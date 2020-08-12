class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    cristina = Pessoa(nome ='Cristina')
    carolina = Pessoa(cristina, nome ='Carolina')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(carolina.olhos)
    print(cristina.olhos)
    print(id(Pessoa.olhos), id(carolina.olhos), id(cristina.olhos))