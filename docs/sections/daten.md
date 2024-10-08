# Daten {#sec:daten}

In diesem Abschnitt sollen die ausgewerteten Daten näher beschrieben
werden. In einem ersten Teil wird die Stichprobe als Ganzes näher beschrieben und
in einem zweiten Teil die beiden Datensätze "Noten des EFZ"
und "Noten der BMS".

## Beschreibung der Stichprobe {#sec:stichprobe}

Die Kantonsschule Büelrain war die erste Kantonsschule, welche eine IMS
angeboten hat. Begonnen hat das Programm im Jahr 2000. Mittlerweile gibt
es 12 Standorte in der ganzen Deutschschweiz. Da die Schulbildung in der
Kompetenz der Kantone liegt, ergeben sich zum Teil erhebliche regionale
Unterschiede in den Zubringerschulen. Diese Unterschiede rechtfertigen
es, die Absolventen der IMS an der Kantonsschule Büelrain als
eigenständige Population zu verstehen.

Beim Start der IMS an der Kantonsschule Büelrain 
waren die Klassen etwas grösser als sie es aktuell sind. Damit kann die
Gesamtpopulation von Absolventen der IMS an der Kantonsschule Büelrain
bis 2022 auf zwischen 350 und 400 geschätzt werden. Die
Stichprobengrösse ist daher etwas kleiner als 50% der gesamten
Population.

Die Daten umfassen Noten von insgesamt 167 Lernenden. 12 davon sind
Frauen. Das Durchschnittsalter zum Zeitpunkt der BMS Prüfungen betrug
19.2 Jahre. Der jüngste Lernende war 17 Jahre alt, der älteste 22. Die
Standardabweichung liegt beim Alter bei 0.9 Jahren.
Die Stichprobe besteht aus allen Lernenden des Beobachtungszeitraums von
2009 bis 2022. Aufgrund der Schuldauer von drei Jahren entspricht dies
10 Prüfungsjahrgängen.

Die Stichprobe darf als für die IMS an der Kantonsschule Büelrain
repräsentativ angesehen werden. Der Anteil junger Frauen hat auf die
ganze Dauer der Existenz der IMS ganz leicht abgenommen. Hat es doch in
der allerersten IMS Klasse mit einem Bestand von 15 Schülerinnen und
Schüler drei Frauen gehabt. Dieser Höchststand wurde nachher nie mehr
erreicht. Damit dürfte die Geschlechterverteilung der Stichprobe jener
der Gesamtpopulation entsprechen.  
Das gleiche gilt für die Altersverteilung. Nach Abschluss
der dritten Klasse der Sekundarschule sind die meisten Schülerinnen und
Schüler 16 Jahre alt. Nach Abschluss des schulischen Teils ihrer
Ausbildung entsprechend 19 Jahre. Die Abweichungen vom
Durchschnittsalter sind auf Repetitionen und in der Volksschule
übersprungene Klassen 
zurückzuführen.

## Beurteilung der Qualität der Datensätze

Die Aussagekraft von Noten wird in der Öffentlichkeit immer wieder
angezweifelt[@nzz_schulnoten].  Dass es keinen objektiven Notenmassstab
gibt ist eine Binsenwahrheit. Trotzdem sind Noten "*eine bewährte Form
von Feedback und für die Kommunikation der Schulen nach aussen
– Arbeitgeber, Eltern et al. – ohne ebenbürtigen
Ersatz*"[@condorcet_noten]. Deshalb kommt Noten durchaus eine gewisse
Verlässlichkeit zu. Darüber hinaus hilft in der vorliegenden Arbeit die Grösse der
Stichprobe, einzelne Extremwerte auszugleichen. Allfällige Unterschiede
in den Bewertungsmassstäben durch unterschiedliche Lehrpersonen in den
gleichen Modulen oder Fächern gleichen sich aus.

Bei fehlenden Werten wurde der Datensatz entsprechend gekürzt. Da die
Beurteilung der Korrelation auf Datenpaaren beruht, weisen die
Korrelationen mit unvollständigen Paaren eine kleinere Stichprobe auf.
Als Konsequenz daraus weisen diese eine grössere Fehlerspanne auf.

Zur Bereinigung der Datensätze wurde in den Python Scripts folgender
Abschnitt verwendet:


```{=latex}
\lstinputlisting[language=Python, firstline=21, lastline=24]{docs/code/09_korrelation_detailliert.py}
`````

