class SleepingTree:
    def __init__(self, nodes_count, node_list):
        self.root = ''
        self.node_dict = {}
        self.from_list(nodes_count)

        for i in node_list:
            self.nodes_exchanger(i) 

    def from_list(self, nodes_count):
        nodes = [str(i) for i in range(1, int(nodes_count) + 1)]
        kids = nodes[::-1]
        self.root = kids.pop()
        self.node_dict[self.root] = {'parent': ''}
        for node in nodes:
            self.node_dict[node]['left'] = ''
            self.node_dict[node]['right'] = ''
            if kids:
                left_kid = kids.pop()
                self.node_dict[node]['left'] = left_kid
                self.node_dict[left_kid] = {'parent': node}
            if kids:
                right_kid = kids.pop()
                self.node_dict[node]['right'] = right_kid
                self.node_dict[right_kid] = {'parent': node}

    def nodes_exchanger(self, u):
        if u == self.root:
            return
        p = self.node_dict[u]['parent']
        pp = ''
        if p == self.root:
            self.root = u
        else:
            pp = self.node_dict[p]['parent']

        if self.node_dict[p]['left'] == u:
            ul = self.node_dict[u]['left']
            self.node_dict[u]['left'] = p
            self.node_dict[p]['left'] = ul
            if ul != '':
                self.node_dict[ul]['parent'] = p
        else:
            ur = self.node_dict[u]['right']
            self.node_dict[u]['right'] = p
            self.node_dict[p]['right'] = ur
            if ur != '':
                self.node_dict[ur]['parent'] = p

        self.node_dict[u]['parent'] = pp
        self.node_dict[p]['parent'] = u

        if pp != '':
            if self.node_dict[pp]['left'] == p:
                self.node_dict[pp]['left'] = u
            else:
                self.node_dict[pp]['right'] = u

    def LVR(self, node, result=None):
        if result is None:
            result = []
        left_child = self.node_dict[node]['left']
        if left_child != '':
            self.LVR(left_child, result)
        result.append(node)
        right_child = self.node_dict[node]['right']
        if right_child != '':
            self.LVR(right_child, result)
        return result
    
    def LVR_print(self):
        print(' '.join(self.LVR(self.root)))

import random
import time

def generate_tree_changes(N, Q):
    changes = [str(random.randint(1, N)) for _ in range(Q)]

    return changes
    

#N = 750
#Q = 1000000
#nodes = generate_tree_changes(N, Q)


N = input().split()[0]
nodes = input().split()

#start_time = time.time()
changer = SleepingTree(N, nodes)
changer.LVR_print()
#print(f"Время выполнения: {time.time() - start_time:.2f} секунд")