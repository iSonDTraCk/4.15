class Cuadrado:
    def __init__(self, n):
        if n >= 2:
            self.n = n
        else:
            raise ValueError("La dimensión debe ser mayor o igual a 2.")

    def dibujar(self):
        for i in range(self.n + 1):
            print("*", end="")
        print()

        for j in range(self.n - 2):
            for k in range(self.n):
                if k == 0:
                    print("*", end="")
                elif k == self.n - 1:
                    print(" *", end="")
                else:
                    print(" ", end="")
            print()

        for i in range(self.n + 1):
            print("*", end="")
        print()
