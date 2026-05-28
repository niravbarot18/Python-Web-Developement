numbers=[5,23,4,78,65,2,4,66]
secret_no=65
chances=3

print("Mystery Number Challenge")
print("No Guess Karo aur Inaam Jito0oooooo😎")
print("Here is Your Numbers:",numbers)

for i in range(1,chances+1):
    guess=int(input(f"Attempt {i} | Enter Your Guess:"))

    if guess == secret_no:
        print("Congrats You Won!")
        print("You Won PS-5")
        break
    elif guess < secret_no:
        print("Too Low")

    else:
        print("Too High")

print("Game Over!")



