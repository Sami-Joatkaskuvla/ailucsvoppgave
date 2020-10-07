import csv
def read_csv(filname):
    filename = filname
    fields=[]
    rows=[]
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("total number of rows: %d"%(csvreader.line_num))
        print('field names are: ' + ', '.join(field for field in fields))
    
        print('\nFirst %d'%(csvreader.line_num - 1) +' rows are:\n')
        for row in rows[:(csvreader.line_num - 1)]:
            for col in row:
                print(col),
            print('\n')
    global lis
    dunk = [fields]
    lis = dunk + rows
    
read_csv("characters.csv")

def write_csv(filname, dataray):
    with open(filname, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(dataray)

write_csv("ok.csv", lis)

        
