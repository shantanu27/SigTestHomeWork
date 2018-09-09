from MetricTest import MetricTest
from scipy.stats import wilcoxon


class WilcoxonTest(MetricTest):

    def calculate(self, listA, listB):
        value, pvalue = wilcoxon(listA, listB)
        return pvalue
