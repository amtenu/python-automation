import csv

file_csv = 'csv_file.txt'


with open(file_csv, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
      
        name = row['Name']
        phone = row['Phone']
        role = row['Role']
        
        print("Fullname: {}, Phone_No: {}, Company_Role: {}".format(name, phone, role))