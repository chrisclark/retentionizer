import unittest
from web import app
from utils import parse, plot_sbg_results


class SbgTestCase(unittest.TestCase):

    def test_predict(self):
        data = {'csvurl': './zoo/2.csv'}

        response = app.test_client().post('/predict', data=data)

        self.assertIn('Alpha', response.data)

    def test_predict_values(self):
        res = parse('zoo/2.csv', 0, 0, 0)

        # Regular
        self.assertAlmostEqual(res[0].alpha, 0.697, 3)
        self.assertAlmostEqual(res[0].beta, 1.169, 3)

        # High end
        self.assertAlmostEqual(res[1].alpha, 0.596, 3)
        self.assertAlmostEqual(res[1].beta, 3.327, 3)

    def test_plot(self):
        res = parse('zoo/2.csv', 0, 0, 0)
        script, div = plot_sbg_results(res)
        self.assertIn("<script", script)
        self.assertIn("<div", div)