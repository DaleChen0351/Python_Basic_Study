import csv

# 采用一般的reader and writer
with open("name.csv", "r") as file:
    csv_reader = csv.reader(file)
    # print(next(csv_reader))
    with open("new_name.csv", "w", newline="") as new_file: # 注意python 3.0版本中需要添加此参数，否则会出现空行
        csv_writer = csv.writer(new_file, delimiter="\t")  # 采用table键分割后保存
        for line in csv_reader:
            csv_writer.writerow(line)


# 采用dictwrite and dictwriter
with open("name.csv", "r") as file:

    csv_dict_reader = csv.DictReader(file)

    # for line in csv_dict_reader:
    #     print(line["email"])  # 如果采用上面的line[2]的话，阅读代码的人可能根本就不知道什么是 line[2]的内容

    # with open("new_name2.csv", "w",newline="") as new_file2:
    #     field_names = ["first_name", "last_name", "email"]
    #     csv_dict_writer = csv.DictWriter(new_file2, delimiter="\t", fieldnames=field_names)
    #     csv_dict_writer.writeheader()
    #     for line in csv_dict_reader:
    #         csv_dict_writer.writerow(line)

    with open("new_name3.csv", "w", newline="") as new_file_no_email:
        field_names_no_email = ["first_name", "last_name"]
        csv_dict_writer_no_email = csv.DictWriter(new_file_no_email, delimiter="\t", fieldnames=field_names_no_email)
        csv_dict_writer_no_email.writeheader()
        for line in csv_dict_reader:
            del line["email"]
            csv_dict_writer_no_email.writerow(line)


with open("new_name2.csv","r") as new_file_read:
    csv_reader2 = csv.reader(new_file_read, delimiter="\t")
    for line in csv_reader2:
        print(line)




# CSV Module - How to Read, Parse, and Write CSV Files
# https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=16&t=0s