# 概览
java的io大概可以分成以下几类
* 磁盘操作:File
* 字节操作:inputStream和OutputStream
* 字符操作:Reader和Writer
* 对象操作:Serializable
* 网络操作
* 新的输入/输出:NIO

# 磁盘操作
## File类
File类可以用于表示文件和目录的信息,但是它不表示文件的内容

# 字节操作
java I/O使用了装饰者模式

# 字符操作
* GBK 编码中,中文字符占2个字节,英文占1个字节
* UTF-8 编码中,中文字符占3个字节,英文占1个字节
* UTF-16be 编码中,中文字符和英文字符都占2个字符
java使用双字节编码UTF-16be，char类型使用UTF-16be进行编码
char类型占两个字节16位，中文或者英文都能使用一个char来储存

# String的编码方式
String 可以看成一个字符序列，可以指定一个编码方式将它编码为字节序列，也可以指定一个编码方式将一个字节序列解码为 String。
```java
String str1 = "中文";
byte[] bytes = str1.getBytes("UTF-8");
String str2 = new String(bytes, "UTF-8");
System.out.println(str2);
```
在调用无参数 getBytes() 方法时，默认的编码方式不是 UTF-16be。双字节编码的好处是可以使用一个 char 存储中文和英文，而将 String 转为 bytes[] 字节数组就不再需要这个好处，因此也就不再需要双字节编码。getBytes() 的默认编码方式与平台有关，一般为 UTF-8。
```java
byte[] bytes = str1.getBytes();
```

# Reader和Writer
不管是磁盘还是网络传输，最小的储存单位都是字节，而不是字符。但是在程序中操作的通常是字符形式的数据,因此需要提供对字符进行操作的方法。
* InputStreamReader实现从字节流解码成字符流
* OutputStreamWriter实现字符流编码成字节流

# 对象操作
## 序列化
序列化就是将一个对象转化为字节序列,方便储存和传输
* 序列化: ObjectOutputStream.writeObject()
* 反序列化: ObjectInputStream.readObject()
不会对静态变量进行序列化,因为序列化只是保存对象的状态,静态变量属于类的状态
### transient
transient关键字可以使一些属性不会被序列化
ArrayList中储存数据的数组elementData是用transiet修饰的,因为这个数组是动态扩展的,并不是所有的空间都被使用，因此就不需要所有的内容都被序列化。通过重写序列化和反序列化方法，使得可以只序列化数组中有内容的那部分数据。
# 网络操作

# NIO
新的输入/输出(NIO)库是在JDK1.4中引入的,弥补了原来的I/O的不足,提供了高速的、面向块的I/O
