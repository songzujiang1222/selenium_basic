181230-�ܽ᣺
git���ذ�װ��git-2.20.1-64-bit.exe����git��վ��Զ�̴���⣻
�����й���  cmd  
git --version   #�鿴git�汾�����ְ汾�ţ���ʾ��װ�ɹ���
cd desktop     #������
git clone Զ�̴�����ַ  #�ڱ������洴��git��
cd selenium_basic #����selenium_basic�ļ���
notepad demo.py  #�½�demo.py�ļ�--��д-����-�ر�
git add -A  #�ѸղŵĶ���������ӵ�����git��
git commit -m "add demo.py"  #���������ύ�Ķ���
git config --global user.emall "�˺ŵĵ����ʼ�"
git config --global user.name "�˺ŵ��û���"
git commit -m "add demo.py"  #�ٴ��ύ
git push #�ѱ���git��������ϴ���Զ�ֿ̲�
��½�������˺�/����
�ύ�ɹ���

python3.7.1���ذ�װ(x86-64)��
python -V #�鿴�汾��
vscode��װ����(https://code.visualstudio.com)�����򿪺�����python�����
chrome��������أ�����-�鿴������汾
������������أ�https://npm.taobao.org  ѡ��chromedriver.storage ��������32��64λ
selenium�����ذ�װ(python�ĵ�������)��pip install selenium (��װ�ɹ�����ʾselenium�汾)(macĬ��ָ��python2������������pip3)
��vscode-�½���.py���ļ�
from selenium import webdriver #����selenium��webdriverģ��
driver = webdriver.Chrome()#���������ʵ���������ص�������ѹ���Ƶ�vscode����ִ��·���ӵ�������executable_path="./chromedriver"
driver.get("http://www.baidu.com")#�򿪰ٶ�
���г��򣬴򿪰ٶ����������ô��ϲ���������óɹ��ˣ�

��chrome�����߹��ߣ����๤��-�����߹��ߣ��Ҽ�-inspect��f12��fn+f12��
Ԫ��ѡ��������ɫ/�������ɫ/ѡ��/������ʾ/Դ��/
�ֻ��˵�ҳ����ʾ����ѡ���ֻ��ͺ�/
��ҳԴ����棺Ԫ��/
ҳ����Դ��ڣ�
��Դ������ͼƬ/
������壺����ȥ����������/
���ܼ�����壺
�ڴ�ʹ����壺
Ӧ��ʹ����壺
��ȫ����壺
ҳ��������壺

��ҳ������
ҳ��Ԫ�ز��ң�input��Ԫ�ر���Ԫ�����ԣ�id/name����������Ҫ�鿴�Ƿ�Ψһ�ԣ���
driver.find_element_by_id("kw").send_keys("hello world")
driver.find_element_by_name("wd").send_keys("hello world")




���ܽ᣺
��ǩ ����
id
Name
cssʹ�÷�ʽ��Դ��-�һ�-copy-selector-ctrl+f -ctrl+v - 
xpath
class_name:ֻ֧��һ��ֵ��������ǣ��ͻᱨ���˷��������ã�����Ķ�λ������ 
ֻ�б�ǩ��
��ҳ���ԭ��html-��ǩ-��β��Ӧ-head��js�������ļ�/�ؼ���/title/    body������ҳ����ʾ���ݣ�
div  id �����ţ���ʾ��Ԫ�أ�
�ٶ�����cssѡ������
�㣺