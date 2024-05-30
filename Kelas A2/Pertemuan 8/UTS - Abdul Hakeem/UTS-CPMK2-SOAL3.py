from abc import ABC, abstractmethod

class team():
    def __init__(self, tn, tp):
        self.team_name = tn
        self.team_pts = tp

    @abstractmethod
    def addpts(self):
        pass
    
    @abstractmethod
    def fl(self):
        pass

class driver(team):
    pos_to_pts = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)

    def __init__(self, tn, tp, dn, dp):
        super().__init__(tn, tp)
        self. driver_name = dn
        self.driver_pts = dp

    def addpts(self, pos):
        self.driver_pts += driver.pos_to_pts[pos-1]
        self.team_pts += driver.pos_to_pts[pos-1]
    
    def fl(self):
        self.driver_pts += 1
        self.team_pts += 1

    def getdata(self):
        print(f"""
+---------------+-----------------+
      Name      | {self.driver_name}  
+---------------+-----------------+
  Team          | {self.team_name} 
  Driver Points | {self.driver_pts}              
  Team Points   | {self.team_pts}              
+---------------+-----------------+
              """)
        
              
driver_MV1 = driver("Red Bull", 0, "Max Verstappen", 0)
driver_OP81 = driver("McLaren", 0, "Oscar Piastri", 0)

driver_MV1.addpts(1)
driver_MV1.fl()
driver_OP81.addpts(4)

driver_MV1.getdata()
driver_OP81.getdata()

team_RedBull = team("Red Bull", 0)
team_RedBull.addpts()






