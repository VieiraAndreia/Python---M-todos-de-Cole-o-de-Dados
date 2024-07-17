#Programa que busca um elemento em uma lista
#OBS: POSSIBILIDADE DE USAR 'IN' PARA PROCURAR UM ASSUNTO, ELE PODE SER  SUBSTITUIDO PELA A ESTRUTURA DE REPETIÇÃO "FOR"

lista=[1,2,3,4,5,6,7,8,9,10]  # é preciso estabelecer os números da lista de início
resp="sim"

while True:         #loop se repete enquanto "resp"== sim
    n=int(input("Digite um número para buscar na lista: "))
    if n in lista:    # busca o número digitado na lista                      
        print(f"O número {n} está na lista!")
    else:              # quando o número digitado não está na lista
        print(f"O numero {n} não está na lista!")
    resp=input("Deseja buscar outro número?")
    if resp=="não":         
        break        # o loop para assim que a condição do if foi verdareira
    print("Fim do programa!")