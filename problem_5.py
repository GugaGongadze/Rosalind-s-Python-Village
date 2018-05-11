filename = "jabberwock_monty.txt"
file = open(filename, "r")

currIndex = 1
evenString = ''

for line in file:
    if currIndex % 2 is 0:
        evenString += line
    currIndex += 1

print(evenString)