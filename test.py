print("hello pycharm")
a = 1
print(a)
#id可以打印变量的存储地址
print(id(a))

int_a=1
float_a=2.0
complex_a=1.2j
# 通过type查看数据类型

print(type(int_a))
print(type(float_a))
print(type(complex_a))

list1=[1,2,3,4,5,6]
print(list1[0])
print(list1[0:5:2])


a=4
if a==0:
    print("a=0")
elif a==2:
    print("a=2")
elif a==3:
    print("a=3")
else:
    print("a不等于0、1、2")