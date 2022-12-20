file = open('Input.txt', 'r')
finput = file.read()

c = int(finput[:finput.find(',')])
finput = finput[finput.find(',')+1:]
h = int(finput[:finput.find(',')])
o = int(finput[:finput.find(','):-1])

listout = []
listout.append(c//2)
listout.append((h-1)//5)
listout.append(o//1)

out = str(min(listout))
file = open('Output.txt', 'w')
print = (file.write('Максимальное кол-во молекул спирта: %s' %out))
file.close()