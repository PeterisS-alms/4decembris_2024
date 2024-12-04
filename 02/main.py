""" Method 1 """
# Parbauda skaitli 
num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: ")) # Dala ciparu

if num % 4 == 0:
    print(num, "is a multiple of 4") # Termināli pārbauda vai ir vairāki 4
elif num % 2 == 0:
    print(num, "is an even number") # Parbauda termināli vai tas dalas ar 2 un ir pāra skaitlis
else:
    print(num, "is an odd number") # Pārbauda termināli vai tas dalās ar 2 un ir nepāra skaitlis

if num % check == 0:
    print(num, "divides evenly by", check) # Parbauda Termināli vai tas dalās vienlīdzīgi
else:
    print(num, "doesn't divide evenly by", check) # Pārbauda termināli vai tas nedalās lidzigi

""" Method 2 """
num = int(input("Enter a number: ")) # ievada skaitli un dala ar 2
mod = num % 2
if mod > 0:
    print("You picked an odd number.") # Parāda vai tu izvēlejies nepāra skaitli dalot tavu skaitli ar 2
else:
    print("You picked an even number.") # Parāda vai tu izvēlejies pāra skaitli dalot tavu skailti ar 2
