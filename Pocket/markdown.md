# Markdown的使用
在Sublime Text中使用Markdown编辑并实时预览

md格式可以上传到github

用浏览器预览时可以直接复制文本
## 一、安装插件
Ctrl + `,调出控制台
安装软件包管理器
```
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```
Shift + Ctrl+ P  打开快捷菜单 pcip 安装以下插件

参考:```http://www.jianshu.com/p/aa30cc25c91b```
### 1.Markdown Editing
支持Markdown语法高亮；支持Github Favored Markdown语法；
### 2.OmniMarkupPreviwer
实时在浏览器中预览,快捷键如下：

```Ctrl+Alt+O```: Preview Markup in Browser.

```Ctrl+Alt+X```: Export Markup as HTML.

```Ctrl+Alt+C```: Copy Markup as HTML.

### 3.MarkdownPreview
```Ctrl + Shift + P```+```mp```打开浏览器进行预览<br>
可以选择github语法查看

## 二、关于语法
### 1.标题
    #表示标题,一二级自带横线
Markdown在github上语法要求更严格

标题要求```# + (空格)```

eg:
# 一级标题  
## 二级标题
### 三级标题
    # 一级标题  
    ## 二级标题
    ### 三级标题
### 2.强调和文字块
前空4格或一个Tab键表示文字块

    ```(文字)```强调
```(文字)```
### 3.

