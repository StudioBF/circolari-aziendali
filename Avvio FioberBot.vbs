Set WshShell = CreateObject("WScript.Shell")
' 0 = Hide Window, False = Do not wait for completion
WshShell.Run "pythonw telegram_publisher.py", 0, False
