import csv

with open(r'C:\Users\kurs\PycharmProjects\bootcampPS\Zjazd4\praca_z_plikami\pliki_wejsciowe\sales.csv') as f:
    #dane = csv.reader(f)
    dane = csv.DictReader(f)

    revenue_sum = 0
    revenue_counter = 0
    quant_sum = 0
    quant_counter = 0
    gm_sum = 0
    gm_counter = 0

    for row in dane:
        revenue_sum += float(row['Revenue'])
        revenue_counter += 1
        revenue_mean = revenue_sum/revenue_counter
    print(revenue_mean)

    for row in dane:
        if row
        quant_sum += float(row['Quantity'])
        quant_counter += 1

    print(quant_sum/quant_counter)

    # for row in dane:
    #     gm_sum += float(row['Gross margin'])
    #     gm_counter += 1
    #     gm = gm_sum/gm_counter
    # print(gm)