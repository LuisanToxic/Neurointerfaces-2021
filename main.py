import matplotlib.pyplot as plit
from scipy.signal import savgol_filter
from statistics import mean
import math
import os


file = open('data/21_5_2021_13_53_39_EEG.dat', 'r')

# перенос данных из файла
dataX = []
dataY =[]
while (True):
    try:
        temp = list(map(float, file.readline().split()))
        dataX.append(temp[0])
        dataY.append(temp[1])
    except:
        break



# первое сглаживание
smoothY = savgol_filter(dataY, 51, 3)
graf = plit.plot(dataX, smoothY)
plit.show()

# перенос точек в одну сторону и перенос графика к нулю
pa = 150 #pointAccuracy
for i in range(round(smoothY.size / pa)):
    if max(smoothY[i*pa : (i+1)*pa]) - min(smoothY[i*pa : (i+1)*pa]) < 0.25:
        meanOfFunk = mean(smoothY[i*pa : (i+1)*pa])
        break

centeredY = []
for i in smoothY:
    if i >= meanOfFunk:
        centeredY.append(i - meanOfFunk)
    else:
        centeredY.append(meanOfFunk - i)

graf = plit.plot(dataX, centeredY)
plit.show()


# большее сглаживание
avg = mean(centeredY)

trigY = []
for i in centeredY:
    trigY.append(math.exp(pow(-i, 2))-1)

graf = plit.plot(dataX, trigY)
plit.show()

# второе сглаживание
res = savgol_filter(trigY, 51, 3)
graf = plit.plot(dataX, res)
plit.show()
