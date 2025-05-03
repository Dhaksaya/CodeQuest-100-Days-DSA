print('Which path do you choose?(left/right):')
a=input()
if a=="Left" or a=="left":
    print("You found a hidden tunnel! You're safe.")
elif a=="Right" or a=="right":
    print("Oh no! The Glitch's trap was here! Try again.")
else:
    print("Invalid choice.Please enter 'left'or 'right'")