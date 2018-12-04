### 安装weblogic
打开startWebLogic
登陆http://localhost:7001/console
配置数据源 
第一页 不能随意 BSN_DATA_SOURCE
数据库驱动选第4个
```*Oracle's  Driver (Thin) for Instance connections; Versions:9.0.1,9.2.0,10,11
```
第二页默认
第三页 
devdb
192.168.17.200 port:1521
bosswg_sx

```
控制台修改密码完要把boot.properties里username和password修改成明文的新的密码
```

```
部署新项目问题
ide中lib不要引用到Applet文件夹下去,有旧版本的jar包,会冲突

BeanDefinitionStoreException Invalid bean definition with name AMQPConnectionFactory
把数据源配置对了就行

The Network Adapter could not establish the connection
开发的库连不上

```


```
心得
1.jdk版本
2.lib问题，基本上只需要webconten/lib下的库，不要多引入其他的

没试过的方法
1.编译排除
2.Run/Debug Configurations下build -> build,no error check
```

```
数据源配置
jdni是通过名字来的，大概