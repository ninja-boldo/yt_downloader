# Video Downloader 🎬

Ein einfaches Tool zum Herunterladen von Videos auf deinen Computer.

## Was macht dieses Programm?

Mit diesem Programm kannst du:
- 📹 Videos herunterladen
- 🎵 Nur den Ton (Audio) von Videos speichern
- 🔗 Mehrere Videos zu einem zusammenfügen
- 📝 Videos automatisch in Text umwandeln (Transkription)

---

## 📥 Schritt 1: Programm herunterladen

Du hast zwei Möglichkeiten, das Programm auf deinen Computer zu bekommen:

### Option A: Als ZIP-Datei herunterladen (Einfacher)

1. Öffne diese Seite in deinem Browser: https://github.com/ninja-boldo/yt_downloader
2. Klicke auf den grünen Button **"Code"** (oben rechts)
3. Wähle **"Download ZIP"**
4. Speichere die ZIP-Datei auf deinem Computer
5. Entpacke die ZIP-Datei:
   - **Windows**: Rechtsklick auf die Datei → "Alle extrahieren"
   - **Mac**: Doppelklick auf die Datei
6. Du hast jetzt einen Ordner namens `yt_downloader-main`

### Option B: Mit Git herunterladen (Für Fortgeschrittene)

Falls du Git installiert hast, öffne ein Terminal/Eingabeaufforderung und tippe:

```bash
git clone https://github.com/ninja-boldo/yt_downloader.git
```

---

## 🐍 Schritt 2: Python installieren

Dieses Programm braucht Python zum Laufen. Falls du Python noch nicht hast:

### Windows:
1. Gehe zu https://www.python.org/downloads/
2. Klicke auf "Download Python" (gelber Button)
3. Öffne die heruntergeladene Datei
4. **Wichtig:** Setze den Haken bei "Add Python to PATH" ✅
5. Klicke auf "Install Now"

### Mac:
1. Gehe zu https://www.python.org/downloads/
2. Klicke auf "Download Python"
3. Öffne die heruntergeladene Datei und folge den Anweisungen

### Prüfen ob Python installiert ist:
Öffne ein Terminal/Eingabeaufforderung und tippe:
```bash
python --version
```
Es sollte eine Versionsnummer angezeigt werden (z.B. `Python 3.11.4`).

---

## 📦 Schritt 3: Benötigte Pakete installieren

Bevor du das Programm nutzen kannst, musst du einige Pakete installieren.

1. Öffne ein Terminal/Eingabeaufforderung
2. Navigiere zum Ordner des Programms:
   ```bash
   cd pfad/zum/yt_downloader
   ```
   (Ersetze `pfad/zum/yt_downloader` mit dem tatsächlichen Pfad)

3. Installiere die benötigten Pakete:
   ```bash
   pip install pytubefix
   ```

**Optional** (falls du Videos transkribieren möchtest):
```bash
pip install pywhispercpp
```

**Optional** (falls du Videos zusammenfügen möchtest):
Du brauchst FFmpeg. Installation:
- **Windows**: Lade FFmpeg von https://ffmpeg.org/download.html herunter
- **Mac**: Mit Homebrew: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

---

## 🚀 Schritt 4: Das Programm benutzen

### Methode 1: Direkt in main.py URLs eintragen

1. Öffne die Datei `main.py` mit einem Texteditor (z.B. Notepad)
2. Finde diese Zeile:
   ```python
   urls = ["https://www.youtube.com/watch?v=cSOQPJl53Ng", "https://www.youtube.com/watch?v=34mk2F4iff4"]
   ```
3. Ersetze die URLs mit deinen gewünschten YouTube-Links
4. Speichere die Datei
5. Führe das Programm aus:
   ```bash
   python main.py
   ```

### Methode 2: In Python direkt nutzen

Du kannst das Programm auch in deinen eigenen Python-Skripten verwenden:

```python
from fetch import downloader

# Erstelle einen Downloader
dl = downloader()

# Ein einzelnes Video herunterladen (nur Audio)
dl.download("https://www.youtube.com/watch?v=DEIN_VIDEO", only_audio=True)

# Mehrere Videos herunterladen (mit Video)
videos = [
    "https://www.youtube.com/watch?v=VIDEO1",
    "https://www.youtube.com/watch?v=VIDEO2"
]
dl.download(videos, only_audio=False)
```

---

## 📁 Wo werden die Videos gespeichert?

Die heruntergeladenen Videos findest du im Ordner `downloaded_videos` innerhalb des Programmordners.

---

## ❓ Häufige Probleme

### "pip wird nicht erkannt"
→ Python wurde nicht zum PATH hinzugefügt. Installiere Python neu und setze den Haken bei "Add Python to PATH".

### "ModuleNotFoundError: No module named 'pytubefix'"
→ Du hast die Pakete noch nicht installiert. Führe `pip install pytubefix` aus.

### Das Video wird nicht heruntergeladen
→ Manche Videos sind geschützt und können nicht heruntergeladen werden. Probiere ein anderes Video.

### "FFmpeg not found"
→ FFmpeg ist nicht installiert. Siehe Schritt 3 für die Installation.

---

## ⚠️ Wichtiger Hinweis zum Urheberrecht

**Bitte beachte:** Das Herunterladen von Videos ist nur erlaubt, wenn:
- Du die Erlaubnis des Urhebers hast
- Das Video unter einer freien Lizenz (z.B. Creative Commons) steht
- Es sich um deine eigenen Videos handelt
- Du das Recht hast, das Video privat zu nutzen

**Lade keine urheberrechtlich geschützten Inhalte ohne Erlaubnis herunter!**

---

## 📜 Lizenz

Dieses Projekt ist kostenlos und frei verwendbar.

---

## 💡 Tipps

- Bei langen Videos kann der Download etwas dauern
- Die Audio-Option (`only_audio=True`) spart Speicherplatz
- Achte immer auf das Urheberrecht!

---

Bei Fragen oder Problemen erstelle gerne ein Issue auf GitHub! 😊
