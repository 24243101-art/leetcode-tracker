// Last updated: 7/19/2026, 8:15:38 AM
1class Solution {
2    private int dominantCount = 0;
3    public int countDominantNodes(TreeNode root) {
4        dominantCount = 0;
5        helper(root);
6        return dominantCount;
7    }
8    private int helper(TreeNode node){
9        if(node == null){
10            return Integer.MIN_VALUE;
11        }
12        int leftMax = helper(node.left);
13        int rightMax = helper(node.right);
14        int childrenMax = Math.max(leftMax, rightMax);
15        if(node.val >= childrenMax){
16            dominantCount++;
17        }
18        return Math.max(node.val, childrenMax);
19    }
20}