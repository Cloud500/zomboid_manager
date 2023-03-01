Functions
=========

Manager
-------

- Verwalte mehrere Server unabhängig ob "local" oder auf anderem Server
- Verwalten von mehreren Server Configs
- Verwalten von mehreren Sandbox Configs
- Verwalten von mehreren Spawn regions
- Verwalten von mehreren "Modsets"
- News/Informationen Verwalten
- Bug/Ticket System
    - Prüfen ob das vom Spiel genutzt werden kann
- Verwalten der Server per RCRON
    - Neu Starten
    - Backup erstellen
    - User manage
    - etc.
- Syncen der Configs mit dem Server (per REST?)
- REST API zur kommunikation mit den Servern

Mods
""""
Da Workshop Mods mehrere Mods und Maps enthalten können, werden die Mods Gelistet und nicht die Workshop's
bzw. "primäre" Tabelle sollte Mod und nicht Workshop sein.

- Benötigte Infos
    - Workshop ID
    - Mod ID
    - Name
    - Abhängige Mods
    - Link zum Worksop
    - Thumbnail

Maps
""""
Wenn wir die Zellen mit auflisten können wir super die Kompatibilität prüfen und überlappungen finden unf ggf.
mit ladereihenfolge korrigieren

- Benötigte Infos
    - Map ID
    - Zugehöriger Mod
    - Belegte Zellen

----------

Game server helper
------------------

- Läuft lokal auf dem Server
- REST API zur kommunikation mit dem Manager
- Lesen und auswerten von Logs und andern daten des Servers
- Senden der Information an den Manager
- Empfangen der Informationen vom Manager

----------

Game Mod
--------

- Vergeben einer UUID für jeden Charakter
- Schreiben der Informationen in die modData Tabelle des Charakters
- Regelmäßiges update der Daten welche der helper beobachtet
- Charakter Informationen die gesammelt/ausgegeben werden
    - UUDI
    - Vorname
    - Nachname
    - Geschlecht
    - Fähigkeiten
    - Getötete Zombies
    - Traits
    - Beruf
    - Online
    - Offline
    - Todesart
    - ❓Ist Zombie geworden
    - ❓Zombie getötet von/durch oder noch am Leben

- Events und die daten
    - tba