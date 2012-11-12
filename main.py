#!/usr/bin/env python
#coding: utf-8

#TODO: 1. Главный процесс генерирует списки целых чисел
#TODO: 2. ..и отдает их второму процессу, который сортирует их
#TODO: 3. ..и отдает 3-му процессу, который выкидывает из них простые числа и выводит на экран

import random
from multiprocessing import Queue

def main():
    queue_one = Queue()
    queue_two = Queue()

    # генерация m списков по n целых элементов в диапазоне (p, q)
    p = 10
    q = 100
    m = 5
    n = 10
    for i in xrange(m):
        temp_list = list()
        for j in xrange(n):
            temp_list.append(random.randint(p, q))
        print temp_list
        queue_one.put(temp_list)

if __name__ == '__main__':
    main()