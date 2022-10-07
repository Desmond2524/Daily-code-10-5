import random 

#----------------------------------------------------------
def battleSystem(monsterType, playerHealth): 
    if monsterType == "Creeper":
        monsterHealth = 20
        print("A creeper attacks!")
    elif monsterType == "Skeleton":
        monsterHealth = 40 
        print("A skeleton attacks!")
    elif monsterType == "Dragon":
        monsterHealth = 50
        print("A skeleton 2 attacks")
    elif monsterType == "Zombie":
        monsterhealth = 40
        print("A creeper 2 attacks") 
    while monsterHealth>0 and playerHealth >0:
        if monsterType == "Creeper":
            monsterAttack = random.randrange(20, 30)
        elif monsterType == "Skeleton":
            monsterAttack = random.randrange(10, 16)
        print("The", monsterType, "attacks for", monsterAttack)
        playerHealth= playerHealth-monsterAttack
        print("your health is now", playerHealth)
        
        playerAttack = random.randrange(30, 35)
        print("You attacks for", playerAttack)
        monsterHeealth = monsterHealth - playerAttack 
        print("The monster's health is now", monsterHealth)
        
    if monsterHealth<0:
        print("you win!")
    else:
        print("You are defeated by the monster")
    return playerHealth 
#----------------------------------------------------------------
        
battleSystem("Skeleton", 100) 




