### 01switch语句解构
* A:switch语句解构
	* a:switch只能针对某个表达式的值作出判断，从而决定程序执行哪一段代码。
    	* b:格式如下:
			```java
      		swtich(表达式){
      			case 常量1 :
      			  要执行的语句;
      			break;
      			case 常量2 :
      			  要执行的语句;
      			break;
      			case 常量3 :
      			  要执行的语句;
      			break;
      			default:
      			  要执行的语句;
      			break;
      		}
			```
      	* c: 执行流程:  表达式,和case后面的常量进行比较和哪个case后的常量相同,就执行哪个case后面的程序,遇到break,就全结束 
      	* d: 关键字: switch case default break




### 02switch语句的星期判断
* A: switch语句的星期判断
	* a: 明确需求: 需求:初始化int类型变量(1-7)代表星期几,使用switch语句进行判断,并打印出该整数对应的星期
	* b: 代码实现
		```java
		public class SwitchDemo01 {
			public static void main(String[] args) {
				int week = 5;
				switch (week) {
				case 1:
					System.out.println("星期一");
					break;
				case 2:
					System.out.println("星期二");
					break;
				case 3:
					System.out.println("星期三");
					break;
				case 4:
					System.out.println("星期四");
					break;
				case 5:
					System.out.println("星期五");
					break;
				case 6:
					System.out.println("星期六");
					break;
				case 7:
					System.out.println("星期天");
					break;
				default:
					System.out.println("输入的数字不正确...");
					break;
				}
			}
		}
		```

​			
### 03switch语句接受的数据类型
* A: switch语句接受的数据类型
	* a:注意事项
		* switch语句中的表达式的数据类型,是有要求的
		* JDK1.0 - 1.4  数据类型接受 byte short int char
		* JDK1.5   数据类型接受 byte short int char enum(枚举)
		* JDK1.7   数据类型接受 byte short int char enum(枚举), String	
​	

### 04case穿透
* A:case穿透
	* a: 在使用switch语句的过程中，如果多个case条件后面的执行语句是一样的，则该执行语句只需书写一次即可，这是一种简写的方式。
	* b: 例如，要判断一周中的某一天是否为工作日，同样使用数字1~7来表示星期一到星期天，当输入的数字为1、2、3、4、5时就视为工作日，否则就视为休息日。



​				

### 05数组的概述
* A: 数组的概述
	* a:数组的需求
		现在需要统计某公司员工的工资情况，例如计算平均工资、最高工资等。假设该公司有50名员工，用前面所学的知识完成，
		那么程序首先需要声明50个变量来分别记住每位员工的工资，这样做会显得很麻烦.
	* b:数组的概述
		数组是指一组数据的集合，数组中的每个数据被称作元素。在数组中可以存放任意类型的元素，但同一个数组里存放的元素类型必须一致。

### 06数组的定义
* A：数组的定义
* B:格式:
	* 数据类型[] 数组名 = new 数据类型[元素个数或数组长度];
	* 举例: int[] x = new int[100];
* C:要点说明
	* 数据类型: 数组中存储元素的数据类型
	*  [] 表示数组的意思
	*  变量名  自定义标识符  
	*  new  创建容器关键字
	* 数据类型: 数组中存储元素的数据类型
	* []  表示数组的意思
	* 元素个数,就是数组中,可以存储多少个数据 (恒定, 定长) 





### 07JVM内存划分			
* A：内存划分
	* JVM对自己的内存划分为5个区域
		* a: 寄存器:内存和CUP之间
		* b: 本地方法栈: JVM调用了系统中的功能
		* c: 方法和数据共享: 运行时期class文件进入的地方
		* d: 方法栈:所有的方法运行的时候进入内存
		* e: 堆:存储的是容器和对象
​		


### 08数组的内存
* A: 数组的内存
	* int[] x;	            	// 声明一个int[]类型的变量
	*	x = new int[100];		// 创建一个长度为100的数组
	*	接下来，通过两张内存图来详细地说明数组在创建过程中内存的分配情况。
	*	第一行代码 int[] x; 声明了一个变量x，该变量的类型为int[]，即一个int类型的数组。变量x会占用一块内存单元，它没有被分配初始值
	*	第二行代码 x = new int[100]; 创建了一个数组，将数组的地址赋值给变量x。在程序运行期间可以使用变量x来引用数组，这时内存中的状态会发生变化


