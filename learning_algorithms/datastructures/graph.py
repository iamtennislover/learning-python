class Node:
    def __init__(self,v,nbrs):
        self.v = v
        self.nbrs = nbrs
    def __repr__(self):
        return f"Node({self.v}, {[n.v for n in self.nbrs]})"
    
class FindArticulatePoint():
    """
    Find SPOF

    e.g. adj_list1
                
                1
              /   \
             /     \
            /       \
           /         \
          /           \
         -             -2
        4              /
          --\        /-
             ---\  /-
                 --
                 3
                /  -\
               /     -\
             /-        -\
            /            -
           -
           5  ----------6
    """
    adj_list1 = [
        [2,4],
        [1,4,3],
        [4,2,5,6],
        [1,2,3],
        [3,6],
        [3,5]
    ]
    def __init__(self):
        pass
    
    def build_graph(self, adj_list):
        nodes_by_id = {}
        for v in range(1,len(adj_list)+1):
            # print("creating node",v)
            nodes_by_id[v] = Node(v,[])
        for v in range(1, len(adj_list) + 1):
            for nbr_id in adj_list[v-1]:
                # print(f"adding new nbr {nbr_id} ({nodes_by_id[nbr_id]}) to {v} ({nodes_by_id[v]})")
                nodes_by_id[v].nbrs.append(nodes_by_id[nbr_id])
        # print(f"nodes_by_id: {nodes_by_id}")
        # verify
        for v in range(1,len(adj_list)+1):
            assert [n.v for n in nodes_by_id[v].nbrs] == adj_list[v-1]
        return nodes_by_id[list(nodes_by_id.keys())[0]]

    def find_articulate(self, adj_list):
        """TODO"""



def main():
    pass
    f = FindArticulatePoint()
    print(f.adj_list1)
    f.build_graph(f.adj_list1)

main()