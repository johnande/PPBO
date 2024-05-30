class racer:
    TEAM = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Aston Martin", "Alpine", "AlphaTauri", "Alfa Romeo", "Haas", "Williams")
    POINTS = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)

    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.pts = 0

    @classmethod
    def finishposition(cls,self, pos:int):
        self.pts += cls.POINTS[pos-1]
        return (f"""{self.name} finished in {pos} position and gained {cls.POINTS[pos-1]} points.""")
        

ALO = racer("Fernando Alonso", "Alpine")
print(ALO.finishposition(ALO, 3))
        
