import unittest

from .cn2an import Cn2An


class Cn2anTest(unittest.TestCase):
    def setUp(self):
        self.error_input_data = [
            "零点点",
            "零点零大"
        ]

        self.strict_input_data = {
            "一": 1,
            "壹": 1,
            "十一": 11,
            "一十一": 11,
            "一百万零五十四": 1000054,
            "壹佰万零伍十肆": 1000054,
            "三千壹佰万零伍十肆": 31000054,
            "一百万零五十": 1000050,
            "壹佰万零伍十": 1000050,
            # python 默认只有16位的有效精度
            "零点零零零五零零零五零零零五零零零五零": 0.000500050005,
            "零点零零零五零零零五": 0.00050005,
            "零点零零零零五零": 0.00005,
            "零点零零零零五": 0.00005,
            "零点零零": 0,
            "零点零": 0,
            "一百万零五十四点四三二一": 1000054.4321,
            "一百万零一": 1000001
        }

        self.normal_input_data = {
            "一": 1,
            "壹": 1,
            "十一": 11,
            "一十一": 11,
            "一百万零五十四": 1000054,
            "壹佰万零伍十肆": 1000054,
            "三千壹佰万零伍十肆": 31000054,
            "一百万零五十": 1000050,
            "壹佰万零伍十": 1000050,
            "一二一二": 1212,
            # python 默认只有16位的有效精度
            "零点零零零五零零零五零零零五零零零五零": 0.000500050005,
            "零点零零零五零零零五": 0.00050005,
            "零点零零零零五零": 0.00005,
            "零点零零零零五": 0.00005,
            "零点零零": 0,
            "零点零": 0,
            "一百万零五十四点四三二一": 1000054.4321,
            "一百万零五十四点": 1000054,
            "点四三二一": 0.4321
        }

        self.ca = Cn2An()

    def test_cn2an(self):
        with self.assertRaises(ValueError):
            for error_data in self.error_input_data:
                self.ca.cn2an(error_data)

        for strict_item in self.strict_input_data.keys():
            self.assertEqual(self.ca.cn2an(strict_item, "strict"),
                             self.strict_input_data[strict_item])

        for normal_item in self.normal_input_data.keys():
            self.assertEqual(self.ca.cn2an(normal_item, "normal"),
                             self.normal_input_data[normal_item])


if __name__ == '__main__':
    unittest.main()
