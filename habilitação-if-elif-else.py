print("-------------------")
print("---Habilitação-----")
print("-------------------")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Parabéns ", nome, "Você já pode tirar sua habilitação!")
elif idade == 17:
    print("Aguarde ", nome, ", em breve você poderá estar habilitado!")
else:
    idade <= 16
    print(nome, "você ainda não pode tirar habilitação!")
