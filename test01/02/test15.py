str = "aliPay"
match str:
    case "aliPay":
        print("支付宝支付")
    case "weixinPay":
        print("微信支付")
    case "yinPay":
        print("银联支付")
    case _:
        print("未匹配成功")