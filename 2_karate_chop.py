import unittest

class ChopTest(unittest.TestCase):

    def iterative_chop(self, value, arr):
        first = 0
        last = len(arr) - 1

        while first <= last:
            middle = (first + last) / 2

            if value == arr[middle]:
                return middle
            elif value > arr[middle]:
                first = middle + 1
            elif value < arr[middle]:
                last = middle - 1
        
        return -1

    def recursive_chop(self, value, arr, low=0, high=None):
        if high == None:
            high = len(arr) - 1

        if low > high:
            return -1

        middle = (low + high) / 2

        if value == arr[middle]:
            return middle
        elif value > arr[middle]:
            return self.recursive_chop(value, arr, middle+1, high)
        elif value < arr[middle]:
            return self.recursive_chop(value, arr, 0, middle-1)
        else:
            return -1

    def test_chop(self):
        self.run_tests_with(self.iterative_chop)
        self.run_tests_with(self.recursive_chop)

    def run_tests_with(self, chop_method):
        self.assertEqual(-1, chop_method(3, []))
        self.assertEqual(-1, chop_method(3, [1]))
        self.assertEqual(0,    chop_method(1, [1]))
        self.assertEqual(0,    chop_method(1, [1, 3, 5]))
        self.assertEqual(1,    chop_method(3, [1, 3, 5]))
        self.assertEqual(2,    chop_method(5, [1, 3, 5]))
        self.assertEqual(-1, chop_method(0, [1, 3, 5]))
        self.assertEqual(-1, chop_method(2, [1, 3, 5]))
        self.assertEqual(-1, chop_method(4, [1, 3, 5]))
        self.assertEqual(-1, chop_method(6, [1, 3, 5]))
        self.assertEqual(0,    chop_method(1, [1, 3, 5, 7]))
        self.assertEqual(1,    chop_method(3, [1, 3, 5, 7]))
        self.assertEqual(2,    chop_method(5, [1, 3, 5, 7]))
        self.assertEqual(3,    chop_method(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_method(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_method(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_method(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_method(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_method(8, [1, 3, 5, 7]))

if __name__ == '__main__':
        unittest.main()