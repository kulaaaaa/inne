a="roquefort"
a1=12.50
b="stilton"
b1=11.24  
c="brie"
c1=9.30  
d="gouda" 
d1=8.55
e="edam" 
e1=11.00
f="parmezan" 
f1=16.50  
g="mozzarella"
g1=14.00 
h="czeski_ser_z_owczego_mleka"
h1=122.32
i="ser"
j="cena"
k="PLN/kg"
l="PLN"

list = f"Oto lista zakupów:\n {i} {a} {j} {a1} {k}\n {i} {b} {j} {b1} {k}\n {i} {c} {j} {c1} {k}\n {i} {d} {j} {d1} {k}\n {i} {e} {j} {e1} {k}\n {i} {f} {j} {f1} {k}\n {i} {g} {j} {g1} {k}\n {i} {h} {j} {h1} {k}\n"
print(list)

print('Aktualizacja listy zakupów:\n +2 kg roqueforta, +3,5 kg parmezanu, +130 dag mozzarelli, +220 dag sera owczego, oraz po +1 kg pozostałych oraz 200g listka miętowego\n')

m="listek miętowy"
m1=100
n="masa"
o="kg"

list2 = f"Raport zakupów:\n {i} {a} {n} 3 {o} {j} {a1*3} {l}\n {i} {b} {n} 2 {o} {j} {b1*2} {l}\n {i} {c} {n} 2 {o} {j} {c1*2} {l}\n {i} {d} {n} 2 {o} {j} {d1*2} {l}\n {i} {e} {n} 2 {o} {j} {e1*2} {l}\n {i} {f} {n} 4.5 {o} {j} {f1*4.5} {l}\n {i} {g} {n} 1.13 {o} {j} {round(g1*1.13,2)} {l}\n {i} {h} {n} 1.2 {o} {j} {round(h1*1.22,2)} {l}\n {m} {n} 0.2 {o} {j} {m1/5} {l}\n"

suma = a1*3 + b1*2 + c1*2 + d1*2 + e1*2 + f1*4.5 + g1*1.13 + h1*1.22 + m1/5
print(list2)
print("Suma:", round(suma,2), "zł")

