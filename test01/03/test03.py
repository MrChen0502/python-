sum = 0 #记录总合值
count = 1  ## 计数器 循环的次数
while count<=10: #1<10 True
    # while 执行 条件为True才可以 False 不会继续执行
    # 执行循环体代码
    sum += count
    count += 1
    print(f"sum:{sum}")
    print("---")
    print(f"count:{count}")

    ## 计数器 求1-10的总和
print("循环执行结束")