package InterfaceDemo;
/*
 * 接口
 * 一个接口可以继承另一个接口extends
 * 接口可以多继承
 */
public interface Animal {
	/*变量隐式指定为public static final*/
	String name = "gay gay Animal";
	/*方法隐式指定为public abstract*/
	public void eat();
	public void travel(); 
}
