"""Script de demonstração — útil para depurar manualmente."""

import sys

from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def print_path(result):
    """Desenha cada etapa do caminho da solução: estado + ação aplicada."""
    if not result.found:
        return
    states = result.solution.path()
    print("\nEtapas da busca:")
    for i, state in enumerate(states):
        if i == 0:
            print(f"\nPasso {i} (inicial):")
        else:
            print(f"\nPasso {i} — ação: {state.action}")
        print(state)


def print_result(name: str, result, show_steps: bool = True):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    if result.found:
        print(f"Solução   : {' → '.join(result.actions)}")
        print(f"Custo     : {result.path_cost}")
        print(f"Profund.  : {result.depth}")
    else:
        print("Solução   : NÃO ENCONTRADA")
    print(f"Expandidos: {result.nodes_expanded}")
    print(f"Gerados   : {result.nodes_generated}")
    print(f"Fronteira : {result.max_frontier_size} (máx)")
    if show_steps:
        print_path(result)


if __name__ == "__main__":
    initial = State((2, 6, 8, 7, 1, 4, 0, 5, 3))   # 20 movimentos até a solução

    print("Estado inicial:")
    print(initial)

    print_result("BFS",  BFS().search(initial))
    print_result("DFS",  DFS().search(initial))
    print_result("A*",   AStar().search(initial))
