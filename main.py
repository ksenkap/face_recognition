import random as r
import cv2
import numpy as np
import tkinter
from tkinter import *
import time
from PIL import Image, ImageTk


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
    p_vec = []
    p_vec.clear()
    for p in range(len(points)):
        x, y = points[p][0], points[p][1]
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

def showimage(mylbl,path): #Функция отображения Lebel изображения в интерфейсе
    img = Image.open(path) # Открывваем изображение с помощью библиотеки PIL
    img = ImageTk.PhotoImage(img)
    mylbl.config(image=img) # Присваиваем Лейбел наше изображение
    mylbl.image = img
    mylbl.pack(side=LEFT) # Отрисовываем лейбел с параметром лево,чтобы изображения были в строчку

def showtext(mylbl):
    mylbl.pack(side=LEFT) #Отрисовываем лейбел текст

def stop():
    time.sleep(6)

def printing(i):
    global a
    k, g = map(int, a[i][0].split())
    #showimage(label0, "empty.png")
    showimage(label1, f"faces/s{k}/{g}.pgm")
    showimage(label2, f"faces/s{k}/1.pgm")
    showimage(label3, f"faces/s{a[i][1]+1}/1.pgm")
    showimage(label4, f"faces/s{a[i][2] + 1}/1.pgm")
    showimage(label5, f"faces/s{a[i][3] + 1}/1.pgm")
    showimage(label6, f"faces/s{a[i][4] + 1}/1.pgm")
    showtext(l1txt)
    showtext(l2txt)
    showtext(l3txt)
    showtext(l4txt)
    showtext(l5txt)
    showtext(l6txt)
    showimage(label11, f"gist/{k}.{g}.png")
    showimage(label12, f"rand_points/{k}.{g}.pgm")
    showimage(label13, f"mash/{k}.{g}.pgm")
    showtext(l1txt1)
    showtext(l2txt1)
    showtext(l3txt1)
    if i<len(a)-1:
        root.after(1000, printing, i+1)



