##continue 结束本次循环 然后继续下一次循环
##break 整个循环直接退出
for number in range(1,10):
    # number循环第五次的时候 不会继续输出 number
    if number == 5:     ##结束第五次的循环 然后继续
        continue
    print(f"number值为:{number}")

