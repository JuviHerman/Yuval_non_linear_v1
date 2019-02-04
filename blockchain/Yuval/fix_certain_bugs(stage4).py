from blockchain.Yuval.functions import read_csv_into_page_object,replace_broken_page_object_with_fixed,Save_To_binary_file,Read_From_Binary_File

fixed_csv_file = '1NMGSU61UmYP3i5etkkaH9bm47cyEhjb1P.csv'
x = read_csv_into_page_object(fixed_csv_file)

old_pages = Read_From_Binary_File('1')

#replace_broken page and return a new list of corrected pages
new_pages = replace_broken_page_object_with_fixed(x,old_pages)

#save new pages to main binary file
Save_To_binary_file(new_pages,'1')
