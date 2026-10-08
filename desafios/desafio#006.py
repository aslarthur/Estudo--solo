# Crie uma variável "temperatura" e exiba uma mensagem diferente para cada situação. "Frio" para quando estiver baixa, "normal" quando estiver normal, e "quente" quando estiver alta.

graus = float(input("Digite quantos graus está na sua cidade: °C "))
if graus <= 15:
    print ("Está frio!")
elif graus <= 23:
    print ("Está normal!")
else:
    print ("Está quente")