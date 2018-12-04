# mysql四种引擎
## 1. MyISAM存储引擎
不支持事务，不支持外键，访问速度快

## 2. InnoDB存储引擎
事务安全，对比MyISAM写的处理效率会差一些，占用更多空间保留数据和索引<br>
特点:支持自动增长列，支持外键约束

## 3. MEMORY存储引擎
.frm 快<br>
可以使用BTREE索引或者HASH索引
HASH索引效率高 不支持范围查找

## 4. MERGE存储引擎
Merge存储引擎是一组MyISAM表的组合