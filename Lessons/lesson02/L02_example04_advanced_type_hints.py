# Referensexempel: mer avancerade typannoteringar. Överkursmaterial.
#
# Allt i den här filen är frivillig läsning och inte obligatoriskt kursmaterial.
# Du behöver inte kunna skriva eller använda de här annoteringarna för att följa
#     Lektion 02 eller senare workshops. Läs en del i taget om du är nyfiken.

# Vissa av dessa kanske kommer att dyka upp i senare lektioner. Vi kommer att
#   gå igenom dem då om de gör det.

# DISCLAIMER: I överkursmaterial använder jag AI som hjälpreda för att spara tid.

# Den här raden måste ligga högst upp i filen, efter dokumentationssträngen.
# Den gör att Python sparar typannoteringar för senare tolkning i stället för
#   att försöka slå upp alla namn direkt. Därför kan Classroom nämna Student
#   innan klassen Student har definierats längre ned i filen.
#
# Importen ändrar inte programmets vanliga beteende och kontrollerar inga typer.
# Den används främst i filer med många typannoteringar och är inte ett krav här.
from __future__ import annotations

from typing import (
    Annotated,
    Any,
    Callable,
    Generic,
    Iterable,
    Literal,
    NewType,
    Optional,
    Protocol,
    Sequence,
    TYPE_CHECKING,
    TypeAlias,
    TypeGuard,
    TypeVar,
    TypedDict,
    overload,
)


# TYPE_CHECKING är False när programmet körs och True för ett verktyg som
#   kontrollerar typer. Kod här inne körs alltså inte av programmet. Det är
#   användbart för import eller information som bara typkontrollen behöver.
if TYPE_CHECKING:
    type_checker_note: str = "Typkontrollen läser den här raden."


# En framåtreferens är ett klassnamn som används innan klassen har definierats.
# Citattecknen runt Student gör namnet till text. Med framtidsimporten ovan
#   behövs inte citattecknen, men de visas här för att göra idén tydlig.
def copy_student(student: "Student") -> "Student":
    """Returnerar samma elev."""
    return student


# 1. Namn på typer

# TypeAlias ger ett långt typuttryck ett kortare, beskrivande namn. Det ändrar
#   inte värdet scores; namnet gör bara annoteringen lättare att läsa.
ScoresByStudent: TypeAlias = dict[str, list[tuple[str, int]]]
scores: ScoresByStudent = {"Ada": [("ord", 10)]}

# I tuple[str, ...] anger ... att tuplen kan innehålla valfritt många
#   strängar. Det skiljer sig från tuple[str, int], som har exakt två värden.
words: tuple[str, ...] = ("apa", "banan", "citron")

# NewType ger typkontrollen ett nytt, särskilt namn för samma sorts värde.
# Här är både StudentId(1) och 1 heltal när programmet körs. Skillnaden syns
#   främst för typkontrollen: den kan varna om ett vanligt tal skickas till en
#   funktion som uttryckligen vill ha ett elev-id.
#
# Detta kan vara användbart när flera heltal betyder olika saker, till exempel
#   ett elev-id och en poäng. NewType validerar inte värdet och gör inte om det
#   till ett säkrare heltal. Det beskriver bara avsikten tydligare.
StudentId = NewType("StudentId", int)
student_id: StudentId = StudentId(1)

# TypedDict beskriver vilka nycklar och värdetyper en ordbok förväntas ha.
class StudentRecord(TypedDict):
    name: str
    score: int


student_record: StudentRecord = {"name": "Ada", "score": 10}

# Literal begränsar ett värde till exakt de strängar som står mellan
#   hakparenteserna.
difficulty: Literal["grund", "extra"] = "grund"

# Annotated lägger metadata bredvid en vanlig typ. Grundtypen är fortfarande
#   int, så typkontrollen behandlar points som ett heltal. Texten efter kommat är
#   bara extra information. Python kontrollerar inte automatiskt att värdet är
#   noll eller högre.
#
# Annotated används när ett särskilt bibliotek väljer att läsa metadata, till
#   exempel för validering eller dokumentation. Utan ett sådant bibliotek har
#   texten ingen effekt när programmet körs.
points: Annotated[int, "Bör vara noll eller högre"] = 10

