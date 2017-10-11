package SwingDemo;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class SwingLoginExample {
	public static void main(String[] args) {
		//����JFrameʵ��
		JFrame frame = new JFrame("Login Example");
		//Setting the width and height of frame
		frame.setSize(350,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		/*
		 * �������,���������HTML��div��ǩ
		 * ���ǿ��Դ��������岢��JFrame��ָ��λ��
		 * ��������ǿ�������ı��ֶ�,��ť���������
		 */
		
		JPanel panel =new JPanel();
		//������
		frame.add(panel);
		//�����û�����ķ����������������
		placeComponents(panel);
		
		//���ý���ɼ�
		frame.setVisible(true);
	}
	
	/** 
	 * �����������
	 */
	private static void placeComponents(JPanel panel) {
		
		//���ò���Ϊnull
		panel.setLayout(null);
		
		//����userLabel(�û���ǩ)
		JLabel userLabel = new JLabel("User:");

		/*������������������λ�á�
		 *setBound(x,y,width,height)
		 *x �� y ָ�����Ͻǵ���λ��,��width��heightָ���µĴ�С�� 
		 * */
		userLabel.setBounds(10,20,80,25);
		panel.add(userLabel);
		
		/*�����ı��������û�����*/
		JTextField userText = new JTextField(20);//20��
		userText.setBounds(100,20,165,25);
		panel.add(userText);
		
		//����passwordLabel(�����ǩ)
		JLabel passwordLabel = new JLabel("Password:");
		passwordLabel.setBounds(10,50,80,25);
		panel.add(passwordLabel);
		
		//����������ı���
		JPasswordField passwordText = new JPasswordField(20);
		passwordText.setBounds(100,50,165,25);
		panel.add(passwordText);
		
		//������½��ť
		JButton loginButton = new JButton("login");
		loginButton.setBounds(127,80,80,25);
		panel.add(loginButton);
	}
}




