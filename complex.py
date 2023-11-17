class LiczbaZespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, inna):
        nowa_re = self.re + inna.re
        nowa_im = self.im + inna.im
        return LiczbaZespolona(nowa_re, nowa_im)

    def __sub__(self, inna):
        nowa_re = self.re - inna.re
        nowa_im = self.im - inna.im
        return LiczbaZespolona(nowa_re, nowa_im)

    def __str__(self):
        return "{}{}{}i".format(self.re, "+" if self.im >= 0 else "-", abs(self.im))

if __name__ == "__main__":
    z1 = LiczbaZespolona(4, 5)
    z2 = LiczbaZespolona(3, -2)

    suma = z1 + z2
    print(f"Suma: {suma}")

    roznica = z1 - z2
    print(f"Różnica: {roznica}")
