class MinStack {

    Stack<Integer> stack;
    Stack<Integer> min;

    public MinStack() {
        stack = new Stack<Integer>();
        min = new Stack<Integer>();
    }
    
    public void push(int val) {
        stack.push(val);
        if((!min.empty()) && (min.peek() < val)){
            min.push(min.peek());
        }else{
            min.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        min.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}
