import multiprocessing

class SortowanieRownolegle:
    def __init__(self, dane):
        self.dane = dane

    def sortowanie_babelkowe(self, dane):
        n = len(dane)
        for i in range(n):
            for j in range(0, n-i-1):
                if dane[j] > dane[j+1]:
                    dane[j], dane[j+1] = dane[j+1], dane[j]
        return dane

    def counting_sort(self, dane):

        max_value = max(dane)
        min_value = min(dane)

        histogram = {}
        sorted_list = []

        for i in range(min_value, max_value + 1):
            histogram[i] = 0

        for i in dane:
            histogram[i] += 1

        for k, v in histogram.items():
            for i in range(v):
                sorted_list += [k]

        return sorted_list

    def sortuj(self, liczba_procesow=None):
        if liczba_procesow is None:
            liczba_procesow = multiprocessing.cpu_count()
        rozmiar_fragmentu = len(self.dane) // liczba_procesow
        fragmenty = [self.dane[i * rozmiar_fragmentu:(i + 1) * rozmiar_fragmentu] for i in range(liczba_procesow)]

        with multiprocessing.Pool(processes=liczba_procesow) as pool:
            posortowane_fragmenty = pool.map(self.sortowanie_babelkowe, fragmenty)

        posortowane_dane = []
        for fragment in posortowane_fragmenty:
            posortowane_dane.extend(fragment)

        return self.sortowanie_babelkowe(posortowane_dane)

if __name__ == "__main__":
    dane_do_posortowania = [50, 23, 9, 18, 61, 32, 11, 24, 45, 67, 82, 2, 8, 18, 56, 44]
    print(dane_do_posortowania)
    sorter = SortowanieRownolegle(dane_do_posortowania)
    posortowane_dane = sorter.sortuj()
    print(posortowane_dane)
