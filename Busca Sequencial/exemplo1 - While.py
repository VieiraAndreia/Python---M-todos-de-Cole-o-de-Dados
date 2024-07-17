#Programa que busca um elemento em uma lista
#USA A ESTRUTURA DE REPETIÇÃO "WHILE"

#linha 12: len = quantidade de elementos da lista

lista=[1,2,3,4,5,6,7,8,9,10]      # é preciso estabelecer os números da lista de início
resp="sim"
while True:       #loop se repete enquanto "resp"== sim
    achou=False    # utilizada para verificar se o número está na lista
    n=int(input("Digite um número para buscar na lista: "))
    cont=0   #representa a posição dos elementos
    while cont<len(lista):       #2° loop para buscar o elemento na lista
        if lista[cont]==n:    #verifica se o número que está na posição "cont" é igual ao número que foi digitado
            achou=True     #se o if for verdade 
            break          # programa para se condição for verdadeira
        cont+=1

#verifificação da busca e impressão do resultado
    if achou:     #variavel sozinha significa que está igualado a "TRUE"            
        print(f"O número {n} foi encontrado na lista!", cont+1)
    else:
        print(f"O número {n} não está na lista!")
        
    resp=input("Deseja buscar outro número?")
    if resp=="nao":
        break        # o loop para assim que a condição do if foi verdareira 
    print("Fim do programa!")