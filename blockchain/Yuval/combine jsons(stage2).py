from blockchain.Yuval.functions import Read_From_Binary_File,Save_To_binary_file

x1 = Read_From_Binary_File('stored_json1') # returned a list
print(len(x1),' items')
x2 = Read_From_Binary_File('stored_json2') # returned a list
print(len(x2),' items')


all_json = x1 +x2
print(len(all_json),' items combined')


Save_To_binary_file(all_json,'stored json')



