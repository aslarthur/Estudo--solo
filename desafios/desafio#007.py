# Crie uma variável “horário” e exiba uma mensagem de cumprimento relativa ao horário: “Bom dia”, “Boa tarde” etc.
while True:
    print ("Manhã")
    print ("Tarde")
    print ("Noite")
    novo_horario = input("Digite qual horário você está: ")
    horario = novo_horario.upper().strip()
    if horario == "MANHÃ":
        print ("Bom dia!")
        break
    elif horario == "TARDE":
        print ("Boa tarde!")
        break
    elif horario == "NOITE":
        print ("Boa noite!")
        break
    else:
        print ("Não encontrado! Tente novamente")
        continue