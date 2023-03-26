from faker import Faker
import time


# 生成身份证号
def fak():
    fa = Faker(locale='zh-CN')
    s = fa.ssn()
    t = time.strftime("%Y%m%d")  # 获取当前日期
    c = int(t[0:4]) - int(s[6:10])  # 计算日期差
    if c > 18 & c < 65:
        print(s[6:10])
        print('年龄:%d' % c)
        print(s[0:3] + '-' + s[3:6] + '-' + s[6:14] + '-' + s[14:18])
    else:
        fak()


fak()
