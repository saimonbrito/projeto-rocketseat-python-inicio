"""Module providing a function printing python3.12.2"""


minha_lista = [1,10,56,3,4]

print(minha_lista)

minha_lista[0]= 28
print(minha_lista)

minha_lista.append(99)
lista = minha_lista.index(3)

minha_lista.insert(0,88)

print(minha_lista)

minha_lista.pop(5)
print(minha_lista)

minha_lista.sort()
print(minha_lista)


dicionario = {
  "terra":"chao", 
  "praia":'agua',
  "sapato":" chule"
}

for vaçor in dicionario.items():
  print(vaçor)

dis = dicionario.items()


idade = 18

mensagem = "Pode retira abilitaçao" if idade >18 else "nao pode tirar abilitacao"

