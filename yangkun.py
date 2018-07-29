# 基准单位 万
# 当是亿单位时转换
Y = lambda w: w*(10**4)
# 当是兆单位时转换
Z = lambda w: w*(10**8)

# 当前鲲的价格数据
all_price = [
    13.93,   # 1
    49.19,   # 2
    96.77,   # 3
    218.15,  # 4
    486.51,  # 5
    1647.46, # 6
    3024.51, # 7
    5798.55, # 8
    Y(1.16), # 9
    Y(2.59), # 10
    Y(3.97), # 11
    Y(5.02), # 12
    Y(10.22),# 13
    Y(20.47),# 14
    Y(34.30),# 15
    Y(67.16),# 16
    Y(130.38),# 17
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