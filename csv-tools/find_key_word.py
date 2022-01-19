import csv

def read_csv(file_path_name,origin_row_header,keyword):
    res_arr = []
    csv_file = open(file_path_name,"r")
    print('文件打开完成，地址在'+file_path_name)
    dict_reader = csv.DictReader(csv_file)
    for row in dict_reader:  
        if if_find_keyword(row[origin_row_header],keyword) == 1:
            res_arr.append(row)
    csv_file.close()
    return res_arr 

def if_find_keyword(text,keyword):
    if text.find(keyword) == -1:
        return 0
    else:
        return 1

def write_csv(data,file_path_name,file_header):
    csv_file = open(file_path_name, "w")
    dict_writer = csv.DictWriter(csv_file, file_header)
    dict_writer.writeheader()
    for row in data:
        dict_writer.writerow(row)
    csv_file.close()
    print('文件写入完成，地址在'+file_path_name)
    return 0    

res_data = read_csv(file_path_name,origin_row_header,keyword);
write_csv(data,file_path_name,file_header);