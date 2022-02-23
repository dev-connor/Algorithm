import java.util.Arrays;
import java.util.stream.Stream;

public class 가장_큰_수 {
	String answer = "";
	
    public String solution(int[] numbers) {
    	String[] arr = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
    	Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));
    	Stream.of(arr).forEach(s -> answer += s);
    	return answer.charAt(0) == '0' ? "0" : answer;
	}
}