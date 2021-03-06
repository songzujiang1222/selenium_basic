python录屏复习：
vscode安装
项目不需要在VScode里建，建文件夹的时候命名不能有空格；打开文件/打开文件夹；文件的后缀是以.py结尾；
python3里打印东西，需要强行添加括号，不然会报语法错误；print("Hello World") 需要保存一下，文件-save或ctrl+s；
打开终端：Terminal - new terminal - python 文件名称（tab会自动补全） - enter运行程序；
python只能运行“.py”结尾的文件；
放大字体显示：view  -  appearance  -  zoom in ；
pycharm编译器：针对于python的编译器，而vscode不是，vscode可以编译所有语言的编译器-自适应；工具环境变量配置；
右键表示粘贴：
python3基础语法：
敏感词/保留字/关键字：import keyword       print(keyword.kwlist)
False大写的F是关键字,小写的f就不是，即可以定义；
assert:断言，判断
= 赋值，给值
== 判断
class  类
def   = define：定义
del   = delete：删除
elif  = else if：否则
for   迭代器，对什么而言
global   全局的
lambda   匿名函数：a = lambda x:x+10      print(a(3))#必须给值；
try    和except连用
yield   生成器，

a = 10 #在编程语言里，都是从右往左读，即把10赋给a，后面用到都是对左边进行操作；之间用空格隔开，好的代码习惯，更美观；
标识符，就是起名字的；
注释代码：选中后按住ctrl+/；所有语言的注释都可以用此方法；
缩进：顶格写的代码是真的，生效的，缩进里的内容才会去执行，否则缩进里的内容不会执行；缩进里的内容属于前面冒号的内容；都是顶格写的，就谁都不属于；
运算符：+-*/   **:表示多少次方    1/2:表示开根号   //：表示取商    %：表示取余数（判断基偶性，1-代表基数） 
比较运算符：== 判断     > 大于   < 小于   != 不等于  >= 大于等于   
a = 1
a += 1    (等同于a = a + 1 ，但一般不用后者，因为需要读两次a）,同样的适用+-*/
a,b = b,a  换值：即a/b交换值；
i,j,k = 1,2,3 连续赋值：即i=1，j=2，k=3；
以上是python第一节课上午录屏；


查看类型：type（内容）     print(type（1+2j）) 
字符串：单引号/双引号/三个单引号/三个双引号,里面都是字符串，不同的是换行时，三个的不需要"\",而前两个需要“\”;
向上箭头表示上一次执行的命令；
python大神：全程用python写出--游戏博物馆/电脑博物馆；
+：可以将字符串拼接；如print（a+b+c）
，：只是分开打印；如：print(a,b,c)
end=“，”   不换行，且以逗号隔开；
print（）  默认是换行的，不换行需要用end=“”，引号内没有东西就是无间隔不换行；
a.join(b)  把b拆开，插入到a里，最后一个字符没有a；即b1ab2ab3ab4abn...
a1 = "app\nle"   打印出来是换行的app   le    \n表示换行；
a2 = r"app\nle"  打印出来是不换行的app\nle  ;r表示隐身/不解析；
打开文件方法：open（"文件地址","打开方式"）；打开方式a表示追加；文件同一时刻只能执行一个动作，即读的时候不能去写等；文件打开之后需要关闭：file.close()
file = open('c:\users\dell\..\a.txt','r')#报错解决办法：1）把单反斜杠变成双反斜杠，2）在引号前加'r',3)把反斜杠改为正斜杠；
print(flie.read())  #打印读到文件的内容
file.close()  #关闭文件
打开方式：r/w/a/x/   b表示二进制，需和其他连用；
查看open方法使用的参数使用：英文格式下，按住ctrl，然后鼠标放上去；或print（help（open）），会在终端打印；
另一种打开文件的方法：（执行效率高，且不用担心用上面方法时会忘了关闭文件）
with open('c:/users/dell/../a.txt','r') as file:  #with本身就是一个关闭器，运行完自动关闭；
    file.readline() 
同一个文件同时只能执行一次；所以必须注释掉其他的动作，只留一个运行；

with open('c:/users/dell/../a.txt','a') as file:  #a是追加写东西，#写中文的话会乱码，解决方法是在后面加'encoding='utf-8''
    file.write('222222\nwerwer\n')   #写日志；\n表示换行；

file.read()      #读取整个文本
file.readline()  #读取一行
file.readlines() #读取多行
一个单词后面有（），表示它是个方法；

if  如果，假如   表示判断，后加条件；“三条平行的大河”
elif   再或，再假如 #后可加条件，代码往上找第一个冒号的条件；是对一个变量进行判断，“一条大河分了三个分支”
else  否则，不然  #后只能接冒号，不能接条件，所以有elif；
赋值定义变量 a = 1  空格习惯
表达式：a+b>c       没有空格
注意if和elif使用场合的区别：if后的内容都会去执行，而elif是如果不成立，就不会往它下面的内容走了；所以elif的效率更高；但if不用考虑条件；
嵌套：


第二节课：数据结构
字符串：string = 'hello'
取值：中括号里加下标 string[0]  第一个字符的下标是0，最后一个字符的下标是‘-1’；
切片：切片的长度（后面的值减去前面的值）代表取出的个数，也就是最后一个值是取不到的，string[0:-1],头和尾可以省略不写；
步长：每几个值然后取第一个值，不够的话还是取第一个值；一个一个的取的步长为1，跳一个数取值的步长是2；string[::2]
字符串的方法：能有这个字符串可以去干什么事情
1）string.count('e')  #计算e出现的次数；  能匹配大小写？？？
2）str(a)  #把括号里的内容a转换成字符串类型；
3）string.capitalize()  #首字母大写
4）string.upper()       #把所有字母都变为大写；
5) string.lower()       #把所有字母都变为小写；
6）string.islower()     #结果里面全都是小写，判断语句，返回true或false；
7）string.isdigit()     #判断字符串里内容是否都是数字，判断语句，返回true或false；
8）string.find('e')     #找，找到引号里内容第一次出现的地方，显示出现地方的下标，找到第一个就不找了，结束了；
9）string.index('e')    #也是找，和find类型，都是找到了显示下标。区别在于，find找不到会报“-1”，而index找不到会报错；

