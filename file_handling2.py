with open('data_folder/data.txt', 'r') as f:
    # for line in f:
    #     print(line)
    # print(f.read()) #this will read the entire file
    print(f.read(10))
    f.seek(20) #this is use to move the cursor
    print(f.read(10))




'''
here the file will automatically get closed and there is no need to write
close() fnc
'''
