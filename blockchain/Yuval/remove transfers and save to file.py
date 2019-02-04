from blockchain.Yuval.functions import Read_From_Binary_File
import pandas as pd



#pickle -> objects -> dataframe -> csv

#load from pickle
Client_name = input("Please Enter pickle file name in directory: ")
pages = Read_From_Binary_File(Client_name)

#add each page to Dataframe for processing
dataframes1 = []
cols = ['Address','Time', 'Money-In', 'Money-Out', 'Balance', 'Txid', 'Block']
for i in pages:
     page_transactions = []
     for j in i.transactions:
          try:
              page_transactions.append([i.address,j.time, j.moneyin,j.moneyout, j.balance, j.txid, j.block])
          except Exception:
              pass
     dataframes1.append(pd.DataFrame(page_transactions, columns=cols))
#concatenate
master_dataframe1 = pd.concat(dataframes1)


dataframes2 = []
Client_name = input("Please Enter pickle file name in directory: ")
pages1 = Read_From_Binary_File(Client_name)
for i in pages1:
     page_transactions = []
     for j in i.transactions:
          try:
              page_transactions.append([i.address,j.time, j.moneyin,j.moneyout, j.balance, j.txid, j.block])
          except Exception:
              pass
     dataframes2.append(pd.DataFrame(page_transactions, columns=cols))

#concatenate
master_dataframe2 = pd.concat(dataframes2)

list= [master_dataframe1,master_dataframe2]
#concatenate master 1+2
master_dataframe = pd.concat(list)
filtered_dataframes = master_dataframe.drop_duplicates(subset=['Txid'], keep=False)

filtered_dataframes.to_csv('filtered transfers.csv')