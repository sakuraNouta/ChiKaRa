# 小知识
1. HTC(HTML Component) 
>HTC(HTML Component)直译为HTML组件,实际上只是IE浏览器内置的一种脚本封装机制。
2. ```&nbsp;``` 空格占位符
3. ```<fieldset>```标签 功能：组合表单中相关元素
4. table属性
>单元格边距(表格填充)(cellpadding) -- 代表单元格外面的一个距离,用于隔开单元格与单元格空间。<br>
>单元格间距(表格间距)(cellspacing) -- 代表表格边框与单元格补白的距离,也是单元格补白之间的距离。

# html
### html区块元素
* 块级元素 ```<h1> <p> <ul> <table>```
* 内联元素 ```<b> <td> <a> <img>```

### display:inline/block/inline-block
* display:inline的特点

1、inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。<br>
2、inline元素设置width,height属性无效<br>
3、inline元素的margin和padding属性，水平方向的padding-left, padding-right, margin-left, margin-right都产生边距效果；但竖直方向的padding-top, padding-bottom, margin-top, margin-bottom不会产生边距效果。<br>

* display:block的特点

1、block元素会独占一行，多个block元素会各自新起一行。默认情况下，block元素宽度自动填满父元素宽度。<br>
2、block元素可以设置width,height属性。块级元素即使设置了宽度,仍然是独占一行。<br>
3、block元素可以设置margin和padding属性。<br>

* display:inline-block的特点

让多个元素在同一行显示，而且能够固定宽度

### 隐藏元素
```
display: none 不显示
visibility: hidden 隐藏可见性
```

### 清除浮动
```
clear:right/left/both 指定元素左右不允许有浮动元素(float)
```

# js、jq
### 数字处理
```
数组加数据 array.push()
丢弃小数 parseInt()
Math.random() 返回0-1
toFixed(num) 是一种四舍六入五取偶（又称四舍六入五留双）法 -num 保留位数
Math.round() 方法可把一个数字舍入为最接近的整数 
对于X进行保留两位小数的处理，可以使用Math.round(X * 100) / 100.进行处理。
```
#### js array方法
```
push pop 添加/删除末尾元素
shift unshift 删除/添加第一个元素
splice 从某个已有的数组返回选定的元素 
删除index位置一个元素
splice(index,1)
```
### 插入元素
```
append() 被选元素的结尾插入内容
prepend() 被选元素开头插入内容
after() 被选元素后
before() 被选元素前
remove 删除被选元素及其子元素。
empty() 方法删除被选元素的子元素。
jQuery remove() 方法也可接受一个参数，允许您对被删元素进行过滤。
该参数可以是任何 jQuery 选择器的语法。
```
### jquery动态添加元素无法触发绑定的事件的解决方案。
```
利用on（）事件绑定 ($(ParentEle).on("click",".thisEle",function(){})
parentEle - 是thisEle的父辈或祖父元素，要一直在页面上的
thisEle - 需要绑定事件的元素
/*动态增加元素绑定事件*/
$("table").on("click", ".tr", function(){
    if($(this).attr("class").search("active") == -1)
        $(this).addClass("active");
    else $(this).removeClass("active");
});
```
### js对新增的元素绑定事件解决方案
```
对新增的元素绑定事件可能会失效
可以通过页面上已存在的父元素->子元素的方式绑定
```
### jQuery下ajax的XML解析
在jQuery下ajax的XML解析十分简单，
ajax获得的返回值直接解析即可(servlet发送type为xml)
```
$.ajax({
    url : url,
    type : "post",
    dataType : "xml",
    data : {"data" : xml},
    success : function(result){
        /* js对xml进行解析 */
        //alert(result);
        var code = result.getElementsByTagName("code")[0].childNodes[0].nodeValue;
        if(code == '0')
            alert("执行成功");
        else
            alert("执行失败")
    },
    error : function(XMLHttpRequest, textStatus, errorThrown){
        alert(XMLHttpRequest.status); 
　　                  alert(XMLHttpRequest.readyState); 
　　                  alert(textStatus);        
    }
});
```

### jquery ajax 和fetch方式传送json数据的不同
jquery ajax默认以application/x-www-form-urlencoded方式提交，也就是常见的表单提交方式。
```
data : {"data" : JSON.stringify(json)},
不指明contentType
```
接收以```request.getParameter("data")```
也可以
```
data : JSON.stringify({username: 'username', pwd: 'pwd'}), //这个是json字符串
contentType: 'application/json',  //规定传的值是json
```
而fetch以x-www-form-urlencoded方式提交需要拼接字符串
指明contentType: 'application/json'的话
```
body:JSON.stringify(data)
```
接收以
```
BufferedReader reader = request.getReader();
            data = reader.readLine();
```
## js,jq遍历子孙元素
```
jq .children() .find()
children() 子元素
find("*") 按条件搜索全部子孙元素
```
