import heapq
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """Distância de Manhattan — admissível e consistente para o 8-puzzle."""
        goal_positions = {value: idx for idx, value in enumerate(GOAL_STATE)}
        total = 0
        for idx, value in enumerate(state.tiles):
            if value == 0:
                continue
            goal_idx = goal_positions[value]
            r1, c1 = divmod(idx, 3)
            r2, c2 = divmod(goal_idx, 3)
            total += abs(r1 - r2) + abs(c1 - c2)
        return total

    def search(self, initial: State) -> SearchResult:
        counter = count()
        start_f = self.heuristic(initial)
        frontier: list = [(start_f, next(counter), initial)]
        best_cost: dict = {initial.tiles: 0}
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))
            _, _, node = heapq.heappop(frontier)

            if node.cost > best_cost.get(node.tiles, node.cost):
                continue

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=node.cost,
                )

            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1
                prev = best_cost.get(child.tiles)
                if prev is None or child.cost < prev:
                    best_cost[child.tiles] = child.cost
                    f = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (f, next(counter), child))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
            depth=0,
        )
