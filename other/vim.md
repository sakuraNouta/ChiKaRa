# vim的使用
## first
vi 文件名(新建一个文件)
## 模式
1) 命令行模式command mode）

控制屏幕光标的移动，字符、字或行的删除，移动复制某区段及进入Insert mode下，或者到 last line mode。

2) 插入模式（Insert mode）

只有在Insert mode下，才可以做文字输入，按「ESC」键可回到命令行模式。

3) 底行模式（last line mode）

将文件保存或退出vi，也可以设置编辑环境，如寻找字符串、列出行号……等。

不过一般我们在使用时把vi简化成两个模式，就是将底行模式（last line mode）也算入命令行模式command mode）。
## 操作(简化)
刚进入时是 命令行模式 ,按 i键 进入 插入模式 ，按 Esc键 退回命令行
命令行模式下按下 ：(冒号) 进入 Last line mode,例如:

: w filename （输入 「w filename」将文章以指定的文件名filename保存）

: wq (输入「wq」，存盘并退出vi)

: q! (输入q!， 不存盘强制退出vi)