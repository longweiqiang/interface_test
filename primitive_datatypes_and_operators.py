# -*- coding: UTF-8 -*-
# @Time       : 2018/12/2 15:59
# @Author     : Weiqiang.long
# @File       : primitive_datatypes_and_operators.py
# @Software   : PyCharm
# @Description: 
# @TODO       :

# from __future__ import division

# '''XXX''' 单行注释

"""
    使用3个双引号
    来定义多行文本
    多行文本一般被用来
    做注释用了
"""

# 这是数字
print(3) # >=3

# 简单的算术
print(1 + 1)    # 2
print(8 - 1)    # 7
print(10 * 2)   # 20
print(35 / 5)   # 7.0

# python3除法中会保留小数
print(5 / 2)

# 我们一般所认知的除法在python里其实就是浮点数除法，嗯，首先要了解什么是浮点数(floats)
print(2.0) # 浮点数
print(11.0 / 4.0)

# 强制返回整数，正负数都可以
print(5 // 3)   # 用两个//标识
print(5.0 // 3.0)   # 1.0
print(-5 // 3)  #-2
print(-5.0 // 3.0)  # -2.0

# 注意，我们可以可以import division 模块,注意，from __future__ import division只能写在py文件开头，不然会报导包错误
# 这样 '/' 就可以实现普通的我们所熟悉的除法功能了
print(11 / 4)   # 普通除法

# 模/取余操作
print(7 % 3)    # 1

# 乘方
print(2 ** 4)   # 16

# 用括号强制改变算术的结合律
print((1 + 3) * 2)  # 先运算加法，再运算乘法-->8

# 布尔值的操作或者叫逻辑运算
# 注意 "and" 和 "or" 是区分大小写的
print(True and False)   # False
print(False or True)    # True

# 注意布尔操作跟整数搅在一起的时候
print(0 and 2)  # 0
print(-5 or 0)  # -5
print(0 == False)   # True






