def l():
    print ("-=" * 66)
def e():
    print()
l()
print ("Bem vindo(a) a minha calculadora! Espero que tenha uma ótima experiencia.")
l()
e()
while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    l()
    e()
    print ("OPERADORES: ")
    e()
    print ("1. +")
    print ("2. -")
    print ("3. *")
    print ("4. /")
    print ("5. //")
    print ("6. %")
    print ("7. **")
    e()
    op = input("Digite o número ou operador que ira querer: ")
    l()
    if op == "1" or op == "+":
        print (f"{num1} + {num2} = {num1 + num2}")
        
    elif op == "2" or op == "-":
        print (f"{num1} - {num2} = {num1 - num2}")
        
    elif op == "3" or op == "*":
        print (f"{num1} x {num2} = {num1 * num2}")
        
    elif op == "4" or op == "/":
        print (f"{num1} / {num2} = {num1 / num2}")
        
    elif op == "5" or op == "//":
        print (f"{num1} // {num2} = {num1 // num2}")
        
    elif op == "6" or op == "%":
        print (f"{num1} % {num2} = {num1 % num2}")
        
    elif op == "7" or op == "**":
        print (f"{num1} ** {num2} = {num1 ** num2}")
        
    else:
        print ("Operador não encontrado! Tente novamente.")
        continue
    while True:
        
        l()
        e()
        novo_sn = input("Deseja continuar?\n\n1.Sim\n2.Não\n\nDigite o número ou a resposta aqui: ")
        l()
        e()
        sn = novo_sn.upper().strip()
        if sn == "1" or sn == "SIM":
            e()
            
            print ("Ótimo!")
            
            e()
            break
        elif sn == "2" or sn == "NÃO":
            e()
            l()
            print ("Tudo bem!")
            e()
            l()
            exit()
        else:
            e()
            l()
            print ("Não encontrado! Tente novamente")
            l()
            e()