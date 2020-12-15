import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Collections;

public class Extra {
	public static Integer Digital_root(int n) {
		Integer num = Integer.valueOf(n);
		if (num >=10) {
			String[] temp = num.toString().split("", -1);
			Integer s = 0;
			for(int i = 0; i<num.toString().length(); i++) {
				s+=Integer.valueOf(temp[i]);
			}
			num = s;
		return Digital_root(num.intValue());
	}
		return num;
	}
	
	public static int recursive_check (int num) {
		if (num < 10) return -1;
		String[] temp = String.valueOf(num).split("", -1);
		if (Integer.valueOf(temp[0]) >= Integer.valueOf(temp[1])) {
			String[] newNum = Arrays.copyOfRange(temp, 1, temp.length);
			return recursive_check(Integer.valueOf(String.join("", newNum)));} 
		return 0;
	}
	
	public static int nextBigger (int num) {
		if (recursive_check (num) == -1) return -1;
		int Num = num;
		String[] num_str = String.valueOf(num).split("", -1);
		String[] temp = num_str;
		String[] newNum = Arrays.copyOfRange(temp, 1, temp.length);
		Num = Integer.valueOf(String.join("", newNum));
		while(recursive_check(Num)!=-1) {
			temp = String.valueOf(Num).split("", -1);
			newNum = Arrays.copyOfRange(temp, 1, temp.length);
			Num = Integer.valueOf(String.join("", newNum));
		}
		String[] next_beg = Arrays.copyOfRange(num_str, 0, num_str.length - newNum.length-1);
		String[] next_end = Arrays.copyOfRange(num_str, num_str.length -newNum.length-1, num_str.length-1);
		List<Integer> int_next_end = Arrays.stream(next_end).map(Integer::valueOf).collect(Collectors.toList());
		List<Integer> int_next_beg = Arrays.stream(next_beg).map(Integer::valueOf).collect(Collectors.toList());
		List<Integer> int_next_end_sorted = new ArrayList<>(int_next_end);
		Collections.sort(int_next_end_sorted);
		for(int i = 1; i<next_end.length; i++) {
			if((int_next_end_sorted.get(i) > int_next_end.get(0)) &(int_next_end_sorted.get(i-1)!=int_next_end_sorted.get(i))) {
				Integer temp_s = int_next_end_sorted.get(0);
				int_next_end_sorted.set(0, int_next_end_sorted.get(i));
				int_next_end_sorted.set(i, temp_s);
				break;
			}
		}
		Collections.sort(int_next_end_sorted.subList(1, int_next_end_sorted.size()));
		int res = 0, k = 0;
		for(int i = 0; i< int_next_beg.size(); i++) {
			res+=int_next_beg.get(i)*Math.pow(10, num_str.length - i-2);
			k+=1;
		}
		for(int i = 0; i<int_next_end_sorted.size(); i++) {
			res+=int_next_end_sorted.get(i)*Math.pow(10, num_str.length - i-2-k);
		}
		return res;
		}
	
	public static String IP_adress(long num) {
		long last_digit = num%(long) (Math.pow(2, 8));
		num-=last_digit;
		long pre_last_digit = num % (long) (Math.pow(2, 16)) / (long) (Math.pow(2, 8));
		num-=(num % (int) (Math.pow(2, 16)));
		long pre_first_digit = num % (long) (Math.pow(2, 24)) / (long) (Math.pow(2, 16));
		num-=(num % (long) (Math.pow(2, 24)));
		long first_digit = num / (long) (Math.pow(2, 24));
		return String.valueOf(first_digit) + "." + String.valueOf(pre_first_digit) + "."
				+ String.valueOf(pre_last_digit) + "." + String.valueOf(last_digit);
	}
	
	public static void main(String[] args) {
		System.out.println(Digital_root(132189));
		System.out.println(nextBigger(513));
		System.out.println(IP_adress(2149583361L));
	}
}
