"""
Autonomous Agent Kuhn-Munkres (Hungarian) Assignment Algorithm Skill
Pure Python Standard Library implementation in O(n^3).
"""
from typing import List, Dict, Any

class HungarianMunkres:
    """
    Kuhn-Munkres (Hungarian) Algorithm for optimal minimum/maximum cost bipartite matching.
    """
    def __init__(self, cost_matrix: List[List[float]], maximize: bool = False):
        self.original_matrix = [[float(v) for v in r] for r in cost_matrix]
        self.maximize = maximize
        self.n_rows = len(cost_matrix)
        self.n_cols = len(cost_matrix[0])
        self.n = max(self.n_rows, self.n_cols)

    def solve(self) -> Dict[str, Any]:
        n = self.n
        cost = [[0.0] * n for _ in range(n)]
        max_val = max(max(row) for row in self.original_matrix)

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.maximize:
                    cost[i][j] = max_val - self.original_matrix[i][j]
                else:
                    cost[i][j] = self.original_matrix[i][j]

        u = [0.0] * (n + 1)
        v = [0.0] * (n + 1)
        p = [0] * (n + 1)
        way = [0] * (n + 1)

        for i in range(1, n + 1):
            p[0] = i
            j0 = 0
            minv = [float("inf")] * (n + 1)
            used = [False] * (n + 1)

            while True:
                used[j0] = True
                i0 = p[j0]
                delta = float("inf")
                j1 = 0

                for j in range(1, n + 1):
                    if not used[j]:
                        cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j

                for j in range(n + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta

                j0 = j1
                if p[j0] == 0:
                    break

            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break

        assignment = {}
        total_original_cost = 0.0

        for j in range(1, n + 1):
            if p[j] <= self.n_rows and j <= self.n_cols:
                row_idx = p[j] - 1
                col_idx = j - 1
                assignment[row_idx] = col_idx
                total_original_cost += self.original_matrix[row_idx][col_idx]

        sorted_pairs = [{"agent_id": r, "task_id": assignment[r], "cost": self.original_matrix[r][assignment[r]]} 
                        for r in sorted(assignment.keys())]

        return {
            "total_cost": round(total_original_cost, 4),
            "assignments": sorted_pairs,
            "dual_potentials": {
                "u": [round(x, 4) for x in u[1:self.n_rows + 1]],
                "v": [round(x, 4) for x in v[1:self.n_cols + 1]]
            }
        }
