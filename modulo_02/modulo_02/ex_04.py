while True:
    try:
        n = int(input("Digite um número: "))
        n1 = int("Digite -1 para pousar. ")

    except ValueError:
        print("erro")

        if n == -1:
            print(n)