points = [[2, 0], [1, 5], [3, 9], [3, 14], [3, 20], [0, 20], [4, 26], [1, 31], [3, 36], [0, 36], [4, 40], [2, 45], [4, 48], [0, 56], [3, 59], [0, 62], [2, 66], [2, 72], [3, 74], [4, 77], [3, 80], [4, 84], [2, 90], [0, 92], [3, 99], [0, 100], [2, 107], [7, 1], [7, 7], [5, 11], [6, 16], [4, 20], [7, 23], [4, 25], [5, 28], [8, 34], [4, 38], [8, 42], [7, 44], [6, 50], [8, 52], [8, 56], [6, 60], [5, 64], [6, 68], [5, 74], [8, 80], [8, 82], [5, 85], [5, 92], [8, 92], [5, 99], [7, 100], [8, 104], [11, 1], [9, 6], [10, 12], [9, 13], [9, 20], [10, 23], [12, 28], [11, 31], [9, 36], [12, 37], [8, 41], [11, 46], [11, 52], [10, 56], [10, 57], [10, 62], [10, 66], [8, 70], [10, 72], [11, 76], [11, 80], [8, 86], [11, 88], [12, 95], [9, 96], [9, 100], [8, 108], [14, 1], [13, 5], [12, 8], [14, 14], [12, 17], [14, 22], [14, 25], [13, 29], [16, 35], [15, 37], [13, 43], [13, 48], [14, 49], [14, 52], [14, 57], [15, 61], [13, 64], [13, 69], [12, 76], [15, 76], [16, 83], [15, 87], [12, 91], [12, 94], [14, 97], [15, 103], [16, 105], [19, 1], [19, 5], [17, 12], [16, 13], [19, 17], [17, 23], [16, 27], [20, 31], [19, 33], [20, 36], [19, 42], [16, 46], [20, 50], [16, 55], [19, 58], [16, 61], [20, 67], [18, 69], [17, 76], [16, 79], [20, 83], [18, 85], [17, 90], [19, 93], [20, 100], [16, 104], [18, 105], [23, 4], [21, 7], [23, 11], [21, 15], [24, 19], [21, 20], [24, 28], [23, 35], [24, 40], [23, 44], [23, 48], [20, 48], [20, 53], [21, 56], [23, 62], [24, 66], [21, 70], [20, 73], [22, 76], [22, 84], [22, 86], [20, 92], [22, 92], [22, 102], [22, 105], [28, 0], [26, 4], [26, 11], [28, 15], [28, 20], [25, 23], [28, 25], [28, 28], [25, 32], [28, 37], [28, 44], [25, 45], [24, 50], [24, 52], [27, 58], [25, 61], [27, 64], [28, 72], [24, 75], [28, 76], [27, 81], [28, 87], [27, 88], [24, 93], [28, 100], [25, 101], [25, 108], [30, 0], [30, 7], [31, 11], [32, 13], [32, 19], [28, 24], [31, 28], [29, 32], [31, 36], [29, 40], [32, 41], [28, 47], [31, 52], [28, 53], [28, 57], [31, 61], [29, 64], [28, 68], [29, 75], [30, 80], [29, 88], [30, 88], [30, 93], [30, 99], [31, 100], [30, 108], [33, 0], [32, 7], [36, 8], [33, 14], [32, 20], [36, 21], [36, 24], [33, 29], [32, 32], [33, 37], [36, 40], [35, 45], [35, 49], [34, 54], [32, 57], [36, 63], [32, 68], [34, 72], [36, 75], [33, 77], [36, 84], [33, 88], [34, 91], [35, 96], [36, 99], [34, 103], [36, 106], [38, 2], [40, 7], [38, 8], [37, 15], [38, 19], [36, 20], [40, 27], [40, 32], [39, 35], [38, 36], [38, 41], [39, 46], [38, 52], [40, 56], [36, 61], [40, 68], [38, 70], [38, 72], [40, 78], [38, 81], [40, 87], [39, 88], [37, 94], [39, 97], [39, 103], [39, 106], [43, 1], [40, 6], [43, 11], [40, 15], [42, 16], [44, 21], [44, 27], [41, 29], [41, 34], [41, 39], [42, 40], [44, 45], [44, 49], [40, 53], [41, 57], [43, 61], [41, 65], [43, 70], [43, 75], [44, 78], [42, 84], [42, 88], [42, 90], [40, 96], [42, 97], [42, 101], [41, 108], [48, 4], [45, 4], [45, 9], [44, 13], [45, 19], [46, 24], [44, 24], [45, 30], [44, 34], [45, 40], [48, 43], [44, 46], [47, 50], [47, 56], [48, 59], [44, 63], [47, 67], [48, 68], [44, 73], [44, 76], [47, 83], [44, 88], [46, 92], [45, 97], [48, 102], [46, 108], [51, 3], [49, 6], [48, 9], [52, 12], [49, 16], [49, 22], [49, 27], [48, 30], [52, 34], [48, 37], [52, 42], [51, 47], [48, 52], [49, 52], [49, 57], [50, 63], [49, 65], [51, 69], [50, 76], [51, 78], [52, 80], [51, 87], [48, 91], [48, 92], [51, 98], [49, 100], [49, 107], [56, 4], [54, 10], [56, 13], [56, 19], [56, 21], [56, 28], [55, 29], [54, 35], [54, 37], [54, 40], [55, 48], [54, 51], [52, 56], [56, 57], [55, 61], [56, 67], [56, 71], [56, 74], [53, 80], [55, 81], [54, 87], [55, 92], [55, 93], [55, 98], [54, 100], [53, 108], [60, 4], [57, 12], [59, 13], [60, 17], [58, 22], [57, 27], [58, 30], [59, 36], [56, 38], [58, 43], [57, 44], [58, 48], [57, 54], [56, 58], [60, 61], [57, 67], [58, 72], [57, 75], [59, 77], [57, 82], [56, 86], [60, 92], [59, 94], [56, 97], [59, 100], [58, 107], [62, 1], [60, 6], [61, 11], [61, 16], [60, 20], [62, 22], [64, 26], [60, 29], [62, 34], [61, 40], [60, 41], [61, 48], [62, 48], [61, 52], [60, 59], [64, 60], [64, 66], [62, 71], [60, 72], [61, 80], [62, 84], [63, 86], [64, 90], [64, 93], [60, 96], [61, 103], [60, 105], [64, 2], [66, 7], [68, 12], [65, 16], [65, 19], [65, 22], [68, 26], [65, 32], [64, 32], [65, 37], [67, 44], [64, 48], [67, 50], [67, 56], [66, 56], [65, 63], [65, 68], [65, 72], [66, 77], [64, 84], [68, 88], [66, 89], [68, 96], [64, 96], [66, 104], [64, 108], [69, 1], [72, 5], [70, 12], [70, 15], [69, 17], [69, 24], [70, 26], [68, 29], [70, 34], [68, 37], [72, 42], [70, 46], [69, 50], [68, 52], [70, 59], [69, 60], [71, 64], [72, 68], [71, 72], [69, 77], [72, 84], [71, 90], [68, 95], [71, 100], [69, 101], [69, 104], [72, 1], [73, 5], [73, 10], [73, 13], [75, 16], [75, 22], [75, 28], [75, 29], [74, 35], [73, 39], [76, 42], [74, 48], [74, 50], [72, 52], [75, 56], [76, 60], [73, 68], [73, 71], [73, 74], [74, 78], [75, 82], [74, 90], [73, 93], [73, 98], [76, 100], [75, 105], [77, 3], [76, 5], [76, 11], [77, 15], [79, 17], [77, 21], [79, 27], [78, 31], [80, 32], [76, 36], [78, 42], [76, 46], [77, 51], [77, 56], [77, 60], [78, 63], [79, 66], [79, 71], [78, 74], [79, 80], [76, 84], [77, 86], [78, 88], [79, 94], [77, 99], [79, 104], [77, 108], [84, 1], [81, 5], [83, 12], [83, 13], [82, 16], [82, 20], [82, 27], [82, 30], [83, 32], [82, 39], [84, 44], [81, 45], [81, 50], [83, 54], [82, 56], [80, 63], [80, 67], [84, 68], [84, 73], [84, 80], [80, 80], [80, 85], [84, 92], [81, 95], [83, 100], [84, 104], [87, 2], [87, 7], [86, 10], [85, 16], [88, 19], [85, 24], [84, 24], [86, 32], [86, 35], [87, 36], [87, 43], [87, 47], [86, 52], [86, 56], [84, 56], [84, 61], [86, 65], [87, 69], [88, 76], [87, 77], [86, 84], [87, 85], [85, 91], [84, 96], [86, 97], [87, 102], [85, 106]]
"""points = []
p_y = []
kp = 23
for i in range(0, 92-92//kp, 92 // kp):
    for j in range(0, 112-112//kp, 112 // kp):
        f = (r.randint(i, (i + 92 // kp)))
        e = (r.randint(j, (j + 112 // kp)))
        p_y.append([e, f])
        points.append(str(f)+" "+str(e))
for i in range(len(points)):
    p = []
    p.append(int(points[i].split()[0]))
    p.append(int(points[i].split()[1]))
    points[i] = p
poin = []
for i in points:
    if i not in poin:
        poin.append(i)
print(len(poin))
print(poin)"""

