""""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力
hp的初始值为1000，power的初始值为200
定义一个fight方法：
my_final_hp=hp-enemy_power
enemy_final_hp=enemy_hp-my_power
两个hp进行对比，血量剩余多的人获胜
"""

def game():
    my_hp=1000
    my_power=200
    enemy_hp=1000
    enemy_power=200

    while True:
        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power
        print(my_hp)
        # 判断如果的的血量先小于等于0时，打印我输了
        if my_hp <=0:
            print("我输了")
            break
        # 跳出
        # 如果敌人的血量小于等于0时，就打印你输了
        elif enemy_hp <=0:
            print("你输了")
            break
# 调用game函数
game()
