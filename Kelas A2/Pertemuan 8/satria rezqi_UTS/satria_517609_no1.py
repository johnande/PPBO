def milesToKm(distance:float):
    return f"{distance} mil = {distance * 1.60934} kilometer"

distance = float(input("Enter distance in miles: "))
print(milesToKm(distance))