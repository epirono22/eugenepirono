public class Fibo {

	
	public static int fibo_rec(int n) {
		// base case // 
		if ( n <=1) {
			return n; 
		}
		// recursive case // 
		else {
			return fibo_rec(n-1) + fibo_rec (n-2); 
		}
	}
	
	public static int fibo_loop(int n) {
		int a = 0; 
		int b = 1; 
		for (int i = 0 ; i < n ; i++) {
			int tmp = b;
			b += a; 
			a = tmp; 
		}
		return a; 
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("fibo_rec: " + fibo_rec(10));
		System.out.println("fibo_loop: " + fibo_loop(10));
	}

}
