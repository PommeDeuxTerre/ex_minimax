import random


class Node:
    def __init__(self):
        self.score = None
        self.children = []

    def generate_tree(self, depth: int = 0):
        counter = 0
        while random.randint(0, 10) <= 4 - depth - counter:
            self.children.append(Node().generate_tree(depth + 1))
            counter += 1
        if not self.children:
            self.score = random.randint(0, 100)
        return self

    def get_best_score(self):
        if self.score:
            return self.score

        # the min score is -100
        best_score = -101
        for child in self.children:
            best_score = max(best_score, -child.get_best_score())
        return best_score