读取文件方法：
with open(r'路径','方式',encoding='utf-8') as file:
    a = file.read()
    print(a)

正则表达式：
import re  # 导入正则表达式，regular expression的缩写，
string = 'wehoisifwe23423423'
pattern = re.compile(r'e')  #创建/制作正则表达式，引号里是要匹配的内容，字符串‘e’可以更改成任意你想要的东西
result = re.findall(pattern.string) #等效于 result = pattern.findall(string)；用正则表达式去目标字符串匹配；string是你要查找的对象
print(result)  #查找的内容是以列表的形式['e','e','e','e','e','e']

举例：
with open(r'路径','方式',encoding='utf-8') as file:
    a = file.read()
    pattern = re.compile(r'e')
    result = pattern.findall(a)
    result = str(result)
    b = result.count('e')
    print(b)

 Vscode的四边形弹出的搜索框里输入@recommand，安装提示的插件

 第二节课下午：数据结构
 列表list：放数据的集合，特点就是多，各种各样的数据（数字/字符串/列表）都可以放在里面，且整齐有序的，中括号，逗号隔开，[,,'',]
 单双引号的使用：系统给的用单引号，人为输入的用双引号；
 取值：中括号里加下标 string[0]  第一个字符的下标是0，最后一个字符的下标是‘-1’；
 切片：切片的长度（后面的值减去前面的值）代表取出的个数，也就是最后一个值是取不到的，list[0:-1],头和尾可以省略不写；
 取‘值中值’：list[][]
 列表的方法：
 1)list.count('e')   #统计引号里内容e出现的次数；
 2)list.reverse()    #反向，执行了此方法，就改变了原来的值，所以不需要重新定义变量，还是打印原来的变量；
 3)list.remove('e')  #删除列表中的引号里的东西，且只能删一个，如果有多个，只会删第一个，同样改变了原来的值，所以不需要重新定义变量，还是打印原来的变量；
 4)list.pop("n")     #删除列表中的引号里传进来下标的东西，如果不传值的话会删最后一个；
 “先进后出”的原则，类似于栈；“先进先出”的原则用在哪里尼？？？
 5）list.append("watermelon西瓜")  #添加括号里的内容到原本的列表里,如果有引号，也一起添加进去。如果是一个列表，就把这个列表当一个元素添加进来；
 6）list.extend("watermelon西瓜")  #要添加的东西一定是个可以切片的东西，切片分开后添加到原本列表里；
 7）list.copy()    #浅复制，单纯把列表里东西的内存地址拿过来；
 8）import copy     copy.deepcopy(list)  #深复制，重新分配了内存地址；
 9）list.clear()   #清空列表里的内容，只剩下一个中括号；
 10)list.index("e")  #查找括号里引号下内容e出现的位置；
 11)list.insert(n,"e")   #插入（n是要插入位置的下标，e要插入的值）；
 12）list()     #把括号里的内容转换成列表；

 列表的排序：
 1)list.sort()   #从小到大排序；在原来的基础上进行排序，改变了原来的列表
 2)list[::-1]    #从大到小排序；也可以用reverse实现从大到小排序：list.reverse()
 3)sorted(list)  #从小到大排序，是生成了一个新的排了序的列表，但本身没有改变；

 输入：input()  #从终端进行输入，按enter按键结束输入；然后执行打印出结果；
