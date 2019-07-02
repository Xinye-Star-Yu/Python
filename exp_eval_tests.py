# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_General_Addition_Subtraction(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("5 3 -"), 2)

    def test_postfix_eval_General_Muplication_Division(self):
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
        self.assertAlmostEqual(postfix_eval("15 5 /"), 3)

    def test_postfix_eval_General_Power(self):
        self.assertAlmostEqual(postfix_eval("2 3 2 ** **"), 512)
        self.assertAlmostEqual(postfix_eval("2 3 2 ^ **"), 512)

    def test_postfix_eval_General_Shift(self):
        self.assertAlmostEqual(postfix_eval("60 2 >>"), 15)
        self.assertAlmostEqual(postfix_eval("15 2 <<"), 60)

    def test_postfix_eval_General_Mixed(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_INVALIDTOKEN(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_INSUFFICIENTOPERANDS(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_TOOMANYOPERANDS(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_CANTDIVIDEBYZERO(self):
        try:
            postfix_eval("1 0 /")
            self.fail()
        except ValueError as e:
            self.assertEqual(str(e), "Undefined: Can't Divide By 0")

    def test_postfix_eval_ILLEGALBITSHIFT(self):
        try:
            postfix_eval("60 2.0 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_General(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("60 << 2"), "60 2 <<")
        self.assertEqual(infix_to_postfix("1 * 2 + 3 * 4"), "1 2 * 3 4 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3 - ( 4 - 5 ) * ( 6 + 7 )"), "1 2 + 3 * 4 5 - 6 7 + * -")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +")
        self.assertEqual(infix_to_postfix("3 ** 4 ^ 5"), "3 4 5 ^ **")
        self.assertEqual(infix_to_postfix("-3 * 3"), "-3 3 *")
        self.assertEqual("8 2 << 3 >> 4 5 ** **", infix_to_postfix("8 << 2 >> 3 ** 4 ** 5"))

    def test_prefix_to_postfix_General(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("^ 2 2"), "2 2 ^")
        self.assertEqual(prefix_to_postfix("** 2 3"), "2 3 **")
        self.assertEqual(prefix_to_postfix("<< 60 2"), "60 2 <<")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("6"), "6")
        self.assertEqual(prefix_to_postfix("- - 3 4 5"), "3 4 - 5 -")
        self.assertEqual(prefix_to_postfix("** 3 ^ 4 5"), "3 4 5 ^ **")
        self.assertEqual(prefix_to_postfix("^ 3.4 ^ 4 5"), "3.4 4 5 ^ ^")
        self.assertEqual(prefix_to_postfix("* -3 3"), "-3 3 *")


if __name__ == "__main__":
    unittest.main()
