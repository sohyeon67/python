package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl_first, lbl_last;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 280, 459);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl_first = new JLabel("첫별수:");
		lbl_first.setBounds(43, 37, 57, 15);
		contentPane.add(lbl_first);
		
		lbl_last = new JLabel("끝별수:");
		lbl_last.setBounds(43, 81, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(141, 34, 79, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(141, 78, 79, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(43, 125, 177, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(43, 168, 177, 230);
		contentPane.add(ta);
	}
	
	void myclick() {
		String sfist = tf_first.getText();
		String slast = tf_last.getText();
		
		int first = Integer.parseInt(sfist);
		int last = Integer.parseInt(slast);
		
		String result = "";
		
		for(int i=first; i<=last; i++) {
			result += getStar(i) + "\n";
		}
		ta.setText(result);
	}
	
	String getStar(int cnt) {
		String txt = "";
		for(int i=0; i<cnt; i++) {
			txt += "★";
		}
		return txt;
	}
}
