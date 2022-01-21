### 01构造方法引入
* A:构造方法的引入
	* 在开发中经常需要在创建对象的同时明确对象的属性值，比如员工入职公司就要明确他的姓名、年龄等属性信息。那么，创建对象就要明确属性值，那怎么解决呢？也就是在创建对象的时候就要做的事情，当使用new关键字创建对象时，怎么给对象的属性初始化值呢？这就要学习Java另外一门小技术，构造方法。
* B: 那什么是构造方法呢？
	* 从字面上理解即为构建创造时用的方法，即就是对象创建时要执行的方法。既然是对象创建时要执行的方法，那么只要在new对象时，知道其执行的构造方法是什么，就可以在执行这个方法的时候给对象进行属性赋值。
	
### 02构造方法作用
* A: 构造方法的作用:
		在new的同时给成员变量赋值,给对象属性进行初始化。
* B: 举例:
	* Perons p = new Person("张三",23); 在new 的时候给p对象的name属性和age属性进行赋值,使这个对象的属性有值。
			
### 03构造方法的定义和运行特点
* A: 构造方法定义
	* 构造方法的格式：
		```java
		修饰符 构造方法名(参数列表)
		{
		}
		```

* B: 构造方法的体现：
	* 构造方法没有返回值类型。也不需要写返回值。因为它是为构建对象的，对象创建完，方法就执行结束。
	* 构造方法名称必须和类型保持一致。
	* 构造方法没有具体的返回值。
	* 构造方法的代码体现：
* C: 构造方法举例
	```java
	class Person {
		// Person的成员属性age和name
		private int age;
		private String name;
	
		// Person的构造方法，拥有参数列表
		Person(int a, String nm) {
			// 接受到创建对象时传递进来的值，将值赋给成员属性
			age = a;
			name = nm;
		}
	}
	```
* D: 构造方法运行特点: 在new 对象的时候自动调用执行。


### 04默认添加的构造方法
* A: 每一class类都必须有一个构造方法，构造方法不写也有。编译的时候，javac，系统会自动检查类中是否有构造方法，如果没有编译器就会自动添加一个构造方法。比如Person类， 编译器添加一个无参构造 public Person(){}
		
### 05构造方法的调用赋值
* A: 理解构造方法的格式和基本功能之后，现在就要研究构造方法是怎么执行的呢？在创建对象的时候是如何初始化的呢？
	* 构造方法是专门用来创建对象的，也就是在new对象时要调用构造方法。现在来看看如何调用构造方法。


* B: 案例
	```java
	class Person {
		// Person的成员属性age和name
		private int age;
		private String name;
	
		// Person的构造方法，拥有参数列表
		Person(int a, String nm) {
			// 接受到创建对象时传递进来的值，将值赋给成员属性
			age = a;
			name = nm;
		}
	
		public void speak() {
			System.out.println("name=" + name + ",age=" + age);
		}
	}
	
	class PersonDemo {
		public static void main(String[] args) {
			// 创建Person对象，并明确对象的年龄和姓名
			Person p2 = new Person(23, "张三");
			p2.speak();
		}
	}
	```
	上述代码演示了创建对象时构造方法的调用。即在创建对象时，会调用与参数列表对应的构造方法


### 06构造方法的内存
* A:内存加载的过程
	* 有一个Person类, 创建Person 对象new Person()
	* 1、首先会将main方法压入栈中，执行main方法中的 new Person(23,"张三"); 
	* 2、在堆内存中分配一片区域，用来存放创建的Person对象，这片内存区域会有属于自己的内存地址（0x88）。然后给成员变量进行默认初始化（name=null，age=0）。
	* 3、执行构造方法中的代码（age = a ; name = nm;）,将变量a对应的23赋值给age，将变量nm对应的”张三赋值给name，这段代码执行结束后，成员变量age和name的值已经改变。执行结束之后构造方法弹栈，Person对象创建完成。将Person对象的内存地址0x88赋值给p2。

### 07构造方法的重载			
* A：当在描述事物时，要不要在类中写构造方法呢？这时要根据描述事物的特点来确定，当描述的事物在创建其对象时就要明确属性的值，这时就需要在定义类的时书写带参数的构造方法。
	* 若创建对象时不需要明确具体的数据，这时可以不用书写构造方法（不书写也有默认的构造方法）。
	* 构造方法的细节：
		* 1、一个类中可以有多个构造方法，多个构造方法是以重载的形式存在的
		* 2、构造方法是可以被private修饰的，作用：其他程序无法创建该类的对象。
