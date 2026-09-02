# Exempel på hur man använder typannoteringar (type hints) i Python.
# Typannoteringar gör koden lättare att läsa och hjälper din IDE (som PyCharm)
#   att hitta fel tidigare. Python bryr sig inte om dessa när programmet
#   körs, men de är till stor hjälp för oss programmerare då de kan förhindra
#   fel att uppstå genom att förhindra att man använder fel datatyper.

# 1. Variabler
# Man kan ange vilken typ en variabel förväntas ha genom att använda ett kolon.
age: int = 25
name: str = "Anna"
is_student: bool = True


# 2. Funktioner
# Man kan ange typer för argument (tekniskt sett är dessa parametrar) och vad
#   funktionen returnerar (med ->)
def create_greeting(user_name: str, user_age: int) -> str:
    """Skapar en hälsningsfras för en användare."""
    return "Hej " + user_name + "! Du är " + str(user_age) + " år gammal."

create_greeting("Johan", 36)


# 3. Klasser
# I klasser kan vi annotera både attribut och metoder.
class Product:

    def __init__(self, name: str, price: float) -> None:
        # Variablerna som skapas här har redan implicit fått sina typer annoterade
        #   i parametrarna men man kan ändå ange typerna explicit för att
        #   vara tydligare.
        self.name: str = name
        self.price: float = price

    def get_discounted_price(self, discount_percent: float) -> float:
        """Beräknar priset efter en procentuell rabatt."""
        discount_amount = self.price * (discount_percent / 100)
        return self.price - discount_amount


# Exempel på användning:

# Vi behöver inte, men vi kan om vi vill, annotera message nedan. Vi vet redan
#   att message är en sträng då det är vad create_greeting() returnerar.
message = create_greeting(name, age)
print(message)

# Skapar ett objekt av klassen Product
# Notera att my_product har annoterats med typen Product som vi skapade ovan.
my_product: Product = Product("Kaffe", 45.5)

# Beräknar rabatterat pris
new_price: float = my_product.get_discounted_price(10.0)

print("Det nya priset för", my_product.name, "är", new_price, "kr.")


# 4. Alternativa typer med |
# Ett lodrätt streck betyder "eller" i en typannotering. Typen str | None
#   betyder att variabeln antingen är en sträng eller None. None betyder här
#   att det inte finns någon hälsning att returnera.
# Syntaxen kräver Python 3.10 eller senare.
#   Tidigare behövde man använda Union[str, None] istället för str | None
#   Union behövde man importera från modulen typing.
#       from typing import Union

def find_greeting(user_name: str) -> str | None:
    """Returnerar en hälsning för Anna eller None för andra namn"""
    if user_name == "Anna":
        return "Hej Anna!"
    return None


greeting: str | None = find_greeting(name)
if greeting is not None:
    print(greeting)
else:
    print("Vi hälsar bara på Anna!")