import random
import unittest

from course_one.karatsuba_mult import multiply


class KaratsubaMultiplicationTest(unittest.TestCase):
    def test_unary(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(1, 121), 121)
        self.assertEqual(multiply(121, 1), 121)

    def test_zero(self):
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(-1, 0), 0)
        self.assertEqual(multiply(0, -1), 0)

    def test_negative(self):
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-123456789, 987654321), -121932631112635269)
        self.assertEqual(multiply(123456789, -987654321), -121932631112635269)
        self.assertEqual(multiply(-123456789, -987654321), 121932631112635269)

    def test_random(self):
        a = 1000000000
        n = 1000
        for x, y, in zip(random.sample(range(-a, a), n), random.sample(range(-a, a), n)):
            self.assertEqual(multiply(x, y), x * y)

    def test_large(self):
        large_product = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
        self.assertEqual(
            multiply(
                3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627
            ),
            large_product,
        )
        self.assertEqual(
            multiply(
                -3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627
            ),
            -large_product,
        )
