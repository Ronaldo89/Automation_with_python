# f = 'inputFile.txt'
# f = open(r'C:\Users\Ronaldo Gebashe\Downloads\desktop copy\Ronaldo\Learning\Ex_Files_Python_Automation\Ex_Files_Python_Automation\Exercise Files\inputFile.txt')
#print(f.read())

#printing information for people that have passed the test 
f = 'inputFile.txt'
f = open(r'C:\Users\Ronaldo Gebashe\Downloads\desktop copy\Ronaldo\Learning\Ex_Files_Python_Automation\Ex_Files_Python_Automation\Exercise Files\inputFile.txt')
count = 0
for line in f:
	line_split = line.split()#reading for the people that have passed
	if line_split[2] =='P':
		print(line)

print(f.read())
