#!/usr/bin/python
# -*- coding: utf-8 -*-
# 基准单位 万
# 当是亿单位时转换
Y = lambda w: w*(10**4)
# 当是兆单位时转换
Z = lambda w: w*(10**8)

# 当前鲲的价格数据
all_price = [
    92.64,     # 1
    112.55,    # 2
    221.39,    # 3
    499.08,    # 4
    677.42,    # 5
    1647.46,   # 6
    3568.92,   # 7
    6842.29,   # 8
    Y(1.62),   # 9
    Y(2.59),   # 10
    Y(6.53),   # 11
    Y(11.5),   # 12
    Y(23.39),  # 13
    Y(46.83),  # 14
    Y(92.61),  # 15
    Y(181.30), # 16
    Y(351.99), # 17
    Y(678.62), # 18
    Y(1534.74),# 19
    Y(2926.42),# 20
    Y(6555.19),# 21
    Z(1.46),   # 22
    Z(1.67),   # 23
]

# データの正規化
all_price_regular = []
level = 0
for price in all_price:
    temp_regular_price = price / 2 ** level
    all_price_regular.append(temp_regular_price)
    level += 1

level = 1
print("等级\t一次购买单价\t二次购买单价")
for price in all_price_regular:
    print("%d:\t%.6f\t%.6f" % (level, price, price*1.09))
    level += 1