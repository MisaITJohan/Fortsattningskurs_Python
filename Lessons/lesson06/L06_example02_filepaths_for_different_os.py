# Exempel på hur sökvägar kan skilja sig åt mellan operativsystem.
# Nu för tiden så klarar Python av att tolka dessa utan problem men dessa hade
# inte fungerat på alla operativsystem tidigare.

windows_path = open("test\\test.txt")
unix_linux_macos_path = open("test/test.txt")

print(windows_path.read())
print(unix_linux_macos_path.read())