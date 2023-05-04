import unittest
import price_info as pif

class MyTestCase(unittest.TestCase):
    def test_something(self):
        price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90,
                      'papaya': 2.95, 'pomegranate': 4.95}

        quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1,
                         'pomegranate': 2}
        self.assertEqual(pif.total_cost_shopping(), 20.6)  # add assertion here
        self.assertEqual(pif.cost_of_fruits('apple', 10), 12)  # add assertion here

if __name__ == '__main__':
    unittest.main()