int（）  #转化成整数
float()  #转化成小数

元组tuple ：本身不能被更改；小括号，逗号，只能进行查询操作，不能增删改；所以查询效率会特别高；
取值：
切片：
排序：
1）倒序：tup[::-1]
元组的方法：
1）tuple.count("e")  #统计括号里引号的内容e出现的次数；
2) tuple.index("e")  #查询括号里引号的内容e第一次出现的位置；
3）tuple（a）         #把a转化成元组

编辑器里第一行写#coding = utf-8；一般变量名我们用小写；

字典：大括号，键，冒号，值，逗号，键值对的形式，无序的，字典里的键不能是相同的，不然后面的会把前面的值覆盖掉；
查：dic["键"]  #通过键，查出值；
字典的方法：
1)dic.clear()  #清空，只剩下一个大括号；
2)dic.copy()   #浅复制，
3)dic.pop("e") #删除，括号里需要给参数，给键，
4)dic.popitem()  #删除，随机删除，因为是无序的，不用给参数；
5)dic.get("e")  #取值，括号里需要给参数，给键；如果没有的话返回none，不会报错，而print（）没有的话会报错；
6)dic.keys()  #获取所有的键，结果是那种类型？？？
7)dic.values() #获取所有的值，结果是那种类型？？？
8)dic.items()   #把字典里的东西一对对的组成元组当成一个元素取出来，结果是那种类型？？？
9)dic.fromkeys("","")  #初始化创建字典，第一个参数会拆，第二个参数是值，没有的话值给none，不会拆；
10）s=''.join(dic)  #把字典转化成字符串，此方法会把乱七八糟的符号去掉的；
11）s=str(dic)   #把字典转化成字符串，是在字典外直接加个引号让它变成字符串，如果取值的话，会有各种符号的影响；
12）dic["e"] = "f" #修改字典里e的值，先通过键e取出来，然后重新赋值f即可；
13）dic["w"] = "z" #往字典里添加"w":"z"值，前提是没有键w这个键，此方法可以在字典里添加新的键值对；

方法里如果除了self还有别的参数，说明需要传参，如果只有一个self，则不需要传参；

第三节课：for循环/while循环
上午：
len(str)  #length 长度  返回字符串的长度，能切片的都有长度；
for 后面的变量一定要是刚刚定义的，之前没有被定义过；
i是后面的每一个遍历的值；
range 数字范围，表示从零开始到什么数结束；默认从零开始数，如果是两个参数的话，后面的数是取不到的；第三个参数是步长；range(1,10,2)
for i in range(len(str)):   #i是全新的变量，只在for循环内有效，对range有用，range(7)就是range(0,7)，值是1-6
    print(str[i])
对有顺序的数字结构进行循环：只要是能切片的都可以；切片只是一个查询操作，并没有对原来的值进行修改；能用下标去取的；
for i in str:   #str是字符串，当然也可以换成list等；
    print(i)
往列表里添加值的方法：先定义一个空列表，再调用append方法添加；extend方法是把原本是个集合的东西打散后添加；
for循环是对每一个元素进行处理；
列表生成器：lis2 = [i*i for i in lis1 if i%2 == 1]  #先定义一个列表lis2，for前面的是值的处理，for后面是循环，i*i等效于i**2，循环后面可加条件；

下午：
循环的过程，叫遍历；
列表生成式：python里特有的快速生成列表的表达式，新列表名 = [结果表达式 for i in 原列表 if 条件]
双循环：外循环/内循环；越在里面的循环就越先执行完；外循环取第一个值时，内循环要完成一个循环，才会出来取外循环的第二个值，前提是没有键w这个键，此方法可以在字典里添加新的键值对；
九九乘法表:
for i in range(1,10):  #1-9
    for j in range(1,i+1): #1-9
        print(j,'*',i,"=",i*j,end="\t")   #错写成了ending=,*忘了加引号，漏写了"=";end="\t"表示四个空格；
    print()  #等效于print(end="\n")

