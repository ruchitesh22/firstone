class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return (str(self.x) + '+' + str(self.y) + 'j' )
	def __add__(self,other):
		x=self.x+other.x
		y=self.y+other.y
		return point(x,y)

p=point(2,3)
q=point(4,5)
print(p+q)