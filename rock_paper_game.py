import random
l=['rock','paper','scissor']




while True:
    mycount=0
    ccount=0
    user_choice=int(input('''
     game start......
     1 yes
     2 no |exit
     '''))
    if user_choice==1:
        for i in range(5):
            user_input=int(input(
            '''
            1 rock
            2 paper
            3 scissor
            '''
        ))
         
            if user_input==1:
                choice='rock'
            elif user_input==2:
                choice='paper'
            elif user_input==3:
                choice='scissor'
            print("choice")
            comp_choice = random.choice(l)
            print(comp_choice)
            if comp_choice==choice:
                print("computer value is:",comp_choice)
                print("my choice",choice)
                print("game draw")
                mycount+=1
                ccount+=1
            elif ((choice=="rock" and comp_choice=="scissor") or (choice=="scissor" and comp_choice=="paper") or 
                (choice=="paper" and comp_choice=="rock")):
                print("computer value is:",comp_choice)
                print("my choice",choice)
                print("i win")
                mycount+=1
            else:
                print("computer value is:",comp_choice)
                print("my choice",choice)
                print("computer win")
                ccount+=1
        if(mycount==ccount):
            print("finally match draw")
        elif mycount>ccount:
            print("i won the match")   
        else:
            print("computer won the match")     

    else:
        break