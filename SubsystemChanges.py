#Python Script to get the changes and data related from Clearcase
import os
import time

scriptresultsdirectory = r"C:\scriptresultsdirectory"
scriptresult = r"result"+time.strftime('%d%m%Y_%H%M%S')+".txt"
searchdir = r"Z:\AX_Singapore_Sensis\Nebula\Src\Subsystems\PocDocumentation\EditDictionary"

#open(scriptresultsdirectory+"\\"+scriptresult, 'w').close()

if not os.path.exists(scriptresultsdirectory):
	os.makedirs(scriptresultsdirectory)
os.chdir(scriptresultsdirectory)
print (os.getcwd())

ccversionlist = os.popen("cleartool find "+searchdir+" -version \"created_since(20140101)&&!created_since(20170115)\" -print").read()
versionlist = ccversionlist.splitlines()

with open(scriptresultsdirectory+"\\"+scriptresult, "a") as resultfile:
	for version in versionlist:
		# resultfile.writelines(version)
		# resultfile.writelines("\n")
		filename = os.popen(r'cleartool describe -fmt %En '+ version).read()
		# resultfile.writelines(filename)
		# resultfile.writelines("\n")
		#print(type(filename))
		slashsplit = filename.split("\\")
		if 'Subsystems' in slashsplit:
			subsys = slashsplit[slashsplit.index("Subsystems")+1]
		elif 'Framework' in slashsplit:
			subsys = "Framework"
		elif 'Applications' in slashsplit:
			subsys = 'Applications'
		else:
			subsys = 'Other'
		resultfile.writelines(subsys)
		resultfile.writelines(", ")
		resultfile.writelines(version)
		resultfile.writelines(", ")
		
		creator=os.popen(r'cleartool describe -fmt %Fu '+ version).read()
		resultfile.writelines(creator)
		resultfile.writelines("\n")
		
		# TODO: RSM integration
		# difference = os.popen(r'ct diff -predecessor ' + version).read()
		# resultfile.writelines(difference)
		# resultfile.writelines("\n")
		
