class University:

    def __init__(self, name, grade, numOfStudent):
        self.name = name
        self.grade = grade
        self.numOfStudent = numOfStudent

    def __add__(self, other):
        print("banyaknya siswa baru:", other.total, "orang")
        return self.numOfStudent + other.total
    

class newStudent:
    def __init__(self, total) -> None:
        self.total = total

ugm = University("UGM", "A", 500000)
UGM_newStudent = newStudent(300000)
print(f"total siswa di UGM sekarang: {ugm + UGM_newStudent} orang")

