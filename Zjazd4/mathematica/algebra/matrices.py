def add_matrices(X, Y):
    result = []

    for i in range(len(X)):

        row = []
    # iterate through columns
        for j in range(len(X[0])): #range(len(X[0]) bierze zakres bazujacy na dlugosci pierwszego elementu w matrycy X, czyli pierwszego wiersza. Rafal napisal zamiast 0 'i'
            element = X[i][j] + Y[i][j]
            row.append(element)
        result.append(row)

    return result

# def add_matrices_zip(X, Y):
#     result = []

    # for i in range(len(X)):
    #     row = []
    # # iterate through columns
    #     for j in range(len(X[0])): #range(len(X[0]) bierze zakres bazujacy na dlugosci pierwszego elementu w matrycy X, czyli pierwszego wiersza. Rafal napisal zamiast 0 'i'
    #         element = X[i][j] + Y[i][j]
    #         row.append(element)
    #     result.append(row)

def substract_matrices(X, Y):
    result = []

    for i in range(len(X)):
        row = []
    # iterate through columns
        for j in range(len(X[0])): #range(len(X[0]) bierze zakres bazujacy na dlugosci pierwszego elementu w matrycy X, czyli pierwszego wiersza. Rafal napisal zamiast 0 'i'
            element = X[i][j] - Y[i][j]
            row.append(element)
        result.append(row)

    return result