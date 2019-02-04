from blockchain.Yuval.functions import Read_From_Binary_File,Human_time
from blockchain.Yuval.New_Class import PageBook, Book_Transaction
import pandas as pd
import os

if __name__ == '__main__':

    # saving to file
    def Create_csv(cols: [],address: str, pages: []):
        pd2 = pd.DataFrame(pages, columns=cols)
        dirpath = os.getcwd()
        pd2.to_csv(str(dirpath)+'\\'+'temp'+'\\' + str(address) +'.csv', encoding='utf-8', index=False)

    #preparing objects to dataframe and forewarding for save
    Client_name = input("Please Enter pickle file name in directory: ")
    pages = Read_From_Binary_File(Client_name)
    for i in pages:
        list1 = []
        cols = ['Time', 'Money-In', 'Money-Out', 'Balance', 'Txid', 'Block']
        try:
            for j in i.transactions:
                list1.append([j.time, j.moneyin, j.moneyout, j.balance, j.txid, j.block])
        except Exception:
             pass
        Create_csv(cols,i.address,list1) # create relevant csv for every address listed (columns names, address, list of book_transaction objects)
