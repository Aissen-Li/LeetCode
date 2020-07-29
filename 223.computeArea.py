class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if A>G or E>C or B>H or F>D:
            return (C-A)*(D-B) + (G-E)*(H-F)
        left = max(A, E)
        right = min(C, G)
        up = min(D, H)
        down = max(B, F)
        return (C-A)*(D-B) + (G-E)*(H-F) - (right - left) * (up - down)