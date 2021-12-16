class MinStack {
    List<Integer> rStack = new ArrayList<>();
    List<Integer> minStack = new ArrayList<>();
    int top = -1;
    int msTop = -1;

    public MinStack() {
        
    }
    
    public void push(int x) {
        if(msTop<0 || x<=minStack.get(msTop)) {
            minStack.add(x);
            msTop++;
        }else {
            int val = minStack.get(msTop);
            minStack.add(val);
            msTop++;
        }
        rStack.add(x);
        top++;
    }
        
    
    public void pop() {
        if(top>=0 && msTop>=0){
            minStack.remove(msTop);
            rStack.remove(top);
            msTop--;
            top--;
        }
        
    }
    
    public int top() {
        if(top>=0)
            return rStack.get(top);
        else
            return -1;
        
    }
    
    public int getMin() {
        if (minStack.size()>0)
            return minStack.get(msTop);
        else
            return -1;
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */