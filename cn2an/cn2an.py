import sys

from . import utils


class Cn2An():
    def __init__(self):
        self.conf = utils.get_default_conf()

    def cn2an(self, input_data="default_key"):
        if input_data:
            # 检查数据是否有效
            self.check_input_data_is_valid(input_data)
            
            # 切割整数部分和小数部分
            split_result = input_data.split("点")
            len_split_result = len(split_result)
            if len_split_result == 1:
                # 不包含小数的输入
                integer_data = split_result[0]
                output = self.integer_convert(integer_data)
            elif len_split_result == 2:
                # 包含小数的输入
                integer_data = split_result[0]
                decimal_data = split_result[1]
                output = self.integer_convert(integer_data) + self.decimal_convert(decimal_data)
            else:
                raise ValueError("输入格式错误：{}！".format(input_data))
        else:
            raise ValueError("输入数据为空！")
        
        if len(sys.argv) == 1:
            return output
        elif len(sys.argv) == 2:
            return str(output)
        else:
            raise ValueError("参数过多！")

    def cn2an_shell(self, input_data="default_key"):
        len_argv = len(sys.argv)
        if len_argv == 1:
            if input_data == "default_key":
                raise Exception("请在cn2an后输入需要转化的中文数字！")
            else:
                return input_data
        elif len_argv == 2:
            input_cn = sys.argv[1]
        else:
            raise Exception("cn2an后的参数过多！")

        return self.cn2an(input_cn)

    def check_input_data_is_valid(self, check_data):
        # 检查输入数据是否在规定的字典中
        all_check_keys = list(self.conf["number_unit"].keys())
        all_check_keys.append("点")
        for data in check_data:
            if data not in all_check_keys:
                raise ValueError("输入的数据不在转化范围内：{}！".format(data))
        
    def integer_convert(self, integer_data):
        output_integer = 0
        unit_value = 1
        ten_thousand_unit_key = 1
        for index in range(len(integer_data)-1, -1, -1):
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

        return output_integer

    def decimal_convert(self, decimal_data):
        len_decimal_data = len(decimal_data) 
        
        if len_decimal_data > 15:
            print("warning: 小数部分长度为{}，超过15位有效精度长度，将自动截取前15位！".format(len_decimal_data))
            decimal_data = decimal_data[:15]
            len_decimal_data = 15
        
        output_decimal = 0
        for index in range(len(decimal_data)-1, -1, -1):
            unit_key = self.conf["number_unit"].get(decimal_data[index])
            output_decimal += unit_key * 10 ** -(index + 1)

        # 处理精度溢出问题
        output_decimal = round(output_decimal, len_decimal_data)

        return output_decimal
