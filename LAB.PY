from shutil import copyfile
print("enter X for exit")
sourcefile=input("enter source file name(copy from):")
if sourcefile=='X':
	exit()
else:
	destinationfile=input("enter destination filename(copy to):")
	copyfile(sourcefile,destinationfile)
	print("file copied successfully")
	print("want to display the content?(Y?N):")
	check=input()
	if check=='n':
		exit()
	else:
		c=open(destinationfile,'r')
		print(c.read())