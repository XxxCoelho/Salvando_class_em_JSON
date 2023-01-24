import json


class Pessoa():

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


pessoa_1 = Pessoa('Everton', 'Coelho', 23)
pessoa_2 = Pessoa('Fabiana', 'Coelho', 50)
pessoa_3 = Pessoa('Airton', 'Coelho', 58)
pessoa_4 = Pessoa('Clea', 'Coelho', 85)

# Json salva ser estiver em dicionario
list_classes = [pessoa_1.__dict__, pessoa_2.__dict__, pessoa_3.__dict__, pessoa_4.__dict__]

with open('Salvo_json.txt', 'w+') as file:
    json.dump(list_classes, file, indent=3)

with open('Salvo_json.txt', 'r') as file:
    dados_python = json.load(file)
    print(dados_python)

Nova_pessoa = Pessoa(**dados_python[0])
print(Nova_pessoa.nome)