* B: 举例
	```java
	class Person {
		private int age;
		private String name;
	
		// 私有无参数的构造方法，即外界不能通过new Person();语句创建本类对象
		private Person() {
		}
	
		// 多个构造方法是以重载的形式存在
		Person(int a) {
			age = a;
		}
	
		Person(String nm, int a) {
			name = nm;
			age = a;
		}
	}
	```

### 08构造方法和一般方法区别
* A: 目前为止，学习两种方法，分别为构造方法和一般方法，那么他们之间有什么异同呢？
	* 1.格式不同
		* 构造方法 :
			```java
			修饰符  类名(参数类型 参数 ...){
			初始化成员变量
			}
			```
		* 一般方法: 需要有返回值类型
	* 2.作用不同
		* 构造方法一般用来给成员变量初始化;
		* 一般方法根据需求而定;
	* 3.调用方式不同
		* 构造方法创建对象时调用, 或者this() super() 语句调用
		* 普通方法需要对象调用或者静态方法直接调用静态方法.
	* 4.执行不同
		* 构造方法在对象创建时就执行了，而且只执行一次。
		* 一般方法是在对象创建后，需要使用时才被对象调用，并可以被多次调用。


		
### 09this在构造方法之间的调用
* A: 在之前学习方法之间调用时，可以通过方法名进行调用。可是针对构造方法，无法通过构造方法名来相互调用。
	* 构造方法之间的调用，可以通过this关键字来完成。
	* 构造方法调用格式：
		* this(参数列表);
* B:调用构造方法的案例
	```java
	class Person {
		// Person的成员属性
		private int age;
		private String name;
	
		// 无参数的构造方法
		Person() {
		}
	
		// 给姓名初始化的构造方法
		Person(String nm) {
			name = nm;
		}
	
		// 给姓名和年龄初始化的构造方法
		Person(String nm, int a) {
			// 由于已经存在给姓名进行初始化的构造方法 name = nm;因此只需要调用即可
			// 调用其他构造方法，需要通过this关键字来调用
			this(nm);
			// 给年龄初始化
			age = a;
		}
	}
	```


### 10this在构造方法调用的内存图
* A: 被加载的代码
	```java
	class Person {
		private int age;
		private String name;
		Person() {
		}
		Person(String nm) {
			name = nm;
		}
		Person(String nm, int a) {
			this(nm);
			age = a;
		}
	}
	class PersonDemo {
		public static void main(String[] args) {
			Person p = new Person("张三", 23);
		}
	}
	```

	
	* B: 构造方法调用的原理图
	*   图略
		* 1、先执行main方法，main方法压栈，执行其中的new Person(“张三”,23);
		* 2、堆内存中开辟空间，并为其分配内存地址0x33，，紧接着成员变量默认初始化（name=null  age = 0）；
		* 3、拥有两个参数的构造方法（Person（String nm , int a））压栈，在这个构造方法中有一个隐式的this，因为构造方法是给对象初始化的，那个对象调用到这个构造方法，this就指向堆中的那个对象。
		* 4、由于Person（String nm , int a）构造方法中使用了this(nm);构造方法Person(String nm)就会压栈，并将“张三”传递给nm。在Person（String nm , int a）构造方法中同样也有隐式的this，this的值同样也为0x33，这时会执行其中name = nm，即把“张三”赋值给成员的name。当赋值结束后Person（String nm , int a）构造方法弹栈。
		* 5、程序继续执行构造方法（Person（String nm , int a）中的age = a；这时会将23赋值给成员属性age。赋值结束构造方法（Person（String nm , int a）弹栈。
		* 6、当构造方法（Person（String nm , int a）弹栈结束后，Person对象在内存中创建完成，并将0x33赋值给main方法中的p引用变量。
		* 注意：this到底代表什么呢？this代表的是对象，具体代表哪个对象呢？哪个对象调用了this所在的方法，this就代表哪个对象。调用其他构造方法的语句必须定义在构造方法的第一行，原因是初始化动作要最先执行。