Wobei `efz` im Beispiel für den pandas DataFrame mit dem Notensatz der
Berufsausbildung steht.
Die Schwelle von 20 für die Elimination von kleinen Datensätzen wurde
gewählt, weil dies einer durchschnittlichen angestrebten Klassengrösse
entspricht. Damit konnten Wahlmodule, welche nur von einigen wenigen
Lernenden gewählt worden sind, ausgeschlossen werden.

Die Paarung erfolgte in Schlaufen wie der unten dargestellten:

```{=latex}
\lstinputlisting[language=Python, firstline=38, lastline=43]{docs/code/09_korrelation_detailliert.py}
`````

Wobei hier `bm` bzw. `efz` für den DataFrame mit den Noten der BMS bzw.
der Berufsausbildung steht. Entscheidend ist die Zeile 3:
`tmp.dropna(axis="index", inplace=True)`. In dieser Zeile werden aus dem
Temporären DataFrame `tmp` alle Notenpaare mit fehlenden Werten
entfernt.

Da der Datensatz ausschliesslich auf Noten basiert, können viele
Störvariabeln nicht identifiziert werden. Mögliche Störvariabeln sind
beispielsweise der sozioökonomische Hintergrund der Lernenden. Dieser
hat sich im Verlauf des Beobachtungszeitraums deutlich verändert. Der
Anteil an Lernenden mit Migrationshintergrund hat gegenüber der
Gesamtbevölkerung der Schweiz überproportional stark zugenommen.
Dies schränkt die Analyse der Resultate entsprechend ein. Da Noten
aber grundsätzliche ausdrücken, ob jemand den beruflichen Anforderungen
genügt, werden hier trotzdem vorsichtige Schlussfolgerungen gezogen. 

## Beschreibung der Datensätze

Das Notensystem in der Berufsausbildung und in der BMS ist das gleiche.
Die Notenskala reicht von 1 bis 6. Die tiefste Note liegt bei 1, die
beste bei 6. Noten über 4 sind genügend, Noten unter 4 ungenügend.
Allerdings kennt die Berufsausbildung, anders als die BMS, kein strenges
Fachsystem. Aus diesem Grund werden die beiden Datensätze im
Folgenden getrennt besprochen.

### Noten der Berufsbildung {#sec:begruendung}

Wie in allen Lehrberufen erfolgt die theoretische Ausbildung der
Lernenden in den ICT-Berufen an einer Berufsschule. Anders als in der
klassischen Schulbildung und in vielen Lehrberufen ist diese
theoretische Ausbildung vollständig modularisiert[@modulbaukasten]. Eine
Auflistung aller an der Berufsschule unterrichteten Module findet sich
in [@tbl:modulliste]. Der
für die inhaltlichen Aspekte der Berufsausbildung zuständige Verband,
ICT-Berufsbildung Schweiz, hat alle Module im Modulbaukasten.ch
zusammengestellt.  
Aufgrund dieser Modularisierung absolvieren die Lernenden der IMS in der
Berufsausbildung keine theoretische Abschlussprüfung. Als
Leistungsnachweis für die theoretischen Kenntnisse in der
Berufsausbildung dienen die Noten aus den einzelnen Modulen (Art. 19
Abs. 2 lit. d und Abs. 4 lit. a der Verordnung des SBFI über die
berufliche Grundbildung Informatikerin/Informatiker mit eidgenössischem
Fähigkeitszeugnis (BiVo)).

Nicht alle der in [@tbl:modulliste] aufgeführten Module wurden durchgehend
während des ganzen Beobachtungszeitraums unterrichtet und geprüft. Dies
ist eine Folge der periodisch durchgeführten Massnahmen der
Qualitätsentwicklung nach Art. 22 Abs. 4 lit. a BiVo. Diese Massnahmen
der Qualitätsentwicklung führen dazu, dass neue Module zum Modulbaukasten
hinzugefügt und andere entfernt worden sind. Als Konsequenz der
Anpassung der ausgebildeten Module ergeben sich unterschiedlich grosse
Stichproben pro Modul. Die Grösse der Stichprobe sowie der sich daraus
ergebende Fehlerbereich ist in der
Zusammenstellung der Module in [@tbl:modulliste] ausgewiesen. Die
Berechnung des Fehlerbereichs basiert im Sinne einer Worst Case Annahme
auf dem oberen Rand der Schätzung der Gesamtpopulation von 400 Lernenden
(vgl. [@sec:stichprobe]). In der Zusammenstellung der an der
Berufsschule unterrichteten Module wurden jene Module, welche für die
Schulung von Fähigkeiten in Computational Thinking besonders wichtig,
sind *kursiv* gesetzt. Die Auswahl wird in den folgenden Abschnitten
begründet.

