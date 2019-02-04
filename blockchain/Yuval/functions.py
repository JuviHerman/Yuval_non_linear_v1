from blockchain.Yuval.New_Class import Book_Transaction,PageBook
import pickle
import blockcypher
import time
from time import mktime
from datetime import date,datetime
import pandas as pd
import csv

def read_csv_into_page_object(addree):
    with open(addree, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        tran_list = []
        for row in csv_reader:
            try:
                transaction = Book_Transaction(f'\t{row["Time"]}', round(float(f'\t{row["Money-In"]}'),8), round(float(f'\t{row["Money-Out"]}'),8),round(float(f'\t{row["Balance"]}'),8), f'\t{row["Txid"]}',float(f'\t{row["block"]}'))
            except Exception:
                transaction = Book_Transaction(f'\t{row["Time"]}', round(float(f'\t{row["Money-In"]}'), 8),
                                               round(float(f'\t{row["Money-Out"]}'), 8),
                                               round(float(f'\t{row["Balance"]}'), 8), f'\t{row["Txid"]}',0)
            tran_list.append(transaction)
        page_object = PageBook(addree[:-4],1,1,1,1,tran_list)
        page_object.set_total_sent()
        page_object.set_total_received()
        page_object.set_n_tx()
        page_object.set_final_balance()
    return page_object


def replace_broken_page_object_with_fixed(new_page_object,all_page_objects):
    new_list = []
    for i in all_page_objects:
        if i.address == new_page_object.address:
            print('duplicates found and the old page was deleted')
        else:
            new_list.append(i)
    new_list.append(new_page_object)
    return new_list



def import_addresses_from_local_csv(addr:str):
    pd1 = pd.read_excel(addr)
    list1 = pd1['address'].tolist()
    return list1

def Unix_Time(year,month,day):
        start = date(year, month, day)
        return mktime(start.timetuple())

def Human_time(unix):
    return datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

def Manual_addresses():
    address_bitstamp = '3NkhwtgnvycFvqBdCCzAVzsQejuezz7yad'
    address_1 = '1KQFEu1Dw7iF9UFXqEG68Ze2BhfmUkXYYR'
    address_2 = '179XwNRYE5GYM9qUXPQg1QpUS92i5oMtWW'
    address_3 = '1QFbvSpTCN8zqhBhuFYcbs1faYTyjR9hRU'
    address_4 = '1Jrt55XqXyeSdYKD1aG6YrM6tJyL3aFXGu'
    address_5 = '1MZqxAPnKuxXB6WxZec92iE7c5t2SjGb8D'
    address_6 = '15L4eQzdHG4jT9e6u3TGiHZQ7ZZxKwMA6W'
    address_7 = '12r9kPuzHqjX8dW4zobBTyLMmPm7kyym1w'
    address_8 = '13SwkipTvWkXfEa8Wa4YAfMhJEMA1Fuy4C'
    address_9 = '1RWeB8C5FuDhaX6ex51Qq4UXMph4WCz4H'
    address_10 = '1DwQXbj3KMzVZJouZGEcPjBBSXSWF358fr'
    address_11 = '1C4jGhnywvd1xPPvZuSj5yUJADrG9fVAav'
    tuple1 = (address_bitstamp,address_1,address_2,address_3,address_4,address_5,address_6,address_7,address_8,address_9,address_10,address_11)
    return tuple1

def import_data_from_blockcypher_In_Json_Form_and_pickle(Imported_addresses_list):
    list = []
    for i in Imported_addresses_list:
        list.append(blockcypher.get_address_details(i,api_key='80e6f438a5854a99971fbe09c3a7d446'))
    return list

def Json_time_variable_to_Human(json_time):
    unix_x = time.mktime(json_time.timetuple())
    return datetime.fromtimestamp(unix_x).strftime('%Y-%m-%d %H:%M:%S')

def Convert_blockcypher_address_to_class_Page(j):
    address = j['address']
    final_balance = j['final_balance']
    n_tx = j['n_tx']
    total_sent = j['total_sent']
    total_received = j['total_received']
    sub_total = 0
    tran_list = []
    for i in reversed(j['txrefs']):
        input = 0
        output = 0
        sub = 0
        tx_hash = i['tx_hash']
        block_height = i['block_height']
        if int(i['tx_input_n'])== -1:
            input = round(i['value']/100000000,8)
            output = 0
        else:
            input = 0
            output = round(i['value']/100000000,8)
        sub = round(input - output,8)
        sub_total += sub

        #fixing time variable in three lines
        times = Json_time_variable_to_Human(i['confirmed'])

        if sub > 0:
            a = Book_Transaction(times,sub,0,round(sub_total,8),tx_hash,block_height)
        else:
            a = Book_Transaction(times,0,-sub,round(sub_total,8),tx_hash,block_height)
        tran_list.append(a)
    page = PageBook(address,final_balance,n_tx, total_received,total_sent,tran_list)
    return page

def Filter_Transaction_by_date(List_of_Page_Objects: [PageBook],year,month,day):
    pages_list = []
    for n in List_of_Page_Objects:
        list1 = []
        for i in n.transactions:
            if i.time <= Human_time(Unix_Time(year, month, day)):
                list1.append(i)
        a = PageBook(n,n.final_balance,n.n_tx,n.total_received,n.total_sent, list1)
        a.set_final_balance()
        a.set_n_tx()
        a.set_total_received()
        a.set_total_sent()
        pages_list.append(a)
    return pages_list

def Save_To_binary_file(list_of_page_objects,File_name):
    pickling_on = open(File_name, "wb")
    pickle.dump(list_of_page_objects, pickling_on)
    pickling_on.close()

def Read_From_Binary_File(File_name: str) -> object:
    pickle_off = open(File_name, "rb")
    list_of_page_objects = [PageBook]
    list_of_page_objects = pickle.load(pickle_off)
    return list_of_page_objects

def Get_total_balance(pages: [PageBook]):
    list1 = []
    for i in pages:
        try:
            if round(i.transactions[-1].balance,2) != 0:
                print(i.address, '   ',i.transactions[-1].balance )
                list1.append([i.address, '   ',i.transactions[-1].balance])
        except Exception:
            pass
    return list1

def print_number_of_transactions_per_page(pages: [PageBook]):
    for i in pages:
        try:
            print(i.address,': ', 'Transactions received:',len(i.transactions), 'balance:', i.transactions[-1].balance)
        except Exception:
            pass