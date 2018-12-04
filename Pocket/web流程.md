
1. HTTP无状态协议，是指协议对于事务处理没有记忆能力

# cookie
cookie.setPath("/")
>path表示cookie所在的目录。<br>
 ”/”表示根目录，所有页面都能访问根目录下面的cookie。<br>
 如果cookie的path为test，那么只test目录下或者是test下的子目录的页面和代码才获取到这个cookie。<br> 
 当cookie的path为null的时候，会自动设置path的值。

# SpringMVC
构造型stereotype <br>
@Controller 返回的String值被SpringMVC解读为要渲染的视图名称<br>

@RequestParam vs @PathVariable
* 通过@PathVariable，例如/blogs/1 @PathParam类似
* 通过@RequestParam，例如blogs?blogId=1 可设defaultValue
>@RequestParam实质是将Request.getParameter() 中的Key-Value参数Map利用Spring的转化机制ConversionService配置，转化成参数接收对象或字段。
@RequestBody post方法->json字符串 绑定对象


RPC Remote Procedure Call 远程过程调用

 各位领导、同事大家好：

    本周我主要学习了以下部分内容：

    1.完成培训
    2.学习单元测试
    3.为Ext.js页面增加功能
