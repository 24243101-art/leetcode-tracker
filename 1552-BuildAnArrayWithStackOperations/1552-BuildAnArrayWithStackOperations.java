// Last updated: 7/9/2026, 10:07:20 AM
import java.util.*;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<>();
        int curr = 1;

        for (int num : target) {
            while (curr < num) {
                result.add("Push");
                result.add("Pop");
                curr++;
            }

            result.add("Push");
            curr++;
        }

        return result;
    }
}