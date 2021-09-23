public class Fact {
    
	// Computing factorial function with recursion
	public static int fact_rec(int n) {
		
		if (n<= 0) {
			return 1; 
			
		}
		else {
			return n * fact_rec(n-1);
		}
	}
	
	// computing factorial function with loops 
	public static int fact_loop(int n ) { 
		int result = 1; 
		// (Initial value, condition, increment), // 
		for (int i =1 ;  i <= n ; i++) {
			result = result * i; 
		}
		return result; 
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// String enclosed with " " Double quote
		System.out.println("fact_rec: " + fact_rec(10) );
		System.out.println("fact_loop: " + fact_loop(10) );
	}







}
