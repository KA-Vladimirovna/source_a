import os
import numpy as np

from keras.utils import to_categorical

def make_labels():
    dirs = np.array([i for i in os.listdir() if os.path.isdir(i)])

    labels = np.arange(0, len(dirs), 1)

    category = to_categorical(labels)

    '''with open('labels_indices.csv', 'w') as fout:
        for i in range(len(dirs)):
            s = dirs[i] + ',' + str(labels[i]) + '\n'
            print(s)
            fout.write(s)
    '''

    np.savetxt('labels.csv', category, delimiter=',', fmt='%u')

    a = {}

    for i in range(len(dirs)):
        a[dirs[i]] = category[i]

    return a

def read_file(fname):
    print(fname)

    result = None

    with open(fname) as fin:
        result = fin.read()

    return result

def read_all_files(path):
    print(path)
    dirs = np.array([i for i in os.listdir(path) if os.path.isdir(i)])

    print(len(dirs))

    data = []

    files = np.array([i for i in os.listdir(path) if os.path.isfile(i)])


    for i in files:
        data.append(read_file(path + '\\' + i))


    if len(dirs) != 0:
            for i in dirs:
                data.extend(read_all_files(path + '\\' + i))


    return data

def one_hot(char, n = 256):
    result = np.zeros(n, dtype=np.uint8)
    result[ord(char)] = 1
    return result

def text_to_one_hot(text):
    result = []

    for i in text:
        result.append(one_hot(i))

    return np.array(result)

'''a = read_all_files(os.getcwd())

print(len(a))


print(os.getcwd())'''

fname = '1.cpp'

a = read_file(fname)

b = text_to_one_hot(a)

np.savetxt(fname + '_onehot.csv', b, delimiter=',')


