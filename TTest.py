from MetricTest import MetricTest
from scipy.stats import ttest_ind


class TTest(MetricTest):

    def calculate(self, listA, listB):
        value, pvalue = ttest_ind(listA, listB)
        return pvalue
