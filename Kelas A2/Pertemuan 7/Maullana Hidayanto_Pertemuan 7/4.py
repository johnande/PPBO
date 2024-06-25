class HasilTanding:
    hasil = []

    def __init__(self, home_team, away_team, home_score, away_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    @classmethod
    def add_hasil(cls, hasil):
        cls.hasil.append(hasil)

    @classmethod
    def tampilkan_hasil(cls):
        print("Hasil Pertandingan Tim Nasional Indonesia:")
        for hasil in cls.hasil:
            print(f"{hasil.home_team} {hasil.home_score} - {hasil.away_score} {hasil.away_team}")

# Class decorator 
def tim_nasional(cls):
    cls.__name__ = "Tim Nasional Indonesia"
    return cls

@tim_nasional
class Match:
    def __init__(self, home_team, away_team, home_score, away_score):
        self.hasil = HasilTanding(home_team, away_team, home_score, away_score)
        self.hasil.add_hasil(self.hasil)

match1 = Match("Indonesia", "Malaysia", 4, 1)
match2 = Match("Indonesia", "Vietnam", 3, 0)

HasilTanding.tampilkan_hasil()