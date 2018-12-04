Vue v-for 传object就行

### vue数组内新push的对象被修改，其他的对象属性同时被修改
```
eg:
user: {'code': '','name': '', 'age': '', 'sex': '男', 'position': '职员'},
users : data,

//之前增加的user数据会和新增加的user一起改变
this.users.push(this.user);
```
原因：
>原因是对象是引用类型，传递的是引用地址，所以你两个数组引用的是同一个对象，只要其中一个数组改变，就会导致对象改变，进而另一个引用的数组也会改。<br>
解决办法就是将需要放入数组的对象先深拷贝一份，用拷贝的对象，这样就不存在引用关系了。<br>
Object.assign({},需要push的对象)可以，用lodash中的assign也行，只要是深拷贝就行。

即```this.users.push(Object.assign({},this.user));```

* v-bind与data绑定
# 单向数据流
```
prop如果是对象或数组绑定将会直接绑定引用(地址)
而与基本数据类型绑定则是只绑定值
```
# 组件间传递
不建议直接修改对象属性值
可以通过.sync在父组件与子组件绑定模型时绑定@update方法
而子组件在监听事件watch中调用$emit去传递 
```javascript

父组件:
<my-component v-bind:num.sync="product.num"></my-component>
相当于
<my-component v-bind:num="product.num" @update:num="val => product.num=val">
</my-component>
子组件:
watch: {
    num(val){
        this.$emit("update:num",val);
    }
}
```
# js数据类型
```
字符串（String）、数字(Number)、布尔(Boolean)、数组(Array)、对象(Object)、空（Null）、未定义（Undefined）。
```