```{=latex}
\small
\begin{longtable}{p{0.07\textwidth}p{0.63\textwidth}rr}
\caption[Liste der Module der Berufsausbildung]{Liste der Module aus
der Stichprobe. \textit{Kursiv} sind jene Module
dargestellt, welche einen deutlichen Bezug zu Computational Thinking aufweisen. In der Spalte
$n$ wird die Grösse der Stichprobe pro Modul angegeben. MoE steht für
\textit{Margin of Error} oder Fehlerbereich. Die Berechnung erfolgte unter
der Annahme, dass die Gesamtpopulation eine Grösse von 400 aufweist.
Die genaue Beschreibung aller Module findet sich auf der von
ICT-Berufsbildung Schweiz betreuten Website modulbaukasten.ch.}\\
\label{tbl:modulliste}\\

\toprule
Nr. & Titel & $n$ & MoE \\
\midrule
\endfirsthead

\multicolumn{4}{c}{Fortsetzung von vorheriger Seite} \\
\toprule
Nr. & Titel & $n$ & MoE \\
\midrule
\endhead

\midrule
\multicolumn{4}{r}{Fortsetzung auf nächster Seite} \\
\endfoot

\bottomrule
\endlastfoot

100 & \textit{Daten charakterisieren, aufbereiten und auswerten} & 167 & 5.80\% \\
103 & Strukturiert programmieren nach Vorgabe & 47 & 13.45\% \\
104 & Datenmodell implementieren & 167 & 5.80\% \\
114 & Codierungs-, Kompressions- und Verschlüsselungsverfahren einsetzen & 120 & 7.49\% \\
117 & Informatik- und Netzinfrastruktur für ein kleines Unternehmen realisieren & 167 & 5.80\% \\
118 & \textit{Analysieren und strukturiert implementieren} & 47 & 13.45\% \\
120 & Benutzerschnittstellen implementieren & 167 & 5.80\% \\
122 & \textit{Abläufe mit einer Scriptsprache automatisieren} & 155 & 6.17\% \\
123 & Serverdienste in Betrieb nehmen & 167 & 5.80\% \\
133 & Web-Applikation mit Session-Handling realisieren & 167 & 5.80\% \\
150 & E-Business-Applikationen anpassen & 165 & 5.86\% \\
151 & Datenbanken in Web-Applikation einbinden & 164 & 5.89\% \\
152 & Multimedia-Inhalte in Webauftritt integrieren & 163 & 5.92\% \\
153 & \textit{Datenmodelle entwickeln} & 165 & 5.86\% \\
183 & Applikationssicherheit implementieren & 166 & 5.82\% \\
214 & Benutzer/innen im Umgang mit Informatikmitteln instruieren & 118 & 7.58\% \\
226 & \textit{Objektorientiert implementieren} & 47 & 13.45\% \\
226a & \textit{Objektorientiert (ohne Vererbung) implementieren} & 120 & 7.49\% \\
226b & \textit{Objektorientiert (mit Vererbung) implementieren} & 120 & 7.49\% \\
242 & \textit{Mikroprozessoranwendung realisieren} & 132 & 6.99\% \\
254 & Geschäftsprozesse im eigenen Berufsumfeld beschreiben & 159 & 6.04\% \\
304 & Einzelplatz-Computer in Betrieb nehmen & 47 & 13.45\% \\
305 & Betriebssysteme installieren, konfigurieren und administrieren & 47 & 13.45\% \\
306 & \textit{Kleinprojekte im eigenen Berufsumfeld abwickeln} & 164 & 5.89\% \\
326 & \textit{Objektorientiert entwerfen und implementieren} & 167 & 5.80\% \\
335 & \textit{Mobile-Applikation realisieren} & 25 & 19.00\% \\
403 & \textit{Programmabläufe prozedural implementieren} & 119 & 7.54\% \\
404 & Objektbasiert programmieren nach Vorgabe & 120 & 7.49\% \\
411 & \textit{Datenstrukturen und Algorithmen entwerfen und anwenden} & 120 & 7.49\% \\
426 & Software mit agilen Methoden entwickeln & 120 & 7.49\% \\
431 & \textit{Aufträge im eigenen Berufsumfeld selbstständig durchführen} & 119 & 7.54\% \\
\end{longtable}

\normalsize
```

