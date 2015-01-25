PyBlendEffects
============

OOS ESA3

URL zum Repository
https://github.com/AndreMommert/PyBlendEffects

Gruppenmitglieder:
Reinsch: reinschs@fh-brandenburg.de
Walther: patrick.walther.1989@gmx.de
Mommert: mommert@fh-brandenburg.de

Beschreibung
Das Projekt zielt auf zwei Aspekte ab. Zum einen Automatisierung von Blender und zum Anderen die Dokumentation von Handlungsschritten.

1) Automatisierung
Es soll eine Automatisierung von Blender mit Hilfe von Python erfolgen. Dadurch soll auch dem
Laien ermöglich werden, Schrift-Effekte zu generieren, die dann als fertiges Video gerendet werden.
Diese kurzen Videos können dann beispielsweise direkt auf eine Webseite eingebunden, oder
als Vorspann vor ein eigentliches Video gelegt werden.

2) Dokumentation
Unsere Applikation erstellt eine Animation von einem Effekt in Blender und
erstellt dazu eine Schritt für Schritt Anleitung zum nachbauen.
In Blender selbst hat man nach dem Ausführen der Applikation das fertige Ergebnis.
Die Schritt für Schritt Anleitung wird als HTML gespeichert und kann im Browser
angeschaut werden.

Vorraussetzung
Die Projektdateien sollten in relativer Nähe zum Verzeichnis liegen in dem sich Blender befindet.
Zur Ausführung muss dann dem Blender der Pfad zum Skript übergeben werden.

Ausführung
Um das Python Skript ausführen zu können, muss folgender Befehl (beispielhaft) ausgeführt werden:

./blender -P PyBlendEffects/pyblendeffects.py -- dissolve "hallo blender"

blender.exe -P PyBlendEffects/pyblendeffects.py -- dissolve "hallo blender"

Die Blenderanwendung muss auf der Kommandozeile mit den Parametern -P aufgerufen werden, anschließend folgt der Pfad zum
Skript. Danach wird der Effekt angegeben und der Text.