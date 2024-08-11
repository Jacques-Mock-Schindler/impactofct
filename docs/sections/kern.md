## Statistische Auswertung von Noten

Als Reaktion auf die beiden gescheiterten Versuche, die Arbeitshypothese
zu bestätigen oder zu verwerfen, wurde in einem nächsten Schritt die
Noten der Berufsausbildung (Eidgenössisches Fähigkeitszeugnis, EFZ) und
der Berufsmittelschule (BMS) der
Lernenden der IMS ausgewertet.

### Beschreibung der Methode {#sec:effektive_methode}

Die im folgenden beschriebenen statistischen Berechnungen wurden in
Python mit den Libraries pandas und SciPy vorgenommen. Die
Visualisierungen wurden ebenfalls in Python mit den Libraries
matplotlib und seaborn erstellt. Eine Liste der verwendeten Scripts
findet sich im Anhang (vgl. [@sec:github]).

Mit der Gegenüberstellung der Noten des EFZ und jener der BMS
soll festgestellt werden, ob und gegebenenfalls wie stark die beiden
Notensätze miteinander korrelieren. Damit das richtige Mass der
Korrelation gewählt werden kann, muss als Vorfrage geklärt werden, ob
die Noten normalverteilt sind. Diese Kontrolle erfolgte in einer ersten
Phase optisch mit der Darstellung der Noten als Histogramm und
darübergelegter theoretischer Normalverteilung (vgl.
[@fig:normalverteilung_bm] und [@fig:normalverteilung_efz10]).

```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_bm}
\caption[Normalverteilung der Noten der BMS]{Grafiken zur optischen
Überprüfung, ob die Noten der BMS normalverteilt sind.
$n$ ist die Stichprobengrösse, $\mu$ der Mittelwert und $\sigma$ die
Standardabweichung. Die gestrichtelte Linie zeigt die Normalverteilung.}
\label{fig:normalverteilung_bm}
\end{figure}
```

Für die BMS ergibt die optische Überprüfung für die Fächer Finanz- und
Rechnungswesen (RW), Wirtschaft und Recht (WR) sowie Geschichte und
Politik (GuP) eine Verteilung, die der Normalverteilung recht nahe
kommt. Bei den anderen Fächern gibt es mehr oder weniger starke
Abweichungen.

Die optische Überprüfung der Normalverteilung der Modulnoten des EFZ
ergibt für die Module 122, 123, 151, 214, 304 und 431 (vgl.
[@fig:normalverteilung_efz10]) eine Verteilung, welche der
Normalverteilung recht nahe kommt. Alle anderen Notenverteilungen
weichen mehr oder
weniger stark von der Normalverteilung ab.

```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz0.png}
\label{fig:normalverteilung_efz0}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz1.png}
\label{fig:normalverteilung_efz1}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz2.png}
\label{fig:normalverteilung_efz2}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz3.png}
\label{fig:normalverteilung_efz3}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz4.png}
\label{fig:normalverteilung_efz4}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz5.png}
\label{fig:normalverteilung_efz5}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz6.png}
\label{fig:normalverteilung_efz6}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz7.png}
\label{fig:normalverteilung_efz7}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz8.png}
\label{fig:normalverteilung_efz8}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz9.png}
\label{fig:normalverteilung_efz9}
\end{figure}
```
```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/normalverteilung_efz/normalverteilung_efz10.png}
\caption[Normalverteilung der Noten des EFZ]{Grafiken zur
optischen Überprüfung, ob die Noten der Berufsausbildung normalverteilt
sind.
$n$ ist die Stichprobengrösse, $\mu$ der Mittelwert und $\sigma$ die
Standardabweichung. Die gestrichtelte Linie zeigt die Normalverteilung.}
\label{fig:normalverteilung_efz10}
\end{figure}
```


