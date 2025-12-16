# Ingenting av följande kod gör att programmet slutar fungera på ett sätt som
# skapar ett felmeddelande, kraschar eller visar något tydligt fel, men det finns
# logiska fel som orsakar problem.

# Exempel 1, beräkna fel genomsnitt:

x = 10
y = range(x)
sum_ = 0

for number in y:
    print(number)
    sum_ += number
average = sum_ / x
print(sum_)
print(average)

# Vi kanske tror att vi räknar ut genomsnittet av alla siffror mellan ett och 10
# men range() börjar per standard från noll och tar inte med det tal som man
# skickar som argument.


# Exempel 2, felaktig jämförelse:

x = 10

if not x > 5 and not x < 8:  # Detta borde vara "not (x > 5 and x < 8)" alternativt "5 < x < 8"
    print(f"x är mindre än fem eller större än 8 och x är: {x}")

# Säg att vi vill garantera att x aldrig är 6 eller 7, nu har vi dock råkat
# göra att koden aldrig körs istället.
# Visst, detta exempel kanske är relativt lätt att upptäcka, men tänk om
# jämförelsen hade haft flera klausuler. Då kan det lätt bli att man råkar göra
# ett misstag.