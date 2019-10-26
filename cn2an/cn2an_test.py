import unittest

from .cn2an import Cn2An


class Cn2anTest(unittest.TestCase):
    def setUp(self):
        self.strict_data_dict = {
            "一": 1,
            "两": 2,
            "十": 10,
            "十一": 11,
            "一十一": 11,
            "一百一十一": 111,
            "一千一百一十一": 1111,
            "一万一千一百一十一": 11111,
            "一十一万一千一百一十一": 111111,
            "一百一十一万一千一百一十一": 1111111,
            "一千一百一十一万一千一百一十一": 11111111,
            "一亿一千一百一十一万一千一百一十一": 111111111,
            "一十一亿一千一百一十一万一千一百一十一": 1111111111,
            "一百一十一亿一千一百一十一万一千一百一十一": 11111111111,
            "一千一百一十一亿一千一百一十一万一千一百一十一": 111111111111,
            "壹": 1,
            "拾": 10,
            "拾壹": 11,
            "壹拾壹": 11,
            "壹佰壹拾壹": 111,
            "壹仟壹佰壹拾壹": 1111,
            "壹万壹仟壹佰壹拾壹": 11111,
            "壹拾壹万壹仟壹佰壹拾壹": 111111,
            "壹佰壹拾壹万壹仟壹佰壹拾壹": 1111111,
            "壹仟壹佰壹拾壹万壹仟壹佰壹拾壹": 11111111,
            "壹亿壹仟壹佰壹拾壹万壹仟壹佰壹拾壹": 111111111,
            "壹拾壹亿壹仟壹佰壹拾壹万壹仟壹佰壹拾壹": 1111111111,
            "壹佰壹拾壹亿壹仟壹佰壹拾壹万壹仟壹佰壹拾壹": 11111111111,
            "壹仟壹佰壹拾壹亿壹仟壹佰壹拾壹万壹仟壹佰壹拾壹": 111111111111,
            "一百零一": 101,
            "一千零一": 1001,
            "一千零一十一": 1011,
            "一千一百零一": 1101,
            "一万零一": 10001,
            "一万零一十一": 10011,
            "一万零一百一十一": 10111,
            "一十万零一": 100001,
            "一百万零一": 1000001,
            "一千万零一": 10000001,
            "一千零一万一千零一": 10011001,
            "一千零一万零一": 10010001,
            "一亿零一": 100000001,
            "一十亿零一": 1000000001,
            "一百亿零一": 10000000001,
            "一千零一亿一千零一万一千零一": 100110011001,
            "一千亿一千万一千零一": 100010001001,
            "一千亿零一": 100000000001,
            "零点零零零零零零零零零零零零零零一": 0.000000000000001,
            "零点零零零零零零零零零零零零零一": 0.00000000000001,
            "零点零零零零零零零零零零零零一": 0.0000000000001,
            "零点零零零零零零零零零零零一": 0.000000000001,
            "零点零零零零零零零零零零一": 0.00000000001,
            "零点零零零零零零零零零一": 0.0000000001,
            "零点零零零零零零零零一": 0.000000001,
            "零点零零零零零零零一": 0.00000001,
            "零点零零零零零零一": 0.0000001,
            "零点零零零零零一": 0.000001,
            "零点零零零零一": 0.00001,
            "零点零零零一": 0.0001,
            "零点零零一": 0.001,
            "零点零一": 0.01,
            "零点一": 0.1,
            "负一": -1,
            "负二": -2,
            "负十": -10,
            "负十一": -11,
            "负一十一": -11,
        }

        self.normal_data_dict = {
            "十万": 100000,
            "十万零一": 100001,
            "十亿零一万零一": 1000010001,
            "一一": 11,
            "一一一": 111,
            "一一一一": 1111,
            "拾万零壹": 100001,
            "拾亿零壹万零壹": 1000010001,
            "壹壹": 11,
            "壹壹壹": 111,
            "壹壹壹壹": 1111,
            "零点": 0,
            "零点零": 0,
            "零点零零": 0,
            "点零": 0,
            "点一": 0.1,
            "一七二零": 1720,
            "一七二零点一": 1720.1,
            "一七二零点一三四": 1720.134,
            "三万五": 35000,
            "两千六": 2600,
            "一百二": 120,
            "一二三": 123,
            "负零点": 0,
            "负点零": 0,
            "负点一": -0.1,
            "负一七二零": -1720,
            "负一七二零点一": -1720.1
        }
        self.normal_data_dict.update(self.strict_data_dict)

        self.error_normal_datas = [
            "零点点",
            "零点零大"
        ]

        self.error_strict_datas = [
            "一一",
            "壹壹",
            "零点",
            "点零",
            "点一",
        ]
        self.error_strict_datas.extend(self.error_normal_datas)

        self.ca = Cn2An()

    def test_cn2an(self):
        for strict_item in self.strict_data_dict.keys():
            self.assertEqual(self.ca.cn2an(strict_item, "strict"),
                             self.strict_data_dict[strict_item])

        for normal_item in self.normal_data_dict.keys():
            self.assertEqual(self.ca.cn2an(normal_item, "normal"),
                             self.normal_data_dict[normal_item])

        for error_strict_item in self.error_strict_datas:
            try:
                self.ca.cn2an(error_strict_item)
            except ValueError as e:
                self.assertEqual(type(e), ValueError)
            else:
                raise Exception(f'ValueError not raised: {error_strict_item}')

        for error_normal_item in self.error_normal_datas:
            try:
                self.ca.cn2an(error_normal_item)
            except ValueError as e:
                self.assertEqual(type(e), ValueError)
            else:
                raise Exception(f'ValueError not raised: {error_normal_item}')


if __name__ == '__main__':
    unittest.main()
