# Exempel på hur f-strängars enklaste användningsområde är.

# Så här kan det se ut om vi vill skriva ut någons ålder:
age = 34
print("Johan är " + str(age) + " år gammal.")

# Inte jättekrångligt, men det är otympligt och man bör inte förlita sig på
# strängkonkatenering.


# Om vi använder oss av en f-sträng så kan vi skriva så här:
print(f"Johan är {age} år gammal.")