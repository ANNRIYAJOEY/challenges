import random

print('WELCOME TO MINI RPG BATTLE')
a=' '
print(a)
gamer_health=100
enemy_health=100

defending=False
while gamer_health >0 and enemy_health >0 :
    print(f'gamer health :{gamer_health}')
    print(f'enemy health :{enemy_health}')

    gamer=input('Enter your choice:-\nAttack\nDefend\nHeal\n').lower()

    if gamer=='attack':
        damage=random.randint(10,30)
        enemy_health=enemy_health - damage
        print(f'You attacked the enemy for {damage} damage.')

        if enemy_health<=0:
            print('Gamer won!!!')
            break

    elif gamer=='heal':
        heal=random.randint(10,25)
        gamer_health=gamer_health+heal
        
        if gamer_health>100:
            gamer_health=100
        print(f'You healed for {heal}, your current health is {gamer_health}')

    elif gamer=='defend':
        defending = True
        print('You chose to defend')

    else:
        print('Invalid choice')

    enemy_attack=random.randint(10,35) 

    if defending==True:
        enemy_attack=enemy_attack//2

        defending=False

    gamer_health=gamer_health-enemy_attack
    print(f'Enemy caused you {enemy_attack} damage!!')
    
    if enemy_health<=0:
        print('Gamer won !!!')
        break

    if gamer_health<=0:
        print('Enemy won!!')
        break


    
