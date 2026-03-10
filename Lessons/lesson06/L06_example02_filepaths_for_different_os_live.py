# Exempel på hur sökvägar kan skilja sig åt mellan operativsystem.
# Nu för tiden så klarar Python av att tolka dessa utan problem men dessa hade
# inte fungerat på alla operativsystem tidigare.

windows_path = "test\\test.txt"
windows_open = open(windows_path)

unix_linux_macos_path = "test/test.txt"
unix_linux_macos_open = open(unix_linux_macos_path)

print(windows_open.read())
print(unix_linux_macos_open.read())

windows_open.close()
unix_linux_macos_open.close()