Aufgrund des zentralen Grenzwertsatzes ist eigentlich davon auszugehen,
dass ab einer Stichprobengrösse von $n \geq 30$ eine gute Annäherung an
eine Normalverteilung erwartet werden
kann[@hollingStatistikTestverfahren2016, S. 69].
Allerdings wirft bereits die optische Überprüfung der Normalverteilung der Noten
in vielen Fällen Zweifel an deren Normalverteilung auf. Zur Sicherheit
wird daher die Normalverteilung mit dem Shapiro-Wilk Test auch
rechnerisch überprüft. Die rechnerische Überprüfung ist zuverlässiger, weil sie auch
Verletzungen der Normalverteilungen überprüft, die optisch nur schwer zu
erkennen sind[@chattamvelliDescriptiveStatisticsScientists2023, S. 28
f]. Die $p$-Werte des Shapiro-Wilk Test sowohl für die Noten der BMS wie
auch für jene für das EFZ liegen alle deutlich unter 0.05.
Damit ist die Annahme der Normalverteilung der Stichproben zu
verwerfen[@hollingStatistikTestverfahren2016, S. 105].

Anschliessend an diese Vorprüfung wurden die Noten jedes Moduls des EFZ 
den Noten jedes Fachs der BMS gegenübergestellt und die Korrelation
zwischen diesen Notenpaaren berechnet.  
Oft werden Korrelationen nach Bravais-Pearson ($r$) berechnet. Das setzt
allerdings voraus, dass es sich um normalverteilte intervallskalierte
Daten handelt[@hollingStatistikTestverfahren2016, S. 123 f]. Die einleitende
Überprüfung der Daten hat jedoch ergeben, dass sie nicht normalverteilt
sind.
Zudem sind Noten grundsätzlich nicht intervallskaliert. Das wäre nur dann der
Fall, wenn ein streng linearer Massstab angelegt worden wäre und
zusätzlich tatsächlich jeder vergebene Punkt in einer Prüfung gleich
viel wert wäre. Dies kann jedoch nicht garantiert werden. Dies
begründet, warum die Noten hier als ordinal skaliert behandelt werden.
Aus diesem Grund wurde von jeder gebildeten 
Paarung der Rangkorrelationskoeffizient
nach Spearman ($\rho$)
berechnet[@hollingStatistikTestverfahren2016, S. 131].

