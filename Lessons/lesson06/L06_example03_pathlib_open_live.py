# Exempel på hur man kan använda pathlibs Path-objekt.

from pathlib import Path

windows_path = Path("test\\test.txt")
windows_open = windows_path.open()

unix_linux_macos_path = Path("test/test.txt")
unix_linux_macos_open = open(unix_linux_macos_path)

print(windows_open.read())
print(unix_linux_macos_open.read())

windows_open.close()
unix_linux_macos_open.close()

print("------")
print(windows_path.read_text(encoding="utf-8"))