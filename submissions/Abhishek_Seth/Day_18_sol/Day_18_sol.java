import java.util.*;
public class Day_18_sol {
    public static void main(String[] args) {
        System.out.println("The maze has a depth of " + findDepth(parse(new Scanner(System.in).nextLine()))+".");
    }
    public static int findDepth(Object obj) {
        if (!(obj instanceof List)) return 0;
        int max = 0;
        for (Object o : (List<?>) obj) max = Math.max(max, findDepth(o));
        return 1 + max;
    }
    public static Object parse(String s) {
        Stack<List<Object>> stack = new Stack<>();
        List<Object> currentList = new ArrayList<>();
        StringBuilder num = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (c == '[') {
                stack.push(currentList);
                currentList = new ArrayList<>();
            } else if (c == ']') {
                if (num.length() > 0) {
                    currentList.add(Integer.parseInt(num.toString()));
                    num.setLength(0);
                }
                List<Object> completedList = currentList;
                currentList = stack.pop();
                currentList.add(completedList);
            } else if (c == ',') {
                if (num.length() > 0) {
                    currentList.add(Integer.parseInt(num.toString()));
                    num.setLength(0);
                }
            } else if (Character.isDigit(c) || c == '-') {
                num.append(c);
            }
        }
        return currentList.get(0); // Return the root list
    }
}