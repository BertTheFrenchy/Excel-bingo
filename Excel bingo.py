import random
columns = ["A", "B", "C", "D", "E"]
cells = []
chosenCells = []
for col in columns:
    for x in range (1, 11):
        cell = col + str(x)
        cells.append(cell)
print('''Welcome to the Bingo caller.
Press Enter to continue
Type "exit" to stop
''')
input()

for i in range (len(cells)):
    randomCell = random.choice(cells)
    position = cells.index(randomCell)
    cells.pop(position)
    print(randomCell)
    chosenCells.append(randomCell)
    print("Cells remaining: ", len(cells))
    #print(cells)
    userIn = input().lower()
    if userIn == "exit":
        break

if userIn != "exit":
    print("No more cells remain:", cells)
else:
    print("Chosen cells were:", chosenCells)
#roll = True
#while roll == True:
#    input()
#    print("Cell:", random.choice(columns), random.randint(1, 10))
