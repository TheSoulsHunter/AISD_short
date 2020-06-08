def dynamic():
    waga = list(map(int, input("wagi:").split()))
    wartosc = list(map(int, input("wartosci:").split()))
    pojemnosc = int(input("pojemnosc:"))
    l_kontenerow = len(waga)
    tabela = [[0 for x in range(pojemnosc + 1)]
              for y in range(l_kontenerow + 1)]
    for i in range(1, l_kontenerow + 1):
        for j in range(1, pojemnosc + 1):
            if j < waga[i - 1]:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i - 1]
                [j - waga[i - 1]] + wartosc[i - 1])
        print(tabela[i])
    print(tabela[l_kontenerow][pojemnosc], end=";")
