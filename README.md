## learn-python3
Learn Python 3 example code.

### Python3 学习

* [基础](./basic)
* [函数](./function)
* [高级特性](./advance)
* [函数式编程](./functional)
* [模块](./module)
* [面向对象编程](./oop)
* [错误、调试和测试](./debug)
* [IO编程](./io)
* [进程和线程](./task)
* [常用内建模块](./common)
* [常用第三方模块](./packages)
* [图形界面](./gui)
* [网络编程](./socket)
* [电子邮件](./mail)
* [数据库](./database)
* [异步IO](./async)


### Python3 实战项目

* [web demo](./web)
* [spider](./spider)

### Python3 内置函数

abs() 数字的绝对值

all() 判断可迭代参数iterable的所有元素是否不可为0、''、False或者iterable为空，返回True,否则返回False

any() 判断可迭代参数iterable是否全部为空，全空返回False，否则True

ascii() 返回一个可打印字符串方式表示，非ASCII会转化ASCII

bin() 返回整型int 或 长整型 long int的二进制表示

bool() 转换为布尔类型

bytearray() 新字节数组，元素0<= x <= 256

bytes() 返回一个新的bytes对象

callable() 检查一个对象是否可调用

chr() 返回0~256内对应的一个字符

classmethod 修饰符对应的函数不需要实例化

compile() 将一个字符串编译为字节代码

complex() 创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数

delattr() 删除属性

dict() 创建一个字典

dir()  获得当前模块的属性列表

divmod() 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)

enumerate() 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

eval() 用来执行一个字符串表达式，并返回表达式的值

exec()  执行储存在字符串或文件中的 Python 语句

filter() 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

float()  用于将整数和字符串转换成浮点数

format()  格式化字符串

frozenset()  返回一个冻结的集合，冻结后集合不能再添加或删除任何元素

getattr() 用于返回一个对象属性值

globals() 以字典类型返回当前位置的全部全局变量

hasattr() 判断对象是否包含对应的属性

hash() 获取取一个对象（字符串或者数值等）的哈希值

help() 查看函数或模块用途的详细说明

hex() 用于将10进制整数转换成16进制整数

id()  获取对象的内存地址

input()  用来获取控制台的输入

int() 将一个字符串会数字转换为整型

isinstance()  判断一个对象是否是一个已知的类型

issubclass()  判断参数 class 是否是类型参数 classinfo 的子类

iter() 用来生成迭代器

len()  对象（字符、列表、元组等）长度或项目个数

list()  将元组转换为列表

locals()  以字典类型返回当前位置的全部局部变量

map()  提供的函数对指定序列做映射

max()  返回给定参数的最大值，参数可以为序列

memoryview() 给定参数的内存查看对象(Momory view)

min() 返回给定参数的最小值，参数可以为序列

next()  迭代器的下一个项目

object()

oct() 将一个整数转换成8进制字符串

open() 用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写

ord()  对应的十进制整数

pow() 返回 xy（x的y次方） 的值

print() 打印输出

property()  在新式类中返回属性值

range()  创建一个整数列表，一般用在 for 循环中

repr()   将对象转化为供解释器读取的形式

reversed()  返回一个反转的迭代器

round()  浮点数x的四舍五入值

set()  创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

setattr() 设置属性值，该属性必须存在

slice()  切片对象，主要用在切片操作函数里的参数传递

sorted()  对所有可迭代的对象进行排序操作

staticmethod()  返回函数的静态方法

str() 将对象转化为适于人阅读的形式

sum()  对系列进行求和计算

super() 调用下一个父类(超类)并返回该父类实例的方法

tuple()  将列表转换为元组

type() 只有第一个参数则返回对象的类型，三个参数返回新的类型对象

vars()  返回对象object的属性和属性值的字典对象

zip()  将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

\_\_import__()  动态加载类和函数

### Python小知识点
* 保留关键字

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

* 在函数中接收元组与字典：使用 * 或 ** 作为元组或字典的前缀，来使它们作为一个参数为函数所接收