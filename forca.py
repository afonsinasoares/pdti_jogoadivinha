import random

lista_frutas = ['abacate','abacaxi','banana',"catole",'melancia','manga','pitomba']
fruta = random.choice(lista_frutas)
fruta = fruta.strip()

tentativas_max = 6
letras_digitais = []
print(fruta)

quant_letras = len(fruta)
caixa = list('_' * quant_letras)
print(caixa)

acertos = 0
erros = 0
# En construção!