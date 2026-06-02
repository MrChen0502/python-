## 模拟 网上购物 支付方式 抖音支付 银联支付 微信支付 QQ支付 支付宝
## 支付方式最终都是 跳转第三方支付平台扣钱
class PayParent:
    def toPay(self):
        print("父类中 toPay")

class AliPay(PayParent):
    def toPay(self):
        print("正在使用支付宝支付")

class WeiXinPay(PayParent):
    def toPay(self):
        print("正在使用微信支付")

p1 = AliPay()
p1.toPay()