#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速测试脚本 - 测试数字范围转换修复功能
"""
import cn2an

def main():
    print("=" * 50)
    print("测试数字范围转换修复功能")
    print("=" * 50)
    print()
    
    # 测试用例
    test_cases = [
        ("1-2个月", "一到二个月"),
        ("3-5年", "三到五年"),
        ("10-20个", "十到二十个"),
        ("1-10天", "一到十天"),
    ]
    
    all_passed = True
    for input_str, expected in test_cases:
        result = cn2an.transform(input_str, "an2cn")
        passed = result == expected
        status = "[PASS]" if passed else "[FAIL]"
        
        print(f"输入: {input_str}")
        print(f"期望: {expected}")
        print(f"实际: {result}")
        print(f"状态: {status}")
        print()
        
        if not passed:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("所有测试通过！")
    else:
        print("部分测试失败！")
    print("=" * 50)
    
    # 额外测试：其他常用功能
    print("\n其他功能测试：")
    print("-" * 50)
    print(f"中文转数字: {cn2an.cn2an('一百二十三')}")
    print(f"数字转中文: {cn2an.an2cn('123')}")
    print(f"句子转换: {cn2an.transform('小王捡了一百块钱', 'cn2an')}")

if __name__ == "__main__":
    main()

