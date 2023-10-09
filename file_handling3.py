data=["raj\n","akash\n","devv\n"]

with open('data_folder/write_file.txt', 'w') as f:
    f.write("ansh\n")
    f.writelines(data)

'''
note :- write mode creates a new file if it does not exist and if it exist
it will erase the entire data and write the new data

hence if we want to keep the previous data also we use append mode
i.e. 'a' it creates the new file if it does not exist and append the 
older data with new one if it exist
'''