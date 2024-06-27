from abc import ABC, abstractmethod

class Activity(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

class Exercise(Activity):
    def start(self):
        print("Start exercising.")

    def end(self):
        print("Finish exercising.")

class Cooking(Activity):
    def start(self):
        print("Start cooking.")

    def end(self):
        print("Finish cooking.")

class Reading(Activity):
    def start(self):
        print("Start reading.")

    def end(self):
        print("Finish reading.")

# Membuat objek-objek dari kelas Exercise, Cooking, dan Reading
exercise = Exercise()
cooking = Cooking()
reading = Reading()

# Menjalankan dan mengakhiri setiap aktivitas
exercise.start()
exercise.end()

cooking.start()
cooking.end()

reading.start()
reading.end()
