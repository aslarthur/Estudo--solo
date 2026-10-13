def l():
    print ("-=" *50)
def e():
    print ()
padaria = "Padaria Bella Paulista"
l()
print (f"Bem vindo a padaria {padaria}! ")
total = 0 
while True: 
    l()
    print ("PRODUTOS: ")
    e()
    produtos = {"Pão": 3.21, "Sonho": 5.23, "Pão de queijo": 2.23}
    ir = 0.5
    
    for n, (a, b) in enumerate(produtos.items(), start=1):
        
        print (f"{n}. {a} R${b:.2f}")
    e()
    l()
    nova_entrada = input("Digite o número ou produto que ira querer: ")
    quantidade = int(input("Digite a quantidade que ira querer: "))
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
        
    else: 
        print ("Produto não encontrado! Tente novamente.")
        break
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
    if sim_ou_nao == "1" or sim_ou_nao == "SIM":
        continue
    else:

        break
taxa = 7.31
viagem = 8.12
total += taxa + viagem
e()
print (f"O total é de R${total:.2f}")