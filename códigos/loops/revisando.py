#O QUE EU SEI:

#1. TABUADA

# num = int(input("Digite o número desejado: "))
# for n in range (1, 11):
#     print (f"{num} x {n} = {num * n}")

#2. NÚMEROS PARES

# while True:
#     num = int(input("Digite um número par: "))
#     if num %2 == 0:
#         print ("Você digtou um número par. Obrigado!")
#         break
#     else:
#         print ("Você digitou um número ímpar! Tente novamente, por favor.")
#         continue        

#3. LISTA ENUMERATE()

# lista = {'Nome': 'Arthur', 'Idade': 11, 'Estudando': 'Programação'}
# for n, (c, v) in enumerate(lista.items(), start=1):
#     print (f"{n}. {c}: {v}")

#4. LISTA ITEMS()

# lista = {'Nome': 'Arthur', 'Idade': 11, 'Estudando': 'Programação'}
# for i in lista.items():
#     print (i)

#5. LISTA KEYS()

# lista = {'Nome': 'Arthur', 'Idade': 11, 'Estudando': 'Programação'}
# for k in lista.keys():
#     print (k)

#6. LISTA VALUES()

lista = {'Nome': 'Arthur', 'Idade': 11, 'Estudando': 'Programação'}
for v in lista.values():
    print (v)