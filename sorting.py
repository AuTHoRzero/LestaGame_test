'''

Для данного задания был выбран алгоритм быстрой сортировки,
на данный момент самый популярный и насколько мне известно самый быстрый алгоритм

'''
import random

def partition(array, begin, end):
    '''
    Данная вспомогательная функция сравнивает элем-ты массива,
    определяет pivot как начальный элемент списка и сравнивает все последующие элементы,
    если он меньше опорного, то данный элем-т будет перемещён
    '''
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    def _quicksort(array, begin, end):
        '''
        Данная функция выбирает опорный элем-т -> pivot,
        разбивает массив на 2 и рекурсивно вызывается, передавая новые списки
        '''
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)
