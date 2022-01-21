<b>Einführung</b><br>
Dieses Projekt entstand im Rahmen des Moduls Programmierung 2.
Dieses Modul dient dazu den Studierenden Erfahrung 
in der Programmierung und eine praktische Einsicht 
in den Softwareentwicklungsprozess zu geben.<br>

<b>Projektidee "Lucas Garten"</b><br>
Die Idee des Projektes ist eine Software, die einen
Pflanzengiessplan erstellen soll. <br>

<b>Datenspeicherung</b><br>
Mittels Formular auf der Seite "Pflanze hinzufügen" werden neue Pflanzen in die Datenbank "pflanzendaten.json" aufgenommen.
Folgende Daten werden erfasst:
- Pflanze
- Abstand an Tagen, an welchen sie gegossen werden soll
- Menge an Wasser
- Sonstige Bemerkungen (z.B. Pflanzendünger verwenden)

Die Software hat zwei json-files: Die Zweite namens "aufgaben.json" wird im nächsten Abschnitt erklärt.

<b>Datenausgabe</b><br>
Alle erfassten Pflanzen werden auf der Seite "Mein Garten" dargestellt 
und dient der Übersicht. Die Seite "Heutige Aufgaben" gibt alle Pflanzen wider, 
welche an dem heutigen Tag gegossen werden sollen. Diese Daten werden aus der Hauptdatenbank "pflanzendaten.json" geholt und
in eine neue Datenbank "aufgaben.json" eingespeisst - nach Berechnung des Datums und der sogenannten "Giessabstandstagen".
Danach werden die zu giessenden Pflanzen in einer Tabelle dargestellt, welche dann als "Erledigt" markiert werden können.
Falls man diese als erledigt markiert, werden sie aus "aufgaben.json" gelöscht und das Datum in "pflanzendaten.json"
auf den heutigen Tag geändert. Somit kann die Software wieder mit den "Giessabstandstagen" vom heutigen Tag aus rechnen.<br>

<b>Ablaufdiagramm</b><br><br><br>
<img src="C:\Users\lucab\OneDrive\Bureau\Studium\21HS\Programmierung 2\pythonProject\images\Lucas_Garten.jpg"/><br><br>

<b>Mögliche Erweiterungen</b><br>
Mögliche Erweiterungen der Software könnten z.B. eine "Statistik"-Seite sein,
welche anzeigt, wie viel Wasser schon gebraucht wurde. Dazu könnte man noch
eine "Verpasste Giessungen"-Seite machen, welche bei einem Giessversäumnis der Pflanzen dort angezeigt wird.