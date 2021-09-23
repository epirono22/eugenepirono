public class Squareroot {

	public static int b_search( int n, int start, int end) {
		if (end == start) {
			return start; 
		}
		else {
			int mid = (start + end) / 2; 
			if (mid * mid < n) {
				return b_search(n, mid+1, end);
				
			}
			else if (mid * mid > n) {
				return b_search(n, start, mid -1);
				
			}
			else {
				return mid; 
			}
		}
	}
	
	public static int sqrt(int n) {
		return b_search(n, 0, n); 
	}
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println( "Square root: " + sqrt(36)); 
	}

}