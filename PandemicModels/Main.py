import numpy as np

statuses = ["healthy", "sick", "recovered", "dead"]


class Agent:
    def __init__(self, status="healthy"):
        assert status in statuses
        self.status = status


population = [Agent() for _ in range(20)]
population[0].status = "sick"
print([a.status for a in population])
