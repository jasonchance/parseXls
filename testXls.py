# coding = UTF-8

from parseXls.parseXls import ParseXls

# TEST
filename = 'backup2.xls'
xlsObj = ParseXls(filename, True)
# print xlsObj.getCell(0, 0)
# exit()
data = xlsObj.readXls()
for row in data:
	print row
exit()