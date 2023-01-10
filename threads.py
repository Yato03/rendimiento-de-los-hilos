import threading
import requests
import os
import queue

import matplotlib.pyplot as plt

from helper import *

cola = queue.Queue()
counter = 1
maximum = 0

def fetch(url):
    r = requests.get(url)
    return r

def read_urls():
    with open ('urls.txt', 'r') as f:
        urls = f.readlines()
        urls = [url.replace('\n', '') for url in urls]
        return urls

def worker():
    global cola, counter, maximum

    while not cola.empty():
        try:
            url = cola.get()
            fetch(url)
        except:
            pass
        counter += 1

@crono
def hacer_fetch(number_threads=20):
    global cola, counter, maximum

    urls = read_urls()
    [cola.put(url) for url in urls]
    
    maximum = len(urls)

    thread_list = []

    for i in range(0,number_threads):
        thread_list.append(threading.Thread(target=worker))
    
    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

def test(rango=range(1,100, 10)):
    res = dict()
    for i in rango:
        print('Testing with {} threads'.format(i))
        value = hacer_fetch(i)
        print('Time: {}'.format(value))
        res[i] = value
        print('-'*20)
    return res

def hacer_grafico(diccionario):
    x = list(diccionario.keys())
    y = list(diccionario.values())
    plt.xlabel('Threads')
    plt.ylabel('Time')
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    diccionario = test()
    hacer_grafico(diccionario)
    

