number_map = {
    "千": 1000,
    "百": 100,
    "十": 10,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9
}

input_data = "九千八百七十六"
result = 0
num = 0
unit = 1

for index, item in enumerate(input_data):
    number = number_map.get(item)
    if number < 10:
        result = result + num * unit
        num = number
    else:
        unit = number

    if index == len(input_data) - 1:
        result = result + num

print(result)
