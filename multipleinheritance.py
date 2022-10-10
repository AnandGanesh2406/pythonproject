import xlrd

loc = ("c:\\user\\anand\\documents\\book1.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
print(sheet.ncols)
