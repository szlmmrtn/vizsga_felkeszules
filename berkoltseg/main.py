from printing import printing

netto_input = input("Kérem a nettó bért! ")

if netto_input.isnumeric():
    netto = float(netto_input)
    fajlbair = printing(netto)
    fajlbair.nyomtatas()

else:
    print("Számot adj meg! ")    


    