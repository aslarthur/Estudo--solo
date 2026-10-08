# Crie um programa onde o preço do pão será guardado em uma variável. Após isso, o usuário digitará quanto dinheiro ele tem. Caso ele tenha dinheiro suficiente, uma mensagem será exibida informando que ele comprou o pão. Caso contrário, sla inventa uma mensagem ai kkkk

produto = "Pão"
valor_do_pao = 6.42
dinheiro = float(input("Digite quanto dinheiro você tem: "))
if dinheiro >= valor_do_pao:
    print ("Você comprou o pão")
else:
    valor = valor_do_pao - dinheiro
    
    print (f"Faltam R${valor:.2f} para você comprar o pão.")