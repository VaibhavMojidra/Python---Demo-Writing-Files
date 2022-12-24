#Writing Files


#Creates file if not exists with 'w' write only option
with open('Sample.txt','w') as myfile:
    myfile.write('Vaibhav')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())

#Just opened file using 'w' write only option this will delete the content of original as soon as opened
with open('Sample.txt','w') as myfile:
    print('Just file opened')

print('\n\n\n File content after using w just opened no write on it will auto delete the content')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())


#Just writing using 'w' 
with open('Sample.txt','w') as myfile:
    myfile.write('V')

print('\n\n\n Reading after write')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())


#Just append using 'a' 
with open('Sample.txt','a') as myfile:
    myfile.write('Mojidra')


print('\n\n\n Reading after append')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())


#Read write file 'r+' 
with open('Sample.txt','r+') as myfile:
    print('Just opened using R+')


print('\n\n\n File content after using w')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())

#Read write file 'r+' 
with open('Sample.txt','r+') as myfile:
    myfile.write('sa')
    print(myfile.readlines())

print('\n\n\n File content after using r+')

#Reads file 'r' 
with open('Sample.txt','r') as myfile:
    print(myfile.readlines())