#### Modul 100: Daten charakterisieren, aufbereiten und auswerten

Die Modulbeschreibung definiert für das Modul 100[@modul100] sechs
Handlungsziele:

1. Daten bzw. Datenbestand nach den für die Verarbeitung resp.
   Auswertung wichtigen Merkmalen hinsichtlich Struktur (Text,
   Datenblätter, Datenbank usw.) charakterisieren.
2. Daten bzw. Datenbestand nach den für die Auswertung wichtigen
   Merkmalen hinsichtlich Datenqualität (Vollständigkeit, Eindeutigkeit
   und Redundanz) charakterisieren.
3. Aufgrund der Charakteristik eines Datenbestands die Informationen
   auswählen, die sich für eine bestimmte Auswertung eignen.
4. Unstrukturierte Daten in eine strukturierte, verarbeitbare Form
   bringen, um Auswertungen zu ermöglichen.
5. Für Daten und Zusammenhänge eine geeignete, visuell erfassbare Form
   wählen und diese in der gewählten Form darstellen.
6. Bedeutung und Aussagekraft der Auswertung kritisch hinterfragen und
   kommentieren.

Die in Handlungsziel 3 verlangte Auswahl von Daten erfordert, dass
die konkret vorliegenden Daten auf ein Modell reduziert werden können.
Das Erstellen von Modellen verlangt, von konkreten
Situationen zu abstrahieren und die generellen Charakteristika einer
Mehrheit von Situationen herauszuarbeiten. Darüber hinaus müssen diese
Charakteristika so aufbereitet werden, dass eine automatisierte
Verarbeitung möglich wird.

Damit werden von den in der Definition von Computational Thinking
identifizierten Aspekten die Teilaspekte Verallgemeinerung und
Automatisierung geschult.

#### Modul 118: Analysieren und strukturiert implementieren

Das Modul 118 ist eines jener Module, welches durch Massnahmen der
Qualitätsentwicklung aus dem Modulbaukasten entfernt worden ist. Die
Entfernung erfolgte zu Beginn des Beobachtungszeitraums. Aus diesem
Grund ist via ICT Berufsbildung Schweiz keine detaillierte
Modulbeschreibung mehr erhältlich zu machen. Der Titel des Moduls, der
hier als Beschreibung dienen muss, konnte aus den archivierten
Zeugnissen erhoben werden.

Aufgrund des Titels des Moduls wurde es als eines jener
Module identifiziert, welche Computational Thinking fördern.

#### Modul 122: Abläufe mit einer Scriptsprache automatisieren {#sec:m122}

Die Modulbeschreibung definiert für das Modul 122[@modul122] fünf
Handlungsziele:

1. Zu automatisierende Funktion oder zu automatisierenden Ablauf mit den
   dazugehörigen Benutzerinteraktionen als Ablaufstruktur (z.B.
   Programmablaufplan) grafisch darstellen.
2. Ablaufstruktur mit Hilfe einer Scriptsprache umsetzen.
3. Script in eine Systemumgebung integrieren.
4. Script auf eine vollständige und korrekte Ausführung der
   erforderlichen Funktionalität bzw. des Ablaufs testen.
5. Dokumentation für den Einsatz des Scripts erstellen.

Das Handlungsziel 1 erfordert die Fähigkeit, das zu automatisierende
Problem in Teilprobleme zu zerlegen. Das Zerlegen von Problemen in
Teilprobleme ist ein Aspekt gemäss der Definition von Computational
Thinking. Im zweiten und dritten Handlungsziel
geht es darum, die gefundene Lösung zu implementieren und damit effektiv
zu automatisieren. Automatisieren ist ebenfalls ein Teilaspekt gemäss
der Definition von Computational Thinking. Die in Handlungsziel
4 verlangten Tests erfordern, dass die zu automatisierenden Abläufe in
ihrer Gesamtheit erfasst werden. Damit alle denkbaren Grenzfälle
getestet werden können, müssen die Abläufe von ihrer konkreten
Ausprägung abstrahiert werden. Die Fähigkeit der Abstraktion ist ein
weiterer Teilaspekt der Definition von Computational Thinking.

#### Modul 153: Datenmodelle entwickeln

Die Modulbeschreibung definiert für das Modul 153[@modul153] fünf
Handlungsziele:

