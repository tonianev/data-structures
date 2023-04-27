import pytest
from src.graph import Graph

def test_graph():
    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    assert set(graph.adjacency_list.keys()) == {'A', 'B', 'C', 'D'}

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')

    assert 'B' in graph.adjacency_list['A']
    assert 'C' in graph.adjacency_list['A']
    assert 'A' in graph.adjacency_list['B']
    assert 'A' in graph.adjacency_list['C']

    graph.remove_edge('A', 'B')

    assert 'B' not in graph.adjacency_list['A']
    assert 'A' not in graph.adjacency_list['B']
    assert 'C' in graph.adjacency_list['A']

    graph.remove_vertex('A')

    assert 'A' not in graph.adjacency_list
    assert 'C' not in graph.adjacency_list['B']
    assert 'B' in graph.adjacency_list['C']

    graph.add_edge('C', 'D')
    graph.remove_vertex('C')

    assert 'C' not in graph.adjacency_list
    assert 'D' not in graph.adjacency_list['B']
    assert 'B' not in graph.adjacency_list['D']