print("Введите количество эталонов в каждом классе: ")
kst = int(input())
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
answers = []
for i in range(400):
    folder = r.randint(1, 40)
    file = r.randint(1, 10)
    if (str(folder) + " " + str(file)) not in used:
        used.append(str(folder) + " " + str(file))
        answer = []
        answer.append(str(folder) + " " + str(file))

        test_histo = histogram(folder, file)
        distances_histo.clear()
        for j in range(40 * kst):
            summ_histo = compare(test_histo, standarts_h[j])
            distances_histo.append(summ_histo)
        result_histo = distances_histo.index(min(distances_histo))
        while result_histo >= 40:
            result_histo -= 40
        answer.append(result_histo)
        if result_histo+1 == folder:
            correct_histo += 1

        test_points = points_vector(folder, file)
        distances_points.clear()
        for j in range(40 * kst):
            summ_points = compare(test_points, standarts_p[j])
            distances_points.append(summ_points)
        result_points = distances_points.index(min(distances_points))
        while result_points >= 40:
            result_points -= 40
        answer.append(result_points)
        if result_points + 1 == folder:
            correct_points += 1

        test_compression = compression(folder, file)
        distances_compression.clear()
        for j in range(40 * kst):
            summ_comprassion = compare(test_compression, standarts_c[j])
            distances_compression.append(summ_comprassion)
        result_compression = distances_compression.index(min(distances_compression))
        while result_compression >= 40:
            result_compression -= 40
        answer.append(result_compression)
        if result_compression + 1 == folder:
            correct_compression += 1

        if result_compression == result_points or result_compression == result_histo:
            result_voting = result_compression
        else:
            result_voting = result_compression
        answer.append(result_voting)
        if result_voting + 1 == folder:
            correct_voting += 1
        answers.append(answer)

