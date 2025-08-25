# GerenciadordeLoginSimples

'''
Gerenciador de login simples, com o máximo de 3 tentativas. 
(Apenas um único usuário e senha permitidos)

Usuário - paulanunes
senha - senha123

Após 3 tentativas, após 3 tentativas. se o usuário errar, exibir:
"Aguarde 30 minutos antes de tentar novamente!"

Se o usuário acertar a senha antes disso, exibir "Login feito com sucesso!"
'''

usuario =""
senha =""
tentativas = 0

while (usuario != "paulanunes" and senha != "senha123") and tentativas < 3:
    usuario = input ("Digite seu usuário: ")
    senha = input ("Digite sua senha: ")
    tentativas += 1

if usuario != "paulanunes" and senha != "senha123":
    print ("Aguarde 30 minutos nates de tentar novamente")
else:
    print ("Login feito")
