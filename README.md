# README

Hier finden sich verschiedene technische Notizen für das Erstellen der
Arbeit.

## Arbeit mit Sub-Files

m4 is a general-purpose macro processor that comes pre-installed on most
Unix-like systems (including Linux and macOS). It's a powerful tool that
reads input, copies it to output, and expands macros along the way. 

Key features of m4:

1. Text substitution: It can replace text patterns with other text.
2. Built-in macros: It comes with a set of predefined macros for common
   operations. 
3. User-defined macros: You can create your own macros.
4. File inclusion: It can include the contents of other files.
5. Conditional processing: It supports if-else like constructs.

Basic usage for file inclusion:

1. In your main Markdown file, you can use:
   ```
   include(file.md)
   ```

2. Then process your file with m4 before passing it to Pandoc:
   ```
   m4 main.md | pandoc -o output.pdf
   ```

A simple example:

1. Create a file named `chapter1.md`:
   ```markdown
   # Chapter 1
   This is the content of chapter 1.
   ```

2. Create your main file `book.md`:
   ```markdown
   # My Book
   
   include(chapter1.md)
   
   # Chapter 2
   This is chapter 2.
   ```

3. Process with m4 and Pandoc:
   ```
   m4 book.md | pandoc -o book.pdf
   ```

## Verwendung von pandoc zur Erstellung des PDF

```powershell
 pandoc .\docs\sections\einleitung.md .\docs\sections\verzeichnisse.md .\docs\sections\computational_thinking.md .\docs\sections\arbeitshypothese.md .\docs\sections\methode.md .\docs\sections\kern.md .\docs\sections\daten.md .\docs\sections\auswertung.md .\docs\sections\ausblick.md .\docs\sections\reflexion.md .\docs\sections\literatur.md .\docs\sections\import_code.md --number-sections --filter pandoc-crossref --metadata-file='G:\Meine Ablage\Studium\impactofct\docs\layout.yaml' --citeproc -o docs/240808_fahne.pdf --pdf-engine=xelatex --highlight-style=pygments
```

Wichtig ist die Reihenfolge der Argumente. `--number-sections` muss vor
`--filter pandoc-crossref` muss vor `--metadata-file` muss vor
`--citeproc` stehen.

Die verarbeiteten Dateien stehen neu am Ende der Datei layout.yaml.

Der Befehl für die Konvertierung lautet daher:

```pwoershell
 pandoc (yq e '.input-files[]' 'G:\Meine Ablage\Studium\impactofct\docs\layout.yaml') --number-sections --filter pandoc-crossref --metadata-file='G:\Meine Ablage\Studium\impactofct\docs\layout.yaml' --citeproc -o docs/240808_fahne.pdf --pdf-engine=xelatex --highlight-style=pygments
```

## Git Einstellungen mit verschiedenen Accounts

Damit der Accountauswahl Dialog bei git push nicht jedesmal durchlaufen
werden muss, gibt es hier 
[eine
Anleitung](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/multiple-users.md) 
für das Set Up.

## Rendering mit Quarto

Um das Schlussresultat mit Quarto zu rendern, muss das ganze Verzeichnis
auf einem lokalen Laufwerk gespeichert sein. Zudem muss der Dokumentpfad
für die Grafiken auf ../graphics/bild.svg und die Querverweise auf
#fig-bild bzw. @fig-bild angepasst werden.

## Einstellungen für den Zotero Export

BetterBibTeX Einstellungen anpassen:
a) Öffnen Sie Zotero
b) Gehen Sie zu Bearbeiten > Einstellungen > BetterBibTeX
c) Wählen Sie den Reiter "Export"
d) Suchen Sie die Option "Title casing" oder "Groß-/Kleinschreibung des Titels"
e) Ändern Sie diese Einstellung auf "As is" oder "Wie eingegeben"