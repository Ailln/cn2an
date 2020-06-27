import re

from . import utils
from .an2cn import An2Cn


class Cn2An(object):
    def __init__(self) -> None:
        self.conf = utils.get_default_conf()
        self.all_num = "".join(set(self.conf["number_low"] + self.conf["number_up"])) + "幺两"
        self.ac = An2Cn()
        self.strict_cn_number = self.conf["strict_cn_number"]
        self.normal_cn_number = self.conf["normal_cn_number"]
        self.check_key_dict = {
            "strict": "".join(self.strict_cn_number.values()) + "点负",
            "normal": "".join(self.normal_cn_number.values()) + "点负",
            "smart": "".join(self.normal_cn_number.values()) + "点负" + "01234567890.-"
        }
        self.pattern_dict = self.__get_pattern()

    def cn2an(self, inputs: str = None, mode: str = "strict") -> int:
        if inputs is not None or inputs == "":
            # 检查转换模式是否有效
            if mode not in ["strict", "normal", "smart"]:
                raise ValueError("mode 仅支持 strict normal smart 三种！")

            # 检查输入数据是否有效
            sign, integer_data, decimal_data, is_all_num = self.__check_input_data_is_valid(inputs, mode)

            if not is_all_num:
                if decimal_data is None:
                    output = self.__integer_convert(integer_data)
                else:
                    output = self.__integer_convert(integer_data) + self.__decimal_convert(decimal_data)
            else:
                if decimal_data is None:
                    output = self.__direct_convert(integer_data)
                else:
                    output = self.__direct_convert(integer_data) + self.__decimal_convert(decimal_data)
        else:
            raise ValueError("输入数据为空！")

        return sign * output

    def __get_pattern(self) -> dict:
        # 整数严格检查
        _0 = "[零]"
        _1_9 = f"[一二三四五六七八九]"
        _10_99 = f"{_1_9}?[十]{_1_9}?"
        _1_99 = f"({_10_99}|{_1_9})"
        _100_999 = f"({_1_9}[百]([零]{_1_9})?|{_1_9}[百]{_10_99})"
        _1_999 = f"({_100_999}|{_1_99})"
        _1000_9999 = f"({_1_9}[千]([零]{_1_99})?|{_1_9}[千]{_100_999})"
        _1_9999 = f"({_1000_9999}|{_1_999})"
        _10000_99999999 = f"({_1_9999}[万]([零]{_1_999})?|{_1_9999}[万]{_1000_9999})"
        _1_99999999 = f"({_10000_99999999}|{_1_9999})"
        _100000000_9999999999999999 = f"({_1_99999999}[亿]([零]{_1_99999999})?|{_1_99999999}[亿]{_10000_99999999})"
        _1_9999999999999999 = f"({_100000000_9999999999999999}|{_1_99999999})"
        str_int_pattern = f"^({_0}|{_1_9999999999999999})$"
        nor_int_pattern = f"^({_0}|{_1_9999999999999999})$"

        str_dec_pattern = "^[零一二三四五六七八九]{0,15}[一二三四五六七八九]$"
        nor_dec_pattern = "^[零一二三四五六七八九]{0,16}$"

        for str_num in self.strict_cn_number.keys():
            str_int_pattern = str_int_pattern.replace(str_num, self.strict_cn_number[str_num])
            str_dec_pattern = str_dec_pattern.replace(str_num, self.strict_cn_number[str_num])
        for nor_num in self.normal_cn_number.keys():
            nor_int_pattern = nor_int_pattern.replace(nor_num, self.normal_cn_number[nor_num])
            nor_dec_pattern = nor_dec_pattern.replace(nor_num, self.normal_cn_number[nor_num])

        pattern_dict = {
            "strict": {
                "int": str_int_pattern,
                "dec": str_dec_pattern
            },
            "normal": {
                "int": nor_int_pattern,
                "dec": nor_dec_pattern
            }
        }
        return pattern_dict

    def __check_input_data_is_valid(self, check_data: str, mode: str) -> (int, str, str, bool):
        # 去除 元整、圆整
        check_data = check_data.replace("元整", "").replace("圆整", "")

        for data in check_data:
            if data not in self.check_key_dict[mode]:
                raise ValueError(f"当前为{mode}模式，输入的数据不在转化范围内：{data}！")

        # 将 smart 模式中的阿拉伯数字转化成中文数字
        if mode == "smart":
            check_data = re.sub(r"\d+", lambda x: self.ac.an2cn(x.group()), check_data)
            check_data = check_data.replace(".", "点").replace("-", "负")
            mode = "normal"

        # 确定正负号
        if check_data[0] == "负":
            check_data = check_data[1:]
            sign = -1
        else:
            sign = 1

        if "点" in check_data:
            split_data = check_data.split("点")
            if len(split_data) == 2:
                integer_data, decimal_data = split_data
            else:
                raise ValueError("数据中包含不止一个点！")
        else:
            integer_data = check_data
            decimal_data = None

        result_int = re.compile(self.pattern_dict[mode]["int"]).search(integer_data)

        if result_int:
            if result_int.group() == integer_data:
                if decimal_data is not None:
                    result_dec = re.compile(self.pattern_dict[mode]["dec"]).search(decimal_data)
                    if result_dec:
                        if result_dec.group() == decimal_data:
                            return sign, integer_data, decimal_data, False
                else:
                    return sign, integer_data, decimal_data, False
        else:
            if mode == "strict":
                raise ValueError(f"不符合格式的数据：{integer_data}")
            elif mode == "normal":
                # 纯数模式：一二三
                ptn_all_num = re.compile(f"^[{self.all_num}]+$")
                result_all_num = ptn_all_num.search(integer_data)
                if result_all_num:
                    if result_all_num.group() == integer_data:
                        if decimal_data is not None:
                            result_dec = re.compile(self.pattern_dict[mode]["dec"]).search(decimal_data)
                            if result_dec:
                                if result_dec.group() == decimal_data:
                                    return sign, integer_data, decimal_data, True
                        else:
                            return sign, integer_data, decimal_data, True

                # 口语模式：一万二，两千三，三百四
                ptn_speaking_mode = re.compile(f"^[{self.all_num}][万千百][{self.all_num}]$")
                result_speaking_mode = ptn_speaking_mode.search(integer_data)
                if result_speaking_mode:
                    if result_speaking_mode.group() == integer_data:
                        _unit = self.conf["unit_to_number"][self.conf["number_unit"].get(integer_data[1])//10]
                        integer_data = integer_data + _unit
                        if decimal_data is not None:
                            result_dec = re.compile(self.pattern_dict[mode]["dec"]).search(decimal_data)
                            if result_dec:
                                if result_dec.group() == decimal_data:
                                    return sign, integer_data, decimal_data, False
                        else:
                            return sign, integer_data, decimal_data, False

        raise ValueError(f"不符合格式的数据：{check_data}")

    def __integer_convert(self, integer_data: str) -> int:
        # 核心
        output_integer = 0
        unit = 1
        ten_thousand_unit = 1
        for index, cn_num in enumerate(reversed(integer_data)):
            num = self.conf["number_unit"].get(cn_num)
            # 数值
            if num < 10:
                output_integer += num * unit
            # 单位
            else:
                # 判断出"万、亿、万亿、千万亿"
                if num % 10000 == 0:
                    if num > ten_thousand_unit:
                        # 万 亿
                        ten_thousand_unit = num
                    else:
                        # 万亿 千万亿
                        ten_thousand_unit = num * ten_thousand_unit
                        num = ten_thousand_unit

                if num > unit:
                    unit = num
                else:
                    unit = num * ten_thousand_unit

                if index == len(integer_data) - 1:
                    output_integer += unit

        return int(output_integer)

    def __decimal_convert(self, decimal_data: str) -> float:
        len_decimal_data = len(decimal_data)

        if len_decimal_data > 16:
            print(f"注意：小数部分长度为 {len_decimal_data} ，将自动截取前 16 位有效精度！")
            decimal_data = decimal_data[:16]
            len_decimal_data = 16

        output_decimal = 0
        for index in range(len(decimal_data) - 1, -1, -1):
            unit_key = self.conf["number_unit"].get(decimal_data[index])
            output_decimal += unit_key * 10 ** -(index + 1)

        # 处理精度溢出问题
        output_decimal = round(output_decimal, len_decimal_data)

        return output_decimal

    def __direct_convert(self, data: str) -> int:
        output_data = 0
        for index in range(len(data) - 1, -1, -1):
            unit_key = self.conf["number_unit"].get(data[index])
            output_data += unit_key * 10 ** (len(data) - index - 1)

        return output_data
