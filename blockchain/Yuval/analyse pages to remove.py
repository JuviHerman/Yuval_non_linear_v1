from blockchain.Yuval.functions import Human_time, Unix_Time, \
    Manual_addresses,Filter_Transaction_by_date,\
    Save_To_binary_file,Get_total_balance,import_data_from_blockcypher_In_Json_Form_and_pickle,Convert_blockcypher_address_to_class_Page,import_addresses_from_local_csv,Read_From_Binary_File


pages = Read_From_Binary_File('1')

#remove unneccessary json addresses (exchanges mostly)
x = 0
y = 0
f = 0
for i in pages:
    y += i.n_tx
    if i.n_tx > 5  and i.total_received > 500:
        x += i.total_received
        f += i.n_tx
        print(i.address,'    ', i.n_tx, '  ' , i.final_balance)

print(x,' ','total BTC received in bad addresses')
print(y,' ','total transactions until 31/12/2017')
print(f, '  ','suspected transactions')

#check results
j=0
for i in pages:
    j += i.total_received

print(j,'   BTC received in original pages')
