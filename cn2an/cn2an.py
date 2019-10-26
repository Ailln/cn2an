import re

from . import utils


class Cn2An(object):
    def __init__(self):
        self.conf = utils.get_default_conf()

    def cn2an(self, inputs=None, mode="strict"):
        if inputs is not None:
            # 检查转换模式是否有效
            if mode not in ["strict", "normal"]:
                raise ValueError("mode 仅支持 strict normal 两种！")

            negative = 1
            if inputs[0] == "负":
                negative = -1
                inputs = inputs[1:]

            # 检查输入数据是否有效
            data_type = self.check_input_data_is_valid(inputs, mode)

            if data_type == "integer":
                # 不包含小数的输入
                output = self.integer_convert(inputs)
            elif data_type == "decimal":
                # 包含小数的输入
                integer_data, decimal_data = inputs.split("点")
                output = self.integer_convert(integer_data) + self.decimal_convert(decimal_data)
            elif data_type == "all_num":
                output = self.direct_convert(inputs)
            else:
                raise ValueError(f"输入格式错误：{inputs}！")
        else:
            raise ValueError("输入数据为空！")

        return negative*output

    def check_input_data_is_valid(self, check_data, mode):
        # 检查输入数据是否在规定的字典中
        all_check_keys = list(self.conf["number_unit"].keys())
        all_check_keys.append("点")

        for data in check_data:
            if data not in all_check_keys:
                raise ValueError(f"输入的数据不在转化范围内：{data}！")

        if "点" in check_data:
            split_data = check_data.split("点")
            if len(split_data) == 2:
                integer_data, decimal_data = split_data
            else:
                raise ValueError("数据中包含不止一个 点！")
        else:
            integer_data = check_data
            decimal_data = None

        all_num = "".join(set(self.conf["number_low"] + self.conf["number_up"])) + "两"
        all_unit = "".join(set(self.conf["unit_low"] + self.conf["unit_up"]))

        # 整数部分检查
        ptn_normal = re.compile(
            f"(([{all_num}十拾]+[{all_unit}]+)+零?[{all_num}]|([{all_num}十拾]+[{all_unit}]+)+|[十拾][{all_num}]|[{all_num}]|[十拾])$")
        re_normal = ptn_normal.search(integer_data)

        if re_normal:
            if re_normal.group() != integer_data:
                if mode == "strict":
                    raise ValueError(f"不符合格式的数据：{integer_data}")
                elif mode == "normal":
                    # 纯数字情况
                    ptn_all_num = re.compile(f"[{all_num}]+")
                    re_all_num = ptn_all_num.search(integer_data)
                    if re_all_num:
                        if re_all_num.group() != integer_data:
                            raise ValueError(f"不符合格式的数据：{integer_data}")
                        else:
                            return "all_num"
                else:
                    raise ValueError(f"不符合格式的数据：{integer_data}")
            else:
                if decimal_data:
                    return "decimal"
                else:
                    if check_data[-1] == "点":
                        if mode == "strict":
                            raise ValueError(f"不符合格式的数据：{check_data}")
                        elif mode == "normal":
                            return "decimal"
                    else:
                        return "integer"
        else:
            if mode == "strict":
                raise ValueError(f"不符合格式的数据：{integer_data}")
            elif mode == "normal":
                if decimal_data:
                    return "decimal"
                else:
                    raise ValueError(f"不符合格式的数据：{integer_data}")
            else:
                raise ValueError(f"不符合格式的数据：{integer_data}")

    def integer_convert(self, integer_data):
        all_num = "".join(set(self.conf["number_low"] + self.conf["number_up"])) + "两"
        ptn_speaking_mode = re.compile(f"^[{all_num}][万千百][{all_num}]$")
        result = ptn_speaking_mode.search(integer_data)

        if result:
            high_num = self.conf["number_unit"].get(integer_data[0]) * self.conf["number_unit"].get(integer_data[1])
            low_num = self.conf["number_unit"].get(integer_data[2]) * self.conf["number_unit"].get(integer_data[1])/10
            output_integer = high_num + low_num
        else:
            output_integer = 0
            unit_value = 1
            ten_thousand_unit_key = 1

            for index in range(len(integer_data) - 1, -1, -1):
                unit_key = self.conf["number_unit"].get(integer_data[index])
                if unit_key < 10:
                    output_integer += unit_value * unit_key
                else:
                    if unit_key % 10000 == 0:
                        if unit_key > ten_thousand_unit_key:
                            ten_thousand_unit_key = unit_key
                        else:
                            ten_thousand_unit_key = ten_thousand_unit_key * unit_key

                    if unit_key > unit_value:
                        unit_value = unit_key
                    else:
                        unit_value = ten_thousand_unit_key * unit_key

                    if index == 0:
                        output_integer += unit_value

        return int(output_integer)

    def decimal_convert(self, decimal_data):
        len_decimal_data = len(decimal_data)

        if len_decimal_data > 15:
            print("warning: 小数部分长度为{}，超过15位有效精度长度，将自动截取前15位！".format(
                len_decimal_data))
            decimal_data = decimal_data[:15]
            len_decimal_data = 15

        output_decimal = 0
        for index in range(len(decimal_data)-1, -1, -1):
            unit_key = self.conf["number_unit"].get(decimal_data[index])
            output_decimal += unit_key * 10 ** -(index + 1)

        # 处理精度溢出问题
        output_decimal = round(output_decimal, len_decimal_data)

        return output_decimal

    def direct_convert(self, data):
        output_data = 0
        if "点" in data:
            point_index = data.index("点")
            for index_integer in range(point_index - 1, -1, -1):
                unit_key = self.conf["number_unit"].get(data[index_integer])
                output_data += unit_key * 10 ** (point_index - index_integer - 1)

            for index_decimal in range(len(data)-1, point_index, -1):
                unit_key = self.conf["number_unit"].get(data[index_decimal])
                output_data += unit_key * 10 ** -(index_decimal - point_index)

            # 处理精度溢出问题
            output_data = round(output_data, len(data) - point_index)
        else:
            for index in range(len(data)-1, -1, -1):
                unit_key = self.conf["number_unit"].get(data[index])
                output_data += unit_key * 10 ** (len(data)-index-1)

        return output_data
