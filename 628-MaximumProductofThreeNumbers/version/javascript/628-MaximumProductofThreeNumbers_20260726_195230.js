// Last updated: 7/26/2026, 7:52:30 PM
1var maximumProduct = function (nums) {
2    nums = nums.sort((a, b) => b - a);
3
4    let n = nums.length;
5    let top3 = nums[0] * nums[1] * nums[2];
6    let oneLargeTwoSmall = nums[0] * nums[n - 2] * nums[n - 1];
7
8    return Math.max(top3, oneLargeTwoSmall);
9};