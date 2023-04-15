from typing import List
class ColorNode():
    def __init__(self, id, color, edges):
        # DON'T USE DEFAULT VALUE FOR EDGES LIST.
        self.id=id
        self.color=color
        self.edges=edges

from collections import defaultdict

class Solution_v1:
    # TODO: better solution, this one is TLE 
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Topological sorting could work?
        # Try building Rooted tree. If no rooted tree is possible, -1

        # Find nodes with the least incoming edges.
        # Start BFS from those.
        # Keep track of largest color value in bfs exploration.
        
        ### VERSION 1.0

        nodes = [
            ColorNode(i, colors[i], edges=[])
            for i in range(len(colors))
        ]
        degree = {i: 0 for i in range(len(nodes))}     
  
        for e in edges:
            # src to dest
            nodes[e[0]].edges.append(nodes[e[1]])
            degree[e[1]] += 1
        print([f"{n.id}: {[x.id for x in n.edges]}\n" for n in nodes])

        print("degrees", degree)

        nodes_by_degree = sorted(degree.keys(), key=degree.get)
        print("Least to most incoming edges")
        print(nodes_by_degree)
        
        def max_color_dfs(node, color_dict, curr_path):
            # Performs dfs and keeps track of largest color value
            # Returns -1 if a cycle is found
            if node is None:
                return 0
            if node.id in curr_path:
                print(f"node {node.id} in current path {curr_path}")
                return -1

            color_dict[node.color] += 1
            color_dict["max"] = max(color_dict[node.color], color_dict["max"])

            curr_path.add(node.id)
            print("adding", node.id, "new path", curr_path)
            print("edges to expand", [x.id for x in node.edges])

            for neighbor in node.edges:
                res = max_color_dfs(neighbor, color_dict.copy(), curr_path.copy())
                if res == -1:
                    return -1
                # Update max of all children paths
                color_dict["max"] = max(color_dict["max"], res)
            
            return color_dict["max"]

        already_on_path = set()
        max_color_value = 0
        
        for start_id in nodes_by_degree:
            print("startid", start_id)
            if start_id in already_on_path:
                continue
            
            colors_dict = defaultdict(int)
            colors_dict["max"] = 0
            seen = set()

            result = max_color_dfs(nodes[start_id], colors_dict, seen)
            if result == -1:
                return -1

            max_color_value = max(result, max_color_value)

        return max_color_value

        
