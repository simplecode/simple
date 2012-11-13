#!/usr/bin/env python
#coding: utf-8

#TODO: 1. Первый процесс генерирует списки целых чисел
#TODO: 2. ..и отдает их второму процессу, который сортирует их и добавляет количество делителей
#TODO: 3. ..и отдает 3-му процессу, который выводит их на экран

import random
from time import sleep
from multiprocessing import Process, Queue

def num_divisors(p):
    k = 0
    for i in xrange(2, p):
        if p % i == 0:
            k += 1
    return k

def add_divisors(lst):
    for i in xrange(len(lst)):
        d = num_divisors(lst[i])
        lst[i] = (lst[i], d)

def func_one(queue_out):
    print "start process one"
    p, q, m, n = 10000, 1000000, 10, 20
    for i in xrange(m):
        print "\t*"
        lst = list()
        for j in xrange(n):
            lst.append(random.randint(p, q))
        queue_out.put(lst)
    queue_out.put([])

def func_two(queue_in, queue_out):
    print "start process two"
    work = True
    while work:
        if not queue_in.empty():
            print "\t* *"
            lst = queue_in.get()
            if lst:
                lst.sort()
                add_divisors(lst)
            else:
                work = False
            queue_out.put(lst)

def func_three(queue_in):
    print "start process three"
    work = True
    while work:
        #print "\t* * *"
        if not queue_in.empty():
            lst = queue_in.get()
            if lst:
                print lst
            else:
                work = False

def main():
    queue_one = Queue()
    queue_two = Queue()

    proc_one = Process(target=func_one, args=(queue_one,))
    proc_one.daemon = True
    proc_one.start()

    #sleep(2)

    proc_two = Process(target=func_two, args=(queue_one, queue_two,))
    proc_two.daemon = True
    proc_two.start()

    proc_three = Process(target=func_three, args=(queue_two,))
    proc_three.daemon = True
    proc_three.start()

    proc_one.join()
    proc_two.join()
    proc_three.join()

if __name__ == '__main__':
    main()