1. Informationsbedürfnisse und Anforderungen an die Datenhaltung
   zusammen mit dem Auftraggeber aufnehmen (z.B. Geschäftsfälle),
   analysieren, sowie Schutz- und Sicherheitsbedürfnisse der Daten
   definieren und dokumentieren.
2. Konzeptionelles Datenmodell erstellen und fehlende Informationen
   ermitteln bzw. Redundanzen klären.
3. Konzeptionelles Datenmodell in ein logisches überführen und
   Attribute, Identifikationsschlüssel, Fremdschlüssel und Datentypen ergänzen.
4. Konzeptionelles Datenmodell zusammen mit dem Auftraggeber überprüfen
   und allfällige Anpassungen vornehmen.
5. Für das vorliegende logische Datenmodell das physikalische
   Datenbankschema entwickeln und implementieren.

Wie den Handlungszielen des Moduls 153 zu entnehmen ist, geht es in
diesem Modul darum, aus den Informationsbedürfnissen eines Kunden eine
Datenbank zu erstellen. Die Transformation von Informationsbedürfnissen
in das Datenschema einer Datenbank erfordert ein hohes
Abstraktionsvermögen. Diese Fähigkeit zu abstrahieren, ist eine der
Komponenten  gemäss Definition von Computational Thinking.

#### Module 226 bw. Modul 326: Objektorientiert implementieren

Das Modul 226 ist im Rahmen der Qualitätsentwicklung in die Module 226a
und 226b Objektorientiert implementieren (mit und ohne Vererbung)
aufgeteilt worden. Das Modul 326 vertieft die beiden Module 226a und
226b mit einem Businessbezug. Die Begründung für die Aufnahme in die
Liste der Module mit starkem Bezug zu Computational Thinking wird deshalb hier für alle Module
zur objektorientierten Programmierung zusammengefasst.

Die Modulbeschreibung definiert für die Module 226a, 226b sowie 326 die
folgenden zehn konsolidierten Handlungsziele [@modul226a; @modul226b;
@modul326]:

1. Ein SW-Design mit Klassen nachvollziehen und mit eigenen fachlichen
   und technischen Klassen ergänzen.
2. Die Notation dynamischer und statischer Strukturen einer Anwendung
   mittels Unified Modeling Language (UML) nachvollziehen.
3. Klassen- bzw. Objektbasiertes Design implementieren.
4. Für funktionale Einheiten einer Anwendung Testfälle implementieren,
   um die Anwendung automatisch zu prüfen.
5. Klassen der Anwendung systematisch, unter Verwendung der hierfür
   vorgesehenen Infrastruktur, dokumentieren.
6. Ein objektorientiertes Design nachvollziehen und durch Einsatz der
   Vererbung erweitern.
7. Fortgeschrittene Testfälle für funktionale Einheiten implementieren,
   welche durch geeignete Techniken von anderen Systemteilen unabhängig
   sind.
8. Aufgrund der Businessanalyse Anwendungsfälle formulieren und daraus
   die fachlichen Klassen ableiten.
9. Objektorientiertes Design implementieren.
10. Applikations-Architektur nachvollziehbar dokumentieren.

Die objektorientierte Programmierung ist ein gutes Beispiel für die
Anwendung von Computational Thinking.  
Die Modellierung von Situationen des realen Lebens als Klassen mit
Attributen und Methoden entspricht genau dem in der Definition von
Computational Thinking
beschriebenen Zerlegen von Problemen in lösbare Teilprobleme. Dadurch,
dass im Modul 226b explizit mit Vererbung gearbeitet wird, wird auch die
als Teilkomponente von Computational Thinking identifizierte Abstraktion geübt. Dies wird
noch verstärkt, indem Testfälle identifiziert und implementiert werden
müssen (vgl. [@sec:m122]).

Insgesamt kann festgehalten werden, dass die vier Module 226, 226a, 226b
und 326 alle Aspekte von Computational Thinking gemäss Definition abbilden.

#### Modul 242 Mikroprozessoranwendung realisieren {#sec:modul242}

Die Modulbeschreibung definiert für das Modul 242[@modul242] fünf
Handlungsziele:

1. Vorgabe auf verlangte Funktionen und benötigte Input- und
   Outputdaten/-Signale analysieren.
2. Zeitkritische und zeitlich unabhängige Funktionen identifizieren und
   in einem Programmentwurf logisch gliedern, Datentypen den
   Daten/Signalen zuordnen.