$$
\rho = 1 - \frac{6 \cdot \sum_{i=1}^{n} d_{i}^{2}}{n \cdot (n^2 - 1)}
$$ {#eq:spearman}

wobei

* $d_{i}^{2} =$ quadrierte Rangplatzdifferenz der $i$-ten
  Untersuchungseinheit
* $n =$ Anzahl der Untersuchungseinheiten

sind[@kuckartzStatistikVerstaendlicheEinfuehrung2013, S. 217].

Obwohl Noten nicht intervallskaliert sind, werden in Untersuchungen zu
Noten trotzdem oft Korrelationen nach
Bravais-Pearson berechnet. Zur Überprüfung der Robustheit der Auswertung
wurde diese Berechnung ebenfalls vorgenommen. Die Berechnung erfolgt
nach der Formel

$$
r = \frac{cov(x,y)}{s_x \cdot s_y}
$$ {#eq:pearson}

wobei

* $cov(x,y) =$ Kovarianz der Variablen $x$ und $y$
* $s_x$ und $s_y$ = Standardabweichungen der Variablen $x$ und $y$

sind[@kuckartzStatistikVerstaendlicheEinfuehrung2013, 212]. In den
Berechnungen entspricht $x$ jeweils den Noten der BMS, $y$ jenen der
Berufsausbildung.

Zur Auswertung der Resultate wurden die Ergebnisse in einer Heatmap
visualisiert. Die Darstellung der Daten in einer Heatmap ermöglicht es,
jene Fächer der BMS, welche stark mit jenen der Berufsausbildung
korrelieren optisch klar zu erkennen.
Da in den Sozialwissenschaften Ursache und Wirkung nicht
im gleichen Mass isoliert werden können wie in den Naturwissenschaften,
wurde die Schwelle für eine relevante Korrelation bei 0.3 angesetzt.
Dies entspricht in den Sozialwissenschaften einer mittleren
Effektstärke[@cohenStatisticalPowerAnalysis1988, S. 129]. Der Effekt ist
damit beobachtbar und selbst unter Berücksichtigung der Tatsache, dass
Korrelation nicht das gleiche ist wie Kausalität, bietet eine
entsprechende Korrelation gegebenenfalls Anlass zu weiteren
Untersuchungen. Unterhalb der Schwelle von 0.3 dürfte es schwierig
werden, geeignete Methoden zu finden, um die Ursachen für die
Korrelation zu finden.

### Begründung der Wahl der Methode {#sec:kernbegruendung}

Die beiden gescheiterten Methoden haben darauf basiert, den Unterschied
im Lernerfolg bei unterschiedlichen Lehr- und Lernmethoden zu messen.
Dabei wurde in der Testgruppe eine Computational Thinking basierte Methode eingesetzt. Die
Schülerinnen und Schüler bzw. die Lernenden mussten ein Programm
schreiben, welches ein Problem des Faches Finanz- und Rechnungswesen
gelöst hat. Weil die beiden Methoden keine verwertbaren Resultate
gezeitigt haben, musste ein indirekter Ansatz gewählt werden. Dieser
indirekte Ansatz basiert auf der Gegenüberstellung von ausgewiesenen
Fähigkeiten in Computational Thinking und 
solchen in der
Allgemeinbildung. Wenn zwischen den Leistungen in den beiden
Bereichen eine positive Korrelation beobachtet werden kann, ist dies
eine Indiz für die Gültigkeit der Arbeitshypothese.

Wie in der Einleitung erwähnt, erwerben die Lernenden der IMS parallel
zu ihrer Ausbildung als Informatiker/in, Fachrichtung
Applikationsentwicklung, eine kaufmännische Berufsmatur. Angehende
Applikationsentwicklerinnen und Applikationsentwickler in der
betrieblich orientierten Grundbildung (BOG) erwerben, wenn sie das den
wollen, in der Regel eine Berufsmatur mit technischer
Ausrichtung[@sbfiBerufsmaturitaet]. Damit weist die IMS gegenüber der
BOG eine Besonderheit auf. Diese Besonderheit hat sich ergeben,
weil sich die IMS aus historischen Gründen sehr stark am Modell der
Handelsmittelschule im Kanton Zürich orientiert.

Als weitere Besonderheit findet in der IMS, im Gegensatz zur BOG per
Ende eines jeden
Semesters eine promotionswirksame Beurteilung statt. Dabei kommt der
Leistung in der Berufsbildung lediglich ein Gewicht von etwas mehr als
10% zu. Die so gesetzte Anreizstruktur führt gelegentlich dazu, dass die
Lernenden die Prioritäten eher auf die Fächer der BMS legen. Das heisst
allerdings nicht, dass sie in beruflicher Hinsicht schlecht qualifiziert
wären. Die Lernenden der IMS belegen überdurchschnittlich oft
Spitzenplätze bei der kantonalen Rangierung aller Lehrabschlüsse in den
ICT-Berufen. 

Diese Ausgangslage hat es ermöglicht, Leistungen im Fachbereich
Informatik, die mit Computational Thinking in Verbindung gebracht werden
können, mit Leistungen im Bereich Allgemeinbildung zu korrelieren.
Die Noten der Module werden dabei als Ursache und jene der BMS als
Wirkung behandelt.  
31 der an der für die Berufsausbildung zuständigen Berufsschule
unterrichteten Module hatten mehr als 20 Teilnehmer.
Damit standen aus der Berufsausbildung 31 Noten zur Verfügung. 15
davon stammen aus Modulen, welche Fähigkeiten in Computational Thinking erfordern. 16 Noten
sind in Modulen vergeben worden, welche allgemeine berufliche
Fähigkeiten von Informatiker/innen, Fachrichtung
Applikationsentwicklung, vermitteln. Eine Begründung für die Gruppierung
der Module folgt in [@sec:begruendung].

Das Berufsmaturzeugnis beinhaltet
neun Noten. Diese Noten Gruppieren sich in Grundlagenbereich (erste
Landessprache, zweite Landessprache, dritte Sprache, Mathematik; Art.
8 Abs. 1 Verordnung über die eidgenössische Berufsmaturität, BMV),
Schwerpunktbereich (Finanz- und Rechnungswesen,
Wirtschaft und Recht; Art. 9 Abs. 2 und 3 BMV) und den Ergänzungsbereich
(Geschichte und Politik sowie Technik und Umwelt; Art. 10 Abs. 2 und
3 BMV). Ausserdem gibt es noch eine Note für interdisziplinäres Arbeiten
(Art. 11 BMV).

Die Möglichkeit, Computational Thinking spezifische Fähigkeiten mit allgemeinbildenden
Fächern zu korrelieren, ist der Grund für die Wahl des Vorgehens.

### Beschreibung der Vorgehensweise

Die ausgewerteten Daten stammen von einer Zürcher Mittelschule und sind
nicht öffentlich verfügbar. Möglicherweise hätten die Daten gestützt auf
§ 18 des Gesetzes über die Information und den Datenschutz (IDG) des
Kantons Zürich verfügbar gemacht werden können. Dieser Schritt war
vorliegend allerdings nicht erforderlich, da der Verfasser als
Mitarbeiter dieser Schule Zugriff auf den Datenbestand hatte.

Zusammenstellungen von Leistungsbeurteilungen sind nach 
§ 3 Abs. 4 lit. b IDG besondere Personendaten. Besondere
Personendaten müssen speziell geschützt werden. Aus diesem Grund wurden
die Daten anonymisiert. Allerdings erforderte die Art der Archivierung
der Daten ein zweistufiges Vorgehen.

Die Daten der IMS waren auf Papier, jene der HMS als PDF
archiviert. Damit im Rahmen der vorliegenden Untersuchung jederzeit wieder auf die Daten der IMS zugegriffen
werden kann, wurden diese vor der eigentlichen Erfassung eingescannt.  
Die Form der Archivierung machte es in einem ersten Schritt nötig, die
relevanten Informationen abzuschreiben. Die manuelle Datenerfassung ist
Fehleranfällig und musste daher aus Konzentrationsgründen in mehrere
Phasen unterteilt werden. Ausserdem mussten die erfassten Daten
kontrolliert werden. Damit diese Kontrolle einfacher erfolgen konnte,
wurden die Namen und Klassen erst nach erfolgter Kontrolle anonymisiert.
Um trotz Anonymisierung die Nachvollziehbarkeit zu erhalten, wurden die
Namen und die Klasse mit folgender Funktion gehasht:

```{=latex}
\lstinputlisting[language=Python, firstline=8, lastline=13]{docs/code/anonymisierung.py}
`````

Die anonymisierten Daten wurden in CSV-Dateien zur Weiterverarbeitung
abgespeichert. Die Daten wurden in die folgenden drei Tabellen
aufgeteilt: 

* Personalien

    In dieser Tabelle wurden Name, Klasse, Gender und Alter erfasst. Dies ermöglicht
    trotz Anonymisierung die Zuordnung der erfasste Noten zu einer
    Person. Ausserdem würde die Erfassung von Alter und Gender
    gegebenenfalls weitere Auswertungen zulassen.

* Noten der Berufsausbildung

    In dieser Tabelle wurden die Noten der besuchten Module erfasst.  
    Der Hashwert des Namens dient dabei als Identifikator.

* Noten der BMS

    In  dieser Tabelle wurden die Noten der BMS Abschlussprüfungen
    erfasst.  
    Der Hashwert des Namens dient auch hier als Identifikator.

Die Aufteilung der Daten in drei Tabellen hatte zum einen praktische
Gründe. Die Tabellen behielten überschaubare Dimensionen. Andererseits
brauchen die Daten bei der Analyse nicht nach Herkunft gefiltert zu
werden.

Eine Beurteilung der Qualität der Daten erfolgt im [@sec:daten] "Daten" vor
der Analyse der Resultate.

Die Auswertung der Daten erfolgte in einem Python Skript. In diesem
Skript wurden die Daten in pandas Datafram geladen. Die Analyse erfolgte
mit den durch SciPy.stats zur Verfügung gestellte Funktion
`shapiro()` sowie die durch pandas zur
Verfügung gestellten Funktionen `spearman()` und `df.corr()`.  

Die Visualisierung als Heatmap wurde mit Hilfe der Libraries matplotlib
und seaborn erstellt. Um die relevante Schwelle der Korrelation von 0.3
sichtbar zu machen, wurde ein eigenes Farbschema angelegt. Dieses
Farbschema wechselt von Grau zu Grün. Die Schwelle des für den Umschlag
der Farbe wurde dabei auf 0.3 festgelegt.

Die verwendeten Python Skripten sind im Anhang aufgelistet. Sowohl die
Datentabellen wie auch die Scripts werden via GitHub zur Verfügung
gestellt (vgl. [@sec:github]). Damit soll die
Nachvollziehbarkeit der Resultate sichergestellt werden.
