#Escreva um programa onde o sistema exibe uma tabuada de 1 a 100
def l():
    print ("-=" * 30)

for num in range (1, 101):
    l()
    for n in range (1, 11):
        
        print (f"{num} x {n} = {num * n } ")
    l()