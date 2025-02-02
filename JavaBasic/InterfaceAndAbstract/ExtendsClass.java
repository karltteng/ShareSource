import java.util.Date;

/**
 * 綜合所有程序的program實體
 */
public class ExtendsClass extends AbsClass {

	public ExtendsClass(String name, String age) {
		super(name, age);
	}

	public void printName(String name) {
		System.out.println("your name is " + name);
	}
	public void showAge(int age) {
		System.out.println("your age now is " + age);
	}
	public void countYear(int age) {
		Date d = new Date();
		System.out.println("you are born at " + ((d.getYear()+1900)-age));
	}
}
