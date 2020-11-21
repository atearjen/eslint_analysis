import os
#https://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/

#Array Print Function
def printArray(ary):
	i = 0
	while(i < len(ary)):
		print(ary[i])
		i = i + 1

#Copy Paste The Excel Cells into a text file, I named mine "npmpackages.txt"
file = open("gitCloneLinks.txt") #2790 - 2990

#I wwant to empty my filesi nto an array
cloneLinks = [] 

#Iterate through the file and append them
for packages in file:
	cloneLinks.append(packages)


#each Packages had a '\n' char attached
#Remove the "\n" character
i = 0
while(i < len(cloneLinks)):
	if("\n" in cloneLinks[i]):
		cloneLinks[i] = cloneLinks[i].replace("\n", "")
		#print("Has New line")
	i = i + 1

#Test to make sure it removes the '\n' char
#printArray(cloneLinks)

file.close()
#_________________________
# This will now run the npmScript

#String you want your terminal to say
cmd2 = 'git clone '

i = 0
while(i < len(cloneLinks)):
	print("INSTALLING: ", cloneLinks[i].upper())
	cmd = cmd2 + cloneLinks[i]
	os.system(cmd)
	cmd = cmd2 #Reset the CMD. to NPMInstall
	i = i + 1


print("Number of Packages Successfully installed", i)
