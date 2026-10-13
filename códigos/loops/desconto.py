desconto = 10
precos = [1.92, 8.29, 2.38, 91.92]
for preco in precos:
    novo = preco - (preco * desconto) / 100
    print (f"De R${preco:.2f} para R${novo:.2f}")