import java.util.Arrays;

class Solution {
    //  사고과정 먼저 정리
    // 그렇다면 배열의 각 요소의 크기를 우선적으로 비교하는데
    // 9 10 이라고하면 10이 크다고 생각하겠지만 앞자리 수의 크기로 보아서 계산하는 로직으로 하면 바로 끝아닌가?
    // 앞자리수 기준으로 가장 큰걸 앞에 배치하는 정렬을 해야할듯하다.
    // 각 요소들을 숫자로 치환하고 거기서 맥스인 값 추출하면 끝.
    public String solution(int[] numbers) {
        //문자열로 바꾸고
        String[] arr = new String[numbers.length];
        for (int i = 0; i<numbers.length; i++){
            arr[i] = String.valueOf(numbers[i]); 
        }
        
        // 문자열 이어붙이기를 내림차순으로 정렬 먼저
        //a가 앞일때의 수 (a+b) b가 앞일때의 수 (b+a)
        Arrays.sort(arr, (a,b) -> (b+a).compareTo(a+b));
        
        if(arr[0].equals("0")) return "0";
        //이어붙이기
        StringBuilder sb = new StringBuilder();
        for (String s: arr){
            sb.append(s);
        } 

        return sb.toString();
    }
}