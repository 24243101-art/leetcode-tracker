// Last updated: 7/9/2026, 10:11:45 AM
import java.util.*;

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String current, int open, int close, int max) {
        // If the current string is complete
        if (current.length() == max * 2) {
            result.add(current);
            return;
        }

        // Add "(" if we still have open brackets left
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }

        // Add ")" if we have more opens than closes
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
}
