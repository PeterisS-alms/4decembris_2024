a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # parāda ka a ir vienāds ar šiem skaitļiem

num = int(input("Choose a number: ")) # Prasa tev ievadīt skaitli

new_list = [] # izveido jaunu sarakstu

for i in a:
    if i < num:
        new_list.append(i) # Pievieno jaunu sarakstu

print(new_list) # printē jaunu sarakstu