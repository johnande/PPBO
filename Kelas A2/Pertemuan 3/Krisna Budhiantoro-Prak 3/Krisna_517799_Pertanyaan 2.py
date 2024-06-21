class Shape:
    """
    Kelas dasar untuk semua bentuk geometri.
    """

    def __init__(self, width):
        """
        Konstruktor kelas.

        Args:
            width (float): Lebar bentuk.
        """
        self.width = width


class Square(Shape):
    """
    Kelas untuk mewakili persegi.
    """

    name = "Square"

    def get_area(self):
        """
        Menghitung luas persegi.

        Returns:
            float: Luas persegi.
        """
        return self.width**2


class Triangle(Shape):
    """
    Kelas untuk mewakili segitiga.
    """

    name = "Triangle"

    def __init__(self, width, height):
        """
        Konstruktor kelas.

        Args:
            width (float): Lebar segitiga.
            height (float): Tinggi segitiga.
        """
        super().__init__(width)
        self.height = height

    def get_area(self):
        """
        Menghitung luas segitiga.

        Returns:
            float: Luas segitiga.
        """
        return 0.5 * self.width * self.height


# Membuat objek SquareX dan TriangleY
SquareX = Square(5)
TriangleY = Triangle(5, 3)

# Menampilkan luas SquareX dan TriangleY
print(f"Luas ({SquareX.name}): {SquareX.get_area()}")
print(f"Luas ({TriangleY.name}): {TriangleY.get_area()}")
