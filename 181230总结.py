181230-总结：
git下载安装（git-2.20.1-64-bit.exe）；git网站建远程代码库；
命令行工具  cmd  
git --version   #查看git版本，出现版本号，表示安装成功；
cd desktop     #到桌面
git clone 远程代码库地址  #在本地桌面创建git库
cd selenium_basic #进入selenium_basic文件夹
notepad demo.py  #新建demo.py文件--编写-保存-关闭
git add -A  #把刚才的动作内容添加到本地git库
git commit -m "add demo.py"  #引号里是提交的动作
git config --global user.emall "账号的电子邮件"
git config --global user.name "账号的用户名"
git commit -m "add demo.py"  #再次提交
git push #把本地git库的内容上传到远程仓库
登陆动作：账号/密码
提交成功！

python3.7.1下载安装(x86-64)：
python -V #查看版本号
vscode安装下载(https://code.visualstudio.com)：（打开后下载python插件）
chrome浏览器下载：帮助-查看浏览器版本
浏览器驱动下载：https://npm.taobao.org  选择chromedriver.storage 驱动不分32或64位
selenium库下载安装(python的第三方包)：pip install selenium (安装成功会显示selenium版本)(mac默认指向python2，所以命令是pip3)
打开vscode-新建“.py”文件
from selenium import webdriver #引入selenium里webdriver模块
driver = webdriver.Chrome()#创建浏览器实例，把下载的驱动解压后复制到vscode，把执行路径加到驱动后executable_path="./chromedriver"
driver.get("http://www.baidu.com")#打开百度
运行程序，打开百度浏览器，那么恭喜，环境配置成功了；

打开chrome开发者工具：更多工具-开发者工具；右键-inspect；f12或fn+f12；
元素选择器：灰色/激活呈蓝色/选择/高亮显示/源码/
手机端的页面显示：可选择手机型号/
网页源码界面：元素/
页面调试窗口：
资源：包括图片/
网络面板：发出去的所有请求/
性能监视面板：
内存使用面板：
应用使用面板：
安全性面板：
页面设置面板：

网页操作：
页面元素查找；input；元素本身；元素属性；id/name（此属性需要查看是否唯一性）；
driver.find_element_by_id("kw").send_keys("hello world")
driver.find_element_by_name("wd").send_keys("hello world")




周总结：
标签 属性
id
Name
css使用方式：源码-右击-copy-selector-ctrl+f -ctrl+v - 
xpath
class_name:只支持一个值，如果不是，就会报错，此方法不适用，换别的定位方法； 
只有标签：
网页设计原理：html-标签-首尾相应-head：js等引用文件/关键字/title/    body：整个页面显示内容；
div  id 尖括号：表示子元素；
百度搜索css选择器：
点：