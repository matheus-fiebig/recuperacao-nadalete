pais_A = 15000
pais_B = 45000
taxa_A = 10/100
taxa_B = 5/100

anos1 = 0

while True:
    pais_A += pais_A*taxa_A
    pais_B += pais_B*taxa_B
    anos1 += 1
    if pais_A >= pais_B:
        break
print (f"A população A igualou ou ultrapassou a população B em {anos1} anos")



pais_A = 15000
pais_C = 65000
taxa_A = 10/100
taxa_C = 2.5/100

anos2 = 0

while True:
    pais_A += pais_A*taxa_A
    pais_C += pais_C*taxa_C
    anos2 += 1
    pais_c_23 = pais_C*(23/100)
    if pais_A > pais_C+pais_c_23:
        break
print (f"A população A ultrapassou a população C em 23% em {anos2} anos")
