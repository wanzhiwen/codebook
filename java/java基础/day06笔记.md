今日内容介绍
1、自定义类型的定义及使用
2、自定义类的内存图
3、ArrayList集合的基本功能
4、随机点名器案例及库存案例代码优化

	
### 01引用数据类型_类
* A: 数据类型
	* a: java中的数据类型分为：基本类型和引用类型
* B: 引用类型的分类
	* a: Java为我们提供好的类，比如说：Scanner,Random等。
	* b: 我们自己创建的类，按照类的定义标准，可以在类中包含多个方法与属性，来供我们使用。 
		
	
### 02自定义类的概述
* A: 自定义类的概述
	* java代码映射成现实事物的过程就是定义类的过程。
	* 举例：
		我们就拿一部手机进行分析，它能用来做什么呢？它可以打电话，上网，聊微信等，这些就是手机所提供的功能，也就是方法；手机也有它的特征，如颜色、尺寸大小、品牌型号等，这些就是手机的特征，也就是属性
	* 目前，我们只关注类中的属性，类中的方法在面向对象部分再进行学习。
				
			
### 03自定义类的格式
* A: 自定义类的格式
	* a: 使用类的形式,对现实中的事物进行描述。
	* b: 事物由方法和属性两部分组成。
		* 方法: 这个事物具备的功能。
		* 属性: 这个事物具备的特征。
	* c: 格式
		```java
		public class 类名{
			属性定义
			  修饰符 数据类型 变量名 = 值
			
			方法定义
			  修饰符 返回值类型  方法名(参数列表){
				  
			  }
		}
		```


### 04自定义的手机类
* A: 自定义的手机类
	* a: 案例代码
		```java
		public class Phone{
			/*
			    定义手机的属性
			*/
			String color ;
			String brand ;
			double size ; 
		}
		```


### 05测试手机类
* A: 调用方法执行流程
	* a: 实现引用类型的步骤
		* 1: 导入包 , 类都是在同一个文件夹,不需要导入包
		* 2: 创建引用类型的变量
		* 3: 变量.类型中的功能
	* b: 案例代码
		public class TestPhone{
			public static void main(String[] args){
				// 2: 创建引用类型的变量
				Phone p = new Phone();
				//System.out.println(p);  //输出内存的地址
			
		     	//3: 变量.类型中的功能
				//变量 p.的方式,调用类中的属性
				//属性就是变量 , 赋值和获取值
				p.color = "土豪金";
				p.brand = "爱立信";
				p.size = 5.0;
				
				//获取属性值
				System.out.println(p.color+"  "+p.brand+"  "+p.size);
			}
		}

	
### 6ArrayList创建变量的步骤
* A: ArrayList创建变量的步骤
	* a: 导入包 java.util包中
	* b: 创建引用类型的变量
		* 数据类型< 集合存储的数据类型>  变量名 = new 数据类型<集合存储的数据类型>();
			* 集合存储的数据类型: 要将数据存储到集合的容器中
   			* 创建集合引用变量的时候,必须要指定好,存储的类型是什么
	* c: 变量名.方法 
    	* 注意: 集合存储的数据,8个基本类型对应8个引用类型
		* 存储引用类型,不存储基本类型
		
### 7ArrayList创建变量举例
* A: ArrayList创建变量的示例代码
	```java
	import java.util.ArrayList;
	public class ArrayListDemo{
		public static void main(String[] args){
			//创建集合容器,指定存储的数据类型
			//存储字符串
			ArrayList<String> array = new ArrayList<String>();
			
			//创建集合容器,存储整数
			ArrayList<Integer> array2 = new ArrayList<Integer>();
			
			//创建集合容器,存储手机类型
			ArrayList<Phone> array3 = new ArrayList<Phone>();
		}
	}
	```


### 8ArrayList的常见方法
* A: ArrayList的常见方法
	* a: add(参数) 向集合中添加元素
	* b: get(int index) 取出集合中的元素,get方法的参数,写入索引
	* c: size() 返回集合的长度, 集合存储元素的个数
* B: 案例代码
	```java
	import java.util.ArrayList;
	public class ArrayListDemo_1{
		public static void main(String[] args){
			//定义集合,存储字符串元素
			ArrayList<String> array = new ArrayList<String>();
			//调用集合方法add存储元素
			array.add("abc");
			array.add("itcast");
		    array.add("love");
			array.add("java");
			//输出集合的长度,调用集合方法size, size方法的返回值类型 int
			int size = array.size();
			System.out.println(size);
			
			//获取出集合中的一个元素,获取1索引的元素
			//集合的方法get, 获取元素后结果数据类型
			String s = array.get(1);
			System.out.println(s);
			
			
			System.out.println(array.get(0));
			System.out.println(array.get(1));
			System.out.println(array.get(2));
			System.out.println(array.get(3));
		}
	}
	```


### 9ArrayList集合的遍历
* A: 案例代码
	```java
	/*
	   集合的遍历
	   实现思想也是索引思想
	   集合的索引从0开始,到 size()-1
	   方法get(int index)
	*/
	import java.util.ArrayList;
	public class ArrayListDemo_2{
		public static void main(String[] args){
			ArrayList<Integer> array = new ArrayList<Integer>();
			array.add(121);
			array.add(125);
			array.add(123);
			array.add(120);
			array.add(128);
			
			//对集合进行遍历
			//使用方法 size+get组合进行遍历
			for(int i = 0 ; i < array.size(); i++){
				System.out.println( array.get(i) );
			}
		}
	}
	```


### 10ArrayList补充方法
* A: ArrayList补充方法
	* a: add(int 索引,存储的元素) 	将元素添加到指定的索引上
	* b: set(int 索引,修改后的元素) 	将指定索引的元素,进行修改
	* c: remove(int 索引) 			删除指定索引上的元素
	* d: clear() 					清空集合中的所有元素
* B: 案例代码
	```java
	import java.util.ArrayList;
	public class ArrayListDemo_3{
		public static void main(String[] args){
			ArrayList<Integer> array = new ArrayList<Integer>();
			array.add(1);
			array.add(2);
			array.add(3);
			array.add(4);
			//在索引2上,添加元素7
			array.add(2,7);
			//将0索引上的元素,修改成10
			array.set(0,10);
			//将4索引上的元素,删除
			array.remove(4);
			array.clear();
			//使用方法 size+get组合进行遍历
			for(int i = 0 ; i < array.size(); i++){
				System.out.println( array.get(i) );
			}
		}
	}
	```