格式化字符串：'%d*%d=%d'%(i,j,i*j)  即："表达式需要替换的用%表示"   %  (参数，以逗号隔开)，把变量都提取出来了，参数顺序一一对应；

print()  #默认换行
print(end="")  #空格，不换行
print(end="\n")  #换行，等效于什么都不写print()，只要把\n改成任何其他的，就是不换行，如\w就在结尾加w；
print(end="\t")  #四个空格，不换行

while循环：条件，冒号，循环体，
1)while后的条件为真，则执行缩进里的循环体，执行完后再继续执行while的条件判断，直到不满足条件后，while循环结束；
2)注意条件进不去，或者时一直为真成为了死循环；
3）使用场景：

for循环和while循环的区别：
1）荷花第几天时开了多少朵？开到多少朵的时候是第多少天？


定义函数：def name():
1)定义：def name（self） #定义时括号里是参数，调用时就必须传具体的值；
2）调用：name(10)  #调用时，如果定义的时候有参数，就必须给值；
3）封装了一个简单的调用方法；调用的时候才会被执行，不调用就不会被执行；
4）函数和方法的区别;???
5)返回值：return 值，如果没有则是none； #return是给调用这个方法的人看的，而print只是在终端秀一下；


第四节课：定义函数
def get_info(name,age):  #定义函数
    print("")

 字符串也支持乘法，表示字符串几倍的出现；
 默认值：如果不传值，就使用默认值，如果传，就使用传的值；
 定义函数的时候，括号里参数是什么类型，传值的时候就要给什么样类型的值；
 get_info("xiaoming",14) #调用，传值的时候，如果没有把变量名和值一起传的话，默认就是会一一对应，如果类型不同就会报错；
函数冒号后缩进里定义的变量只能被此函数使用，如果是定义在外面，就是公用的；

def get_infos(*args):  #定义函数，括号里*代表传进来的是一个元组tuple，
    print(args)
get_infos(1,2,45,6)  #调用，会把括号里的内容当成一个元组传进去；

求和的方法：先定义求和变量s=0，再for循环for i in 对象，然后s += i，最后打印s即可；
a = [1,3,6,9,23]
s = 0
for i in a :
    s += i   #s = s + i 
    print(s)
print(s)

举例：
def word(args):
    with open(r"E:\selenium_basic\2019-01\0106.txt",'w',encoding="utf-8") as a:
        a.write(args)
word(input('请输入单词：'))


第四节课下午：
try用法：
1）捕获代码中出现的异常：一旦try块的代码报错，就执行except块的代码；
2）作用：把原本报错的代码，通过此方法让它执行下去；
except块：
1）后面跟的异常名，如果没有此类型错误的话，代码还是会报错，但如果不跟，就代表所有情况；
尝试看代码报错信息：
1）很多错误的时候，只会报try块中第一个的错误，然后执行中断；
2）语法错误捕捉不到，因为python自带的编译器会编译失败，就不会去执行；
except后面的as内容：#在异常类型后面加参数as：
1）as后面的变量，一般用e，具体告诉你错误的原因；
else块：
1）try块运行正常，有此块的话会执行此else块；
finally块：
1）最终一定会执行的代码；

重点：
1)首先确定是否是python自带的模块，是的话直接import即可。但如果不是，需要先在终端使用命令pip安装后导入模块；
2）一般python会自带pip安装包，如果没有，需要先安装pip安装包；
3）一个是导入模块，引用时使用模块点方法；
import keyword  #导入模块包
print(keyword.kwlist)  #使用时使用模块.方法；
4）一个是导入模块中的方法，引用时直接用模块；
from keyword import kwlist  #引入某一个方法，此只引用了此模块包下的一个方法；
print(kwlist)   #使用这一个已经引入了方法
5)导入模块下包所有的方法：
from keyword import *   #引入包下所有的方法，*代表所有的方法；
print(kwlist)
6）
import requests
response = requests.get("http://www.baidu.com")  # get方法，后面跟网址？？？状态：2-成功，3-重定向，4-找不到，5-服务器异常；
print(response.text)  #text表示文本内容；


