
def eslintParser(fileName):

	file = open(fileName,"r")
	#print(file.read())


	for words in file:
		if(words[0] == "🔥"):
			#print(words)
			numberOfProblems = words.split(" ")[2]
			numberOfErrors = words.split(" ")[6].replace("(","")
			numberOfWarnings = words.split(" ")[8]

			problemsList.append(numberOfProblems)
			errorsList.append(numberOfErrors)
			warningsList.append(numberOfWarnings)
			successfulFileNames.append(fileName)

			#print(numberOfErrors)
			print(words.split(" "))
	file.close()



file2 = open("eslintDirs.txt") #2790 - 2990
fileList = [] 
for packages in file2:
	fileList.append(packages)
#each Packages had a '\n' char attached
#Remove the "\n" character
i = 0
while(i < len(fileList)):
	if("\n" in fileList[i]):
		fileList[i] = fileList[i].replace("\n", ".txt")
		#print("Has New line")
	i = i + 1

file2.close()




#Creating Global Lists
problemsList = []
errorsList = [] 
warningsList = []




successfulFileNames = []

print(fileList)



#____
i = 0 
while(i < len(fileList)):
	eslintParser(fileList[i])
	i = i + 1



#### UNcomment to see them parsed
# print(successfulFileNames)
# print(problemsList)
# print(errorsList)
# print(warningsList)

print("Number of successfulFileNames", len(successfulFileNames))
print("Number of Problems ", len(problemsList))
print("Number of Errors ", len(errorsList))
print("NumberOFwarnings ", len(warningsList))


