class StockSpanner(object):

    def __init__(self):
        self.stack=[]
        self.cnt=0
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.cnt+=1
        if len(self.stack)==0:
            self.stack.append([price,self.cnt])
            return self.cnt
        while len(self.stack)>0 and self.stack[-1][0]<=price:
            self.stack.pop()
        self.stack.append([price,self.cnt])
        if len(self.stack)==1:return self.cnt
        else:return self.cnt-self.stack[-2][1]
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)