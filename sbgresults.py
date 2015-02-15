from sbg import maximize, predicted_survival


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
        self.actual = actual_survival.values()

        res = maximize(self.actual)
        alpha, beta = res.x

        self.alpha = alpha
        self.beta = beta
        self.predicted = predicted_survival(self.alpha, self.beta, t)

    def __repr__(self):
        return self.name