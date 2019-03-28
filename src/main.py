from b_search import binary_search
from index_search import index_search
from linear_search import linear_search
from interpolation_search import interpolation_search
import matplotlib.pyplot as plt
import time
import random
import pandas as pd

def time_check(choice: str, ite: int):
    l = []
    lim = 1000000
    if choice == 'sorted':
        for i in range(lim):
            l.append(random.randint(0, lim))
        l.sort()

    elif choice == 'normalized':
        for i in range(lim):
            l.append(i)

    inter_time = []
    seq_time = []
    bnry_time = []
    indexed_time = []

    inter_counter = []
    seq_counter = []
    bnry_counter = []
    indexed_counter = []

    for i in range(0, ite):
        value = random.randint(0, lim)
        if(choice == 'normalized'):
            start1 = time.clock()
            counter1 = interpolation_search(l, value)
            end1 = time.clock()
            time1 = end1 - start1
            inter_time.append(time1)
            inter_counter.append(counter1)
            

        start2 = time.clock()
        counter2 = linear_search(l, value)
        end2 = time.clock()
        time2 = end2 - start2
        seq_time.append(time2)
        seq_counter.append(counter2)
        

        start3 = time.clock()
        counter3 = binary_search(l, value)
        end3 = time.clock()
        time3 = end3 - start3
        bnry_time.append(time3)
        bnry_counter.append(counter3)
        

        start4 = time.clock()
        counter4 = index_search(l, value)
        end4 = time.clock()
        time4 = end4 - start4
        indexed_time.append(time4)
        indexed_counter.append(counter4)
        
    #print(seq_counter.shape)
    plt.title("Counter x Number of searchs")
    plt.xlabel('Steps')
    plt.ylabel('Number of searchs')
    if len(inter_time) != 0:
        plt.subplot(2, 2, 1)
        plt.hist(inter_counter,  color='red', label='interpolation')
        plt.xlabel('Steps')
        plt.ylabel('Number of searchs')
        plt.legend()
        plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.hist(seq_counter,  color='green', label='sequential')
    plt.xlabel('Steps')
    plt.ylabel('Number of searchs')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.hist(bnry_counter,  color='blue', label='binary')
    plt.xlabel('Steps')
    plt.ylabel('Number of searchs')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.hist(indexed_counter,  color='purple', label='indexed')
    plt.xlabel('Steps')
    plt.ylabel('Number of searchs')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.title("Number of searchs x Time")
    plt.xlabel('Number of searchs')
    plt.ylabel('Time')
    if len(inter_time) != 0:
        plt.plot(inter_time,  color='red', label='interpolation')
    plt.plot(seq_time,  color='green', label='sequential')
    plt.plot(bnry_time,  color='blue', label='binary')
    plt.plot(indexed_time,  color='purple', label='indexed')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print("Chose a initialization method: normalized or sorted")
    method = input()
    print("Chose a specified number of iterations")
    it = int(input())

    time_check(method, it)