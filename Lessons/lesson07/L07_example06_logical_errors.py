# Ingenting av följande kod gör att programmet slutar fungera på ett sätt som
# skapar ett felmeddelande, kraschar eller visar något tydligt fel, men det finns
# logiska fel som orsakar problem.

# Exempel 1, beräkna fel genomsnitt :

x = 10
y = range(x)
sum = 0
for number in y:
    sum += number
average = sum / x
print(sum)
print(average)

# Vi kanske tror att vi räknar ut genomsnittet av alla siffror mellan ett till tio
# men range() börjar per standard från noll.


# Exempel 2, felaktig jämförelse:

x = 10

if x < 5 and x > 8:
    print(f"x är mindre än 5 eller större än 8 och är: {x}")

# Säg att vi vill garantera att x aldrig är 6 eller 7, då gör den här koden
# det helt motsatta.
# Visst, detta exempel kanske är relativt enkelt att upptäcka, men tänk om
# jämförelsen hade haft flera klausuler. Då kan det lätt bli att man råkar göra ett
# misstag.