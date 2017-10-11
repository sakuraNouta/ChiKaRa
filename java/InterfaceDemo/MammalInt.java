package InterfaceDemo;
/*
 *接口的实现 
 *一个类只能继承一个类(单继承)
 *但可以实现多个接口
 */
public class MammalInt implements Animal {
	
	//泛型简写print
	public static < E > void print(E x) {
		System.out.println(x);
	}
	
	public void eat() {
		//接口的变量可以直接传递到实现类当中
		print("i am " + name + " eat!");
	}
	
	public void travel() {
		print("travels");
	}
	
	/*驱动函数*/
	public static void main(String[] args) {
		MammalInt m = new MammalInt();
		m.eat();
		m.travel();
	}
	
}