3. Mittels einer Programmiersprache und Programmierumgebung den
   Programmentwurf umsetzen.
4. Aus der Vorgabe die Testfälle identifizieren, spezifizieren und
   dokumentieren.
5. Realisierte Applikation mit geeigneten Werkzeugen auf der
   Zielhardware austesten, Fehler identifizieren, korrigieren und
   dokumentieren.

In diesem Modul sticht insbesondere das vierte Handlungsziel heraus. Das
Identifizieren von Testfällen erfordert ein tiefes Verständnis der
gestellten Aufgabe. Man muss dazu das Problem so weit verallgemeinern,
dass alle möglichen Grenzfälle bedacht werden können. Das bedeutet, dass man
von der konkreten Probleminstanz abstrahieren, und alle
erdenklichen Ausprägungen bedenken muss. Dazu muss das Gesamtproblem in
Teilprobleme zerlegt werden (vgl. [@sec:m122]).  
Mit dem hier verlangten Abstraktionsvermögen und der Fähigkeit, Probleme
in Teilprobleme zu zerlegen, werden zwei wesentliche Aspekte von
Computational Thinking gemäss Definition geschult.

#### Modul 306, 431 und 335: Kleinere Projekte und Mobile-Applikationen

Die Module 306, 431 und 335 befassen sich alle mit der Planung und Umsetzung
kleinerer Projekte. Wegen den sich daraus ergebenden Parallelen wurden
die drei Module zur Begründung ihres Zusammenhangs mit Computational
Thinking zusammengefasst.  
Die Handlungsziele können für die drei Module zu folgenden 12
Handlungszielen konsolidiert werden[@modul306; @modul335; @modul431].

1. Prüfen einer Zielsetzung unter Berücksichtigung der vorgegebenen
   Ressourcen, Anforderungen und Termine auf Machbarkeit, Festhalten der
   Erkenntnisse und Besprechung mit dem Auftraggeber.
2. Vorgabe analysieren, Funktionalität und Storyboard entwerfen.
3. Ein Projekt identifizieren und Massnahmen zur Bewältigung
   anhand eines Business Cases bestimmen (Stakeholder, Risikoanalyse,
   Machbarkeits- und Wirtschaftlichkeitsanalyse, Zeitmanagement,
   Zielentwicklung).
4. Lösungskonzept für die Applikation erarbeiten und Einbettung in
   bestehenden Lösungen überprüfen.
5. Einen Projektplan erstellen zur systematischen Abwicklung eines
   Auftrags unter Berücksichtigung der Ressourcen, Termine,
   Problemstellungen und Arbeitsteilung (Wasserfallmethode/agile Methode
   unabhängig von Methode im Lehrbetrieb).
6. Arbeitsaufträge erteilen (Arbeitspaket/Stories) koordinieren und
   überwachen von
   deren Ausführung (Qualität, Termine, Kosten).
7. Einen Arbeitsfortschrittsbericht erstellen (Projektstatusbericht,
   Projektjournal/Board) und darin den Stand des Projekts
   (Ressourcen, Termine, geleistete Arbeiten) für den Auftraggeber
   dokumentieren.
8. Mobile-Applikation mit einer gängigen Entwicklungsumgebung unter
   Berücksichtigung der Möglichkeiten und Einschränkungen von mobilen
   Geräten programmieren.
9. Veröffentlichung der Applikation auf einer gängigen Plattform planen
   und nötige Schritte festhalten.
10. Das Projektergebnis (Lösung) für den
   Auftraggeber dokumentieren und erläutern.
11.  Mobile-Applikation gemäss Testplan überprüfen, Testergebnisse
    festhalten und allenfalls erforderliche Korrekturen vornehmen.
12. Den Projektverlauf mit den Projektbeteiligten im Team reflektieren und
   Erkenntnisse daraus ableiten, wie effiziente Projektarbeit gestaltet werden
   kann.

