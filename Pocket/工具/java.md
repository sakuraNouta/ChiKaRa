## volatile关键字
可见性，原子性，有序性

## &与 |或 ~非
与运算，0xff是11111111，进行与运算时只取低八位，其他为0，进行求余。
# 容器
## Collection
1. Set
    * TreeSet：基于红黑树实现，支持有序性操作，例如根据一个范围查找元素的操作。但是查找效率不如 HashSet，HashSet 查找的时间复杂度为 O(1)，TreeSet 则为 O(logN)。

    * HashSet：基于哈希表实现，支持快速查找，但不支持有序性操作。并且失去了元素的插入顺序信息，也就是说使用 Iterator 遍历 HashSet 得到的结果是不确定的。

    * LinkedHashSet：具有 HashSet 的查找效率，且内部使用双向链表维护元素的插入顺序。

2. List
    * ArrayList：基于动态数组实现，支持随机访问。

    * Vector：和 ArrayList 类似，但它是线程安全的。

    * LinkedList：基于双向链表实现，只能顺序访问，但是可以快速地在链表中间插入和删除元 素。不仅如此，LinkedList 还可以用作栈、队列和双向队列。

3. Queue
    * LinkedList：可以用它来实现双向队列。

    * PriorityQueue：基于堆结构实现，可以用它来实现优先队列。
## Map
* TreeMap：基于红黑树实现。

* HashMap：基于哈希表实现。
> 内部包含了一个Entry类型的数组table<br>
> Entry存储着键值对，包含四个字段，是一个链表<br>
> HashMap以拉链法解决冲突，同一个链表中存放着hash值相同的Entry<br>
> 键值可以存储null

* HashTable：和 HashMap 类似，但它是线程安全的，这意味着同一时刻多个线程可以同时写入 HashTable 并且不会导致数据不一致。它是遗留类，不应该去使用它。现在可以使用 ConcurrentHashMap 来支持线程安全，并且 ConcurrentHashMap 的效率会更高，因为 ConcurrentHashMap 引入了分段锁。

* LinkedHashMap：使用双向链表来维护元素的顺序，顺序为插入顺序或者最近最少使用（LRU）顺序。

其余参考：<a href="https://github.com/CyC2018/CS-Notes/blob/master/notes/Java%20%E5%AE%B9%E5%99%A8.md">容器</a>

# 堆栈
堆中存放对象的内容<br>
栈中存放原始数据类型的局部变量数据和对象的引用<br>
字符串是一个特殊包装类,其引用是存放在栈里的<br>
而对象内容必须根据创建方式不同定(常量池和堆)<br>
有的是编译期就已经创建好，存放在字符串常量池中<br>
运行时才被创建的.使用new关键字，存放在堆中。
### 字符串常量池
* jdk6前 方法区
* jdk7后 堆

## equals() 与 ==
* equals()是对象的方法
* 对于基本类型, == 判断两个值是否相等，基本类型没有equals()方法
* 对于引用类型，== 判断两个变量是否引用同一个对象，而equals()判断引用的对象是否等价

### equals()类问题
String类型有常量池<br>
字符串常量，它们在编译期就被确定了
当一个字符串由多个字符串常量连接而成时，它自己肯定也是字符串常量,也同样在编译期就被解析为一个字符串常量
```java
String str1 = "hello";
String str2 = "hello";
String str3 = "he" + "llo";
System.out.println(str1 == str2); //true
System.out.println(str1 == str3); //true
```
如果没有对equals方法进行重写，则比较的是引用类型的变量所指向的对象的地址；<br>
诸如String、Date等类对equals方法进行了重写的话，先比较类型，后比较所指向的对象的内容。<br>
一般的immutable class都有重写
```java
String str1 = new String("hello");
String str2 = new String("hello");
System.out.println(str1 == str2);//false 比较引用
System.out.println(str1.equals(str2));//true 比较内容
```
### imutable class(不可变类)
String，基本类型的包装类,Date,BigInteger,BigDecimal等


# 数据类型 
Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

* boolean/1
* byte/8
* char/16
* short/16
* int/32
* float/32
* long/64
* double/64

# 自动类型转换
```
低  ------------------------------------>  高
byte,short,char—> int —> long—> float —> double 
从位数低到位数高 -> 自动类型转换
反之 需要强制类型转换
```

# 数据结构
set 唯一，无序 通过hasCode() -> equals()判断

# 关键字
* final
* static

# tip
* 从java7开始,可以在swith条件判断语句中使用String对象
* 静态内部类不能访问外部类的非静态的变量和方法，非静态内部类依赖于外部类的实例
```java
// 静态方法不能访问外部类的非静态类
// innerClass非静态内部类
OuterClass outerClass = new OutClass();
InnerClass innerClass = outerClass.new InnerClass();
```

# 泛型(Generic)
java泛型是类型擦除的
泛型不能使用基本类型
Integer是int的包装类
    
1. 泛型的class对象是相同的
2. 泛型```数组```初始化时不能声明泛型类型
3. instanceof不允许存在泛型参数 


## 初始化顺序 
静态变量和静态语句块优先于实例语句和普通语句块，静态变量和静态语句块的初始化顺序取决于它们在代码中的顺序。

