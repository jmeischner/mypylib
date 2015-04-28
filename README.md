# MyPy Lib
Soll eine Ansammlung an Modulen werden, mit deren Hilfe einfache Aufgaben schneller gelöst werden können. Es enthält bis jetzt die folgenden Module:
1. **File**:
- zum ein- und auslesen von einfachen Textdateien
- zum ein- und auslesen von *JSON* Dateien
2. **Logger**:
- einfacher Decorator zum loggen von Funktionsaufrufen
3. **Shell**:
- *help_option*: Decorator zur Angabe von Funktionsargumenten die per Kommandozeile übergeben werden können und einem *--help* Menü zu Anzeige dieser

## Weiter Ideen
1. Shell
	- In den Decorator kann ein weiteres Objekt übergeben werden, welches die Funktionsbeschreibung und den Namen der Funktion enthält, oder ein weiteres Objekt wird dafür angelegt um für ein Skript mit mehreren Funktionen eine Hilfe der enthaltenen Funktionen zur Verfügung zu stellen.