Wie den Handlungszielen entnommen werden kann, übernehmen die Lernenden
in den hier zusammengefassten Modulen
die Rolle eines Projektleiters. 
In der IT-Branche kommen eine Vielzahl von
Projektmanagement-Methoden zum Einsatz. Auch wenn man in solchen
Methoden geschult ist, muss man sich für die Detailaspekte einen eigenen
Arbeitsablauf erarbeiten. Solche allgemeinen Arbeitsabläufe können als
Algorithmus verstanden werden.  
Als Projektleiter muss man, um alle Teammitglieder in die Arbeit
einzubeziehen, zudem Aufgaben in
Teilprobleme zerlegen. Ausserdem müssen äussere Abhängigkeiten
berücksichtigt werden. Handlungsziel 2 schreibt für die
Mobile-Applikation vor, dass die Vorgaben zu analysieren seien.
Handlungsziel 3 präzisiert dies für die Kleinprojekte im eigenen
beruflichen Umfeld dahingehend, dass insbesondere die
Interessen der
Stakeholder und der Faktor Zeit zu berücksichtigen sind.
Die dafür erforderliche Analyse der
Aufgabenstellung übt ebenfalls den Aspekt Aufteilen von Problemen in
kleinere Teilprobleme. Das Erarbeiten von Algorithmen und die Aufteilung
von Problemen in Teilproblem sind Teilaspekte
der Definition von Computational Thinking. 

#### Modul 403: Programmabläufe prozedural implementieren

Die Modulbeschreibung definiert für das Modul 403[@modul403] sechs
Handlungsziele:

1. Vorgegebenen Programmablauf in Form einer Ablaufstruktur abbilden.
2. Die erforderlichen Daten für Eingabe, Verarbeitung und Ausgabe
   bestimmen und ihre Datentypen festlegen.
3. Kontrollstrukturen für die Steuerung des Programmablaufs anwenden.
4. Ablaufstruktur und Daten mit einer Programmiersprache in einen
   Programmablauf umsetzen.
5. Vorgegebene funktionale Testfälle (Eingabewerte, erwartete
   Ergebnisse) anwenden um Fehler im Programmablauf zu erkennen und zu
   beheben.
6. Einen Debugger einsetzen um die Programmausführung zu überwachen und
   Fehler zu erkennen.

Die Implementation von prozeduralen Programmabläufen ist möglicherweise
etwas weniger anspruchsvoll als die Implementation von
objektorientierten Programmen. Trotzdem werden auch in diesem Modul
Teilaspekte von Computational Thinking geschult. Insbesondere gilt dies
für die Feststellung der für
das Programm erforderlichen Daten mit deren Datentypen nach
Handlungsziel 2. Dazu ist es erforderlich, das zu lösende Problem in
seine Komponenten zu zerlegen um festzustellen, an welcher Stelle welche
Daten mit welchen Datentypen erforderlich sind. Ausserdem verlangt
Handlungsziel 5, dass Testfälle identifiziert werden. Wie bereits in
[@sec:m122] festgehalten, erfordert dies, dass die Problemstellung
verallgemeinert werden kann.

Es werden damit die Computational Thinking Teilaspekte Aufteilen von Problemen sowie
Verallgemeinern von konkreten Probleminstanzen geschult.

#### Modul 411: Datenstrukturen und Algorithmen entwerfen und anwenden

Die Modulbeschreibung definiert für das Modul 411[@modul411] sechs
Handlungsziele:

1. Für ein gegebenes Problem eine geeignete Datenstruktur definieren und
   mit den Mitteln einer Programmiersprache, wie Structs,
   Referenzen/Zeiger und Arrays umsetzen.
2. Ein Problem analysieren und einen geeigneten Algorithmus zur Lösung
   mit den Grundelementen Zuweisung, Verzweigung und Schleife entwerfen
   und mit Prozeduren und Funktionen umsetzen.
3. Algorithmen und Datenstrukturen hinsichtlich Speicher- und
   Zeitkomplexität analysieren und dokumentieren.
4. Ein komplexeres Problem auf kleinere Teilprobleme zurückführen und je
   nach Problemstellung Iteration oder Rekursion einsetzen.
5. Abstrakte Datentypen, wie Liste, Set, Map etc. und die darauf
   definierten Operationen kennen und zielgerichtet einsetzen können.
6. Datenstrukturen und Algorithmen mit dem Debugger und weiteren Tools
   untersuchen und dabei speziell die Situation auf Stack und Heap
   analysieren und in geeigneter Form darstellen.

Selbständig Datenstrukturen und Algorithmen entwerfen darf wohl als
Königsdisziplin des Programmierens bezeichnet werden. Handlungsziel
2 entspricht denn auch fast der Definition von Computational Thinking. Eine weitere
Begründung erübrigt sich daher.

### Charakterisierung der Noten der Berufsausbildung {#sec:modulcharakter}

In der Übersichtsdarstellung der Noten der Module des EFZ
(@fig:boxplotsefz)
fallen drei Aspekte auf:

