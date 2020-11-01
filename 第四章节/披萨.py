pisas = ['haixianpisa','zhishipisa','huotuipisa']#pisas中 总共有3种披萨
pisas.append('jianguopisa')
pisas.append('qiankelipisa')
for pisa in pisas:#从列表pisas中取出名字储存在变量pisa中
    print(pisa)
    print('wo xihuan,'+ pisa.title()+'.\n')
print('我喜欢海鲜,芝士,火腿,我超级喜欢批萨')

print('\nthe first three items in the list are:')
for pisa in pisas[0:3]:
    print(pisa.title())

print('\nthree items from the middle of the list are:')
for pisa in pisas[1:4]:
    print(pisa.title())

print('\nthe last three items in the list are:')
for pisa in pisas[2:]:
    print(pisa.title())


friend_pisa = pisas[:]
print('\n')
print(friend_pisa)

pisas.append('shabipisa')
friend_pisa.append('hanpipisa')

print('\nmy favorite pisa are:')
print(pisas)


print('\nmy friend favorite pisa are:')
print(friend_pisa)