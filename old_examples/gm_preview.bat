@ECHO off

WHERE /Q gm.exe

IF ERRORLEVEL 1 (
	START "\\\kps-datencenter\3d-Daten\Software\GraphicsMagick-1.3.30-Q16-win64-dll.exe"
	ECHO Bitte nach der Installation von Graphicsmagick die Batch-Datei erneut ausfuehren.
	PAUSE
	EXIT
)

ECHO Die Verarbeitung ist gestartet ...
ECHO.

ECHO Die 512 Pixel Variante wird erstellt ...

gm.exe mogrify -output-directory ../512/ -create-directories -strip -trim -resize "512x512>" -quality 80 *.jpg

ECHO ... und ist auch bereits fertig verarbeitet.
ECHO.

CD ../512

ECHO Die 150 Pixel Variante wird erstellt ...

gm.exe mogrify -output-directory ../150/ -create-directories -resize "150x150>" *.jpg

ECHO ... und ist auch bereits fertig verarbeitet.

ECHO.
ECHO.
ECHO Die Verarbeitung ist beendet und dieses Fenster wird in Kuerze geschlossen ...

PING -n 3 127.0.0.1>NUL

EXIT
