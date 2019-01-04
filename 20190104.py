"""
处理excel文件:https://github.com/python-excel/xlrd  
安装xlrd模块：pip install xlrd  --》显示版本号
引入xlrd
"""
import xlrd   #引入xlrd
book = xlrd.open_workbook("")  #文件的路径是相对路径，执行的话要到对应的路径，不能是外面的，不然会报找不到的；excel是怎么导出的？
print("The number of worksheets is {0}".format(book,nsheets))
print("Worksheet name(s):{0}".format(book.sheet_names()))

sh = book.sheet_by_index(0)
print("{0}{1}{2}".format(sh.name,sh.nrows,sh.ncols))
print("cell D3@ is {0}".format(sh.cell_value(rowx=29,colx=3)))

for rx in range(sh.nrows):
    print(sh.row(rx))


"""
查找多个元素定位:
先写css
li.class值 空格（尖括号）div.class值
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("")
eles = driver.find_element_by_css_selector("li.gl-item div.p-price")
print(len(eles))
for index in range(len(eles)):
    print(eles(index).text)


"""
写入内容到excel文件里：
1.拿到数据，2.循环，3.写入文件：xlwt库模块
3.1.安装，3.2.引入，3.3.
"""
