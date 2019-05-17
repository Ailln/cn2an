import unittest

from .an2cn import An2Cn


class An2CnTest(unittest.TestCase):
    def setUp(self):
        self.error_input_data = [
            "123.1.1",
            "0.1零"
        ]
        self.integer_data = {
            0: ["零", "零", "零元整"],
            1: ["一", "壹", "壹元整"],
            11: ["十一", "拾壹", "拾壹元整"],
            1000000: ["一百万", "壹佰万", "壹佰万元整"],
            1000054: ["一百万零五十四", "壹佰万零伍拾肆", "壹佰万零伍拾肆元整"],
            31000054: ["三千一百万零五十四", "叁仟壹佰万零伍拾肆", "叁仟壹佰万零伍拾肆元整"],
            11.: ["十一", "拾壹", "拾壹元整"]
        }
        self.integer_decimal_data = {
            0.000500050005005: ["零点零零零五零零零五零零零五零零五", "零点零零零伍零零零伍零零零伍零零伍", "零元整"],
            0.00005: ["零点零零零零五", "零点零零零零伍", "零元整"],
            0.4321: ["零点四三二一", "零点肆叁贰壹", "肆角叁分"],
            1000054.4321: ["一百万零五十四点四三二一", "壹佰万零伍拾肆点肆叁贰壹", "壹佰万零伍拾肆元肆角叁分"],
            1.01: ["一点零一", "壹点零壹", "壹元零壹分"],
            1.10: ["一点一零", "壹点壹零", "壹元壹角"],
            1.00: ["一点零零", "壹点零零", "壹元整"],
            1.1: ["一点一", "壹点壹", "壹元壹角"],
            1.0: ["一点零", "壹点零", "壹元整"],
            0.01: ["零点零一", "零点零壹", "壹分"],
            0.10: ["零点一零", "零点壹零", "壹角"],
            0.00: ["零点零零", "零点零零", "零元整"],
            0.1: ["零点一", "零点壹", "壹角"],
            0.0: ["零点零", "零点零", "零元整"]
        }

        self.ac = An2Cn()

    def test_an2cn(self):
        with self.assertRaises(ValueError):
            for error_data in self.error_input_data:
                self.ac.an2cn(error_data)

        for integer_item in self.integer_data.keys():
            self.assertEqual(self.ac.an2cn(integer_item),
                             self.integer_data[integer_item][0])
            self.assertEqual(self.ac.an2cn(integer_item, "low"),
                             self.integer_data[integer_item][0])
            self.assertEqual(self.ac.an2cn(integer_item, "up"),
                             self.integer_data[integer_item][1])
            self.assertEqual(self.ac.an2cn(integer_item, "rmb"),
                             self.integer_data[integer_item][2])

        for integer_decimal_item in self.integer_decimal_data.keys():
            self.assertEqual(self.ac.an2cn(integer_decimal_item),
                             self.integer_decimal_data[integer_decimal_item][0])
            self.assertEqual(self.ac.an2cn(integer_decimal_item, "low"),
                             self.integer_decimal_data[integer_decimal_item][0])
            self.assertEqual(self.ac.an2cn(integer_decimal_item, "up"),
                             self.integer_decimal_data[integer_decimal_item][1])
            self.assertEqual(self.ac.an2cn(integer_decimal_item, "rmb"),
                             self.integer_decimal_data[integer_decimal_item][2])


if __name__ == '__main__':
    unittest.main()
