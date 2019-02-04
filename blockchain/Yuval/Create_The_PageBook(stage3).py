from blockchain.Yuval.functions import Human_time, Unix_Time, \
    Manual_addresses,Filter_Transaction_by_date,\
    Save_To_binary_file,Get_total_balance,import_data_from_blockcypher_In_Json_Form_and_pickle,Convert_blockcypher_address_to_class_Page,import_addresses_from_local_csv,Read_From_Binary_File


if __name__ == '__main__':


    Client_name = input(" Please Enter End-Client designation: ")
    print('Time limits of outputs:')
    year = int(input(" Please enter year: "))
    month = int(input(" Please enter month: "))
    day = int(input(" Please enter day: "))

    print('The Choosen Date to limit transactions: ', Human_time(Unix_Time(year, month, day)), '\n')

    Json_list_ready_to_objects = Read_From_Binary_File('stored json')

    #transforming jsons to objects
    List_of_Page_Objects = []
    for i in Json_list_ready_to_objects:
        List_of_Page_Objects.append(Convert_blockcypher_address_to_class_Page(i))

    #filtering transaction by date in all objects
    filtered_Objects = Filter_Transaction_by_date(List_of_Page_Objects,year,month,day)

    #save to pickle
    File_name = str(Client_name)
    Save_To_binary_file(filtered_Objects,File_name)