面向对象：框架已经有了，抽象（的类）-实例化（具体），
面向过程：从零开始，
1)概念：
2)关键词：class 类  抽象的/具体的？？？
3）实例化：类名()   john = student()  #把一个抽象的类定义成一个具体的东西，
4）def study(self)中的self是必传的，且还不是一个参数；
5）共有属性：
6）方法调用：john.study()
7)内置方法：def __init__(self):  #往类里面传参数，就是属性；self把传进来的参数变成属性；如果不传参，可以不写；实例化的入口函数；
8）私有方法：方法名前加双下划线，不能被直接调用；#在某个方法名前加上双下划线，就变成了私有方法；私有方法不能被直接调用
9）如果想传参数给整个类做属性，一定要在init方法里传；
class student:    #定义学生类；
    number = 1234  #方法外定义，是共有属性；
    point = 0    #方法外定义，是共有属性；
    def __init__(self,name,age,gender):  #如果想传参数变成属性，一定要在init方法时传；如果此方法里有参数，则调用时必须给值；
        self.name = name   #self把传进来的参数变成属性；
        self.age =  age     #self把传进来的参数变成属性；
        self.gender = gender  #self把传进来的参数变成属性；
    def study(self):  #定义方法：self必须要传，且还不算参数；
        print("我在学习")
    def ask(self):
        print("我在问问题")
    def think(self):
        print("我在思考")
john = student()  #实例化:类名后面加个括号，就是实例化；此时可以传属性； 
john.study()    #调用：实例化对象.方法后面加个括号，就是调用某个方法；
john.name = "john"  #调用共有属性；
10）除init方法外，在其他方法里传参，就是它这个方法的，和整个类毫无关系；
11）定义方法的名字不能和别的方法名，关键词重复，不然会报错；
12）上面传的只是一个虚的名字，下面调用的时候传实际的值；
13）乘法表：
class ChenFaBiao:  #定义类，类名一般不用下划线，首字母大写
    def jiu_jiu(self,n):   #定义方法，方法名一般用下划线隔开；
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("%d*%d=%d"%(j,i,i*j),end='\t')  #列表生成式
            print()  # j执行完后换行；
a = ChenFaBiao()   #实例化
a.jiu_jiu(5)  # 五五乘法表
14）判断能否组成三角形：
class SanJiaoXing:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c   
    def judge(self):
        a = self.a
        b = self.b
        c = self.c  
        if a+b>c and a+c>b and b+c>a:
            print("能组成一个三角形")
        else:
            print("不能组成一个三角形")
bian = SanJiaoXing(-3,4,5)
bian.judge()

继承：把被继承类的类型放在继承的类的后面的括号里；获得被继承类里的所有；
1）如果自己没有的话，就继承父类的方法；
2)如果自己也有这个方法，则用自己的方法，父类被覆盖，没有的话才会去继承，找父类的方法；
3）什么都没有的话就用pass占位符，不然会报错；


第五节课上午：
继承：
多继承：
1）如果两个都有的时候，会继承第一个（第一位），除非第一位没有此方法，才会调用第一位的方法；
2）如果被继承的类也继承了别的类，就一层层继承；（儿子也继承了爷爷的类）；
3）儿子会优先继承第一个爸爸；
4）python3会先继承自己直接继承的类，即第一个爸爸找不到，就找第二个爸爸；第二个爸爸也找不到的话，会再后头找第一个爸爸的爸爸；
5）python3：是新式类的继承方式，先找最亲的爸爸（括号里第一个继承的类），然后再找第二个爸爸（括号里第二个继承的类），当爸爸都找不到的时候，会再找第一个爸爸的父类；

类的命名方式：多个单词的话，只需要将首字母大写；
方法的命名方式：多个单词的话，只需要将单词之间用下划线连接即可；

函数里方法调用方法：
1）在方法的前面加一个self；
2）参数名传什么名都可以，只需要个数对应，类型对应即可；
3）传参：括号里只是定义，只是一个名字，让方法体看到这个参数；而调用的时候，必须给一个符合的实际的值；
4）调用的话如果没有给出具体的值，会报错：NameError
class PlusNumber:
    def number_int(self,a,b):
        a = int(a)
        b = int(b)
        return a+b
    def number_float(self,a,b):
        a = float(a)
        b = float(b)
        return a+b
    def number_all(self,a,b,c,d):
        return self.number_int(a,b)+self.number_float(c,d)