### 11this简易应用
* A: 当在方法中出现了局部变量和成员变量同名的时候，那么在方法中怎么区别局部变量成员变量呢？可以在成员变量名前面加上this.来区别成员变量和局部变量
* B: 举例1
	```java
	class Person {
		private int age;
		private String name;
	
		// 给姓名和年龄初始化的构造方法
		Person(String name, int age) {
			// 当需要访问成员变量是，只需要在成员变量前面加上this.即可
			this.name = name;
			this.age = age;
		}
	
		public void speak() {
			System.out.println("name=" + this.name + ",age=" + this.age);
		}
	}
	
	class PersonDemo {
		public static void main(String[] args) {
			Person p = new Person("张三", 23);
			p.speak();
		}
	}
	```

### 12super关键字_1
	
* A: 子父类中构造方法的调用
	* 在创建子类对象时，父类的构造方法会先执行，因为子类中所有构造方法的第一行有默认的隐式super();语句。
* B: 格式：
	* 调用本类中的构造方法:this(实参列表);
	* 调用父类中的空参数构造方法:super();
	* 调用父类中的有参数构造方法:super(实参列表);

### 13super关键字_2
* A:子类构造方法,有一个默认添加的构造方法
	```java
	public class Student extends Person {
		 public Student(){
		 	super();
		 }
	}
	```
* B :为什么子类对象创建都要访问父类中的构造方法？因为子类继承了父类的内容，所以创建对象时，必须要先看父类是如何对其内容进行初始化的，看如下程序
	```java
	public class Test {
		public static void main(String[] args) {
			new Zi();
		}
		
	}
	class Fu{
		int num ;
		Fu(){
			System.out.println("Fu构造方法"+num);
			num = 4;
		}
	}
	class Zi extends Fu{
		Zi(){
	         //super(); 调用父类空参数构造方法
			System.out.println("Zi构造方法"+num);
		}
	}
	```
	* 执行结果：
		* Fu构造方法0
		* Zi构造方法4
	* 通过结果发现，子类构造方法执行时中，调用了父类构造方法，这说明，子类构造方法中有一句super()。那么，子类中的构造方法为什么会有一句隐式的super()呢？
	* 原因：子类会继承父类中的内容，所以子类在初始化时，必须先到父类中去执行父类的初始化动作。这样，才可以使用父类中的内容。当父类中没有空参数构造方法时，子类的构造方法必须有显示的super语句，指定要访问的父类有参数构造方法。

	 
### 14子类父类的内存图
* 略: 



### 15super关键字_3
* A: 创建子类对象的时候会必须调用父类的构造方法。
	* 子类默认会调用父类的无参构造， 但如果父类没有无参构造，子类的构造方法继续调用父类的无参构造就会报错。因此子类构造方法的第一行需要调用父类的构造方法，既可以调用父类的无参构造，也可以调用父类的有参构造，这样语法上就不会报错。
		


### 16super关键字_4
* A: 构造方法第一行,写this()还是super()
	*  this() 是调用本类的构造方法,super()是调用父类的构造方法, 且两条语句不能同时存在
	*  保证子类的所有构造方法调用到父类的构造方法即可

* B: 小结:
	* 无论如何,子类的所有构造方法,直接或间接必须调用到父类构造方法;
	* 子类的构造方法什么都不写,默认的构造方法第一行super()

		
### 17创建子类对象过程的细节
* A 创建子类对象过程的细节
* 如果子类的构造方法第一行写了this调用了本类其他构造方法，那么super调用父类的语句还有吗？
* 这时是没有的，因为this()或者super(),只能定义在构造方法的第一行，因为初始化动作要先执行。
* 父类构造方法中是否有隐式的super呢？
* 也是有的。记住：只要是构造方法默认第一行都是super();
* 父类的父类是谁呢？super调用的到底是谁的构造方法呢？
* Java体系在设计，定义了一个所有对象的父类Object
* 注意：
	* 类中的构造方法默认第一行都有隐式的super()语句，在访问父类中的空参数构造方法。所以父类的构造方法既可以给自己的对象初始化，也可以给自己的子类对象初始化。如果默认的隐式super()语句在父类中没有对应的构造方法，那么必须在构造方法中通过this或者super的形式明确要调用的构造方法。