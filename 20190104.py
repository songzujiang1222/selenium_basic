"""
����excel�ļ�:https://github.com/python-excel/xlrd  
��װxlrdģ�飺pip install xlrd  --����ʾ�汾��
����xlrd
"""
import xlrd   #����xlrd
book = xlrd.open_workbook("")  #�ļ���·�������·����ִ�еĻ�Ҫ����Ӧ��·��������������ģ���Ȼ�ᱨ�Ҳ����ģ�excel����ô�����ģ�
print("The number of worksheets is {0}".format(book,nsheets))
print("Worksheet name(s):{0}".format(book.sheet_names()))

sh = book.sheet_by_index(0)
print("{0}{1}{2}".format(sh.name,sh.nrows,sh.ncols))
print("cell D3@ is {0}".format(sh.cell_value(rowx=29,colx=3)))

for rx in range(sh.nrows):
    print(sh.row(rx))


"""
���Ҷ��Ԫ�ض�λ:
��дcss
li.classֵ �ո񣨼����ţ�div.classֵ
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("")
eles = driver.find_element_by_css_selector("li.gl-item div.p-price")
print(len(eles))
for index in range(len(eles)):
    print(eles(index).text)


"""
д�����ݵ�excel�ļ��
1.�õ����ݣ�2.ѭ����3.д���ļ���xlwt��ģ��
3.1.��װ��3.2.���룬3.3.
"""
