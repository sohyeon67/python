package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;

public class MySwing04 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl1 = new JLabel("__");
		lbl1.setBounds(45, 35, 39, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("__");
		lbl2.setBounds(96, 35, 39, 15);
		contentPane.add(lbl2);
		
		JLabel lbl3 = new JLabel("__");
		lbl3.setBounds(147, 35, 39, 15);
		contentPane.add(lbl3);
		
		JLabel lbl4 = new JLabel("__");
		lbl4.setBounds(198, 35, 39, 15);
		contentPane.add(lbl4);
		
		JLabel lbl5 = new JLabel("__");
		lbl5.setBounds(249, 35, 39, 15);
		contentPane.add(lbl5);
		
		JLabel lbl6 = new JLabel("__");
		lbl6.setBounds(300, 35, 39, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int[] arr = myclick();
				lbl1.setText(arr[0]+"");
				lbl2.setText(arr[1]+"");
				lbl3.setText(arr[2]+"");
				lbl4.setText(arr[3]+"");
				lbl5.setText(arr[4]+"");
				lbl6.setText(arr[5]+"");
			}
		});
		btn.setBounds(45, 94, 271, 23);
		contentPane.add(btn);
	}
	
	int[] myclick() {
		int[] arr = {
			1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
			41,42,43,44,45
		};
		
		for(int j=0; j<1000; j++) {
			int rnd = (int)(Math.random() * 45);
			int temp = arr[0];
			arr[0] = rnd;
			arr[rnd] = temp;
		}
		
		return arr;
	}

}
