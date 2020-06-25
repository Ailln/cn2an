import re
from typing import Union

from . import utils
from .an2cn import An2Cn


class Cn2An(object):
    def __init__(self) -> None:
        self.conf = utils.get_default_conf()
        self.all_num = "".join(set(self.conf["number_low"] + self.conf["number_up"])) + "幺两"
        self.all_num_with_ten = self.all_num + "十拾"
        self.all_unit = "".join(set(self.conf["unit_low"] + self.conf["unit_up"]))
        self.ac = An2Cn()

    def cn2an(self, inputs: str = None, mode: str = "strict") -> int:
        if inputs is not None:
            # 检查转换模式是否有效
            if mode not in ["strict", "normal", "smart"]:
                raise ValueError("mode 仅支持 strict normal smart 三种！")

            # 检查输入数据是否有效
            sign, inputs, data_type = self.__check_input_data_is_valid(inputs, mode)

            if data_type == "integer":
                # 不包含小数的输入
                output = self.__integer_convert(inputs)
            elif data_type == "decimal":
                # 包含小数的输入
                integer_data, decimal_data = inputs.split("点")
                output = self.__integer_convert(integer_data) + self.__decimal_convert(decimal_data)
            elif data_type == "all_num":
                output = self.__direct_convert(inputs)
            else:
                raise ValueError(f"输入格式错误：{inputs}！")
        else:
            raise ValueError("输入数据为空！")

        return sign * output

    def __check_input_data_is_valid(self, check_data: str, mode: str) -> (int, str, str):
        # 去除 元整、圆整
        check_data = check_data.replace("元整", "").replace("圆整", "")

        # 正负号
        sign = 1

        if mode == "strict":
            strict_check_key = self.conf["number_low"] + self.conf["number_up"] + ["十", "拾", "百", "佰", "千", "仟", "万",
                                                                                   "亿", "兆", "点", "负"]
            for data in check_data:
                if data not in strict_check_key:
                    raise ValueError(f"当前为{mode}模式，输入的数据不在转化范围内：{data}！")

            # 确定正负号
            if check_data[0] == "负":
                check_data = check_data[1:]
                sign = -1

        elif mode == "normal":
            normal_check_key = list(self.conf["number_unit"].keys()) + ["点", "负"]
            for data in check_data:
                if data not in normal_check_key:
                    raise ValueError(f"当前为{mode}模式，输入的数据不在转化范围内：{data}！")

            # 确定正负号
            if check_data[0] == "负":
                check_data = check_data[1:]
                sign = -1

        elif mode == "smart":
            smart_check_key = list(self.conf["number_unit"].keys()) + ["点", "负", "0", "1", "2", "3", "4", "5", "6", "7",
                                                                       "8", "9", ".", "-"]
            for data in check_data:
                if data not in smart_check_key:
                    raise ValueError(f"当前为{mode}模式，输入的数据不在转化范围内：{data}！")

            # 确定正负号
            if check_data[0] in ["负", "-"]:
                check_data = check_data[1:]
                sign = -1

            def an2cn_sub(matched):
                return self.ac.an2cn(matched.group())

            check_data = re.sub(r"\d+", an2cn_sub, check_data)
            mode = "normal"

        if "点" in check_data:
            split_data = check_data.split("点")
            if len(split_data) == 2:
                integer_data, decimal_data = split_data
            else:
                raise ValueError("数据中包含不止一个 点！")
        else:
            integer_data = check_data
            decimal_data = None

        # 整数部分检查
        # all_num: 零一二三四五六七八九壹贰叁肆伍陆柒捌玖幺两
        # all_num_with_ten: 零一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾幺两
        ptn_normal = re.compile(
            f"(([{self.all_num_with_ten}]+[{self.all_unit}]+)+零?[{self.all_num}]|([{self.all_num_with_ten}]+[{self.all_unit}]+)+|[十拾][{self.all_num}]|[{self.all_num}]|[十拾])$")
        re_normal = ptn_normal.search(integer_data)

        if re_normal:
            if re_normal.group() != integer_data:
                if mode == "strict":
                    raise ValueError(f"不符合格式的数据：{integer_data}")
                elif mode == "normal":
                    # 纯数字情况
                    ptn_all_num = re.compile(f"[{self.all_num}]+")
                    re_all_num = ptn_all_num.search(integer_data)
                    if re_all_num:
                        if re_all_num.group() != integer_data:
                            raise ValueError(f"不符合格式的数据：{integer_data}")
                        else:
                            return sign, check_data, "all_num"
                else:
                    raise ValueError(f"不符合格式的数据：{integer_data}")
            else:
                if decimal_data:
                    return sign, check_data, "decimal"
                else:
                    if check_data[-1] == "点":
                        if mode == "strict":
                            raise ValueError(f"不符合格式的数据：{check_data}")
                        elif mode == "normal":
                            return sign, check_data, "decimal"
                    else:
                        if mode == "strict":
                            if check_data[0] == "十" and len(check_data) > 2:
                                raise ValueError(f"不符合格式的数据：{check_data}")
                        return sign, check_data, "integer"
        else:
            if mode == "strict":
                raise ValueError(f"不符合格式的数据：{integer_data}")
            elif mode == "normal":
                if decimal_data:
                    return sign, check_data, "decimal"
                else:
                    raise ValueError(f"不符合格式的数据：{integer_data}")
            else:
                raise ValueError(f"不符合格式的数据：{integer_data}")

    def __integer_convert(self, integer_data: str) -> int:
        # 口语模式 比如：两千三
        ptn_speaking_mode = re.compile(f"^[{self.all_num}][万千百][{self.all_num}]$")
        result = ptn_speaking_mode.search(integer_data)

        if result:
            high_num = self.conf["number_unit"].get(integer_data[0]) * self.conf["number_unit"].get(integer_data[1])
            low_num = self.conf["number_unit"].get(integer_data[2]) * self.conf["number_unit"].get(integer_data[1]) / 10
            output_integer = high_num + low_num
        else:
            # 核心
            output_integer = 0
            unit = 1
            # 万、亿、万亿、兆、万兆、亿兆、万亿兆
            ten_thousand_unit = 1
            # 万、亿、兆
            max_ten_thousand_unit = 1
            last_unit = 0

            for index, cn_num in enumerate(reversed(integer_data)):
                num = self.conf["number_unit"].get(cn_num)
                # 数值
                if num < 10:
                    output_integer += num * unit
                # 单位
                else:
                    # 判断出"万、亿、兆"
                    if num % 10000 == 0:
                        if num > ten_thousand_unit:
                            ten_thousand_unit = num
                            max_ten_thousand_unit = num
                        else:
                            # 亿兆
                            if last_unit < num < max_ten_thousand_unit:
                                ten_thousand_unit = num * max_ten_thousand_unit
                            else:
                                ten_thousand_unit = num * ten_thousand_unit
                            last_unit = num
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

        if len_decimal_data > 15:
            print("warning: 小数部分长度为{}，超过15位有效精度长度，将自动截取前15位！".format(
                len_decimal_data))
            decimal_data = decimal_data[:15]
            len_decimal_data = 15

        output_decimal = 0
        for index in range(len(decimal_data) - 1, -1, -1):
            unit_key = self.conf["number_unit"].get(decimal_data[index])
            output_decimal += unit_key * 10 ** -(index + 1)

        # 处理精度溢出问题
        output_decimal = round(output_decimal, len_decimal_data)

        return output_decimal

    def __direct_convert(self, data: str) -> Union[int, float]:
        output_data = 0
        if "点" in data:
            point_index = data.index("点")
            for index_integer in range(point_index - 1, -1, -1):
                unit_key = self.conf["number_unit"].get(data[index_integer])
                output_data += unit_key * 10 ** (point_index - index_integer - 1)

            for index_decimal in range(len(data) - 1, point_index, -1):
                unit_key = self.conf["number_unit"].get(data[index_decimal])
                output_data += unit_key * 10 ** -(index_decimal - point_index)

            # 处理精度溢出问题
            output_data = round(output_data, len(data) - point_index)
        else:
            for index in range(len(data) - 1, -1, -1):
                unit_key = self.conf["number_unit"].get(data[index])
                output_data += unit_key * 10 ** (len(data) - index - 1)

        return output_data