​		
### 09使用索引访问数组的元素
* A: 使用索引访问数组的元素
	* 组中有100个元素，初始值都为0。数组中的每个元素都有一个索引(也可称为角标)，要想访问数组中的元素可以通过“x[0]、x[1]、……、x[98]、x[99]”的形式。
	* 需要注意的是，数组中最小的索引是0，最大的索引是“数组的长度-1”
​		

### 10数组的length属性
* A: lenth属性
	* a 在Java中，为了方便我们获得数组的长度，提供了一个length属性，在程序中可以通过“数组名.length”的方式来获得数组的长度，即元素的个数。
	* b 求数组的长度
		```java
		public class ArrayDemo01 {
	 		public static void main(String[] args) {
	 			int[] arr; // 声明变量
	 			arr = new int[3]; // 创建数组对象
	 			System.out.println("arr[0]=" + arr[0]); // 访问数组中的第一个元素
	 			System.out.println("arr[1]=" + arr[1]); // 访问数组中的第二个元素
	 			System.out.println("arr[2]=" + arr[2]); // 访问数组中的第三个元素
	 			System.out.println("数组的长度是：" + arr.length); // 打印数组长度
	 		}
 		}
		```

### 11为数组的元素赋值
* A: 为数组的元素赋值
	* a: 如果在使用数组时，不想使用这些默认初始值，也可以显式地为这些元素赋值。
	* 	赋值过的元素已经变为新的数值,没有赋值的元素默认初始化的数值
	* b: 案例
		```java
	 	public class ArrayDemo02 {
	 		public static void main(String[] args) {
	 			int[] arr = new int[4]; // 定义可以存储4个整数的数组
	 			arr[0] = 1; // 为第1个元素赋值1
	 			arr[1] = 2; // 为第2个元素赋值2
	 			// 下面的代码是打印数组中每个元素的值
	 			System.out.println("arr[0]=" + arr[0]);
	 			System.out.println("arr[1]=" + arr[1]);
	 			System.out.println("arr[2]=" + arr[2]);
				System.out.println("arr[3]=" + arr[3]);
	 		}
 		}
		```

### 12数组的定义_2
* A: 定义数组格式2
	* a: 数组初始化
		* 动态初始化 : 在定义数组时只指定数组的长度，由系统自动为元素赋初值的方式称作动态初始化。
			* 类型[] 数组名 = new 类型[长度];
			* int[] arr = new int[4];
		* 静态初始化: 在初始化数组时还有一种方式叫做静态初始化，就是在定义数组的同时就为数组的每个元素赋值。
			* 类型[] 数组名 = new 类型[]{元素，元素，……};
			* int[] arr = new int[]{1,2,3,4};
			* 类型[] 数组名 = {元素，元素，元素，……};	 
			* int[] arr = { 1, 2, 3, 4 };
​	
​		


### 13遍历数组
* A:遍历数组
	* 在操作数组时，经常需要依次访问数组中的每个元素，这种操作称作数组的遍历
* B:练习
	```java
	public class ArrayDemo04 {
		public static void main(String[] args) {
			int[] arr = { 1, 2, 3, 4, 5 }; // 定义数组
			// 使用for循环遍历数组的元素
			for (int i = 0; i < arr.length; i++) {
				System.out.println(arr[i]); // 通过索引访问元素
			}
		}
	}
	```


### 14数组中常见的异常
* A: 数组操作中,常见的两个异常
	* 数组的索引越界异常
	* 空指针异常
* B: 练习
	```java
	public class ArrayDemo_4{
		public static void main(String[] args){
			//数组的索引越界异常
			//int[] arr = {5,2,1};
			//数组中3个元素,索引 0,1,2
			//System.out.println(arr[3]);//java.lang.ArrayIndexOutOfBoundsException: 3
			
			//空指针异常
			int[] arr2 = {1,5,8};
			System.out.println(arr2[2]);
			arr2 = null; // arr2 不在保存数组的地址了
			System.out.println(arr2[2]);//java.lang.NullPointerException
		}
	}
	```

### 15数组最值
* A: 数组获取最值的原理思想
	* 定义数组的第一个元素arr[0]为最大值;循环arr数组,判断如果有比arr[0] 大的就交换,直到arr数组遍历完毕,那么arr[0]中就保存了最大的元素

​		


