import unittest
from fh import app
import json


class SbgTestCase(unittest.TestCase):

    def test_predict(self):
        data = {'csvurl': './zoo/2.csv'}

        response = app.test_client().post('/predict', data=data)

        self.assertIn('Alpha', response.data)

    def test_predict_values(self):
        from utils import parse
        res = parse('zoo/2.csv')

        # Regular
        self.assertAlmostEqual(res[0].alpha, 0.697, 3)
        self.assertAlmostEqual(res[0].beta, 1.169, 3)

        # High end
        self.assertAlmostEqual(res[1].alpha, 0.596, 3)
        self.assertAlmostEqual(res[1].beta, 3.327, 3)