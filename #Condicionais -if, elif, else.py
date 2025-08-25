# Condicionais -if, elif, else
'''
E ae Jhonatan, bora das uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo
'''
trabalho_terminado = False
if trabalho_terminado == True:
    print("Bora!")
else:
    print("Não posso sair!")

'''
Ei, você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?

Se eu estiver livre, sim. Mas se não der, pede para meu irmão te ajudar!
'''
estou_livre = input("Você está liver? [s/n]")
if estou_livre == "s":
    print ("Ok! Bora mover as caixas")
else:
    print ("Pede ajuda para o meu irmão") 

'''
Eu cheguei atrasado na aula, ainda posso entrar?

Se for a primeira ou segunda vez que você chega atrasado, pode sim.
Mas se for a terceira vez, você será suspenso
'''
atrasos = int(input("Quantas faltas você tem"))
if atrasos >=3:
    print ("Você está suspenso")
elif atrasos ==2:
    print ("Mais uma falta e você estará suspenso")
elif atrasos ==1:
    print ("Mais duas faltas e você estará suspenso")
else:
    print ("pode entrar")

    '''
    programa que recebe 2 valores e retorna o maior entre eles
    '''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    print ("O maior valor é: ", valor1)
else:
    print ("O maior valor é: ", valor2)