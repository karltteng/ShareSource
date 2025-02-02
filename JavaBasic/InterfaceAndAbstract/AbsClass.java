
/**
 * 可引用Interface
 * 可設計constructor
 * 可再加abstract method name
 */
public abstract class AbsClass implements InterfaceClass  {

	//member
	private String Name;
	private int Age;
	
	//constructor
	public AbsClass(String name, String age) {
		setName(name);
		setAge(age);
		
		printName(this.Name);
		showAge(this.Age);
		countYear(this.Age);//此為應用介面中定義的方法原型(交由實作類別定義具體方法)
	}
	
	//getter & setter
	public void setName(String name) {
		this.Name = name;
	}
	public String getName() {
		return this.Name;
	}
	public void setAge(String age) {
		this.Age = Integer.parseInt(age);
	}
	public String getAge() {
		return String.valueOf(this.Age);
	}
	
	//abstract method
	public abstract void printName(String name);
	public abstract void showAge(int age);
	
	
}
