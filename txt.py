import random
all_list=['石头','剪刀','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]

prande = ('''石头剪刀布游戏
    0.石头
    1.剪刀
    2.布
请出拳:''')

cs = 0
ys = 0
while cs < 2 and ys < 2:
    computer = random.choice(all_list)
    y = int(input(prande))
    you = all_list[y]
    if you == computer:
        print(computer,'平局')
    elif [you,computer] in win_list:
        print(computer,'你赢了')
        ys += 1
    else:
        print(computer,'你输了')
        cs += 1

if ys > cs:
    print('三局两胜,你赢了')
else:
    print('三局两胜,你输了')

