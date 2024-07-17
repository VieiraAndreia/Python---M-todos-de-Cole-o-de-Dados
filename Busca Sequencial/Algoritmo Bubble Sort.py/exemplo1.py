#Programa que ordena uma lista usando o algoritmo de ordenação Buble Sort

a=[5,4,3,2,1]    #lista

for i in range(len(a)-1):           # "len(a)-1" ordena o elemento até o penúltimo número
    for j in range(i+1,len(a)):     #  percorre os elementos que não foram ordenados ainda
        if a[i]>a[j]:               #  if usado para comparar os elementos
            a[i],a[j]=a[j],a[i]     #  se o if for verdadeiro troca-se a posição 
print(a)

#Observação: 
# se colocar "<" é para colocar a lista em ordem descrescente e ">" coloca a lista em ordem crescente