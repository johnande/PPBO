import math

def luas_lingkaran (r:float) -> str:

    return f"luas lingkaran dengan jari-jari {r} = {math.pi * r**2:.3f}"

def keliling_lingkarann (r:float) -> str:

    return f"keliling lingkaran dengan jari-jari {r} = {2 * math.pi * r:.3f}"

print(luas_lingkaran(10))
print(keliling_lingkarann(10))


