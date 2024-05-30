class points:
    def __init__(self, points):
        self.points = points
    
    #overloading with magic method
    def __add__(self, other):
        return self.points + other.points
    
pts_bh_ver = points(26)
pts_sa_ver = points(25)

print(f"Max Verstappen's total points: {pts_bh_ver + pts_sa_ver} points")