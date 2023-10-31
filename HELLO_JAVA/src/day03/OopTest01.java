package day03;

public class OopTest01 {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("full:" + hum.full);
		System.out.println("flag_tool:" + hum.flag_tool);
		hum.eat(9);
		hum.momstouch();
		System.out.println("full:" + hum.full);
		System.out.println("flag_tool:" + hum.flag_tool);

	}
}