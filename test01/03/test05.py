### break;
count = 1
while True:
    print(f"第{count}次输出")
    # 如果代码是死循环的情况下 可能会发生cpu使用率飙高的问题
    count += 1
    if count == 50:
        break

    # 多线程