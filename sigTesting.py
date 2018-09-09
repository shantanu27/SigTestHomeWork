from collections import OrderedDict

from numpy import genfromtxt
import csv

from KSTest import KSTest
from MeanDiff import MeanDiff
from TTest import TTest
from WilcoxonTest import WilcoxonTest


class SignificanceTesting(object):
    def __init__(self, filePath):
        self.filePath = filePath
        self.loadData()

    def loadData(self):
        self.models_scores = ['Baseline_R2', 'Baseline+Fusion_R2', 'Baseline+Ordering_R2',
                              'Baseline+Ordering+Fusion_R2', 'Baseline_RSU4', 'Baseline+Fusion_RSU4',
                              'Baseline+Ordering_RSU4', 'Baseline+Ordering+Fusion_RSU4']
        self.data = genfromtxt(self.filePath, delimiter=',')[1:].T
        self.significanceMetrics_rouge2 = {'Baseline & Fusion': (0, 1),
                                           'Baseline & Ordering': (0, 2),
                                           'Fusion & Ordering': (1, 2),
                                           'Baseline & Ordering+Fusion': (0, 3),
                                           'Ordering & Ordering+Fusion': (2, 3),
                                           'Fusion & Ordering+Fusion': (1, 3)}
        self.significanceMetrics_rouge2 = OrderedDict(self.significanceMetrics_rouge2)
        self.significanceMetrics_rougesu4 = {'Baseline & Fusion': (4, 5),
                                             'Baseline & Ordering': (4, 6),
                                             'Fusion & Ordering': (5, 6),
                                             'Baseline & Ordering+Fusion': (4, 7),
                                             'Ordering & Ordering+Fusion': (6, 7),
                                             'Fusion & Ordering+Fusion': (5, 7)}
        self.significanceMetrics_rougesu4 = OrderedDict(self.significanceMetrics_rougesu4)

    def writeOutput(self):
        resultsFile = open('SigTestResults.csv', 'w')
        w = 6
        h = 13
        resultsData = [[0 for x in range(w)] for y in range(h)]
        resultsData[0] = ['metric', 'model', 'mean diff', 'P(T test)', 'P(wilcoxon test)', 'P(ks test)']
        for row in xrange(1, 7):
            resultsData[row][0] = 'ROUGE-2'
        for row in xrange(7, 13):
            resultsData[row][0] = 'ROUGE-SU4'

        self.calculateMetrics(resultsData)

        with resultsFile:
            writer = csv.writer(resultsFile)
            writer.writerows(resultsData)
        resultsFile.close()
        return resultsData

    def calculateMetrics(self, resultsData):

        md = MeanDiff()
        tt = TTest()
        wx = WilcoxonTest()
        ks = KSTest()

        for i, key in enumerate(self.significanceMetrics_rouge2):
            v = self.significanceMetrics_rouge2[key]
            resultsData[i+1][1] = key
            resultsData[i+1][2] = md.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+1][3] = tt.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+1][4] = wx.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+1][5] = ks.calculate(self.data[v[0]], self.data[v[1]])

        for i, key in enumerate(self.significanceMetrics_rougesu4):
            v = self.significanceMetrics_rougesu4[key]
            resultsData[i+7][1] = key
            resultsData[i+7][2] = md.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+7][3] = tt.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+7][4] = wx.calculate(self.data[v[0]], self.data[v[1]])
            resultsData[i+7][5] = ks.calculate(self.data[v[0]], self.data[v[1]])


if __name__ == '__main__':
    filePath = "ROUGE_SCORES.csv"
    sigInstance = SignificanceTesting(filePath)

    results = sigInstance.writeOutput()

