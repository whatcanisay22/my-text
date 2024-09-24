# import xlrd
# import xlwt
# workbook=xlrd.open_workbook(r"C:\Users\19808\Downloads\data1.xls")
# print(workbook.sheet_names())
# table=workbook.sheet_by_name("Sheet1")
# print("rows:",table.nrows)
# print("columns:",table.ncols)
# print(table.cell_value(1,1))
# print(table.row_values(2))
# x=0
# for i in table.row_values(2):
#     x+=i
# print(x)
import xlrd
import xlwt
import math
workbook=xlrd.open_workbook(r"C:\Users\19808\Downloads\data1.xls")
table=workbook.sheet_by_name("Sheet1")
rows=table.nrows
columns=table.ncols
x=list()
t=0
for i in range(rows):
    for j in table.row_values(i):
        t+=j
    x.append(t)
    t=0
HX=-sum(x[i]*math.log2(x[i]) for i in range(rows))
print("表1：")
print("H(X):",HX)
y=list()
t=0
for i in range(columns):
    for j in table.col_values(i):
        t+=j
    y.append(t)
    t=0
HY=-sum(y[i]*math.log2(y[i]) for i in range(columns))
print("H(Y):",HY)
H=0
for i in range(rows):
    for j in range(columns):
        if table.cell_value(i,j)!=0:
            H+=table.cell_value(i,j)*math.log2(table.cell_value(i,j))
print("H(X,Y):",-H)
print("H(X|Y):",-H-HY)
print("H(Y|X):",-H-HX)
print("I(X;Y):",HX+H+HY)
print("_______________________________")
print("表2：")
workbook=xlrd.open_workbook(r"C:\Users\19808\Downloads\data2.xls")
table=workbook.sheet_by_name("Sheet1")
rows=table.nrows
columns=table.ncols
x=list()
t=0
for i in range(rows):
    for j in table.row_values(i):
        t+=j
    x.append(t)
    t=0
HX=-sum(x[i]*math.log2(x[i]) for i in range(rows))
print("H(X):",HX)
y=list()
t=0
for i in range(columns):
    for j in table.col_values(i):
        t+=j
    y.append(t)
    t=0
HY=-sum(y[i]*math.log2(y[i]) for i in range(columns))
print("H(Y):",HY)
H=0
for i in range(rows):
    for j in range(columns):
        if table.cell_value(i,j)!=0:
            H+=table.cell_value(i,j)*math.log2(table.cell_value(i,j))
print("H(X,Y):",-H)
print("H(X|Y):",-H-HY)
print("H(Y|X):",-H-HX)
print("I(X;Y):",HX+H+HY)