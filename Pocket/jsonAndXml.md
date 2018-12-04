# json
JSON : JavaScript Object Notation

```java
java对json的解析 [{"name":"jack"},{"name":"rin"}]
//将json转化为jsonArray
JSONArray jsonArray = JSONArray.fromObject(data);
        for(Object json : jsonArray) {
            System.out.println(json);
            //将json中的object转化为jsonObject
            JSONObject jsonObject = JSONObject.fromObject(json);
            //将jsonObject转化成javaBean
            User user = (User)JSONObject.toBean(jsonObject,User.class);
            System.out.println(user);
            users.add(user);
        }
//js发送
user = { "method":"delete","key":key};
json.push(user);
```
```java
java对json的封装
private JSONObject User2Json(List<User> users,int total) {
        
        //json数组 [{"name":"jack"},{"name":"lin"}]
        JSONArray array = new JSONArray();
        JSONObject json = new JSONObject();
        JSONObject temp = new JSONObject();

        for(User user : users) {
            temp.put("user", JSONObject.fromObject(user));
            array.add(temp);
        }
        json.put("users", array);
        json.put("total", total);
        return json;
    }
对应js解析
//解析返回ajax结果
var json = JSON.parse(result);
    total = json.total; 
    var users = json.users;
    
    //json没有length属性,使用for...in遍历
    for(var i in users){
        var code = users[i].user.code;
        var name = users[i].user.name;
        var sexNum = users[i].user.sex;
        var age = users[i].user.age;
        var positionNum = users[i].user.position;
        var key = users[i].user.key;
    }
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

