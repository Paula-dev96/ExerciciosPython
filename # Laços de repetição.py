# Laços de repetição
'''
for item in range(3):
    print(item)

For item in coleção
    #comandos
'''
# Range não inclui o último número
# (1,10,2) nessa disposição, o primeiro núemro representa o inícios, o segundo quantas numeros mostrarão, terceiro, pular de..
'''
for item in range(10):
    print (item)
'''

#for item in range (2,12,2):
   # print (item)

'''
idades = [13, 15, 18, 30, 50, 75]
#Exiba somente maiores de idade
for idade in idades:
    if idade >= 18:
        print (f"{idade} é maior de idade")
    else:
        print (f"{idade} é menor de idade")
'''

# len(variavel) -> quantidade de caracteres
    #len (senha -> 6 ou não)
senhas = ["abc", "segura123", "12345", "python123", "oi"]
for senha in senhas:
    if len(senha) >=6:
        print (f"A senha {senha} é válida")
    else:
        print (f"A senha {senha} deve possuir 6 ou mais caracteres")


    