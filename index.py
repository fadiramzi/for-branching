import csv
#  open the file
try:
    file = open('data.csv','r')
    rowsReader = csv.reader(file)
# ['#', 'name', 'age', 'email']
# [1, dd, fsdf, df]
    next(rowsReader)
    lst = []
    for r in rowsReader:
        lst.append(r[-1])
    print(lst)
    # lst.pop(0)
except ZeroDivisionError:
    print('Zero div error')
except OSError:
    print("Cannot locate the file")
    
print('process done')
