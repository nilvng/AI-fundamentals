
from unicodedata import name
from util import Queue


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

    def fill(self):
        #self.cur_amount = self.max_volume
        return self.max_volume

    def get_amount(self):
        return self.cur_amount

    def empty(self):
        self.cur_amount  = 0

    def isEmpty(self):
        return self.cur_amount == 0
    
    def fill_other(self, other): # return its amount after filling other jug
        if self.cur_amount > other.max_volume - other.cur_amount:
            return self.cur_amount - other.max_volume + other.cur_amount

class State(object):
    def __init__(self, list_amount):
        self.juga = Jug(list_amount[0])
        self.jugb = Jug(list_amount[1])
        self.goal = 1
    def next_states(self):
        successors = set()
        if self.juga.isEmpty():
        # print("fill a")
            successors.add(State((self.juga.max_volume, self.jugb.cur_amount)))
        else: # transfer a to b
            #print("empty a")
            successors.add(State((0, self.jugb.cur_amount)))
            #print("transfer to fill b")
            successors.add(State((self.juga.fill_other(self.jugb), self.juga.max_volume)))
        # fill jug 2
        if self.jugb.isEmpty():
            #print("fill b")
            successors.add(State((self.juga.cur_amount, self.jugb.max_volume)))
        else: # transfer b to a
            #print("empty b")
            successors.add(State((self.juga.cur_amount, 0)))
            #print("transfer to fill b")
            successors.add(State((self.juga.max_volume ,self.jugb.fill_other(self.juga))))
        return successors

    def __eq__(self, other):
        return self.juga.cur_amount == other.juga.cur_amount and self.jugb.cur_amount == other.jugb.cur_amount

    def is_goal(self):
        return self.juga.cur_amount == self.goal or self.jugb.cur_amount == self.goal

class Node:
    def __init__(self, state) -> None:
        self.state = state
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_successors(self):
        suc_states = self.state.next_states()
        successors = set()
        for suc in suc_states:
            no = Node(suc)
            no.parent = self
            successors.add(no)
        return successors

class JugProblem:
    def __init__(self, initial) -> None:
        self.initial = initial
    def dfs():
        pass

    def bfs(self):

        initial_state = State(self.initial)
        initial_node = Node(initial_state)

        if initial_state.is_goal():
            return initial_node
        
        frontiers = Queue()
        frontiers.push(initial_node)
        reached = (initial_state)

        while not frontiers.isEmpty():
            node = frontiers.pop()
            for child in node.get_successors():
                s = child.state
                if s.is_goal():
                    return child
                if s not in reached:
                    reached.add(s)
                    frontiers.push(child)

        return None


if __name__ == '__main__':
    problem = JugProblem([0,0])
    node = problem.bfs()
    if node == None:
        print("FAILED!!!")
    while node:
        print(node.state)
        node = node.get_parent()
    

        


