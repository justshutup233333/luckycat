'''
a = (0,1,2,7,"haha",True)
print(a[2])
b=(a,3,5,7,5,"haha","xixi","biubiu")

print(b[0])
print(b[0][5])
print(a.index(7))
print(a.count(7))

a=[1,2,3,"李白"]
b=(3,5,7,5,"haha","xixi","biubiu")
a.append("沈周")
a.extend('你吃了吗？')
print(a)
a.extend(b)
print(a)
a.insert(0,"汪直")
a.insert(999,"汪汪队")
# a.[3]="李清照"
a.pop(0)
print(a)
c=[1,2,5,8]
c.sort(reverse=True)
print(c)
a.remove("沈周")
del a[0]
print(a)



d={
    "name":("aa","bb","cc","dd"),
    "age":[3,7,6,80],
    "tel":"123"
}
# print(d)
# print(d["name"][2])
# d.get("tel")
# print(d.pop("name")
print(list(d.keys()))
print(list(d.items()))
d.update(name="abc")
print(d)
d.update(name11=piupiu)
print(d)
del d["name11"]
print(d)




type(2333)
# print(type(23333))数据格式的转换
print(type("morning"))
print(type(233.0))
print(type("沈周"))
print(type(True))
print(type(()))
print(type([]))
# print(type({}))要被包裹起来

a=10
b=11
if a>b:
    print(a)
else:
    print(b)

username=input("请输入用户名：")
passnumber=input("请输入密码")
if username=userinfo.get("username")


username=input("请输入用户名：")
passnumber=input("请输入密码: ")
a=len(username)
b=len(passnumber)
if a>5:
    if b>8:
        print("账号注册成功")
    else:
        print("密码格式错误")
else:
    print("账号格式错误")


# python实现九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end="")
    print()

'''

for i in range(10):
    if i==3:
        break
    print(i)

for i in range(10):
    if i==3:
        continue
    print(i)