from typing import Union
from warnings import warn
from proces import preprocess
from .conf import NUMBER_LOW_AN2CN, NUMBER_UP_AN2CN, UNIT_LOW_ORDER_AN2CN, UNIT_UP_ORDER_AN2CN
import re

class An2Cn(object):
    def __init__(self) -> None:
        self.all_num = "0123456789"
        self.number_low = NUMBER_LOW_AN2CN
        self.number_up = NUMBER_UP_AN2CN
        self.mode_list = ["low", "up", "rmb", "direct"]

    def an2cn(self, inputs: Union[str, int, float] = None, mode: str = "low") -> str:
        """阿拉伯数字转中文数字"""
        if inputs is None or inputs == "":
            raise ValueError("输入数据为空！")

        if mode not in self.mode_list:
            raise ValueError(f"mode 仅支持 {self.mode_list} ！")

        # 转字符串
        if not isinstance(inputs, str):
            inputs = self.__number_to_string(inputs)

        # 数据预处理
        inputs = preprocess(inputs, pipelines=[
            "traditional_to_simplified",
            "full_angle_to_half_angle"
        ])

        # 检查有效字符（仅0-9 . -）
        self.__check_inputs_is_valid(inputs)

        # —— 核心改动：仅当整个输入是负数才加负号 —— #
        inputs = inputs.strip()
        if re.fullmatch(r"-\d+(\.\d+)?", inputs):  # 整体是负数
            sign = "负"
            inputs = inputs[1:]
        else:
            sign = ""

        # 处理模式
        if mode == "direct":
            output = self.__direct_convert(inputs)
        else:
            split_result = inputs.split(".")
            if len(split_result) == 1:
                output = self.__integer_convert(split_result[0], mode)
            elif len(split_result) == 2:
                output = self.__integer_convert(split_result[0], mode) + self.__decimal_convert(split_result[1], mode)
            else:
                raise ValueError(f"输入格式错误：{inputs}！")

        return sign + output

    def __direct_convert(self, inputs: str) -> str:
        _output = ""
        for d in inputs:
            if d == ".":
                _output += "点"
            else:
                _output += self.number_low[int(d)]
        return _output

    @staticmethod
    def __number_to_string(number_data: Union[int, float]) -> str:
        string_data = str(number_data)
        if "e" in string_data:
            parts = string_data.split("e")
            base = parts[0]
            exp = int(parts[1])
            if exp < 0:
                string_data = "0." + "0" * (abs(exp) - 1) + base.replace(".", "")
            else:
                string_data = base.replace(".", "") + "0" * exp
        return string_data

    def __check_inputs_is_valid(self, check_data: str) -> None:
        all_check_keys = self.all_num + ".-"
        for data in check_data:
            if data not in all_check_keys:
                raise ValueError(f"输入的数据不在转化范围内：{data}！")

    def __integer_convert(self, integer_data: str, mode: str) -> str:
        if mode == "low":
            numeral_list = NUMBER_LOW_AN2CN
            unit_list = UNIT_LOW_ORDER_AN2CN
        elif mode == "up":
            numeral_list = NUMBER_UP_AN2CN
            unit_list = UNIT_UP_ORDER_AN2CN
        else:
            raise ValueError(f"error mode: {mode}")

        integer_data = str(int(integer_data))  # 去除前导0
        len_integer_data = len(integer_data)
        if len_integer_data > len(unit_list):
            raise ValueError(f"超出数据范围，最长支持 {len(unit_list)} 位")

        output = ""
        for i, d in enumerate(integer_data):
            if int(d):
                output += numeral_list[int(d)] + unit_list[len_integer_data - i - 1]
            else:
                if not (len_integer_data - i - 1) % 4:
                    output += numeral_list[int(d)] + unit_list[len_integer_data - i - 1]
                if i > 0 and output and output[-1] != "零":
                    output += numeral_list[int(d)]

        output = output.replace("零零", "零").replace("零万", "万").replace("零亿", "亿").replace("亿万", "亿").strip("零")

        # 解决「一十几」问题
        if output[:2] == "一十":
            output = output[1:]

        if not output:
            output = "零"

        return output

    def __decimal_convert(self, decimal_data: str, mode: str) -> str:
        if len(decimal_data) > 16:
            warn(f"小数部分长度为 {len(decimal_data)}，将截取前16位")
            decimal_data = decimal_data[:16]

        if not decimal_data:
            return ""

        output = "点"
        numeral_list = NUMBER_LOW_AN2CN if mode == "low" else NUMBER_UP_AN2CN
        for d in decimal_data:
            output += numeral_list[int(d)]
        return output
