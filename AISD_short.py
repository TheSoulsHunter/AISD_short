import graphs
import qlos
from qlos import quick
from graphs import Graph_M


def grafy():
    print("Wprowadz graf w postaci macierzy:")
    macierz = []
    s = input().split()
    while (len(s) != 0):

        s = list(map(int, s))
        macierz.append(s)
        s = input().split()

    print(macierz)
    w = len(macierz)
    Matrix = Graph_M(w)
    Matrix.graph = macierz
    print(Matrix.graph)
    print("Wybierz:")
    print("1.Topological sort \n2.MST \n3.One Euler \n4.One Hamilton \n5.All Hamiltons \n")
    co = int(input())
    if co == 1:
        Matrix.topologicalSort()
    if co == 2:
        Matrix.primMST()
    if co == 3:
        Matrix.euler_finder()
    if co == 4:
        Matrix.hamilton_finder()
    if co == 5:
        Matrix.hamilton_finder_all()


def qui():
    print("Podaj liste (po spacji)")
    tab = input().split()
    tab = list(map(int, tab))
    piw = int(input("Podaj indeks piwotu(tablica indeksowana od 1):   ")) - 1
    tab = quick(tab, piw)
    tab.quicksort(tab.A)


def main():
    print("1. Grafy. 2.Quick\n")
    print("Wybierz program: ", sep="", end="")
    program = int(input())
    if program == 1:
        grafy()
    if program == 2:
        qui()
    """print(
        "Wybierz sposób wprowadzania danych [tabela/lista] [t/l]: ", sep="", end="")"""
    # sposob=input()


main()
