### python 异常处理
try:
    number=int(input("请输入一个数字:"))
    ## 类型转换异常 字符串无法转换为整数类型 发生了异常的情况下 代码直接终止了运行
    # 异常 捕获异常 ==> 程序继续运行
    number1=number+1
    print(f"用户输入的数字为:{number1}")
except Exception as e:
    print(f"该代码发生了{e}异常")
else:
    ### 在异常捕获过程中 如果代码没有发生任何异常
    ## 才会继续执行
    print("代码没有发生异常")
finally:
    ### 不管代码是否发生异常，都会继续执行
    print("finally")