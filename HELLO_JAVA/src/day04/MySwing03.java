package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(26, 24, 59, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(117, 24, 59, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(247, 24, 59, 21);
		contentPane.add(tf3);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(97, 27, 16, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add();
			}
		});
		
		btn.setBounds(188, 23, 50, 23);
		contentPane.add(btn);
	}

	void add() {
		int num1 = Integer.parseInt(tf1.getText());
		int num2 = Integer.parseInt(tf2.getText());
		int sum = num1 + num2;
		
		tf3.setText(sum+"");
	}
}
