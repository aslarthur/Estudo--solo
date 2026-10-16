# === CAIXA ELETRÔNICO ===
# 1. Consultar saldo
# 2. Sacar dinheiro
# 3. Sair

# Escolha: 2
# Quanto deseja sacar? R$ 150

# Saque realizado!
# Saldo atual: R$ 350,00

def linha():
    print ('-=' * 68)
def espaco():
    print ()

saldo = 500

print (f"-=" * 5,"\033[1;3;4;32mCAIXA ELETRÔNICO\033[m", "-=" * 5)
espaco()
while True:
    opcoes = ["Consultar saldo", "Sacar dinheiro", "Sair"]
    for n, (a) in enumerate(opcoes, start=1):
        linha()
        print (f"{n}. {a}")
        linha()
    espaco()
    nova_escolha = input("Digite o número ou opção que deseja: ")
    linha()
    escolha = nova_escolha.upper().strip()
    if escolha == "1" or escolha == "CONSULTAR SALDO":
        print (f"Seu saldo total é de R${saldo:.2f}")
        linha()
    elif escolha == "2" or escolha == "SACAR DINHEIRO":
        dinheiro = float(input("Digite quanto dinheiro você quer sacar: R$"))
        linha()
        if dinheiro <= 0:
            print ("Digite um valor maior que zero!")
        elif dinheiro > saldo:
            print ("Você não tem esse valor!")
        else:
            saldo -= dinheiro
            print (f"Saque de R${dinheiro:.2f} realizado!")
            linha()
            print (f"Saldo atual: R${saldo:.2f}")
    elif escolha == "3" or escolha == "SAIR":
        linha()
        print ("Tenha um ótimo dia!")
        break
    else:
        print ("Opção inválida!")
        continue
    while True:
        espaco()
        print ("Deseja continuar?")
        print ("1. Sim")
        print ("2. Não")
        espaco()
        son = input("Digite o número ou resposta aqui: ")
        if son == "2":
            break
        elif son == "1":
            break
        else:
            print ("Não encontrado! Tente novamente.")
    if son == "2":
        break