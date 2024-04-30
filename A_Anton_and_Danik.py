n = int(input())
game = list(input())

danik = [i for i in game if i == 'D']
anton = [i for i in game if i == 'A']

if len(anton) > len(danik):
    print("Anton")
elif len(anton) < len(danik):
    print("Danik")
else:
    print("Friendship")
