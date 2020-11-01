din_name =['job','ted','jay']   #晚餐邀请人员

print(din_name)

out_name = 'ted'    #不来的人

print(out_name+ ','+ 'cant come eat')

print(din_name)

cant_name = din_name.pop(1)

new_name = din_name.insert(0,'jack')    #把 jack 插入到din_name的第一个位置

new_name2 = din_name.insert(2,'ted')    #把 ted 插入到din_name 的第二个位置
new_name3 = din_name.append('han')

print(din_name)

yaoqing = 'hello,please,come with me '
mes0 = yaoqing  +   din_name[0]

mes1 = yaoqing  +   din_name[1]

mes2 = yaoqing  +   din_name[2]

mes3 = yaoqing  +   din_name[3]

mes4 = yaoqing  +   din_name[4]
print(mes0)

print(mes1)

print(mes2)

print(mes3)

print(mes4)

print('sorry,new table is break!')

sorry = 'sorry,new table is break!only two guest,but ist not you'

sor_name1 = din_name.pop(0)     #删除din_name 中的第0个

sor_name2 = din_name.pop(1)     #在sor_name1的基础上 删除din_name 中的第1个

sor_name3 = din_name.pop(2)      #在sor_name2的基础上 删除din_name 中的第2个

print(sorry,sor_name1)

print(sorry,sor_name2)

print(sorry,sor_name3)

hello_name = 'welcome,to my din'

print(hello_name,din_name[0].title())

print(hello_name,din_name[1].title())

del din_name[0]     #删除din_name中的第一位
del din_name[0]     #删除din_name中的第一位

print(din_name)