import random
import sys
import time
gladivs = "\n \n <:::::::::::::::||===) TEMPVS I (===||:::::::::::::::> \n"

players = ['Alexander', 'Andreas', 'Biarcvs', 'Celeborn',
           'Erasmvs', 'Ioannes', 'Meiling', 'Severvs']

random.shuffle(players)

matchups = [
    f"A: {players[0]} versus {players[1]} \n",
    f"B: {players[2]} versus {players[3]} \n",
    f"C: {players[4]} versus {players[5]} \n",
    f"D: {players[6]} versus {players[7]}"]

print("\n")

# with open('tornamentvm.txt') as tornamentvm:
#     contents = tornamentvm.read()

# for x in contents:
#     sys.stdout.write(x)
#     sys.stdout.flush()
#     time.sleep(0.2)

print(gladivs)

time.sleep(1)

print('''
Match-ups for Tempvs I: \n''')

time.sleep(1)

for tempvs in matchups:
    sys.stdout.write(tempvs)
    sys.stdout.flush()
    time.sleep(1)

time.sleep(1.5)

# print(f'''

# Faction Draft order:
# 1. {players[0]}
# 2. {players[1]}
# 3. {players[2]}
# 4. {players[3]}
# 5. {players[4]}
# 6. {players[5]}
# 7. {players[6]}
# 8. {players[7]}''')


# a loop based version of the above section - result is exactly the same.
# the enumerate function is a handy little trick that allows you to get the iteration index
# (in this case i) along with the actual iterated item (the player)
print('\n \n Faction Draft order:')
for i, player in enumerate(players):
    print(
        f'{i+1}. {player}'
    )
