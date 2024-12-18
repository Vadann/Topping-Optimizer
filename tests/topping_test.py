import unittest
from models.topping import Topping


class TestTopping(unittest.TestCase):
    def setUp(self):
        self.topping = Topping({'type': 'raspberry', 'ATK': 2.8, 'Crit': 0.0, 'ATK_SPD': 2.5})

    def test_get_base_stat(self):
        result = self.topping.getBaseStats()
        self.assertEqual(result, 9)

    def test_get_stats_by_attribute(self):
        result = self.topping.getStatsByAttribute('ATK')
        self.assertEqual(result, 2.8)



if __name__ == '__main__':
    unittest.main()
