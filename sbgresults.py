from sbg import maximize, predicted_survival
import numpy as np


class SbgResults(object):

    def __init__(self, cohort_name, actual_survival, t=12):
        """

        :param alpha:
        :param beta:
        :param cohort: {t0: survive%, t1: survive%, ..., tn: survive%}
        :return:
        """
        self.name = cohort_name
        self._actual = actual_survival
        self.actual = [a for a in actual_survival.values() if not np.isnan(a)]

        res = maximize(self.actual[1:])
        alpha, beta = res.x

        self.alpha = alpha
        self.beta = beta
        self.predicted = ([1] + predicted_survival(self.alpha, self.beta, t))

    def __repr__(self):
        return self.name