# 需求 判断年龄
# 年龄 判断是否成年 18岁
# 如果未成年 则继续判断 1-3婴儿 4-6幼儿园 7-12小学 13-15初中 16-17高中
# 如果成年 则继续判断 18-21大学 22-30工作 30-45青年 46-60中年 61-75老年
age=11
if age<18:
    print(f"年龄是{age},未成年")
    if age>=1 and age<=3:
        print("是婴儿")
    elif age>=4 and age<=6:
        print("上幼儿园")
    elif age>=7 and age<=12:
        print("上小学")
    elif age>=13 and age<=15:
        print("上初中")
    elif age>=16 and age<=17:
        print("上高中")
else:
    print(f"年龄是{age},成年")
    if age>=18 and age<=21:
        print("上大学")
    elif age>=22 and age<=30:
        print("工作挣钱")
    elif age>=30 and age<=45:
        print("青年")
    elif age>=46 and age<=60:
        print("中年")
    elif age>=61 and age<=75:
        print("老年")
    else:
        print("福如东海 寿比南山")