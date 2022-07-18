#******** several functions for creating, reading, updating, and deleting files. *************
# open("files.txt","w")  w -> change file (add,delete,update)
# open("files.txt","a")  appende mode (a) -> just add to the last line in the file
# open("files.txt","r+")  r+ -> read + write
#print(F.readable()) readable() = true if we can read and find the file else false

#********* Read File 1 ************
F = open("files.txt","r") # r -> Opens a file for reading, error if the file does not exist
print(F.read()) #-> desiplay file
F.close()


#********* Read File 2 ************
# F = open("files.txt","r") 
#print(F.readlines()) #-> read line by line and store the value in array
#print(F.readlines()[2]) -> to access line 2 
# for a in F.readlines():
#     print(a)
# F.close()
#*********** End ***************
