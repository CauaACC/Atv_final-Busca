from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        if initial.is_goal:
            return SearchResult(
                solution=initial,
                nodes_expanded=0,
                nodes_generated=1,
                max_frontier_size=1,
                depth=0,
            )

        stack: list[State] = [initial]
        visited: set = {initial.tiles}
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while stack:
            max_frontier_size = max(max_frontier_size, len(stack))
            node = stack.pop()
            nodes_expanded += 1

            if node.cost >= self.depth_limit:
                continue

            for child in node.neighbors():
                if child.tiles in visited:
                    continue
                nodes_generated += 1
                if child.is_goal:
                    return SearchResult(
                        solution=child,
                        nodes_expanded=nodes_expanded,
                        nodes_generated=nodes_generated,
                        max_frontier_size=max(max_frontier_size, len(stack) + 1),
                        depth=child.cost,
                    )
                visited.add(child.tiles)
                stack.append(child)

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
            depth=0,
        )
