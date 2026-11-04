class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result, sol = [], []

        def backtrack(open: int, closed: int):
            if len(sol) == 2 * n:
                result.append("".join(sol))
                return

            if open < n:
                sol.append("(")
                backtrack(open + 1, closed)
                sol.pop()

            if open > closed:
                sol.append(")")
                backtrack(open, closed + 1)
                sol.pop()

        backtrack(0, 0)
        return result