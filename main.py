# EX1
from operator import index


def fatorial(num):
    if num <= 1:
        return 1
    return num * fatorial(num - 1)


def soma_lista(lista, ind_lista = 0):
    if ind_lista >= len(lista):
        return 0
    return lista[ind_lista] + soma_lista(lista, ind_lista + 1)

def busca_binaria(lista, resp, ini = 0, fim = None):
    if not fim:
        fim = len(lista) - 1
    if fim >= ini:
        ind_chute = ((ini+fim)//2)
        if lista[ind_chute] == resp:
            return ind_chute
        elif lista[ind_chute] < resp:
            ini = ind_chute + 1
        else:
            fim = ind_chute - 1
        return busca_binaria(lista, resp, ini, fim)
    raise IndexError(f'{resp} não esta na lista')

def fibo(num):
    if num == 1 or num == 2:
        return 1
    return fibo(num-1) + fibo(num -2)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    lista_menores = [elem for elem in lista if elem < pivo]
    lista_maiores = [elem for elem in lista if elem > pivo]
    menores = quick_sort(lista_menores)
    maiores = quick_sort(lista_maiores)
    return menores + [pivo] + maiores

def acha_menor(lista):
    index_menor = 0
    menor = lista[index_menor]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor = lista[i]
            index_menor = i
    return index_menor

def selection_sort(lista):
    for i in range(len(lista)):
        index_menor = acha_menor(lista[i:]) +i
        aux = lista[i]
        lista[i] = lista[index_menor]
        lista[index_menor] = aux
    return lista

print(selection_sort([3,1,2,4,-1]))
