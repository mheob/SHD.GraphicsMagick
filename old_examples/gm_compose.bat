@ECHO off

WHERE /Q gm.exe

IF ERRORLEVEL 1 (
	START "\\\kps-datencenter\3d-Daten\Software\GraphicsMagick-1.3.30-Q16-win64-dll.exe"
	ECHO Bitte nach der Installation von Graphicsmagick die Batch-Datei erneut ausfuehren.
	PAUSE
	EXIT
)

SET INPUT=
SET /P INPUT=Bitte den Speicherort angeben (Ordner reicht): 

MKDIR "..\%INPUT%"

ECHO.
ECHO Die Verarbeitung ist gestartet ...
ECHO.

FOR %%f in (*.jpg) do (
	gm composite -gravity northeast "..\Vorlagen\New_256x256.png" "%%f" "..\%INPUT%\%%f"
)

ECHO.
ECHO Die Verarbeitung ist beendet und dieses Fenster wird in Kuerze geschlossen ...
PING -n 3 127.0.0.1>NUL
EXIT
