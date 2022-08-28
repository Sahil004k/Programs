won = "None"

class ninja:
  chackra = 100
  health = 100
  jutsu = []

  def __init__(self , chackra , health , jutsu):
      self.chackra = chackra
      self.health = health
      self.jutsu = jutsu


naruto = ninja(100 , 100 , ['Resengen','Resengan Shuriken','Summon Toad','Shadow Clone x10'])
sasuke = ninja(100 , 100 , ['Chidori','Fire Ball','Summon Eagle','Susanoo L1'])

All_jutsu = {'Resengen': 20 , 'Chidori': 20, 'Resengan Shuriken': 40 , 'Summon Toad': 50 , 'Fire Ball' : 15 , 'Summon Eagle':35 , 'Shadow Clone x10' : 10 , 'Susanoo L1' : 35}
All_Chackra = {'Resengen': 15 , 'Chidori': 20, 'Resengan Shuriken': 35 , 'Summon Toad': 55 , 'Fire Ball' : 15 , 'Summon Eagle':40, 'Shadow Clone x10':10,'Susanoo L1' : 45}

while(True):
    print("\nP1 Turn Naruto")
    print(f'Your Chackra {naruto.chackra}')
    print(f'Your Health {naruto.health}')

    print(naruto.jutsu)
    p1 = int(input("Enter Your Jutsu Number By Position "))
    # a = 1 or 2 or 3
    # print(All_Chackra.get(p1))
    if (p1 <= len(naruto.jutsu)):
        while (True):
            nc2 = All_Chackra.get(naruto.jutsu[p1-1])
            if (naruto.chackra < nc2):
              print("\nYou are Not Able to do this Jutsu Try Other Jutsu Due To Less Chackra\n")
              print(naruto.jutsu)
              p1 = int(input("Enter Your Jutsu Number By Position ")) 
              continue
            else:
                break
   
        p1jutsu = (naruto.jutsu[p1-1])
        p1attack = (All_jutsu.get(str(p1jutsu)))
        print(p1jutsu)
        p1chackra = (All_Chackra.get(str(p1jutsu)))
        naruto.chackra = naruto.chackra - p1chackra
    else:
        print("Please Enter Valid Jutsu Position\n")
        continue
        
    
    if naruto.chackra < 15:
        # print("You are Not Able To Do Jutsu Your Chackra is Over\n")
        if sasuke.chackra > naruto.chackra:
            print("\nSasuke is Won The Fight...")
            won = "Sasuke (Chackra)"
            break
        elif sasuke.chackra == naruto.chackra:
            print("\nThe Match Was Draw Due To Chackra")
            won = "Draw (Chackra)"
            break
        else:
            pass
    else:
        pass


    if naruto.health <= 0:
        # print("You are Not Able To Do Jutsu Your health is Over\n")
        if sasuke.health > naruto.health:
            print("\nSasuke is Won The Fight...")
            won = "Sasuke (Health)"
            break
        elif sasuke.health == naruto.health:
            print("\nThe Match Was Draw Due To health")
            won = "Draw (Health)"
            break
        else:
            pass
    else:
        pass


    print("\nP2 Turn Sasuke")
    print(f'Your Chackra {sasuke.chackra}')
    print(f'Your Health {sasuke.health}')
    print(sasuke.jutsu)
    p2 = int(input("Enter Your Jutsu Number By Position "))
    # a = 1 or 2 or 3
    if (p2 <= len(sasuke.jutsu)):
        if (sasuke.chackra < All_Chackra.get(sasuke.jutsu[p2-1])):
            print("You are Not Able to do this Jutsu Try Other Jutsu\n")
            print(sasuke.jutsu)
            p2 = int(input("Enter Your Jutsu Number By Position ")) 
        else:
            pass  
        p2jutsu = (sasuke.jutsu[p2-1])
        p2attack = (All_jutsu.get(str(p2jutsu)))
        naruto.health = naruto.health - p2attack
        sasuke.health = sasuke.health - p1attack
        print(p2jutsu)
        p2chackra = (All_Chackra.get(str(p2jutsu)))
        sasuke.chackra = sasuke.chackra - p2chackra
    else:
        print("Please Enter Valid Jutsu Position\n")
        continue


    
    if sasuke.chackra < 20:
        # print("You are Not Able To Do Jutsu Your Chackra is Over\n")
        if naruto.chackra > sasuke.chackra:
            print("\nNaruto is Won The Fight...")
            won = "Naruto (Chackra)"
            break
        elif naruto.chackra == sasuke.chackra:
            print("\nThe Match Was Draw Due To Chackra")
            won = "Draw (Chackra)"
            break
        else:
            pass
    else:
        pass

    
    if sasuke.health <= 0:
        # print("You are Not Able To Do Jutsu Your health is Over\n")
        if naruto.health > sasuke.health:
            print("\nNaruto is Won The Fight...")
            won = "Naruto (Health)"
            break
        elif naruto.health == sasuke.health:
            print("\nThe Match Was Draw Due Health")
            won = "Draw (Health)"
            break
        else:
            pass
    else:
        pass
print(f'\nNaruto Chackra {naruto.chackra} & Naruto Health {naruto.health}')
print(f'Sasuke Chackra {sasuke.chackra} & Sasuke Health {sasuke.health}')
print(f'\nThe Winner is {won}')


