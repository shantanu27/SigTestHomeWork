from abc import abstractmethod


class MetricTest:

    @abstractmethod
    def calculate(self, listA, listB):
        pass
