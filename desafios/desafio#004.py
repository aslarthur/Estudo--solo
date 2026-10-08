# Crie uma variável "temperatura" e exiba uma mensagem diferente para cada situação. "Frio" para quando estiver baixa, "normal" quando estiver normal, e "quente" quando estiver alta.
temperatura = float(input("Digite a temperatura: °C "))
if temperatura <= 18:
    print ("Frio")
elif temperatura <= 25:
    print ("Normal.")
else:
    print ("Quente")

#Desafio: Ficha do pet 

#DADOS:
# Nome: Thor
# Idade: 3
# Peso: 12.5
# Vacinado: True

nome = "Thor"
idade = 3
peso = 12.5
vacinado = True

print (f"Nome do pet: {nome}, tipo do dado:", type (nome))
print (f"Idade do {nome}: {idade}, tipo do dado:", type (idade))
print (f"Peso do {nome}: {peso}, tipo do dado:", type (peso))
print (f"Vacinado? {vacinado}, tipo do dado:", type (vacinado))

