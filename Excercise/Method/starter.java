import java.util.Scanner;
class starter {
    public static void multDiv3(int a, int b){
     int x = a;
     int y = b;
     int product = x+y;
     if(product%3 == 0){
         System.out.println("It is divisible by 3");
     }
     else{
         System.out.println("It is not divisible by 3");
     }
     System.out.println(product);
    }
	public static void main(String args[]) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("type an int:");
	    int a = sc.nextInt();
	    System.out.println("type another int:");
	    int b = sc.nextInt();
	    multDiv3(a,b);

   }
}
