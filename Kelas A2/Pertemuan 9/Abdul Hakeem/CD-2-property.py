class racer:
    team = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Aston Martin", "Alpine", "AlphaTauri", "Alfa Romeo", "Haas", "Williams")

    def __init__(self, name, team, pos):
        self.name = name
        self.team = team
        self.pos = pos

    @property
    def info(self):
        return f"{self.name} is a racer from {self.team} team and currently in position {self.pos} in the standings."
    
gas = racer("Pierre Gasly", "AlphaTauri", 9)

print(gas.info)