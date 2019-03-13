import os
import multiprocessing
import glob

def worker(num):
    print('num', num)


if __name__ == '__main__':
    inDir = '/path/to/your/dir/'
    inTxtList = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
    number_of_workers = 4
    pool = multiprocessing.Pool(processes=number_of_workers)
    pool.map(worker,  inTxtList)
    pool.close()
    pool.join()
