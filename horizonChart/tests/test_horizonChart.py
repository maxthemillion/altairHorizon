import unittest
import pandas as pd
import numpy as np
from ..horizonChart import HorizonChartGenerator


class TestHorizonChartGenerator(unittest.TestCase):
    def setUp(self):
        self.x = 'x'
        self.y = 'y'
        dateRange = pd.date_range(
            start='2015-01-01',
            end='2015-01-07',
            freq='D')
        values = [-30, -10, -5, 1, 5, 10, 20]
        self.data = pd.DataFrame(
            {
                self.x: dateRange,
                self.y: values
            })
        self.noLevels = 3
        self.testClass = HorizonChartGenerator(
            self.data, self.x, self.y, self.noLevels)

    def test_setDomain_absolute(self):
        self.assertEqual(np.sum(np.array(self.testClass._setDomain()) < 0), 0)

    def test_setDomain_exact(self):
        self.assertEqual(self.testClass._setDomain(), [0, 10])

    def test_generate(self):
        self.assert
