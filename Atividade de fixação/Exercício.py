#Programa que ordena uma lista com o algoritmo buble sort e depois faz uma busca binária. 

#ordenar a lista com o buble sort
a=[91, 81,77,62,36,22,21,14,10,8,7,4]   #lista

for i in range(len(a)-1):               # "len(a)-1" ordena o elemento até o penúltimo número
    for j in range(i+1,len(a)):         #  percorre os elementos que não foram ordenados ainda
        if a[i]>a[j]:                   #  if usado para comparar os elementos
            a[i],a[j]=a[j],a[i]         #  se o if for verdadeiro troca-se a posição 
print(a)

#ínicio para a busca binária
inicio=0                                #inicio da busca
fim=len(a)-1                            #fim da busca
meio=(inicio+fim)//2                    #meio da lista
x=22                                    #valor do número que deve ser encontrado
while inicio<=fim and a[meio]!=x:     
    if x<=a[meio]:                      #verifica se o elemento do meio é == x
        fim=meio-1                      #restringe a busca
    else:
        inicio=meio+1                   #restringe a busca
    meio=(inicio+fim)//2                #repete essa condição para atender ao if e else
if a[meio]==x:
    print("Elemento encontrado", meio)
else:
    print("Elemento não encontrado")
print("Fim do programa!")

#Observação: 
# se colocar "<" é para colocar a lista em ordem descrescente e ">" coloca a lista em ordem crescente
# "a[meio]" = o número na posição do meio da lista