### 16数组获取最值代码实现
* A: 代码实现
	```java
	public class ArrayDemo05 {
		public static void main(String[] args) {
			int[] arr = { 4, 1, 6, 3, 9, 8 }; 	// 定义一个数组
			int max = arr[0]; 					// 定义变量max用于记住最大数，首先假设第一个元素为最大值
			// 下面通过一个for循环遍历数组中的元素
			for (int x = 1; x < arr.length; x++) {
				if (arr[x] > max) { 			// 比较 arr[x]的值是否大于max
					max = arr[x]; 				// 条件成立，将arr[x]的值赋给max
				}
			}
			System.out.println("max=" + max); 	// 打印最大值
		}
	}
	```

### 17二维数组的定义
* A 二维数组的作用
	* 要统计一个学校各个班级学生的考试成绩，又该如何实现呢？
	* 这时就需要用到多维数组，多维数组可以简单地理解为在数组中嵌套数组。
* B 定义格式
	* a 第一种定义格式:
		*  int[][] arr = new int[3][4];
		*  上面的代码相当于定义了一个3*4的二维数组，即二维数组的长度为3，二维数组中的每个元素又是一个长度为4的数组
	* b 第二种定义格式
		*  int[][] arr = new int[3][];
		*  第二种方式和第一种类似，只是数组中每个元素的长度不确定
	* c 第三种定义格式
		*  	int[][] arr = {{1,2},{3,4,5,6},{7,8,9}};
		*  	二维数组中定义了三个元素，这三个元素都是数组，分别为{1,2}、{3,4,5,6}、{7,8,9}





### 18二维数组元素的访问
* A: 二维数组的访问
	* 案例:
		```java
		class ArrayDemo08 {
			public static void main(String[] args){
				//定义二维数组的方式
				int[][] arr = new int[3][4];
				System.out.println( arr );
				System.out.println("二维数组的长度: " + arr.length);
				//获取二维数组的3个元素
				System.out.println( arr[0] );
				System.out.println( arr[1] );
				System.out.println( arr[2] );
				System.out.println("打印第一个一维数组的元素值");
				System.out.println( arr[0][0] );
				System.out.println( arr[0][1] );//访问的为二维数组中第1个一维数组的第2个元素
				System.out.println( arr[0][2] );
				System.out.println( arr[0][3] );
				System.out.println("打印第二个一维数组的元素值");
				System.out.println( arr[1][0] );
				System.out.println( arr[1][1] );
				System.out.println( arr[1][2] );
				System.out.println( arr[1][3] );
				System.out.println("打印第三个一维数组的元素值");
				System.out.println( arr[2][0] );
				System.out.println( arr[2][1] );
				System.out.println( arr[2][2] );
				System.out.println( arr[2][3] );
			}
		}
		```


### 19二维数组内存图
* A: 二维数组内存图
* 举例:int[][] arr = new int[3][2];
* 外层数组长在内存开辟连续的3个大的内存空间,每一个内存空间都对应的有地址值
* 每一个大内存空间里又开辟连续的两个小的内存空间.



### 20二维数组的定义和访问
* A: 二维数组的定义
	* 格式1: 
	* 	int[][] arr = new int[3][]; 不推荐
	* 格式2
	*  int[][] arr = {{1,2,4},{4,7},{0,9,3}};
	*  

​		
### 22二维数组的遍历
* A:二维数组遍历
	* int[][] arr = {{1,2,4},{4,7},{0,9,3}};
	* 先使用for循环遍历arr这个二维数组,得到每一个元素为arr[i]为一维数组，再外层for循环中嵌套一个for循环遍历每一个一维数组arr[i],得到每一元素
* B:举例:遍历二维数组
	```java
	public class ArrayArrayDemo_2{
		public static void main(String[] args){
			int[][] arr = { {1,2,3},{4,5},{6,7,8,9},{0} };
			
			//外循环,遍历二维数组
			for(int i = 0 ; i < arr.length ;i++){
				//内循环,遍历每个一维数组 arr[0] arr[1] arr[i]
				for(int j = 0 ; j < arr[i].length; j++){
					System.out.print(arr[i][j]);
				}
				System.out.println();
			}
		}
	}
	```
* C:二维数组累加求和
	```java
	class ArrayDemo09 {
		public static void main(String[] args){
		  	int[][] arr2 = { {1,2},{3,4,5},{6,7,8,9,10} };
			int sum2 = 0;
			for (int i=0; i<arr2.length; i++) {
				for (int j=0; j<arr2[i].length; j++) {
		            //System.out.println(arr2[i][j])
					sum2 += arr2[i][j];
				}
			}
			System.out.println("sum2= "+ sum2);
		}
	}
	```

