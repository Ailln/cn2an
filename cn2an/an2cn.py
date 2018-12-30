# encoding: utf-8

from __future__ import absolute_import
import sys

from cn2an import utils


class An2Cn():
    def __init__(self):
        self.conf = utils.get_default_conf()
    
    def an2cn(self, input_data=u"defalut_key", is_cap=False):
        # 从命令行接受参数
        input_data, is_cap = self.input_from_terminal(input_data, is_cap)

        # 将数字转化为字符串
        if not isinstance(input_data, str):
            input_data = self.convert_number_to_string(input_data)

        # 检查数据是否有效
        self.check_input_data_is_valid(input_data)

        # 切割整数部分和小数部分
        split_result = input_data.split(".")
        len_split_result = len(split_result)
        if len_split_result == 1:
            # 不包含小数的输入
            integer_data = split_result[0]
            output = self.integer_convert(integer_data, is_cap)
        elif len_split_result == 2:
            # 包含小数的输入
            integer_data = split_result[0]
            decimal_data = split_result[1]
            output = self.integer_convert(integer_data, is_cap) + self.decimal_convert(decimal_data, is_cap)
        else:
            raise ValueError(u"输入格式错误：{}！".format(input_data))

        return output

    @staticmethod
    def input_from_terminal(input_data, is_cap):
        len_argv = len(sys.argv)
        if len_argv == 1:
            if input_data == u"defalut_key":
                raise Exception(u"请在an2cn后输入需要转化的阿拉伯数字！")
            else:
                return input_data, is_cap
        elif len_argv == 2:
            input_an = sys.argv[1]
        elif len_argv == 3:
            input_an = sys.argv[1]
            if sys.argv[2] == u"cap":
                is_cap = True
            else:
                raise Exception(u"参数2错误，如果你想使用大写功能，参数2应为cap！")
        else:
            raise Exception(u"an2cn后的参数过多！")

        return input_an, is_cap

    @staticmethod
    def check_input_data_is_valid(check_data):
        # 检查输入数据是否在规定的字典中
        all_check_keys = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"."]
        for data in check_data:
            if data not in all_check_keys:
                raise ValueError(u"输入的数据不在转化范围内：{}！".format(data))
    
    @staticmethod
    def convert_number_to_string(number_data):
        # python 会自动把 0.00005 转化成 5e-05，因此 str(0.00005) != "0.00005"
        string_data = str(number_data)
        if u"e" in string_data:
            string_data_list = string_data.split(u"e")
            string_key = string_data_list[0]
            string_value = string_data_list[1]
            if string_value[0] == u"-":
                string_data = u"0." + u"0"*(int(string_value[1:])-1) + string_key
            else:
                string_data = string_key + u"0"*int(string_value)

        return string_data

    def integer_convert(self, integer_data, is_cap):
        if is_cap:
            numeral_list = self.conf["number_capital"]
            unit_list = self.conf["unit_capital"]
        else:
            numeral_list = self.conf["number"]
            unit_list = self.conf["unit"]
            
        output_an = u""
        len_integer_data = len(integer_data)

        for i, d in enumerate(integer_data):
            if int(d):
                output_an += numeral_list[int(d)] + unit_list[len_integer_data - i - 1]
            else:
                if not (len_integer_data - i - 1) % 4:
                    output_an += numeral_list[int(d)] + unit_list[len_integer_data - i - 1]
                
                if i > 0 and not output_an[-1] == u"零":
                    output_an += numeral_list[int(d)]

        output_an = output_an.replace(u"零零", u"零").replace(u"零万", u"万").replace(u"零亿", u"亿").replace(u"亿万", u"亿").strip(u"零")

        # 解决「一十几」和「壹拾几」问题
        if output_an[:2] in [u"一十", u"壹拾"]:
            output_an = output_an[1:]
            
        # 0 - 1 之间的小数
        if not output_an:
            output_an = u"零"
            
        return output_an


    def decimal_convert(self, decimal_data, is_cap):
        len_decimal_data = len(decimal_data) 
        
        if len_decimal_data > 15:
            print("warning: 小数部分长度为{}，超过15位有效精度长度，将自动截取前15位！".format(len_decimal_data))
            decimal_data = decimal_data[:15]

        if is_cap:
            numeral_list = self.conf[u"number_capital"]
        else:
            numeral_list = self.conf[u"number"]

        output_an = u"点"
        for data in decimal_data:
            output_an += numeral_list[int(data)]

        return output_an
