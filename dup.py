import sys,os
print "----------------Duplicate file organization-------------------"
path=raw_input("Specify the path to be scanned for duplicate files: ")
print "Enter your choice from the following operations: "
print "\n1.keep/remove duplicate file set \n2.Size occupied by duplicate files\n3.Summarized information\n4.Recursive duplicate file search\n5.exit"
ch=input()


while(ch):
	if ch==1:
		os.system("fdupes -d "+path)
		break		
	elif ch==2:
		os.system("fdupes -S "+path)
		break
	elif ch==3:
		os.system("fdupes -m "+path)
		break
	elif ch==4:
		os.system("fdupes -r "+path)
		break
	print "Thank you"
	break	




