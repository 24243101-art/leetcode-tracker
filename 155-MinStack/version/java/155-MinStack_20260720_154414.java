// Last updated: 7/20/2026, 3:44:14 PM
1import java.util.Stack;
2
3class MinStack {
4
5    private Stack<Integer> stack;
6    private Stack<Integer> minStack;
7
8    public MinStack() {
9        stack = new Stack<>();
10        minStack = new Stack<>();
11    }
12
13    public void push(int value) {
14        stack.push(value);
15
16        if (minStack.isEmpty() || value <= minStack.peek()) {
17            minStack.push(value);
18        }
19    }
20
21    public void pop() {
22        if (stack.peek().equals(minStack.peek())) {
23            minStack.pop();
24        }
25        stack.pop();
26    }
27
28    public int top() {
29        return stack.peek();
30    }
31
32    public int getMin() {
33        return minStack.peek();
34    }
35}