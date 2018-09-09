from MetricTest import MetricTest
from scipy import stats


class MeanDiff(MetricTest):

    def calculate(self, listA, listB):
        mean_la = stats.tmean(listA)
        mean_lb = stats.tmean(listB)
        return mean_la - mean_lb
