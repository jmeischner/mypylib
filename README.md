# MyPy Lib
Soll eine Ansammlung an Modulen werden, mit deren Hilfe einfache Aufgaben schneller gelöst werden können. Es enthält bis jetzt die folgenden Module:

1. **File**:
- zum ein- und auslesen von einfachen Textdateien
- zum ein- und auslesen von *JSON* Dateien
2. **Logger**:
- einfacher Decorator zum loggen von Funktionsaufrufen
3. **Shell**:
- *help_option*: Decorator zur Angabe von Funktionsargumenten die per Kommandozeile übergeben werden können und einem *--help* Menü zu Anzeige dieser

Um diese Module überall importieren zu können, muss der **PYTHONPATH** erweitert werden. Dies geschieht in der *~/.bash_profile* Datei. Ich habe diese Bibliothek in den Ordner *~/.bin* gelegt, sollte sie woandern abgelegt werden, muss der *Path* dementsprechend anders aussehen
```bash
export PYTHONPATH="$PYTHONPATH:$HOME/.bin/mypylib"
``` 

## Weiter Ideen
