#  Crie um programa para validar a entrada de atletas em uma competição olímpica. Para entrar, o atleta deverá ter entre 18 e 35 anos. Ele também precisa ter um bom condicionamento físico ou permissão médica. As condições devem ser feitas em uma única estrutura if

idade = int(input("Digite sua idade: "))

print ("1. Sim")
print ("2. Não")
permissao = int(input("Você tem pem permissão médica ou um bom condicionamento físico? Digite o número: "))
if 18 <= idade <= 35 and permissao == 1:
    print ("Você pode participar!")
else:
    print ("Não pode participar.")