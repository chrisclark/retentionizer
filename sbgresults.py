from sbg import maximize, predicted_survival, derl
import numpy as np


class SbgResults(object):

    def __init__(self, cohort_name, actual_survival, t, discount, value):
        """
        :param actual_survival: {t0: survive%, t1: survive%, ..., tn: survive%}
        """
        self.name = cohort_name
        self.discount = discount
        self.value = value
        self.t = t
        self._actual = actual_survival
        self.actual = [a for a in actual_survival.values() if not np.isnan(a)]

        res = maximize(self.actual[1:])
        alpha, beta = res.x

        self.alpha = alpha
        self.beta = beta

    @property
    def predicted(self):
        return ([1] + predicted_survival(self.alpha, self.beta, len(self._actual) + self.t - 1))

    @property
    def dltv(self):
        return ((derl(self.alpha, self.beta, self.discount, 0)/(1 + self.discount)) + 1) * self.value

    def __repr__(self):
        return self.name