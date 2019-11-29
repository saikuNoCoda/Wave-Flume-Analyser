import xlrd
import xlwt

from xlutils.copy import copy
from xlwt import Workbook
from xlrd import open_workbook

rb = open_workbook('waves.xls')
mysheet = rb.sheet_by_index(0)

numrows = mysheet.nrows
numcols = mysheet.ncols

wb = copy(rb)
w_sheet = wb.get_sheet(0)

st = xlwt.easyxf('pattern: pattern solid;')
st.pattern.pattern_fore_colour = 4
rows = 2

cnt = 0
while(rows < 1050):
	val = (str(mysheet.cell_value(rows,0))).encode('ascii')
	if(len(val) == 0):
		break

	val = abs((float(val)))

	sta = max(rows-30,2)
	en = min(rows+30,1049)

	print(sta,rows,en)
	fl = 1
	for i in range(sta,en):
		val_t =  abs((float((str(mysheet.cell_value(i,0))).encode('ascii'))))
		if(val_t > val):
			fl = 0

	if(fl == 1):
		w_sheet.write(rows,0,mysheet.cell_value(rows,0),st)
		cnt = cnt + 1
	rows = rows + 1

rows = 2

while(rows < 1050):
	val = (str(mysheet.cell_value(rows,1))).encode('ascii')
	if(len(val) == 0):
		break

	val = abs((float(val)))

	sta = max(rows-30,2)
	en = min(rows+30,1049)

	print(sta,rows,en)
	fl = 1
	for i in range(sta,en):
		val_t =  abs((float((str(mysheet.cell_value(i,1))).encode('ascii'))))
		if(val_t > val):
			fl = 0

	if(fl == 1):
		w_sheet.write(rows,1,mysheet.cell_value(rows,1),st)
		cnt = cnt + 1
	rows = rows + 1

print(cnt)

wb.save('final.xls')
# https://docs.google.com/forms/d/e/1FAIpQLScqXrVopU6t63GdRQI9LpaWfzDHiNaIJGbazhSRj-0WPT3cVQ/formResponse