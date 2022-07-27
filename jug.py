state = [0,0]
from util import Stack, Queue, PriorityQueue

class Jug:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.cur_amount = 0
    
    def set_state(self, amount):
        self.cur_amount = amount

    def pour(self, amount):
        if self.cur_amount + amount > self.max_volume:
            return self.max_volume
        else:
            return self.cur_amount + amount
        #return (self.cur_amount + amount) % self.max_volume 

    def fill(self):
        self.cur_amount = self.max_volume

    def get_amount(self):
        return self.cur_amount

    def empty(self):
        self.cur_amount  = 0

    def isEmpty(self):
        return self.cur_amount == 0
        
class State:
    def __init__(self):
        self.jugs = [Jug(3), Jug(5)]

    def set_state(self,a,b):
        self.jugs[0].cur_amount = a
        self.jugs[1].cur_amount = b

    def get_state(self):
        return [self.jugs[0].cur_amount, self.jugs[1].cur_amount]
    
    def goal_check(self):
        return self.jugs[0].get_amount == 1 or self.jugs[1].get_amount() == 1
        

    def empty(self, index):
        self.jugs[index].empty()

    def transfer(self, from_i):
        self.jugs[2-from_i+1].pour(self.jugs[from_i].get_amount())
        self.jugs[from_i].empty()
     

    def pour_more(self, i):
        self.jugs[i].fill()

    def is_it(self, a,b):
        return self.jugs[0].get_amount() == a and self.jugs[1].get_amount() == b

def transfer_fillb(juga, jugb):
    return (juga.cur_amount - jugb.max_volume + jugb.cur_amount, jugb.max_volume)

def transfer_filla(juga, jugb):
    return (juga.max_volume, jugb.cur_amount - juga.max_volume + juga.cur_amount)

def get_successors(juga,jugb):
    # fill jug 1
    successors = set()
    if juga.isEmpty():
       # print("fill a")
        successors.add((juga.max_volume, jugb.cur_amount))
    else: # transfer a to b
        #jugb.pour(juga.cur_amount)
        #print("transfer a")
        successors.add((0, jugb.pour(juga.cur_amount)))
        #print("empty a")
        successors.add((0, jugb.cur_amount))
        #print("transfer to fill b")
        if juga.cur_amount > jugb.max_volume - jugb.cur_amount:
            successors.add(transfer_fillb(juga,jugb))  
    # fill jug 2
    if jugb.isEmpty():
        #print("fill b")
        successors.add((juga.cur_amount, jugb.max_volume))
    else: # transfer b to a
        #juga.pour(jugb.cur_amount)
        #print("transfer b")
        successors.add((juga.pour(jugb.cur_amount),0))
        #print("empty b")
        successors.add((juga.cur_amount, 0))
        #print("transfer to fill b")
        if jugb.cur_amount > juga.max_volume - juga.cur_amount:
            successors.add(transfer_filla(juga,jugb))  
    return successors

def bfs(a,b):
    pass

def goal_check(a,b):
    return a == 1 or b == 1

def dfs(a,b):
    stack = Stack()
    closed_list = set()

    juga = Jug(3)
    jugb = Jug(5)

    stack.push((0,0))

    while not stack.isEmpty():
        state = stack.pop()
        closed_list.add(state)

        if goal_check(state[0], state[1]):
            print("found it")
            break
        print(f"parent state: {state}")
        juga.set_state(state[0])
        jugb.set_state(state[1])
        successors = get_successors(juga, jugb)
        unvisited = successors.difference(closed_list)

        print(f"nodes: {unvisited}")

        for success in unvisited:
            stack.push(success)
        

def iterative_deepening():
    pass

if __name__ == '__main__':
    dfs(2,5)
    #bfs(3,5)