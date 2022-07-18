#*****************
# "w" - Write - will overwrite any existing content
# "a" - Append - will append to the end of the file
# "x" - Create - will create a file, returns an error if the file exist
#******************

#********** methode 1 **********
F = open("files.txt","a") # add to the end of the file
a = ["\n test - 12 - casa \n" , "fatiha - 22 - fes \n" , "safaa - casa - 24 \n"]
F.writelines(a) 
F.close()

# #********** methode 2 **********
# F = open("files.txt","w") #deleted the content and add new's
# F.write("sanaa - 22 - fes") 
# F.close()
