import unittest

from .an2cn import An2Cn


class An2CnTest(unittest.TestCase):
    def setUp(self):
        self.error_input_data = [
            "123.1.1",
            "0.1零"
        ]
        self.integer_data = {
            0: ["零", "零"],
            1: ["一", "壹"],
            11: ["十一", "拾壹"],
            1000000: ["一百万", "壹佰万"],
            1000054: ["一百万零五十四", "壹佰万零伍拾肆"],
            31000054: ["三千一百万零五十四", "叁仟壹佰万零伍拾肆"],
            11.: ["十一", "拾壹"]
        }
        self.integer_decimal_data = {
            0.000500050005005: ["零点零零零五零零零五零零零五零零五", "零点零零零伍零零零伍零零零伍零零伍"],
            0.00005: ["零点零零零零五", "零点零零零零伍"],
            1000054.4321: ["一百万零五十四点四三二一", "壹佰万零伍拾肆点肆叁贰壹"],
            0.4321: ["零点四三二一", "零点肆叁贰壹"]
        }

        self.ac = An2Cn()

    def test_an2cn(self):
        with self.assertRaises(ValueError):
            for error_data in self.error_input_data:
                self.ac.an2cn(error_data)

        for integer_item in self.integer_data.keys():
            self.assertEqual(self.ac.an2cn(integer_item),
                             self.integer_data[integer_item][0])
            self.assertEqual(self.ac.an2cn(integer_item, True),
                             self.integer_data[integer_item][1])

        for integer_decimal_item in self.integer_decimal_data.keys():
            self.assertEqual(self.ac.an2cn(integer_decimal_item),
                             self.integer_decimal_data[integer_decimal_item][0])
            self.assertEqual(self.ac.an2cn(integer_decimal_item, True),
                             self.integer_decimal_data[integer_decimal_item][1])


if __name__ == '__main__':
    unittest.main()
