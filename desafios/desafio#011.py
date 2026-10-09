#Crie um simulador de tabuada onde o jogador digite um número e a tabuada desse número sera exibida
num = int(input("Digite um número: "))
for n in range (1, 11):
    print (f"{num} x {n} = {num * n}")