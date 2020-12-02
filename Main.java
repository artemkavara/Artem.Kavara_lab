import java.util.*;
import java.util.regex.Pattern;
import java.lang.*;
import java.util.stream.*;


public class Main{
	
	public static ArrayList<Integer> getIntegersFromList (List arr) {
		ArrayList<Integer> res = new ArrayList<Integer>(); 
		for(int i = 0; i<arr.size(); i++) {
			if (arr.get(i).getClass() == Integer.class) {
				res.add(Integer.parseInt(arr.get(i).toString()));
			}
		}
		return res;
	}
	
	public static String first_non_repeating_letter(String s) {
		String temp = s.toLowerCase();
		HashMap<String, List<Integer>> res = new HashMap<String, List<Integer>>();
		for (int i = 0; i < temp.length(); i++ ) {
			if(res.containsKey(String.valueOf(temp.charAt(i)))) {
				List<Integer> num = res.get(String.valueOf(temp.charAt(i)));
				//System.out.println(num++);
				Integer t = num.get(1)+1;
				num.set(1, t);
				res.replace(String.valueOf(temp.charAt(i)), num);
			}
			else {
				res.put(String.valueOf(temp.charAt(i)), Arrays.asList(i, 1));
			}
		}
		for (int i = 0; i < temp.length(); i++ ) {
			if(res.containsValue(Arrays.asList(i, 1))) {
				return String.valueOf(s.charAt(i));
			}
		}
		return "";
	}
	
	public static Integer Digital_root(int n) {
		Integer num = Integer.valueOf(n);
		while(num>=10) {
			String[] temp = num.toString().split("", -1);
			Integer s = 0;
			for(int i = 0; i<num.toString().length(); i++) {
				s+=Integer.valueOf(temp[i]);
			}
			num = s;
		}
		return num;
	}
	
	public static Integer number_of_pairs(int[] lst, int target) {
		Integer num = 0;
		for(int i = 0; i<lst.length; i++) {
			for(int j = i; j<lst.length; j++) {
				if(lst[i]+lst[j] == target) {
					num++;
				}
			}
		}
		return num;
	}
	
	public static int n = 0;
	
	private static void add(int i) {
		n+=i;
	}
	
	public static int number_of_pairs_str(int[] lst, int target) {
		IntStream str = IntStream.range(0,  lst.length-1);
		str.forEach(i -> IntStream.range(i+1,  lst.length)
			            .filter(j -> lst[i]+ lst[j]== target)
			            .forEach(j -> add(1)));
	return n;
	
	}
	public static ArrayList<String[]> temp_str = new ArrayList<> ();
	
	private static void split_2(String j) {
		temp_str.add(j.split(":"));
	}
	
	private static class LastNameComparator implements Comparator<String[]>{
		  
	    public int compare(String[] a, String[] b){
	      
	        return a[1].compareTo(b[1]);
	    }
	}
	
	private static class FirstNameComparator implements Comparator<String[]>{
		  
	    public int compare(String[] a, String[] b){
	      
	        return a[0].compareTo(b[0]);
	    }
	}

	public static String meeting(String s) {
		s = s.toUpperCase();
		String str_main = "";
		String[] str_1 = s.split(";");
		Stream.of(str_1).forEach(j -> split_2(j));
		Comparator<String[]> c = new LastNameComparator().thenComparing(new FirstNameComparator());
		temp_str.sort(c);
		for (String[] elem:temp_str) {
			str_main = str_main+"("+elem[1]+", "+elem[0]+")";
		}
		return str_main;
	}
	
	public static void main(String[] args) {
		System.out.println(meeting("Valerii:Selikhov;Artem:Kavara;Roman:Kavara"));
		int [] arr = {1, 3, 6, 2, 2, 0, 4, 5, 5};
		System.out.println(number_of_pairs_str(arr, 5));
		System.out.println(number_of_pairs_str(arr, 5));
		System.out.println(Digital_root(493193));
		System.out.println(first_non_repeating_letter("ssttrreess"));
		System.out.println((getIntegersFromList(Arrays.asList(2, 4, "r", "aaabbb", "1", 5, "22")).toString()));
	}
}