percent_histo = correct_histo / (len(used) - 40 * kst) * 100
percent_points = correct_points / (len(used) - 40 * kst) * 100
percent_compression = correct_compression / (len(used) - 40 * kst) * 100
percent_voting = correct_voting / (len(used) - 40 * kst) * 100
print(f"Точность метода гистограмм = {percent_histo:.2f}", "%")
print(f"Точность метода случайных точек = {percent_points:.2f}", "%")
print(f"Точность метода сжатия = {percent_compression:.2f}", "%")
print(f"Точность метода голосования = {percent_voting:.2f}", "%")
print("Обработано изображений: ", len(used))


a = answers
root = Tk()
root.title("Faces")
root.geometry("1000x750")
frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)
f_top = Frame(root)
f_bot = Frame(root)
label0 = Label(f_top)
label1 = Label(f_top)
label2 = Label(f_top)
label3 = Label(f_top)
label4 = Label(f_top)
label5 = Label(f_top)
label6 = Label(f_top)
l1txt = Label(f_bot, width=10, text="Тестовое")
l2txt = Label(f_bot, width=17, text="Эталон")
l3txt = Label(f_bot, width=13, text="Гистограммы")
l4txt = Label(f_bot, width=13, text="Точки")
l5txt = Label(f_bot, width=10, text="Сжатие")
l6txt = Label(f_bot, width=20, text="Голосование")

f_top.pack()
f_bot.pack()
f1_top = Frame(root)
f1_bot = Frame(root)
label11 = Label(f1_top)
label12 = Label(f1_top)
label13 = Label(f1_top)
l1txt1 = Label(f1_bot, width=90, text="Гистограмма (кр.-тестовое, зел.-эталон, син.-выбранная, если выбран не эталон)")
l2txt1 = Label(f1_bot, width=10, text="Точки")
l3txt1 = Label(f1_bot, width=10, text="Сжатие")


f1_top.pack()
f1_bot.pack()
btn1 = Button(frm, text="Stop", command=lambda: stop())
btn1.pack(side=tkinter.LEFT, padx=40)

btn2 = Button(frm, text="Exit", command=lambda: exit()) # кнопка выхода с присвоенной ей функцией выхода
btn2.pack(side=tkinter.LEFT, padx=40)

root.after_idle(printing, 0) # start loop
root.after(60*100000, root.destroy)
root.mainloop()