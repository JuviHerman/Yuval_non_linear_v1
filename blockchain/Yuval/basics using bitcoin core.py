from bitcoinrpc.authproxy import AuthServiceProxy
import pickle

def get_json_trans_from_rpc(block_number):
    # rpc_user and rpc_password are set in the bitcoin.conf file
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % ('yuval', 'yuval1'))
    print('block ', block_number)
    block_hash = rpc_connection.batch_([["getblockhash", block_number]])
    print('block hash ', block_hash)
    block = rpc_connection.batch_([["getblock",i] for i in block_hash])
    print('reading raw transactions')
    trans_hex = rpc_connection.batch_([["getrawtransaction", tx] for tx in block[0]['tx']]) #list
    print('decoding raw transactions')
    json_trans = rpc_connection.batch_([["decoderawtransaction", tx_hex] for tx_hex in trans_hex])

    return [block[0]['height'],json_trans]

def build_address(block_file_address):
    #receiving 'D:\\harvested database\\block1.save' - full address
    with open(block_file_address, 'rb') as f:
        addr_tran_list = pickle.load(f)
    for i in addr_tran_list[1]:
        print(i)


if __name__ == '__main__':
    x = get_json_trans_from_rpc(120000) #choose a block to explore
    for i in x[1]:
        print('\n')
        for keys, values in i.items():
            print(keys,' ',values)

    """
    addresses = 'addresses_from_invoices_8-12.2017.xlsm'
    address_list = pd.read_excel(addresses)
    address_list = address_list[['Receiving addresses']]
    list = address_list['Receiving addresses'].values.tolist()
    request_from_rpc(list)
    """


    """
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % ('yuval', 'yuval1'))
    x = rpc_connection.getbestblockhash()
    y = rpc_connection.getblock (x)
    length = int(y['height'])
    print('Size of the entire blockchain :', length)

    begin = int(input('which block should we begin to harvest trasaction from ?'+ '\n'))
    end = int(input('and where should we stop?'+ '\n'))
    for i in range(begin,end):
        json1 = get_json_trans_from_rpc(i) 
        save_path = 'D:\\harvested database\\'
        name_of_file = (str(i))
        completeName = os.path.join(save_path, name_of_file+'.save')
        with open(completeName, 'wb') as f:
            pickle.dump(json1, f)
    """