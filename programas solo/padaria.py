def l():
    print ("-=" *50)
def e():
    print ()
padaria = "Padaria Bella Paulista"
l()
print (f"\033[4;1;3;32mBem vindo a padaria {padaria}!\033[m ")
total = 0 
while True: 
    l()
    print (f"\033[1;4;3;31mP\033[m\033[4;1;3;32mR\033[m\033[4;1;3;33mO\033[m\033[4;1;3;34mD\033[m\033[4;1;3;35mU\033[m\033[4;1;3;36mT\033[m\033[4;1;3;31mO\033[m\033[4;1;3;32mS\033[m: ")
    e()
    produtos = {'Pão': 3.21, 'Sonho': 5.23, 'Pão de queijo': 2.23, 'Coxinha': 3.12, 'Quibe': 3.12 }
    ir = 0.5
    
    for n, (a, b) in enumerate(produtos.items(), start=1):
        
        print (f"{n}. {a} R${b:.2f}")
    e()
    l()
    nova_entrada = input("Digite o número ou produto que deseja: ")
    quantidade = int(input("Digite a quantidade que deseja: "))
    entrada = nova_entrada.upper().strip()
     
    if entrada == "1" or entrada == "PÃO":
        total += produtos ['Pão'] * quantidade
        total += ((produtos ['Pão'] * quantidade)  *ir /100)
        
    elif entrada == "2" or entrada == "SONHO":
        total += produtos ['Sonho']* quantidade
        total += ((produtos ['Sonho'] * quantidade)* ir / 100)
        
    elif entrada == "3" or entrada == "PÃO DE QUEIJO":
        total += produtos ['Pão de queijo'] * quantidade
        total += ((produtos ['Pão de queijo'] * quantidade) * ir / 100)

    elif entrada == "4" or entrada == "COXINHA":
        total += produtos ['Coxinha'] * quantidade
        total += ((produtos ['Coxinha'] * quantidade) * ir / 100)
    else: 
        print ("Produto não encontrado! Tente novamente.")
        continue

    while True:
        e()
        print ("Algo mais?")
        l()
        print ("1. Sim")
        l()
        print ("2. Não")
        l()
        novo_sim_ou_nao = input("Digite o número ou a resposta aqui: ")
        l()
        sim_ou_nao = novo_sim_ou_nao.upper().strip()
        if sim_ou_nao == "2" or sim_ou_nao == "NÃO":
            l()
            print (f"\033[1;3;4;32mTudo bem!\033[m")
            break
        elif sim_ou_nao == "1" or sim_ou_nao == "SIM":
            l()
            print (f"\033[1;4;3;32mÓtimo!\033[m")
            break
        else:
            print ("Não encontrado! Tente novamente.")
            l()
    if sim_ou_nao == "2" or sim_ou_nao == "NÃO":
        break        

    
taxa = 7.31
viagem = 8.12
total += taxa + viagem
e()
l()
print (f"O total é de R${total:.2f}")
l()