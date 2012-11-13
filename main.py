#!/usr/bin/env python
#coding: utf-8

#TODO: 1. Первый процесс генерирует списки целых чисел
#TODO: 2. ..и отдает их второму процессу, который сортирует их
#TODO: 3. ..и отдает 3-му процессу, который выкидывает из них простые числа и выводит на экран

import random
from multiprocessing import Process, Queue

def func_one(queue_out):
    p, q, m, n = 10, 100, 5, 10
    for i in xrange(m):
        lst = list()
        for j in xrange(n):
            lst.append(random.randint(p, q))
        queue_out.put(lst)

def func_two(queue_in, queue_out):
    while not queue_in.empty():
        lst = queue_in.get()
        lst.sort()
        queue_out.put(lst)

def func_three(queue_in):
    while not queue_in.empty():
        lst = queue_in.get()
        print lst

def main():
    queue_one = Queue()
    queue_two = Queue()

    proc_one = Process(target=func_one, args=(queue_one))
    proc_one.daemon = True
    proc_one.start()

    proc_two = Process(target=func_two, args=(queue_one, queue_two))
    proc_two.daemon = True
    proc_two.start()

    proc_three = Process(target=func_three, args=(queue_two))
    proc_three.daemon = True
    proc_three.start()

    proc_one.join()
    proc_two.join()
    proc_three.join()

if __name__ == '__main__':
    main()