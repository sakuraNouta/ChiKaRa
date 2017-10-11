package SwingDemo;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class SwingLoginExample {
	public static void main(String[] args) {
		//创建JFrame实例
		JFrame frame = new JFrame("Login Example");
		//Setting the width and height of frame
		frame.setSize(350,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		/*
		 * 创建面板,这个类似与HTML的div标签
		 * 我们可以创建多个面板并在JFrame中指定位置
		 * 面板中我们可以添加文本字段,按钮及其他组件
		 */
		
		JPanel panel =new JPanel();
		//添加面板
		frame.add(panel);
		//调用用户定义的方法并添加组件到面板
		placeComponents(panel);
		
		//设置界面可见
		frame.setVisible(true);
	}
	
	/** 
	 * 添加组件到面板
	 */
	private static void placeComponents(JPanel panel) {
		
		//设置布局为null
		panel.setLayout(null);
		
		//创建userLabel(用户标签)
		JLabel userLabel = new JLabel("User:");

		/*这个方法定义了组件的位置。
		 *setBound(x,y,width,height)
		 *x 和 y 指定左上角的新位置,由width和height指定新的大小。 
		 * */
		userLabel.setBounds(10,20,80,25);
		panel.add(userLabel);
		
		/*创建文本域用于用户输入*/
		JTextField userText = new JTextField(20);//20列
		userText.setBounds(100,20,165,25);
		panel.add(userText);
		
		//创建passwordLabel(密码标签)
		JLabel passwordLabel = new JLabel("Password:");
		passwordLabel.setBounds(10,50,80,25);
		panel.add(passwordLabel);
		
		//输入密码的文本域
		JPasswordField passwordText = new JPasswordField(20);
		passwordText.setBounds(100,50,165,25);
		panel.add(passwordText);
		
		//创建登陆按钮
		JButton loginButton = new JButton("login");
		loginButton.setBounds(127,80,80,25);
		panel.add(loginButton);
	}
}




