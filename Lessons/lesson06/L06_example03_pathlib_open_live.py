# Exempel på hur sökvägar kan skilja sig åt mellan operativsystem.
# Nu för tiden så klarar Python av att tolka dessa utan problem men dessa hade
# inte fungerat på alla operativsystem tidigare.
from pathlib import Path
import pathlib


windows_path = Path("test\\test.txt")
windows_open = windows_path.open()

unix_linux_macos_path = Path("test/test.txt")
unix_linux_macos_open = open(unix_linux_macos_path)

print(windows_open.read())
print(unix_linux_macos_open.read())

windows_open.close()
unix_linux_macos_open.close()