静态 -> 实例,普通语句块 -> 构造函数

存在继承的情况下，初始化顺序为：

* 父类（静态变量、静态语句块）
* 子类（静态变量、静态语句块）
* 父类（实例变量、普通语句块）
* 父类（构造函数）
* 子类（实例变量、普通语句块）
* 子类（构造函数）

## 浅拷贝与深拷贝
 clone()方法是Object的protected方法,需要重写并继承Cloneable接口
* 浅拷贝shallowClone 拷贝对象和原始对象的引用类型引用同一个对象
* 深拷贝DeepClone 
* 拷贝对象和原始对象的引用类型引用不同对象 即通过值传递

浅拷贝就是设计模式中原型模式的一种体现。<br>
原型模式是用于创建重复的对象,同时又能保证性能,属于创建型模式

# java8
参考:<a href="http://www.cnblogs.com/invoker-/articles/7684932.html">java8</a>
# lambda
Runnable r = () -> syso
# 流
## 内部迭代与外部迭代
java5的增强for循环，本质上是属于iterator迭代器的语法糖，这种使用迭代器的迭代集合的方式，称之为外部迭代，说的通俗一点，就是需要我们程序猿手动的对这个集合进行种种操作才能得到想要结果的迭代方式，叫做外部迭代。<br>
   与外部迭代所对应的，则是内部迭代，内部迭代与之相反，是集合本身内部通过流进行了处理之后，程序猿们只需要直接取结果就行了，这种迭代称为内部迭代。
```java
List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6);
list.stream().filter(n -> n%2==0).forEach(System.out::println);
```
## 常用流的api
* 对于集合来说,直接通过stream()方法即可获取流对象
```java
List<Person> list = new ArrayList<Person>(); 
Stream<Person> stream = list.stream();
```
* 对于数组来说,通过Arrays类提供的静态函数stream()获取数组的流对象
```
String[] names = {"chaimm","peter","john"};
Stream<String> stream = Arrays.stream(names);
```
* 直接将几个普通的数值变成流对象
```
Stream<String> stream = Stream.of("chaimm","peter","john");
```

## collect(toList())
  collect（Collectors.toList()）方法是将stream里的值生成一个列表，也就是将流再转化成为集合，是一个及早求值的操作。
###  关于惰性求值与及早求值
这两者最重要的区别就在于看操作有没有具体的返回值(或者说是否产生了具体的数值)，比如上文的的统计来自英国艺术家人数的代码，第二行代码的操作是首先筛选出来自英国的艺术家，这个操作并没有实际的数值产生，因此这个操作就是惰性求值，而最后的count计数方法，产生了实际的数值，因此是及早求值。惰性求值是用于描述stream流的，因此返回值是stream，而几乎所有对于流的链式操作都是进行各种惰性求值的链式操作，最后加上一个及早求值的方法返回想要的结果。
  你可以用建造者的设计模式去理解他，建造者模式通过一系列的操作进行设置与配置操作，最后调用一个build方法，创建出相应的对象。对于这里也是同样，调用各种惰性求值的方法，返回一个stream流，最后一步调用一个及早求值的方法，得到最终的结果。
那么现在对于这个collect(toList())，使用方法就十分明了了。

    list.stream()//将集合转化成流
        .???()//一系列惰性求值的操作,返回值为stream
        .collect(toList())//及早求值，这个及早求值的方法返回值为集合,再将流转化为集合

## 筛选filter
filter函数接收一个Lambda表达式作为参数，该表达式返回boolean，在执行过程中，流将元素逐一输送给filter，并筛选出执行结果为true的元素。

## 去重distinc
.distinc()
## 截取limit
截取流的前n个元素 .limit(N)
## 跳过skip
跳过流的前n个元素 .skip(N)
## 映射map
List<String> artistNames = allArtists.stream()
        .filter(artist -> artist.isFrom("London"))
        .map(artist -> artist.getArtistName())
        .collect(Collectors.toList());
## flatMap
将一条一条的小流，汇聚成一条大流，好比海纳百川的感觉。
## max min 
stream自带方法
## 归约reduce
```
int count = Stream.of(1,2,3)
        .reduce(0,(acc,element) -> acc + element);
```
reduce的第一个参数表示初始值为0；
reduce的第二个参数为需要进行的归约操作，它接收一个拥有两个参数的Lambda表达式，以上代码acc参数代表当前的数值总和,element代表下一个元素，reduce会把流中的元素两两输给Lambda表达式，最后将计算出累加之和。
也就是说每次acc+element的返回值都会赋给acc
## 双冒号
Integer::sum 像c++的命名空间
一般格式为类名(或者是类的实例对象) :: 方法名（注意这里只是方法名，没有括号）
System.out::println
## optional对象
Optional是Java8新加入的一个容器，这个容器只存1个或0个元素，它用于防止出现NullpointException，它提供如下方法：

* isPresent() <br>
判断容器中是否有值。
* ifPresent(Consume lambda)<br>
容器若不为空则执行括号中的Lambda表达式。
* T get()<br>
获取容器中的元素，若容器为空则抛出NoSuchElement异常。
* T orElse(T other)<br>
获取容器中的元素，若容器为空则返回括号中的默认值。



