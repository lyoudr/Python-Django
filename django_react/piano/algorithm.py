decies1 = set(['cheese', 'vegetable', 'meat', 'mushroom'])
decies2 = set(['milk', 'fish','cheese', 'vegatable', 'mushroom'])
decies3 = set(['vegetable', 'fish', 'mushroom', 'meat'])
decies4 = set(['vegetable', 'milk', 'cheese', 'mushroom'])
dish_list = [decies1, decies2, decies3, decies4]

# Using set to count dishes
def countDishes(inputdishes):
  input_set = set()
  resultdish = []
  for item in inputdishes:
    input_set.add(item)
  for set_item in dish_list:
    intersectiondish = set_item.intersection(input_set)
    if len(intersectiondish) > len(set_item) / 2:
      found_item = 'dish{}'.format(dish_list.index(set_item))
      resultdish.append(found_item)
  return resultdish

### BellmanFord ###
import math

graph = {
  'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
  'edges': [
    { 'u': "A", 'v': "B", 'w': 2 },
    { 'u': "B", 'v': "A", 'w': 2 },

    { 'u': "A", 'v': "C", 'w': 2 },
    { 'u': "C", 'v': "A", 'w': 2 },

    { 'u': "B", 'v': "C", 'w': 3 },
    { 'u': "C", 'v': "B", 'w': 3 },

    { 'u': "B", 'v': "D", 'w': 3 },
    { 'u': "D", 'v': "B", 'w': 3 },

    { 'u': "B", 'v': "E", 'w': 1 },
    { 'u': "E", 'v': "B", 'w': 1 },

    { 'u': "C", 'v': "F", 'w': 4 },
    { 'u': "F", 'v': "C", 'w': 4 },

    { 'u': "C", 'v': "G", 'w': 1.5 },
    { 'u': "G", 'v': "C", 'w': 1.5 },
    ]
}

def BellmanFord(vertices, edges, source):
  distance = {}
  predecessor = {}

  for v in vertices:
    distance[v] = math.inf
    predecessor[v] = None

  distance[source] = 0

  for i in range(1, len(vertices)):
    for edge in edges:
      if(distance[edge["u"]] + edge["w"] < distance[edge["v"]]):
        distance[edge["v"]] = distance[edge["u"]] + edge["w"]
        predecessor[edge["v"]] = edge["u"]
  
  for edge in edges:
    if(distance[edge["u"]] + edge["w"] < distance[edge["v"]]):
      raise Exception("Graph contains a negative-weight cycle")
  
  return predecessor

class find_route:
  def __init__(self, searchresult, pathS):
    self.searchresult = searchresult
    self.path_s = pathS
  
  def define_result(self, vertices, edges, start):
    self.searchresult = BellmanFord(vertices, edges, start)
    print('self.searchresult is =>', self.searchresult)

  def count_path(self, pred_ecessor, final_v):
    if pred_ecessor[final_v] == None:
      self.path_s.append(final_v)
    else:
      self.path_s.append(final_v)
      self.count_path(pred_ecessor, pred_ecessor[final_v])

  def print_path(self, final_v):
    self.count_path(self.searchresult, final_v)
    path = self.path_s
    path.reverse()
    return path


def count_path(start, end):
  newgraph = find_route([], [])
  newgraph.define_result(graph['vertices'], graph['edges'], start)
  return newgraph.print_path(end)
