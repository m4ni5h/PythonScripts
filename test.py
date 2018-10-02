#Converting perl to python
# fn = input('enter testfile: ')
# try:
	# file = open(fn, 'r')
# except:
	# file = open(fn, 'w')
# import os
# # open file for reading
# fn = input("Enter file to open: ")
# if os.path.exists(fn):
    # fh = open(fn, "r")
# else:
    # fh = open(fn, "w")

import os
cd = "Z:\\AX_Singapore_Sensis\\Nebula\\Src\\Subsystems"
with open("C:\\filename.txt", "w") as f:
	f.writelines("new line\n")
	#test = os.system("cleartool find Z:\\AX_Singapore_Sensis\\Nebula\\Src\\Subsystems -version \"created_since(20170101)&&!created_since(20170115)\" -print")
	test = os.popen("cleartool find "+cd+" -version \"created_since(20170101)&&!created_since(20170115)\" -print").read()
	f.write(test)
	listtest = test.splitlines()
for val in listtest:
	print (val)

# os.chdir("G:\\Scripts\\Python")
# print (os.getcwd())
# if os.path.exists("C:\\filename.txt"):
    # print ("File exists")
# else:
   # open("C:\\filename.txt", 'w')

# with open("C:\\filename.txt", "w") as f:
     # f.writelines("new line\n")

# text = open("C:\\filename.txt", 'a')
# text.writelines("less pythonic\n")
# #lsit = os.system("cleartool find $cd -version \"created_since(20170606)&&!created_since(20160506)\" -print")
# text.write(lsit)
# text.close()
