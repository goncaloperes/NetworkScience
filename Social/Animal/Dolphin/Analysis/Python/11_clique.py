# -*- coding: utf-8 -*-
"""
AFRS - Trabalho 4

Author: Gonçalo Peres
Date: 2019/02/02
"""

import networkx as nx

g=nx.read_gml('dolphins.gml')

clique = nx.enumerate_all_cliques(g)

print(list(clique))