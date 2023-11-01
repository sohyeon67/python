package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 260);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나");
		lblMine.setBounds(49, 36, 37, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴");
		lblCom.setBounds(49, 79, 37, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과");
		lblResult.setBounds(49, 124, 37, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(124, 33, 74, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(124, 76, 74, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(124, 121, 74, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(49, 156, 149, 23);
		contentPane.add(btn);
	}
	
	void myclick() {
		String mine = tfMine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		
		if(rnd > 0.66) {
			com = "가위";
		} else if(rnd > 0.33) {
			com = "바위";
		} else {
			com = "보";
		}
		
		if(com.equals("가위")&&mine.equals("가위")) { result="비김"; }
		if(com.equals("가위")&&mine.equals("바위")) { result="이김"; }
		if(com.equals("가위")&&mine.equals("보")) { result="짐"; }
		
		if(com.equals("바위")&&mine.equals("가위")) { result="짐"; }
		if(com.equals("바위")&&mine.equals("바위")) { result="비김"; }
		if(com.equals("바위")&&mine.equals("보")) { result="이김"; }
		
		if(com.equals("보")&&mine.equals("가위")) { result="이김"; }
		if(com.equals("보")&&mine.equals("바위")) { result="짐"; }
		if(com.equals("보")&&mine.equals("보")) { result="비김"; }
		
		tfCom.setText(com);
		tfResult.setText(result);
	}
}
