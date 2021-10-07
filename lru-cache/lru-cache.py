from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size=0
        self.max_size=capacity
        self.omap=OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.omap:
            val=self.omap[key]
            self.omap.pop(key)
            self.omap[key]=val
            return val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.omap:
            self.omap.pop(key)
            self.omap[key]=value
        else:
            if self.size<self.max_size:
                
                self.omap[key]=value
                self.size+=1
            
            else:
                for i in self.omap.keys():break
                self.omap.pop(i)
                self.omap[key]=value
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)