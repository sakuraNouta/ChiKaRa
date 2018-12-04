# oracle
消除重复行 distinct 
条件限定 between and 闭区间
模糊查询 like 

%表示任意匹配，有或者没有都可以

_表示有，并且只有一个

left join 表关联 on 指定关联字段

count() max() min() avg()

# 分组查询
分组的时候，查询字段，只能是统计函数，或者被分组的字段，多表连接查询可以在group by后面加多个被分组字段 
比如
 
```
select avg(salary),e.department_id  from hr.employees e group by e.department_id
```

查询字段就只能是统计函数，或者department_id,但是不能是first_name
比如
```
select avg(salary),e.first_name  from hr.employees e group by e.department_id
```
这个就会报错
因为从逻辑上来讲，按照department_id来分组员工，分在一起的员工，他们的department_id都是一样的，但是他们的first_name是不一样的，所以不能够查询first_name字段

having对分组函数进行条件判断

建表
字段类型
```
create table hero(
  id number,
  name varchar2(30),
  hp number,
  mp number,
  damage number,
  armor number,
  speed number
)
```
```
varchar和varchar2的区别
两种都是变长的，对于汉字(unicode)的处理有区别
varchar如果放的是英文和数字，就用一个字节存放，如果是汉字(unicode)，就用两个字节
varchar2 统一使用两个字节
一般都直接使用varchar2，使用varchar很少了
```
序列
```
create sequence user_seq
  increment by 1
  start with 1
  maxvalue 9999999
insert into user_ values(user_seq.nextval,11,'张三',0,22,2)
```

约束
```
建表时 constraint pk_user_key unique(key)
修改表 alter table user_ add constraint pk_hero_id primary key(code)
```

分页查询
```
select a1.* from (select user_.*,rownum rn from user_) a1 where rn between ? and ?
```

### 存储过程
1、定义
所谓存储过程(Stored Procedure)，就是一组用于完成特定数据库功能的SQL语句集，该SQL语句集经过
编译后存储在数据库系统中。在使用时候，用户通过指定已经定义的存储过程名字并给出相应的存储过程参数
来调用并执行它，从而完成一个或一系列的数据库操作。

2、存储过程的创建
Oracle存储过程包含三部分：过程声明，执行过程部分，存储过程异常。
例子：

#### 过程声明
在绑定表的时候使用
```
create or replace procedure SP_Update_Title
(
 flowId in int,
 applyFormTitle in varchar
)
as
begin
     update CUST_SC_ITSM_TEL_APPLY2 set apply_form_title = applyFormTitle where flow_id = flowId;
     commit;
  
end SP_Update_Title;
/
```
#### 调用
```
declare 
        n NUMBER;
        S varchar(11);
begin
        n := 590000002062;
        s := 'a0';
        SP_UPDATE_TITLE(flowId => n,applyFormTitle => s);
end;
```

## oracle函数
#### 声明
```sql
create or replace function func(name varchar2)
return varchar2 
is
    temp varchar2(10);
begin
    select to_char(sysdate,'YYYYMMDD') into temp from dual;
    temp := concat(temp, name);
    return temp;
end func;
```
#### 调用
``` 
SQL> set serverout on -- 可显示 
```

* PLSQL代码块
```sql
declare
    str varchar2(10);
begin
    str := func('12');
    dbms_output.put_line(str);
end;
/
```
* execute
```sql
SQL> var str varchar2;
SQL> execute :str :=func('110');
```
* call
```sql
SQL> var str varchar2
SQL> call func('10') into :str;
```
* select
```sql
select func('10') from dual;
```
* 将函数作为另一个子程序的参数
```sql
SQL> execute dbms_output.put_line(func('12'));
```

## ORA-01410无效的 ROWID及多表修改
```
用两表联合查询，然后for update；结果肯定是生成新的虚拟表、虚拟rowid，所以无法更改。
解决办法：只查一个表，用查询条件找到对应字段的值，然后进行更改。

-- 修改form_element, form_element_bind, data_table_fields表中字段
select *
from data_table_fields
where table_name = 'CUST_SC_TEL_APPLY_URBO' 
and field_name = 'DISCOUNT_LEVEL' for update

select *
from form_element_bind
where table_field_id = (
  select TABLE_FIELD_ID
  from data_table_fields
  where table_name = 'CUST_SC_TEL_APPLY_URBO' 
  and field_name = 'DISCOUNT_LEVEL') for update
  
select * 
from form_element
where form_element_id = (
  select form_element_id
  from form_element_bind
  where table_field_id = (
    select TABLE_FIELD_ID
    from data_table_fields
    where table_name = 'CUST_SC_TEL_APPLY_URBO' 
    and field_name = 'DISCOUNT_LEVEL')) for update
```



### 修改oracle最大连接数
```
在sqlplus下登陆sysdba
username:sys password:(password) as sysdba
当前的连接数
select count(*) from v$process;
设置的最大连接数（默认值为150）
select value from v$parameter where name = 'processes';
修改最大连接数
alter system set processes = 300 scope = spfile;
重启数据库后生效
shutdown immediate；
startup
```

### 修改Oracle端口
```
Error running Tomcat 7.0.64:
Address localhost:8080 is already in use
```

* 第一步，命令提示符号，执行命令：netstat -ano
>找到占用8080端口的是PID是4296
* 第二步，命令提示符号，执行命令：tasklist(通过pid 4296定位)
>找到进程是TNSLSNR.EXE
* 搜索发现它是Oracle 10g的一个服务
>Oracle 10g服务一启动 TNSLSNR.exe 会占用8080端口，导致tomcat无法正常启动，这时，需要改一下端口

```
sqlplus sys as sysdba / sys as dba
-- 把HTTP/WEBDAV端口从8080改到8081 
SQL> call dbms_xdb.cfg_update(updateXML(dbms_xdb.cfg_get(), 
'/xdbconfig/sysconfig/protocolconfig/httpconfig/http-port/text()',8081)) 
/ 
-- 把FTP端口从2100改到2111 
SQL> call dbms_xdb.cfg_update(updateXML(dbms_xdb.cfg_get(), 
'/xdbconfig/sysconfig/protocolconfig/ftpconfig/ftp-port/text()',2111)) 
/ 
SQL> commit; 
SQL> exec dbms_xdb.cfg_refresh; 
-- 检查修改是否已经成功 
SQL> select dbms_xdb.cfg_get from dual;
也可以访问localhost:8081 可以显示Oracle页面
```
上面的不行试试
```
exec dbms_xdb.sethttpport(8081)
```

### 连接远程数据库
```
oracle\product\10.2.0\server\NETWORK\ADMIN\tnsnames.ora
追加数据库环境连接.txt中内容
注意SID前不能加空格
```