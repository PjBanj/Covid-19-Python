import sys
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import numpy
import pylab as p
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math
import pandas as pd
# from urllib.request import urlopen
# except ImportError:
#     # Fall back to Python 2's urllib2
#     from urllib2 import urlopen

# class window(QMainWindow):
     
#      def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50, 50, 100, 100)
#         self.setWindowTitle('Covid-19 Stats')
#         self.home()

# def home(self):
#     btn = QPushButton('Generate', self)
#     btn.clicked.connect(self.generate_graph)
#     self.show()

def expGrowth(x, a, b, c):
        return a*numpy.exp(b*x)+c

def func(t,a,b):
        return a+b*numpy.log(t)

def CSVintoDict():
    url = 'https://github.com/nytimes/covid-19-data/blob/master/us-states.csv'
    # response = urlopen(url)
    reader = pd.read_csv(r'C:\Users\PJ\Documents\My Web Sites\CoronaVirus\us-states.csv')
    # reader = pd.read_csv(r'C:\Users\PJ\Documents\My Web Sites\CoronaVirus\us-states.csv',header=1, error_bad_lines=False)

    states =  reader.groupby(['date','state']).agg({'cases': 'sum', 'deaths': 'sum'})
    stats =  reader.groupby(['date']).agg({'cases': 'sum', 'deaths': 'sum'})
    days = numpy.empty(40)
    b = numpy.arange(1, 41)
    ind = numpy.arange(len(days))
    numpy.put(days, ind, b)
    casesUS = stats['cases'].as_matrix()
    deathsUS = stats['deaths'].as_matrix() 
    cases = []
    deaths = []
    idx = 0

    for x in casesUS:
        if idx==0:
            cases.append(0)
            deaths.append(0)
        else:
            cases.append(casesUS[idx] - casesUS[idx-1])
            deaths.append(deathsUS[idx] - deathsUS[idx-1])
        idx = idx+1
    
    print(cases)
    print(deaths)

    idx = 0

    return days, cases[47:], deaths[47:]

# days = numpy.empty(32)
# b = numpy.arange(1, 33)
# ind = numpy.arange(len(days))
# numpy.put(days, ind, b)

# xValues=numpy.array([1,2,3,4,5,6,7, 8,9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21 , 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
# yValues = numpy.array([60846, 75698, 93842, 112470, 130478, 151980, 179446, 203788, 234768, 258214])
# totalCases = numpy.array([53, 80, 98, 164, 214, 279, 423, 647, 937, 1215, 1629, 1896, 2234, 3487, 4226, 7038, 10442, 15219, 18747, 24583, 33404,	44183, 54453, 68440, 85356, 103321, 122653,	140904,	163539,	186101,	213144,	239279])
# print(totalCases.size)
# print(xValues.size)
#totalCases = numpy.array([1, 1,	2,	2,	5,	5,	5,	5,	5,	7,	8,	8,	11,	11,	11,	11,	11,	11,	11,	11,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	15,	15,	15,	15,	16,	16,	24,	30,	53,	80,	98,	164,	214,	279,	423,	647,	937,	1215,	1629,	1896,	2234,	3487,	4226,	7038,	10442,	15219,	18747,	24583,	33404,	44183,	54453,	68440,	85356,	103321,	122653,	140904,	163539,	186101,	213144,	239279])


# print(xValues)
# print(totalCases)

def plot(days, cases, deaths):
    zValues=numpy.array([838,1102,1428,1876,2314, 2793, 3539, 4503, 5586, 6600])
    p0 = numpy.random.exponential(size=3)
    bounds = (0, [50000., 3., 1000000000.])
    #(a,b,c,),cov = opt.curve_fit(logGrowth, xValues, yValues, bounds=bounds, p0=p0)
    popt, pcov = opt.curve_fit(func, days, cases, maxfev=100000)
    plt.subplot(2, 1, 1)
    plt.plot(days, cases, '.-')
    plt.title('Real Data of CoronaVirus in US')
    plt.xlabel('Last 40 days')
    plt.ylabel('New Cases per Day')
    plt.subplot(2, 1, 2)
    plt.plot(days, deaths, '.-')
    plt.xlabel('Last 40 Days')
    plt.ylabel('New Deaths per Day')
    print(*popt)
    # plt.plot(days, func(days, *popt))
    plt.show();


days, cases, deaths = CSVintoDict()
print(days)
print(cases)
print(deaths)
plot(days, cases, deaths)

 
 
 