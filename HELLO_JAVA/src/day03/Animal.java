package day03;

public class Animal {
	int full = 1;

	void eat(int amount) {
		full += amount;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println("ani.full:" + ani.full);
		ani.eat(9);
		System.out.println("ani.full:" + ani.full);
	}
}
