# Kör detta program i IDLE eller en terminal istället för PyCharm, PyCharm
# tvingar ett program att avsluta om man säger stop två gånger.

# Detta program kommer inte acceptera kommandot ctrl-c (cmd-c), vilket
# är kommandot för en KeyboardInterrupt, ett sätt för användaren att avbryta
# ett Pythonprogram.

while True:
    try:
        x = input("Skriv in ett värde som ska skrivas ut: ")
        print(x)
    except:
        print("Fångade ett fel! Hurra!")
