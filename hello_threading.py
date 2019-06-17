import threading
from multiprocessing import Process


def calculate():
    for i in range(300000):
        print('Square i = {}'.format(i**2))
        global count
        count += 1
    global flag
    flag = True

def stat():
    while flag == False:
        print('Count of calculations: {}.'.format(count))
    if flag == True:
        print('Calculations is finished. Total count is {} calculations.'.format(count))

if __name__ == '__main__':
    flag = False
    count = 0

    t1 = threading.Thread(target=calculate)
    t2 = threading.Thread(target=stat)
    # t1 = Process(target=calculate)
    # t2 = Process(target=stat)

    t1.start()
    t2.start()

    t1.join()
    t2.join()