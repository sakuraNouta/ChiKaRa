# 数据库字段名和pojo名不一致不能自动映射

1. sql语句设置别名
2. 指定映射关系
```
注解方式
@Results({
    @Result(property = "orderTime", column = "order_time"),
    @Result(property = "refundTime", column = "refund_time"),
    @Result(property = "id", column = "id"),
    @Result(property = "orderItems", javaType = List.class, column = "id", many = @Many(select =
            "com.ffcs.mapper.OrderItemMapper.listByOrder"))
})
```
3. 如果是命名风格不同,数据库下划线风格,java驼峰
可以设置mapUnderscoreToCamelCase
```
springboot application.properties中
mybatis.configuration.mapUnderscoreToCamelCase=true
```

## @ReuqestBody
>@requestBody注解常用来处理content-type不是默认的application/x-www-form-urlcoded编码的内容，比如说：application/json或者是application/xml等。一般情况下来说常用其来处理application/json类型。

## 获取自增长id
```
Mapper:
@Insert("insert into order_(uid,order_time) values(#{uid},now())")
@Options(useGeneratedKeys=true)
void saveOrder(Order order);
Controller:
order.getId();
```

todo.拦截器