# Because Lavender didn't have hashtables yet
class Grid(object):
    def __init__(self):
        self.grid = { (0, 0): 1 }
        self.x = 1
        self.y = 0
        
    def at(self, x, y):
        return self.grid.get((x, y), 0)
    
    def computeNext(self):
        """Computes the value at the cursor
            and stores it for future use.
            Then, moves the cursor appropriately.
            Returns the value computed and its position
            as a tuple (x, y, value).
        """
        val = (self.at(self.x + 1, self.y)
            +  self.at(self.x + 1, self.y + 1)
            +  self.at(self.x, self.y + 1)
            +  self.at(self.x - 1, self.y + 1)
            +  self.at(self.x - 1, self.y)
            +  self.at(self.x - 1, self.y - 1)
            +  self.at(self.x, self.y - 1)
            +  self.at(self.x + 1, self.y - 1))
        self.grid[self.x, self.y] = val
        ret = self.x, self.y, val
        if self.y >= 0 and self.x >= 0:
            if self.x > self.y:
                self.y += 1
            else:
                self.x -= 1
        elif self.y >= 0 and self.x < 0:
            if -self.x < self.y:
                self.x -= 1
            else:
                self.y -= 1
        elif self.y < 0 and self.x < 0:
            if -self.x > -self.y:
                self.y -= 1
            else:
                self.x += 1
        else:
            if self.x <= -self.y:
                self.x += 1
            else:
                self.y += 1
        return ret
        
    def firstAbove(self, num):
        """Returns the first number returned by computeNext()
            that is greater than num.
        """
        cmp = self.at(0, 0)
        while cmp <= num:
            cmp = self.computeNext()[2]
        return cmp
        
def main(num):
    return Grid().firstAbove(num)



