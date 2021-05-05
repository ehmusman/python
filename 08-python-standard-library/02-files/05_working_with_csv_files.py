import csv


# write to CSV
# with open("data1.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["user_id", "user_name", "user_email"])
#     writer.writerow([3, "Ehsan", "Ehsan@gmail.com"])
#     writer.writerow([4, "Ali", "Ali@gmail.com"])

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["user_id", "user_name", "user_email"])
#     writer.writerow([1, "Usman", "Usman@gmail.com"])
#     writer.writerow([2, "farooq", "farooq@gmail.com"])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# Combining two CSV files

with open("data.csv") as file, open("data1.csv") as file1:
    reader = csv.reader(file)
    reader1 = csv.reader(file1)
    reader_list = list(reader)
    reader1_list = list(reader1)
    # print(reader_list, reader1_list)
    header = reader_list[0]
    print("header", header)
    body = reader_list[1:] + reader1_list[1:]
    print("body", body)
    combined_data = [header] + body
    print(combined_data)
    with open("combined.csv", "w") as combined:
        writer = csv.writer(combined)
        writer.writerows(combined_data)
    # print(list(reader))
    # for row in reader:
    #     print(row)
