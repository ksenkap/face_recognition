import cv2
import matplotlib.pyplot as plt
import numpy as np
gist_results = [0 for i in range(360)]

def gist_one(path, g):
    img = cv2.imread(path,  cv2.IMREAD_GRAYSCALE)
    hist, bins = np.histogram(img.ravel(), 64, [0, 256])
    return hist


def gist_all(n, g):
    otvet = [[[] for i in range(10)] for j in range(n)]
    for j in range(n):
        otvet[j][0] = gist_one(f"faces/s{j+1}/1.pgm", g)
    for i in range(n):
        for h in range(9):
            otvet[i][h+1] = gist_one(f"faces/s{i+1}/{h+2}.pgm", g)
    return otvet

def sravnenie_gist(n, g):
    otvet = gist_all(n, g)
    pravilno = 0
    count = 0
    for i in range(n):
        for h in range(9):
            minimum = 100000000
            mesto = 0
            for j in range(n):
                gist1 = otvet[j][0]
                gist2 = otvet[i][h+1]
                raznica = 0
                for a in range(2 ** g):
                    raznica += abs(gist1[a] - gist2[a])
                if raznica < minimum:
                    mesto = j
                    minimum = raznica
            gist_results[i * 9 + h] = mesto
            if mesto == i:
                pravilno += 1
            count += 1


sravnenie_gist(40, 6)
x = np.arange(0, 64)
for i in range(40):
    for j in range(9):
        y = gist_one(f"faces/s{i+1}/1.pgm", 6)
        z = gist_one(f"faces/s{i+1}/{j+2}.pgm", 6)
        w = gist_one(f"faces/s{gist_results[i * 9 + j]+1}/1.pgm", 6)
        plt.plot(x, y, 'b') #эталон
        plt.plot(x, z, 'r') #тестовое
        plt.plot(x, w, 'g') #выбранная, если выбран не эталон
        plt.savefig(f"gist/{i + 1}.{j + 2}.png")
        plt.close()

