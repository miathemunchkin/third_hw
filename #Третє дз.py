#Третє дз
#Перша частина: Многопотокове копіювання файлів

import os
import shutil
from multiprocessing.pool import ThreadPool

def copy_files(source_dir, target_dir='dist'):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    def copy_file(file):
        extension = os.path.splitext(file)[1][1:]
        dest_folder = os.path.join(target_dir, extension)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.copy(os.path.join(source_dir, file), dest_folder)

    def process_directory(root, files):
        for file in files:
            copy_file(os.path.relpath(os.path.join(root, file), source_dir))

    with ThreadPool() as pool:
        for root, dirs, files in os.walk(source_dir):
            pool.apply_async(process_directory, args=(root, files))

#Друга частина: Паралельне факторизація чисел

import multiprocessing

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    with multiprocessing.Pool() as pool:
        return pool.map(factorize_number, numbers)

a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

print("All tests passed successfully!")