1. Der Median aller Modulnoten liegt bei mindestens 4.5.
2. Mit einer Ausnahme liegt das unterste Quartil mindestens bei 4.
3. Es gibt Module, welche eine relativ starke Streuung aufweisen.
   Insbesondere im Vergleich zu den Noten der BMS (vgl.
   @fig:boxplotsbms).

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/boxplots_efz.png}
\caption[Übersicht über die Verteilung der Noten des EFZ.]{Übersicht
über die Verteilung der Noten des EFZ. Die Module mit Bezug zu
Computational Thinking wurden grün
hervorgehoben. Der Median der erzielten Noten ist als rote Linie
dargestellt.}
\label{fig:boxplotsefz}
\end{figure}


Die Noten des EFZ fliessen nur als Durchschnittsnote der in
den jeweiligen Semester unterrichteten Module in die Promotion an der
IMS ein. Die einzelnen Module an und für sich sind nicht
promotionsrelevant. Dies könnte ein Grund sein, weshalb die Noten der
Module des EFZ stärker streuen als jene der BMS (vgl.
@fig:boxplotsbms).

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/semesternoten_efz.png}
\caption[Übersicht über die Verteilung der Semesternoten in der
Berufsausbildung]{Übersicht über die Verteilung der Semesternoten
(ungerundet). Der Darstellung liegt die Annahme zu Grunde, die gesamte
Stichprobe hätte die Ausbildung im Jahr 2017 abgeschlossen. Der Median
der erzielten Noten ist als rote Linie dargestellt.}
\label{fig:semesternotenefz}
\end{figure}

Dass die Streuung bei einer Durchschnittsnote abnimmt, zeigt
[@fig:semesternotenefz]. Die Darstellung beruht auf der Fiktion, dass alle
Lernenden ihren Abschluss 2017 gemacht hätten und die für diesen
Ausbildungsjahrgang geltenden Modulzusammenstellung gehabt hätten. An
dieser Darstellung ist das Phänomen der Regression zur Mitte zu
erkennen[@freedmanStatistics2007, S. 170].

### Noten der BMS

Die Ausbildung an der BMS orientiert sich wie in [@sec:kernbegruendung]
dargelegt an klassischen Fachdisziplinen. Die Archivierung der BMS Noten
ist nicht über den ganzen Beobachtungszeitraum hinweg gleich
organisiert. Konstant archiviert wurden lediglich die Noten, welche
Eingang ins Berufsmaturzeugnis gefunden haben. Aus diesem Grund wurde
für die Auswertung ausschliesslich auf diese Noten abgestellt. So
konnte mit Ausnahme der Noten für das interdisziplinäre Arbeiten in den
Fächern über den ganze Beobachtungszeitraum hinweg von allen Lernenden
alle Noten erhoben werden.  
Aus nicht mehr nachvollziehbaren Gründen wurden die Noten für das
interdisziplinäre Arbeiten in den Fächern in den Jahren 2012 bis 2017
nicht archiviert. Entsprechend konnten hier die Noten nur für die
Abschlüsse von 2018 bis 2022 ausgewertet werden. Damit reduziert sich
der Datensatz gegenüber den anderen Fächer von 167 auf 108 Noten.

Einen graphischen Überblick über die Verteilung der Noten ergibt
[@fig:boxplotsbms].

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/boxplots_bm.png}
\caption[Übersicht über die Verteilung der Noten der BMS.]{Übersicht
über die Verteilung der Noten der BMS. Der Plot der IDAF ist
abgeschwächt dargestellt, weil er auf einer kleineren Stichprobe beruht
als die anderen Noten. Der Median der erzielten Noten ist als rote Linie
dargestellt}
\label{fig:boxplotsbms}
\end{figure}

In der Darstellung von [@fig:boxplotsbms] fallen zwei Charakteristika
besonders ins Auge:

1. Der Median liegt bei allen Fächern mindestens bei 4.5.
2. Das untere Quartil liegt mindestens bei 4.

Dies ist jedoch keine Überraschung. Die Noten stammen aus den
Abschlusszeugnissen der BMS. In den drei Schuljahren vor Erreichen
dieses Zeugnisses findet eine dauernde Selektion statt. Und von den
ausgewerteten Noten stammen lediglich fünf von 167 Datensätzen von
Lernenden, welche die Berufsmatur nicht bestanden haben. Damit bleiben
schwergewichtig Noten von mehr als 4 übrig.
