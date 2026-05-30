# 示例 ：跳过偶数
sun = 0
while sun <100:
    sun += 1
    if sun % 2 == 0:
        continue
    print(f"当前数字为:{sun}")

for number in range(1,101):
    if number % 2 == 0:
        continue
    print(f"当前数字为:{number}")
