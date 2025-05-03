
Flag=1;
while(Flag):
    choice=input("Which path do you choose?");
    if choice=="Left" or choice=="left":
       print("you found a hidden tunnel!You're safe");
       Flag=0;
    elif choice=="Right" or choice=="right":
       print("oh no!The glitch's trap was here!try again");
       Flag=0;
    else:
        print("Invalid choice.Please enter 'left' or 'right'");