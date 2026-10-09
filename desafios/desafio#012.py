#Escreva um programa que conta quantas vogais existem na string que o usuário digita
nova_letra= input("Digite uma palavra ou frase ou sla tbm: ")
letra = nova_letra.upper()
vogais = "AEIOU"
contador = 0 
for caractere in letra:
    if caractere in vogais:
        contador += 1
print (f'A palavra "{nova_letra}" tem {contador} caracteres')