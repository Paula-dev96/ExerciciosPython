# While

''' Syntaxe
while condição:
 #Código a ser executado
'''

# criar um programa que permite 3 tentativas, nates de fechar
tentativas = 0
while tentativas < 3:
    print("Tente novamente")
    tentativas = tentativas + 1

'''
Quando queremos que uma ação continue acontecendo, até que um critério seja satisfeito
só pode logar, se digitar a senha correta.
'''

senha =""
while senha != "123456":
    senha = input ("Digite a senha correta: ")

print ("Bem-vindo ao sistema")

#garantir que algo esteja preenchido
#só deve continuar, quando o usuário informar o seu nome

nome = ""
while nome == "":
    nome = input ("Digite o seu nome: ")

print(f"Bem vindo {nome}")

#Contador dentro do while
#Ser avisado as 17h para ver o por do sol

horario = 0
while horario <=17:
    print (horario)
    horario = horario + 1

print ("Hora de ver o por do sol")