num = PlusNumber()
num.number_int(3,4)
num.number_float(1.2,2.1)
num.number_all(a=1,b=2,c=1.2,d=2.1)

不需要实例化去调用方法：
1）@classmethod    #类方法，类方法可以同时被类和对象调用；
   def name(cls):   #cls和self一样，不是参数
类方法：
1）@classmethod
2）cls
3）调用：类.方法   #用类直接去调用
4）实例化后，也可以调用类方法；#先实例化，再调用方法；


1）@staticmethod   #静态方法，和类没什么太大关系，没什么共同特征，不属于这个类，但是可以被此类和方法调用；
   def have_breakfast():  #静态方法后括号里是空的，可以往里面传参，随便传参，既没有类，也没有对象；但可以同时被类和对象调用；
2）


普通方法：
1）方法后括号里是self：#self代表的是对象，和类方法中的cls代表的是一个类一样；


继承问题：
1）python3:新式类  横向继承
   python2：经典类   纵向继承
2） 
class DecFifteen:

    def __init__(self):  #每次实例化的时候都会被调用
       print("每次实例化的时候都会被调用")

    @classmethod
    def write_file(cls,name,content):
       with open(name,'w',encoding="utf-8") as file:
           file.write(content)
    @staticmethod
    def haha_shouting(a):
       print(a,"hahahahahha")
    def requests_html(self,url):
        response = r.get(url)
        html = response.content
        return str(html,"utf-8")
    def re_exe(self,re_url,html):
        pattern = re.compile(re_url,re.S)
        result = pattern.findall(html)
        return result
songzujiang = DecFifteen()
DecFifteen.write_file("666.txt","这是一个测试")
html = songzujiang.requests_html("http://www.baidu.com")
print(html)
songzujiang.write_file("666.txt","html")

songzujiang.re_exe(r'<img.*?alt=".*?'src=".*?"class="",html)  #匹配：.*?的用法需要巩固；


第五节课下午：
正则表达式：re
1）text和content的区别？？？text是str格式，而content是bite（二进制）格式；json()是字典；
2）import json   #
   import requests  #导入请求的方法：上网
3）pattern = re.compile(r"\d")  #查找一个数字，\d\d就是查找两个数字；\d{1,4}是查找大括号里写的1-4个数字的所有数字；大括号里前面不写表示从零开始找，后面数字不写表示无限大数字；
r"\d+"表示匹配所有数字；
4）\w  #表示匹配数字/字母/下划线；  \w+   表示匹配所有的数字字母下划线；
5）\W   #表示匹配一个不是数字、字母、下划线的东西；   \W+  表示匹配所有不是数字、字母、下划线的东西；
6）\D   表示匹配不是数字的一个东西？？               \D+ 表示匹配不是数字的所有东西；
7）@\w+
8）pingan.johnsw@eric.com  #正则表达式中.号代表匹配所有内容，一个个的匹配；
9）\ 反斜杠表示-转义：
10）+  表示匹配所有
11）{a，b}  表示匹配位数
12）除去第一位：是因为第一位是用w或d去匹配的，后面的是用+去匹配的；
13）\w 字母数字下划线
    \W 非字母数字下划线
    \d  数字   等效于[0123456789],也等效于[0-9]
    \D  非数字
    .   所有
    +   匹配一次或多次,目标效果等于{1，}
    {1,4}  匹配一次到四次
    {，4}  匹配至多四次
    {1，}   匹配至少一次
14）正则表达式默认的是贪婪模式：尽可能多的去匹配；
15）? 解除+号的贪婪模式：再+后加一个问号；#即：？ 问号解除贪婪模式（或称为懒惰模式），一般接在次数的正则表达式后面使用；
16)*  表示匹配零次或多次，目标效果等于{0,}
17）.*?  万能表达式，对于任何东西能够匹配多次；#万能表达式，匹配任何你想匹配的内容；
18）[]   可以放很多东西，是你想匹配的对象；中括号里是你可以匹配的对象；
19)()    表示我只显示括号里的内容；只把括号里的内容秀出来；
20）开头-结尾：万能表达式需要你告诉它从哪里开始匹配，匹配到哪里结束；
21）找到你想找内容的位置；确定你要找的内容的唯一性；确定完之后写正则表达式；
22）换页？？？第五节课没来的及讲
23）爬网页的时候，建议加re.S 是把整个网页当成字符串的意思：
24)js文件？？？
























 


























