'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
import random

shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []


#  2.初始化您的余额
money = input("请输入您本月工资：")
num = int(input('请输入您选择的幸运数字：'))
money = int(money)

# 3.正常购物
i = 1

a = random.randint(1, 6)
if num == a and a == 1:
    b = 0.5
if num == a and a == 2:
    b = 0.1
if num == a and a == 3:
    b = 0.6
else:
    b = 1
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                if chose == 0 and a == 1:
                    money = money - shop[chose][1] * b
                elif chose == 4 and a == 2:
                    money = money - shop[chose][1] * b
                elif chose == 2 and a == 3:
                    money = money - shop[chose][1] * b
                else:
                    money = money - shop[chose][1] * b # 减去价格
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")


    i = i + 1

print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
for h in range(len(shop)):
    sum = 0
    for key, value in enumerate(mycart):
        if value[0] == shop[h][0]:
            sum += 1
    if sum > 1:
        print(h,"------",shop[h][0],'数量：',sum,"价格：￥",shop[h][1])
    if sum == 1:
        print(h,"------",shop[h][0],"价格：￥",shop[h][1])
print("---------------------------------------")
print("您的余额还剩：￥",money)

# for key,value in enumerate(mycart):
#     for h in range(len(shop)):
#         if shop[h][0] == value[0]:
#             sum += 1
#     if sum > 1:
#         print(shop.index(value),"------",value[0],'数量：',sum,"价格：￥",value[1])
#     else:
#         print(shop.index(value),"------",value[0],"价格：￥",value[1])































