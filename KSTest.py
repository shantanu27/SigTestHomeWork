from MetricTest import MetricTest
from scipy.stats import ks_2samp


class KSTest(MetricTest):

    def calculate(self, listA, listB):
        value, pvalue = ks_2samp(listA, listB)
        return pvalue
