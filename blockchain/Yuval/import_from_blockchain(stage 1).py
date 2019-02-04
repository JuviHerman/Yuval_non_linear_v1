from blockchain.Yuval.functions import Human_time, Unix_Time, \
    Manual_addresses,Filter_Transaction,\
    Save_To_binary_file,Get_total_balance,import_data_from_blockcypher_In_Json_Form_and_pickle,Convert_blockcypher_address_to_class_Page,import_addresses_from_local_csv


if __name__ == '__main__':


    #options for address list:
    Imported_addresses_list1 = import_addresses_from_local_csv('addresses2.xlsx')
    address_list = list(Manual_addresses())
    list= ['13VcFu2AotGUUMEfri6RZWLm2duRs3JjQX']


    #receiving Json(s)
    Json_Retreived_From_List = import_data_from_blockcypher_In_Json_Form_and_pickle(Imported_addresses_list1)

    #save to pickle
    Save_To_binary_file(Json_Retreived_From_List, 'stored_json2')