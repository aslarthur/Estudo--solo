#DEF:
def l():
    print ("-=" * 65)
def e():
    print ()
while True:
    l()
    print (f"\033[4;1;31mSeja muito bem vindo(a)\033[m\033[4;1;32m ao \033[m\033[4;1;33mmeu programa!\033[m")
    l()
    print (f"\033[4;1;31mP\033[m\033[4;1;32mR\033[m\033[4;1;33mO\033[m\033[4;1;34mG\033[m\033[4;1;35mR\033[m\033[4;1;36mA\033[4;1;31m\033[4;1;32mM\033[m\033[4;1;33mA\033[4;1;34mS\033[m:")
    e()
    print (f"1. \033[4;1;31mTabuada\033[m")
    print (f"2  \033[4;1;32mCalculadora\033[m")
    print (f"3. \033[4;1;33mDobro\033[m \033[1;4;34me\033[m \033[1;4;35mtriplo\033[m")
    print (f"4. \033[1;4;34mMédia\033[m \033[1;4;31mde\033[m \033[1;4;32mnotas\033[m")
    print (f"5. \033[1;4;35mReais\033[m \033[1;4;33m para \033[m \033[1;4;34mdolar\033[m")
    print (f"6. \033[1;4;36mPar\033[m \033[1;4;32m ou \033[m \033[1;4;32mímpar\033[m")
    print (f"7. \033[1;4;31mCoffee\033[m \033[1;4;32mShop\033[m")
    print (f"8. \033[1;4;33mLista\033[m \033[1;4;34mDe\033[m \033[1;4;35mCompras\033[m")
    print (f"9. \033[1;4;36mSortear\033[m \033[31maluno\033[m")
    print (f"10. \033[1;4;32mAdivinhar\033[m \033[1;4;33mnúmero\033[m")
    print (f"11. \033[1;4;34mCofre\033[m")
    print (f"12. \033[1;4;35mSistema\033[m \033[1;4;36mde\033[m \033[1;4;31mcores\033[m")
    print (f"13. \033[1;4;32mConfirmar\033[m \033[1;4;33midade\033[m")
    print (f"14. \033[1;4;34mCadastro\033[m \033[1;4;35m com \033[m \033[1;4;36mconfirmação\033[m")
    print (f"15. \033[1;4;31mAnalisar\033[m \033[1;4;32mnome\033[m")
    print (f"16. \033[1;4;36mTEMPORIZADOR\033[m")
    e()
    nova_cor = input("Digite o número ou o programa que ira querer: ")
    cor = nova_cor.upper().strip()
    if cor == "1" or cor == "TABUADA":
        l()
        print (f"Que legal, você escolheu a \033[1;4;31mtabuada\033[m")
        l()
        número = float(input("Digite um número: "))
        
        for n in range (1, 11):
            l()
            print (f"\033[1;31m{número}\033[m \033[1;35mx\033[m \033[1;32m{n}\033[m \033[1;34m=\033[m \033[1;33m{número * n}\033[m")
            l()
    elif cor == "2" or cor == "CALCULADORA":
        l()
        print (f"Que legal, você escolheu a \033[1;4;32mcalculadora\033[m!")
        l()
        num1 = float(input("Digite um número: "))
        l()
        num2 = float(input("Digite outro número: "))
        l()
        e()
        print (f"\033[1;4;31mO\033[m\033[1;4;32mP\033[m\033[1;4;33mE\033[m\033[1;4;34mR\033[m\033[1;4;35mA\033[m\033[1;4;36mD\033[m\033[1;4;31mO\033[m\033[1;4;32mR\033[m\033[1;4;33mE\033[m\033[1;4;34mS\033[m:")
        e()
        print ("1. +")
        print ("2. -")
        print ("3. *")
        print ("4. /")
        print ("5. //")
        print ("6. %")
        e()
        while True:
            operador = input("Digite o número ou operador que ira querer: ")
            if operador == "1" or operador == "+":
                l()
                print (f"{num1} + {num2} = {num1 + num2}")
                l()
                break
            elif operador == "2" or operador == "-":
                l()
                print (f"{num1} - {num2} = {num1 - num2}")
                l()
                break
            elif operador == "3" or operador == "*":
                l()
                print (f"{num1} x {num2} = {num1 * num2}")
                l()
                break
            elif operador == "4" or operador == "/":
                l()
                print (f"{num1} / {num2} = {num1 / num2}")
                l()
                break
            elif operador == "5" or operador == "//":
                l()
                print (f"{num1} // {num2} = {num1 // num2}")
                l()
                break
            elif operador == "6" or operador == "%":
                l()
                print (f"{num1} % {num2} = {num1 % num2}")
                l()
                break
            else:
                l()
                print ("Operador não encontrado. Tente novamente!")
                l()
                continue
    elif cor == "3" or cor == "DOBRO E TRIPLO":
        l()
        print (f"Que legal! Você escolheu \033[4;1;33mDobro\033[m \033[1;4;34me\033[m \033[1;4;35mtriplo\033[m")
        l()
        num1 = float(input("Digite um número: "))
        l()
        print (f"O dobro de {num1} é {num1 * 2}")
        l()
        print (f"O triplo de {num1} é {num1 * 3}")
        l()
    elif cor == "4" or cor == "MÉDIA DE NOTAS":
        l()
        print ("Que legal! Você escolheu \033[1;4;34mMédia\033[m \033[1;4;31mde\033[m \033[1;4;32mnotas\033[m")
        l()
        nota1 = float(input("Digite sua primeira nota: "))
        l()
        nota2 = float(input("Digite sua segunda nota: "))
        nota_final = (nota1 + nota2) / 2
        l()
        print (f"O total é de {nota_final}")
        l()
        if nota_final >= 7:
            print ("Você passou!")
            l()
        elif nota_final >=4:
            print ("Você está de recuperação!")
            l()
        else:
            print ("Reprovou.")
    elif cor == "5" or cor == "REAIS PARA DOLAR":
        l()
        print (f"Que legal! Você escolheu \033[1;4;35mReais\033[m \033[1;4;33m para \033[m \033[1;4;34mdolar\033[m")
        l()
        real = float(input("Digite quantos reais você tem: R$"))
        l()
        dolar = real / 5.02
        l()
        print (f"Com R${real} você consegue comprar US${dolar:.2f}")
        l()
    elif cor == "6" or cor == "PAR OU ÍMPAR":
        l()
        print (f"Que legal! Você escolheu \033[1;4;36mPar\033[m \033[1;4;32m ou \033[m \033[1;4;32mímpar\033[m")
        l()
        num1 = int(input("Digite um número: "))
        if num1 %2 == 0:
            l()
            print (f"O número {num1} é \033[31mPAR\033[m")
            l()
        else:
            print (f"O número {num1} é \033[32mÍMPAR\033[m")
    elif cor == "7" or cor == "COFFEE SHOP":
        l()
        print (f"Que legal! Você escolheu \033[1;4;31mCoffee\033[m \033[1;4;32mShop\033[m")
        l()
        print (f"\033[1;4;31mP\033[m\033[1;4;32mR\033[m\033[1;4;33mO\033[m\033[1;4;34mD\033[m\033[1;4;35mU\033[m\033[1;4;36mT\033[m\033[1;4;31mO\033[m\033[1;4;32mS\033[m: ")
        e()
        
        produtos_e_precos = {"Pão": 5.23, 
                        "Sonho": 4.23, 
                        "Pão de queijo": 3.37, 
                        "Baquete": 4.92
                    }
        for p, v in produtos_e_precos.items():
                
                print (f"{p} R${v:.2f}")
        while True:
            e()
            novo_produto = input("Digite o produto que ira querer: ")
            l()
            quantidade =  int(input("Digite a quantidade: "))
            l()
            produto = novo_produto.upper().strip()
            if produto == "PÃO":
                print (f"O total é de R${quantidade * produtos_e_precos['Pão']:.2f}")
                break
            elif produto == "SONHO":
                print (f"O total é de R${quantidade * produtos_e_precos['Sonho']:.2f}")
                break
            elif produto == "PÃO DE QUEIJO":
                print (f"O total é de R${quantidade * produtos_e_precos['Pão de queijo']:.2f}")
                break
            elif produto == "BAQUETE":
                print (f"O total é de R${quantidade * produtos_e_precos['Baquete']:.2f}")
                break
            else:
                print ("Não encontrado. Tente novamente!")
                continue
    elif cor == "8" or cor == "LISTA DE COMPRAS":
        l()
        print (f"Que legal! Você escolheu \033[1;4;33mLista\033[m \033[1;4;34mDe\033[m \033[1;4;35mCompras\033[m")  
        l()
        p1 = input("Digite o primeiro produto: ")
        l()
        v1 = float(input(f"Digite o valor de {p1} R$"))
        l()
        p2 = input("Digite o segundo produto: ") 
        l()  
        v2 = float(input(f"Digite o valor de {p2} R$"))
        l()
        p3 = input("Digite o terceiro produto: ")
        l()
        v3 = float(input(f"Digite o valor de {p3} R$"))
        l()
        p4 = input("Digite o quarto produto: ")
        l()
        v4 = float(input(f"Digite o valor de {p4} R$: "))
        l()
        p5 = input("Digite o quinto produto: ")  
        l()
        v5 = float(input(f"Digite o valor de {p5} R$"))      
        l()
        print (f"O valor total do produto {p1}, {p2}, {p3}, {p4}, {p5} é de R${v1 + v2 + v3 + v4 + v5}")
        l()
    elif cor == "9" or cor == "SORTEAR ALUNO":
        from random import choice
        l()
        print (f"Que legal! Você escolheu \033[1;4;36mSortear\033[m \033[31maluno\033[m")
        l()
        n1 = input("Digite o primeiro nome: ")
        l()
        n2 = input("Digite o segundo nome: ")
        l()
        n3 = input("Digite o terceiro nome: ")
        l()
        n4 = input("Digite o quarto aluno: ")
        l()
        n5 = input("Digite o quanto aluno: ")
        l()
        lista = [n1, n2, n3, n4, n5]
        aluno_sorteado = choice(lista)
        print (f"O aluno sorteado foi {aluno_sorteado}")
    elif cor == "10" or cor == "ADIVINHAR NÚMERO":
        from random import choice
        l()
        print (f"Que legal! Você escolheu \033[1;4;32mAdivinhar\033[m \033[1;4;33mnúmero\033[m")
        l()
        lista = [1, 2, 3, 4, 5 , 6, 7, 8 , 9, 10]
        escolhido = choice(lista)
        num = int(input("Digite um número de 1 a 10: "))
        l()
        if num == escolhido:
            print (f"\033[1;4;32mVocê ganhou de mim!\033[m")
        elif num != escolhido:
            print (f"\033[1;4;31mEu ganhei de você! Eu pensei no número {escolhido}\033[m")
    elif cor == "11" or cor == "COFRE":
        l()
        print (f"Que legal! Você escolheu \033[1;4;34mCofre\033[m")
        l()
        senha_secreta = "BIVJD"
        tentativas = 3
        while tentativas >0:
            l()
            senha = input("Digite sua senha: ")
            l()
            if senha != senha_secreta:
                
                tentativas -= 1
                print (f"Senha incorreta! Você tem {tentativas} tentativas")
                if tentativas == 0:
                            print ("Cofre trancado!")
                            break
                continue
            
            elif senha == senha_secreta:
                print ("Você acertou! Cofre liberado.")
                break
    elif cor == "12" or cor == "SISTEMA DE CORES":
        while True:
            l()
            print (f"Que legal! Você escolheu \033[1;4;35mSistema\033[m \033[1;4;36mde\033[m \033[1;4;31mcores\033[m")
            l()
            print (f"\033[1;4;31mT\033[m\033[1;4;32mE\033[m\033[1;4;33mX\033[m\033[1;4;35mT\033[m\033[1;4;36mO\033[m\033[1;4;31mS\033[m:")
            e()
            print (f"1. \033[1;4;37mBranco\033[m")
            print (f"2. \033[1;4;31mVermelho\033[m")
            print (f"3. \033[1;4;32mVerde\033[m")
            print (f"4. \033[1;4;33mAmarelo\033[m")
            print (f"5. \033[1;4;34mAzul\033[m")
            print (f"6. \033[1;4;35mRoxo\033[m")    
            print (f"7. \033[1;4;36mAzul claro\033[m")
            print (f"8. \033[1;4;30mCinza\033[m")
            e()
            while True:
                nova_cor = input("Digite o número ou a cor que ira querer: ")
                cor = nova_cor.upper().strip()
                if cor == "1" or cor == "BRANCO":
                    cod = "37"
                    txt = "BRANCO"
                elif cor == "2" or cor == "VERMELHO":
                    cod = "31"
                    txt = "VERMELHO"
                elif cor == "3" or cor == "VERDE":
                    cod = "32"
                    txt = "VERDE"
                elif cor == "4" or cor == "AMARELO":
                    cod = "33"
                    txt = "AMARELO"
                elif cor == "5" or cor == "AZUL":
                    cod = "34"
                    txt = "AZUL"
                elif cor == "6" or cor == "ROXO":
                    cod = "35"
                    txt = "ROXO"
                elif cor == "7" or cor == "AZUL CLARO":
                    cod = "36"
                    txt = "AZUL CLARO"
                elif cor == "8" or cor == "CINZA":
                    cod = "30"
                    txt = "CINZA"
                else:
                    l()
                    print ("Não encontrado! Tente novamente.")
                    l()
                    continue
                e()
                print (f"\033[1;4;37;41mF\033[m\033[1;4;37;42mU\033[m\033[1;4;37;43mN\033[m\033[1;4;37;44mD\033[m\033[1;4;37;45mO\033[m\033[1;4;37;46mS\033[m: ")
                e()
                print (f"1. \033[1;4;37;47mBranco\033[m")
                print (f"2. \033[1;4;37;41mVermelho\033[m")
                print (f"3. \033[1;4;37;42mVerde\033[m")
                print (f"4. \033[1;4;37;43mAmarelo\033[m")
                print (f"5. \033[1;4;37;44mRoxo\033[m")
                print (f"6. \033[1;4;37;45mAzul\033[m")
                print (f"7. \033[1;4;37;46mAzul claro\033[m")
                print (f"8. \033[1;4;37;40mCinza\033[m")
                e()
                novo_fundo = input("Digite o número ou a cor do fundo que ira querer: ")  
                e()     
                fundo = novo_fundo.upper().strip() 
                l()
                if fundo == "1" or fundo == "BRANCO":
                    print (f"\033[1;4;{cod};47mFUNDO: BRANCO COR: {txt}\033[m")
                    break
                elif fundo == "2" or fundo == "VERMELHO":
                    print (f"\033[1;4;{cod};41mFUNDO: VERMELHO COR: {txt}\033[m")
                    break
                elif fundo == "3" or fundo == "VERDE":
                    print (f"\033[1;4;{cod};42mFUNDO: VERDE COR: {txt}\033[m")
                    break
                elif fundo == "4" or fundo == "AMARELO":
                    print (f"\033[1;4;{cod};43mFUNDO: AMARELO COR: {txt}\033[m")
                    break
                elif fundo == "5" or fundo == "ROXO":
                    print (f"\033[1;4;{cod};44mFUNDO: ROXO COR: {txt}\033[m")
                    break
                elif fundo == "6" or fundo == "AZUL":
                    print (f"\033[1;4;{cod};45mFUNDO: AZUL COR: {txt}\033[m") 
                    break
                elif fundo == "7" or fundo == "AZUL CLARO":
                    print (f"\033[1;4;{cod};46mFUNDO: AZUL CLARO COR: {txt}\033[m")
                    break
                elif fundo == "8" or fundo == "CINZA":
                    print (f"\033[1;4;{cod};40mFUNDO: CINZA COR: {txt}\033[m")
                    break
                else:
                    print ("Não encontrado! Tente novamente.")
                break
            break    
    elif cor == "13" or cor == "CONFIRMAR IDADE":
        l()
        print (f"Que legal! Você escolheu \033[1;4;32mConfirmar\033[m \033[1;4;33midade\033[m")
        l()
        idade = int(input("Digite sua idade: "))
        l()
        if idade <= 17:
            print ("Tu é de menó")
        elif 18 <= idade <= 30:
            print ("Marromeno")
        elif idade >= 31:
            print ("Tu é de maio")
    elif cor == "14" or cor == "CADASTRO COM CONFIRMAÇÃO":
        l()
        print ("Que legal! Você escolheu \033[1;4;34mCadastro\033[m \033[1;4;35m com \033[m \033[1;4;36mconfirmação\033[m")
        l()
        
        email = input("Digite seu email: ")
        while True:
            l()
            senha = input("Digite sua senha: ")
            l()
            confirmacao = input("Confirme sua senha: ")
            l()
            if confirmacao != senha:
                print ("Senha incorreta! Tente novamente.")
                l()
            elif confirmacao == senha:
                print ("Senha correta! Acesso liberado")
                break
    elif cor == "15" or cor == "ANALISAR NOME":
        l()
        print (f"Que legal! Você escolheu \033[1;4;31mAnalisar\033[m \033[1;4;32mnome\033[m")
        l()
        nome = input("Digite seu nome: ")
        
        l()
        e()
        print (f"Em maiúsculo: {nome.upper()}")
        print (f"Em minúsculo: {nome.lower()}")
        print (f"Escrito normalmente: {nome.title()}")
        print (f"Quantas letras tem no total: {len (nome.replace (' ', ''))}")
        e()
    elif cor == "16" or cor == "TEMPORIZADOR":
        l()
        tmp = int(input("Digite quantos segundos você quer: "))
        l()
        from time import sleep
        sleep(tmp)
        print (f"O tempo de {tmp} segundos acabou!")
    l()
    print ("Deseja continuar?")
    while True:
        l()
        print ("1. Sim")
        l()
        print ("2. Não")
        l()
        novo_son = input("Digite o número ou a resposta aqui: ")
        son = novo_son.upper().strip()
        if son == "1" or son == "SIM":
            l()
            print ("Ótimo!")
            l()
            break
        elif son == "2" or son == "NÃO":
            l()
            print ("Tudo bem. Até a próxima!") 
            l()
            exit()
        else:
            print ("Não encontrado! Tente novamente.")
            l()
            novo_son = input("Digite o número da resposta aqui: ")
            continue