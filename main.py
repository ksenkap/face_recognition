import random as r
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def histogram(s, n: object) -> object:
    name = "faces/s" + str(s) + "/" + str(n) + ".pgm"
    image = cv2.imread(name)
    hist, bins = np.histogram(image.ravel(), 64, [0, 256])
    return hist


def points_vector(s, n):
    global points
    name = "faces/s" + str(s) + "/" + str(n) + ".pgm"
    image = Image.open(name)
    pixels = image.load()
    p_vec=[]
    p_vec.clear()
    for p in range(len(points)):
        x, y = points[p].split()
        p_vec.append(pixels[int(x), int(y)])
    return p_vec


def compression(s, n):
    name = "faces/s" + str(s) + "/" + str(n) + ".pgm"
    image = Image.open(name)
    pixels = image.load()
    compress = []
    compress.clear()
    ch = 20
    for x in range(0, 92-92//ch, 92//ch):
        for y in range(0, 112-112//ch, 112//ch):
            s = 0
            w = x
            u = y
            while w < x+92//ch and u < y+112//ch:
                s += pixels[w, u]
                w += 1
                u += 1
            compress.append(s/((92//ch)*(112//ch)))
    return compress


def compare(v1, v2):
    sum = 0
    for k in range(len(v2)):
        sum += abs(v1[k] - v2[k])
    return sum


points = []
kp = 46
for i in range(0, 92-92//kp, 92 // kp):
    for j in range(0, 112-112//kp, 112 // kp):
        f = (r.randint(i, (i + 92 // kp)))
        e = (r.randint(j, (j + 112 // kp)))
        points.append(str(f)+" "+str(e))

kst = 3
standarts_h = []
standarts_p = []
standarts_c = []
used = []
for i in range(1, kst+1):
    for j in range(1, 41):
        standart_h = histogram(j, i)
        standarts_h.append(standart_h)

        standart_p = points_vector(j, i)
        standarts_p.append(standart_p)

        standart_c = compression(j, i)
        standarts_c.append(standart_c)

        used.append(str(j) + " " + str(i))

distances_histo = []
correct_histo = 0
distances_points = []
correct_points = 0
distances_compression = []
correct_compression = 0
correct_voting = 0

for i in range(400):
    folder = r.randint(1, 40)
    file = r.randint(1, 10)
    if (str(folder) + " " + str(file)) not in used:
        used.append(str(folder) + " " + str(file))

        pic_box = plt.figure(figsize=(10, 5))
        picture = cv2.imread("faces/s" + str(folder) + "/" + str(file) + ".pgm")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        pic_box.add_subplot(2, 5, 1)
        plt.imshow(picture)
        plt.axis('off')
        plt.text(-15, 125, 'Тестовое изображение')

        test_histo = histogram(folder, file)
        distances_histo.clear()
        for j in range(40 * kst):
            summ_histo = compare(test_histo, standarts_h[j])
            distances_histo.append(summ_histo)

        result_histo = distances_histo.index(min(distances_histo))
        while result_histo >= 40:
            result_histo -= 40

        if result_histo+1 == folder:
            correct_histo += 1

        picture = cv2.imread("faces/s" + str(result_histo+1) + "/1.pgm")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        pic_box.add_subplot(2, 5, 2)
        plt.imshow(picture)
        plt.axis('off')
        plt.text(-2, 125, 'Метод гистограмм')

        test_points = points_vector(folder, file)
        distances_points.clear()
        for j in range(40 * kst):
            summ_points = compare(test_points, standarts_p[j])
            distances_points.append(summ_points)

        result_points = distances_points.index(min(distances_points))
        while result_points >= 40:
            result_points -= 40

        if result_points + 1 == folder:
            correct_points += 1

        picture = cv2.imread("faces/s" + str(result_points+1) + "/1.pgm")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        pic_box.add_subplot(2, 5, 3)
        plt.imshow(picture)
        plt.axis('off')
        plt.text(0, 125, 'Метод случайных')
        plt.text(35, 135, 'точек')

        test_compression = compression(folder, file)

        distances_compression.clear()
        for j in range(40 * kst):
            summ_comprassion = compare(test_compression, standarts_c[j])
            distances_compression.append(summ_comprassion)

        result_compression = distances_compression.index(min(distances_compression))
        while result_compression >= 40:
            result_compression -= 40

        if result_compression + 1 == folder:
            correct_compression += 1

        picture = cv2.imread("faces/s" + str(result_compression+1) + "/1.pgm")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        pic_box.add_subplot(2, 5, 4)
        plt.imshow(picture)
        plt.axis('off')
        plt.text(10, 125, 'Метод сжатия')

        if result_compression==result_points or result_compression==result_histo:
            picture = cv2.imread("faces/s" + str(result_compression + 1) + "/1.pgm")
            picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
            pic_box.add_subplot(2, 5, 5)
            plt.imshow(picture)
            plt.axis('off')
            plt.text(15, 125, 'Голосование')
            result_voting = result_compression
        else:
            picture = cv2.imread("faces/s" + str(result_points + 1) + "/1.pgm")
            picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
            pic_box.add_subplot(2, 5, 5)
            plt.imshow(picture)
            plt.axis('off')
            plt.text(25, 125, 'Голосование')
            result_voting = result_points

        if result_voting + 1 == folder:
            correct_voting += 1

    plt.show()

print()
percent_histo = correct_histo / (len(used) - 40 * kst) * 100
percent_points = correct_points / (len(used) - 40 * kst) * 100
percent_compression = correct_compression / (len(used) - 40 * kst) * 100
percent_voting = correct_voting / (len(used) - 40 * kst) * 100
print(f"Точность метода гистограмм = {percent_histo:.2f}", "%")
print(f"Точность метода случайных точек = {percent_points:.2f}", "%")
print(f"Точность метода сжатия = {percent_compression:.2f}", "%")
print(f"Точность метода голосования = {percent_voting:.2f}", "%")