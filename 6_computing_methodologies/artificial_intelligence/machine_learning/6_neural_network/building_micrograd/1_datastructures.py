# %% [markdown]
# """
# references:
#     Karpathy, A. 2022. The spelled-out intro to neural networks and backpropagation: building micrograd. https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
# """

# %%
from graphviz import Digraph
import numpy as np
import matplotlib.pyplot as plt

# %%
"""
scalar valued function
input = x
ouput = y
where x AND y are scalar values
"""


def f(x_p):
    return 3 * x_p**2 - 4 * x_p + 5  # 3x² - 4x + 5


# %%
f(3.0)

# %%
x_scalar_values = np.arange(-5, 5, 0.25)
y_scalar_values = f(x_scalar_values)
plt.plot(x_scalar_values, y_scalar_values)

# %%
# what is the derivative of this function(f(x)) at any input value x

# slope at 3
h = 0.00000001
x = 3.0
how_much_the_function_responded = f(x + h) - f(x)
"""
    normalize by run
        = rise/run
"""
slope = how_much_the_function_responded / h
slope  # numerial approximation. requires h to be very small to get the actual scope

# %%
# slope at -3
h = 0.00000001
x = -3.0
how_much_the_function_responded = f(x + h) - f(x)
slope = how_much_the_function_responded / h
slope

# %%
# slope at 2/3
# i.e. the function does not respond
h = 0.00000001
x = 2 / 3
how_much_the_function_responded = f(x + h) - f(x)
slope = how_much_the_function_responded / h
slope
"""
    slope = 0 i.e the function does not respond
    stay almost the same?
"""

# %%
# another function scalar function
# from 3 scalars to 1 scalar
a = 2.0
b = -3.0
c = 10.0


def linear(m: float, x: float, ct: float) -> float:
    """A simple linear function.

    Args:
        a (float): gradient
        b (float): independent variable
        c (float): constant

    Returns:
        float: dependent variable
    """
    return m * x + ct


d = linear(a, b, c)
d

# %%
a_values = np.arange(-5, 5, 0.25)
b_values = np.arange(-5, 5, 0.25)
c_values = np.arange(-5, 5, 0.25)
d_values = linear(a_values, b_values, c_values)
plt.plot(d_values)

# %%
h = 0.00000001
a = 2.0
b = -3.0
c = 10.0

d1 = linear(a, b, c)
d2 = linear(a + h, b, c)
print("d1 = ", d1)
print("d2 = ", d2)
print("slope = ", (d2 - d1) / h)


# %%
class Value:
    def __init__(self, data, construction_parameters=(), operation="", label=""):
        """
        construction_parameters: Values used to create this Value
        operation: operation that created this Value
        label: name for the Value
        """
        self.data = data
        self.previous = set(construction_parameters)
        self.operation = operation
        self.label = label
        self.gradient = 0.0

    def __repr__(self):
        return f"Value(data={self.data}, gradient={self.gradient})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")


# %% [markdown]
#

# %%
# inputs
a = Value(2.0, label="a")
b = Value(-3.0, label="b")
c = Value(10.0, label="c")
f = Value(-2.0, label="f")

# intermedate values
e = a * b
e.label = "e"

d = e + c
d.label = "d"

# output
LossFunction = d * f
LossFunction.label = "LossFunction"
LossFunction

LossFunction


# %%
def build_graph(root: Value):
    """
    build set of nodes(vertices) and edges
    """
    nodes, edges = set(), set()

    def build(node):
        if node not in nodes:
            nodes.add(node)
            for child in node.previous:
                edges.add((child, node))
                build(child)

    build(root)
    return nodes, edges


# %%


def draw_dot_graph(root):
    dot_graph = Digraph(format="svg")
    dot_graph.graph_attr["rankdir"] = "LR"
    nodes, edges = build_graph(root)
    for n in nodes:
        object_id = str(id(n))
        dot_graph.node(
            name=object_id,
            label=f"{n.label}| data: {n.data}| gradient: {n.gradient}",
            shape="record",
        )
        if n.operation != "":
            operation_node_id = object_id + n.operation
            dot_graph.node(name=operation_node_id, label=n.operation)
            dot_graph.edge(operation_node_id, object_id)
    for edge_1, edge_2 in edges:
        # TODO: Why does this work?
        dot_graph.edge(str(id(edge_1)), str(id(edge_2)) + edge_2.operation)
    # print(dot_graph)
    return dot_graph


# %%
draw_dot_graph(LossFunction)
