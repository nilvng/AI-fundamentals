from cmath import cos
import util

class Node:
    def __init__(self, state, parent=None, action=None, cost=None) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    def trace(self, depth = 0):
        pass

class Problem:

    def getInitialState(self):
        pass
    def isGoal(self, state):
        pass
    def getSuccessors(self, state):
        pass
    def possibleRepeatedState(self):
        pass

def bfs(problem):
    """
    Bread First Search algorithm
    - frontier: queue
    - reached: set of states
    - early goal test

    Usages: problem with a unit cost -> Optimal
    Cons:
    - Space and time = O(b^d)    
    """

    # sanity check
    s = problem.getInitialState()
    if problem.isGoal(s):
        return s

    frontiers = util.Queue()
    reached = set()

    initial_state = problem.getInitialState()
    initial_node = Node(initial_state)

    frontiers.push(initial_node)

    while not frontiers.isEmpty():

        cur_node = frontiers.pop()

        for child in problem.getSuccessors(cur_node.state):
            child_state, action, cost = child
            child_node = Node(child_state, parent=cur_node, action=action, cost=cost)

            if problem.isGoal(child_state):
                return child_node.trace()

            if not child_state in reached:
                reached.add(child_state)
                frontiers.push(child_node)

def dfs(problem):
    """
    Depth First Search algorithm
    - frontier: stack
    - early goal test

    Usages: finite graph space -> Space = O(bm)
    Cons:
    - infinite path
    - cycles (partially fix it using domain knowledge to trace fixed NO.parents)    
    """

    # sanity check
    s = problem.getInitialState()
    if problem.isGoal(s):
        return s

    frontiers = util.Stack()

    initial_state = problem.getInitialState()
    initial_node = Node(initial_state)

    frontiers.push(initial_node)

    while not frontiers.isEmpty():

        cur_node = frontiers.pop()

        for child in problem.getSuccessors(cur_node.state):
            child_state, action, cost = child
            child_node = Node(child_state, parent=cur_node, action=action, cost=cost)

            if problem.isGoal(child_state):
                return child_node.trace()

            if heuristicCycle(problem=problem, state=child_state):
                continue

            frontiers.push(child_node)

def btr_dfs(problem):
    initial_state = problem.getInitialState()
    node = Node(initial_state)
    return recurDFS(problem, node, frontiers=set())


def recurDFS(problem, cur_node, frontiers):

    if problem.isGoal(cur_node.state):
        return cur_node.trace()

    for child in problem.getSuccessors(cur_node.state):
        child_state, action, cost = child
        if child_state in frontiers: # loop detected
            continue
        else:
            child_node = Node(child_state, parent=cur_node, action=action, cost=cost)
            frontiers.add(child_state)
            res = recurDFS(problem, cur_node=child_node, frontiers=frontiers)
            if res:
                return res
            else:
                frontiers.remove(child_state)

    return None

            
def heuristicCycle(problem, state):
    allowed_repeat = problem.possibleRepeatedState()
    cur_state = state
    while allowed_repeat > 0:
        parent = cur_state.parent
        if parent == cur_state:
            return True
        allowed_repeat -= 1
    return False

class BestFirstSearchAlgorithm:
    def fn(self,problem, node):
        pass
    def excute(self,problem):
        # sanity check
        s = problem.getInitialState()
        if problem.isGoal(s):
            return s

        frontiers = util.PriorityQueue()
        reached = {} # {state: Node}
        initial_state = problem.getInitialState()
        initial_node = Node(initial_state)

        frontiers.push(initial_node)

        while not frontiers.isEmpty():

            cur_node = frontiers.pop()

            if problem.isGoal(child_state): # late goal test
                return child_node.trace()

            for child in problem.getSuccessors(cur_node.state):
                child_state, action, cost = child
                child_node = Node(child_state, parent=cur_node, action=action, cost=cost)

                if not child_state in reached.keys() or reached.get(child_state).cost > cost: # allow repeated as long as it's optimal
                    reached[child_state] = child_node
                    fn_value = self.fn(problem, child_node)
                    frontiers.push(child_node,fn_value)

class UCS(BestFirstSearchAlgorithm): 
    def fn(self, problem, node):
        parent_cost = node.parent.cost
        node.cost += parent_cost
        return node.cost

class BFSStar(BestFirstSearchAlgorithm): 
    def fn(self, problem, node):
        return problem.getHeuristicVal(node.state)

class AStar(BestFirstSearchAlgorithm): 
    def fn(self, problem, node):
        node.cost += node.parent.cost
        return problem.getHeuristicVal(node.state) + node.cost
