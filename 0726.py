'''
# 删除del
a = [1,3,5,6]
print(a)
del a[1]
print(a)

# 列表相加,直接在相加
a = [1,4,5,3]
b = a
c = b + a

# 添加元素
# 成员再运算，判断一个元素是否字list里边
# 链表的遍历-for、while
d = [1,2,3,4]
# 挨个打印
for i in d:
    print(i)
# range in后面的东西必须是可迭代的东西
list = [1,2,4,5,6,7,8]
lenth = len(list)
indx = 0
while indx < lenth:
    print(list[indx],end=' ')
    indx += 1
print('\n')
# 双层列表循环
s = [['su',1],['io',3]]
for k,v in s:
    print(k,'...',s)

# 列表内涵：list content - for 创建
n = [1,3,4,5,6]
m = [i for i in n]
print(m)

# 生成一个数列，并将其中的偶数组成一个新数列
p = [q for q in range(1,11)]
j = [i*10 for i in p if i%2 == 0]
print(j)

a = [b for b in range(100,1000)]
c = [d for d in a if d%100 == 0]
print(c)

# 列表生成可以嵌套，也就是一个大括号里有两个列表生成表达式
a = [1,2,4]
b = [100,200,300]
c = [m+n for m in a for n in b]
print(c)


for m in a:
    for n in b:
        print(m+n,end=' ')
'''
# 列表常用的函数
# 1、 len 求列表的长度
# 2、 max 求最大值
# 3、 min 求最小值
# 4、 list 把其他格式的数据转换成list

print(list(range(1,11)),end=' ')
