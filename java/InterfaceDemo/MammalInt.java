package InterfaceDemo;
/*
 *�ӿڵ�ʵ�� 
 *һ����ֻ�ܼ̳�һ����(���̳�)
 *������ʵ�ֶ���ӿ�
 */
public class MammalInt implements Animal {
	
	//���ͼ�дprint
	public static < E > void print(E x) {
		System.out.println(x);
	}
	
	public void eat() {
		//�ӿڵı�������ֱ�Ӵ��ݵ�ʵ���൱��
		print("i am " + name + " eat!");
	}
	
	public void travel() {
		print("travels");
	}
	
	/*��������*/
	public static void main(String[] args) {
		MammalInt m = new MammalInt();
		m.eat();
		m.travel();
	}
	
}
