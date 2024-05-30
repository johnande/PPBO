class driver:
    def describe(self):
        print("This driver is competing in the Formula One World Championship.")


class verstappen(driver):
    def champ_pos(self):
        print("Max Verstappen is first in the current world championship.")
    
    def cur_team(self):
        print("Max Verstappen is currently racing for Red Bull Racing.")

class piastri(driver):
    def champ_pos(self):
        print("Oscar Piastri is fourth in the current world championship.")

    def cur_team(self):
        print("Oscar Piastri is currently racing for McLaren.")

ver = verstappen()
pia = piastri() 

ver.champ_pos()
pia.champ_pos()

ver.cur_team()
pia.cur_team()

ver.describe()
pia.describe()