# Spring
Spring是一个基于IOC(inversion of control)和AOP(aspect oriented program)的结构J2EE系统的框架

IOC 创建对象由以前的程序员自己new 构造方法来调用，变成了交由Spring创建对象 

DI 依赖注入 Dependency Inject. 
简单地说就是拿到的对象的属性，已经被注入好相关值了，直接使用即可。 

注入对象有两种方式 1.ref 2.注解

* 注解
在成员变量或setter方法声明时使用@Autowired注解

* aop<br>
核心业务pointcut<br>
辅助功能aspect<br>
通过aop:config把业务对象与辅助功能编织在一起

* 注解发生aop<br>
@Aspect 注解表示这是一个切面<br>
@Component 表示这是一个bean,由Spring进行管理<br>
@Around 对类中的方法进行切面操作