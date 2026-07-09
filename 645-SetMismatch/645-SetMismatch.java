// Last updated: 7/9/2026, 10:07:25 AM
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];

        for (int num : nums) {
            freq[num]++;
        }

        int duplicate = -1;
        int missing = -1;

        for (int i = 1; i <= n; i++) {
            if (freq[i] == 2) {
                duplicate = i;
            } else if (freq[i] == 0) {
                missing = i;
            }
        }

        return new int[]{duplicate, missing};
    }
}