# Any betyder att typkontrollen inte kontrollerar den här variabelns typ.
unknown_value: Any = "ett värde som kan ha vilken typ som helst"


# 2. Vad en funktion behöver kunna göra

# Iterable[str] betyder "något som går att loopa över och ger strängar".
# En lista, tuple, mängd och sträng är iterable. Funktionen får bara förutsätta
#   att en for-loop fungerar; den får inte förutsätta att len() eller [0] fungerar.
def print_words(words: Iterable[str]) -> None:
    """Skriver ut varje ord."""
    for word in words:
        print(word)


# Sequence[str] är mer specifikt än Iterable[str]. En sequence har ordning,
#   kan mätas med len() och kan läsas med ett index som [0]. Listor, tupler och
#   strängar är sequences, men en mängd (set) är inte det eftersom den saknar ordning.
# Optional[str] betyder samma sak som str | None, men är en äldre skrivform.
def first_word(words: Sequence[str]) -> Optional[str]:
    """Returnerar det första ordet eller None om samlingen är tom."""
    if len(words) == 0:
        return None
    return words[0]


# Callable[[str], str] beskriver något som kan anropas som en funktion.
# De första hakparenteserna innehåller argumenttyperna: här exakt en sträng.
# Typen efter kommat är returtypen: här en sträng. str.upper passar alltså,
#   eftersom "apa".upper() returnerar en sträng.
Formatter: TypeAlias = Callable[[str], str]


def format_word(word: str, formatter: Formatter) -> str:
    """Använder en funktion som har skickats in som argument."""
    return formatter(word)


# 3. Typer som anpassas efter ett värde

# TypeVar och Generic gör att Box kan lagra flera olika typer och ändå komma
#   ihåg vilken typ varje enskild Box har. Detta är främst hjälp för
#   typkontrollen; Python ändrar inte värdet som lagras.
ValueType = TypeVar("ValueType")


class Box(Generic[ValueType]):
    def __init__(self, value: ValueType) -> None:
        self.value: ValueType = value


number_box = Box(42)
letter_box = Box("A")


# Protocol beskriver vilka attribut ett objekt behöver ha, utan att objektets
#   klass behöver ärva från Protocol. Här räcker det att objektet har name: str.
class HasName(Protocol):
    name: str


def display_name(person: HasName) -> None:
    """Skriver ut namnet från ett objekt med attributet name."""
    print(person.name)


# 4. Klass som nämns före sin definition

# Student används här innan klassen Student står i filen. Framtidsimporten
#   högst upp gör att annoteringarna kan vänta tills Student finns. Det är en
#   framåtreferens, inte ett sätt att skapa ett Student-objekt.
class Classroom:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)


class Student:
    def __init__(self, name: str) -> None:
        self.name: str = name


# 5. Flera beskrivningar av samma funktion

# overload ger typkontrollen flera tillåtna anropssätt. Raderna med ... är bara
#   typkontrollens beskrivningar, inte funktioner som körs. Den riktiga funktionen
#   är definitionen utan @overload längst ned i detta block.
@overload
def format_score(value: int) -> str: ...


@overload
def format_score(value: float) -> str: ...


def format_score(value: Any) -> str:
    """Gör om ett poängtal till en sträng."""
    return str(value)

format_score("2")


# TypeGuard talar om för typkontrollen vad som är sant om funktionen returnerar
#   True. Funktionen kontrollerar fortfarande själv varje värde med isinstance().
# TypeGuard ändrar inte listan och gör ingen automatisk kontroll utanför denna
#   funktion. Efter if-satsen kan typkontrollen behandla word_values som list[str].
def is_word_list(values: list[Any]) -> TypeGuard[list[str]]:
    """Kontrollerar om alla värden i listan är strängar."""
    return all(isinstance(value, str) for value in values)


word_values: list[Any] = ["apa", "banan"]
if is_word_list(word_values):
    print_words(word_values)