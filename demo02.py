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
'''
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