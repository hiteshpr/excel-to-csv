
import xlrd
import csv

with xlrd.open_workbook('nayan.xlsx') as wb:
    sh = wb.sheet_by_index(0) 
    with open('nayan.csv', 'w') as f:  
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))


