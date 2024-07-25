## Gegenüberstellung der Noten der Berufsausbildung und solchen aus der Berufsmittelschule

Als Reaktion auf die beiden gescheiterten Versuche, die Arbeitshypothese
zu bestätigen oder zu verwerfen, wurde in einem nächsten Schritt die
Noten der Berufsausbildung und der Berufsmittelschule (BMS) der
Lernenden der IMS ausgewertet.

### Beschreibung der Methode

Die im folgenden beschriebenen statistischen Berechnungen wurden in
Python mit den Libraries pandas und SciPy vorgenommen. Die
Visualisierungen wurden ebenfalls in Python mit den Libraries
matplotlib und seaborn erstellt.

Damit ein Verfahren für die statistische Auswertung der Noten festgelegt
werden konnte, wurde in einem ersten Schritt mit dem
Shapiro-Wilk-Test[@kronthalerDataAnalysisRstudio2021, S. 72;
@chattamvelliDescriptiveStatisticsScientists2023, S. 29 (je als
Begründung für die Wahl des Shapiro-Wilk-Tests)],
dem
Kolmogorov-Smirnov-Test[@kenettModernStatisticsComputerBased2022, S. 175
f.; @chattamvelliDescriptiveStatisticsScientists2023,
S. 29 (je als Begründung für die Wahl des Kolmogorov-Smirnov-Test)] und
dem D'Agostino's K$^2$ Test[@KstestSciPyV1 (als Begründung für die Wahl
des D'Agostino's K$^2$ Test)] überprüft,
ob die Noten der Stichprobe normal verteilt sind.  
Diese Überprüfung hat
schon für die Noten der BMS ergeben, dass nicht garantiert werden kann,
dass die Noten normal verteilt sind. Aus diesem Grund konnte auf eine
Überprüfung der Noten der Berufsausbildung verzichtet werden.

Anschliessend wurden die Noten jedes Moduls der Berufsausbildung 
den Noten jedes Fachs der BMS gegenübergestellt und die Korrelation
zwischen diesen Notenpaaren berechnet.  
Oft werden Korrelationen nach Bravais-Pearson berechnet. Das setzt
allerdings voraus, dass es sich um normalverteilte intervallskalierte
Daten handelt[@KorrelationNachBravaisPearsona]. Die einleitende
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
berechnet[@RangkorrelationNachSpearman].

$$
\rho = 1 - \frac{6 \cdot \sum_{i=1}^{n} d_{i}^{2}}{n \cdot (n^2 - 1)}
$$

wobei

* $d_{i}^{2} =$ quadrierte Rangplatzdifferenz der $i$-ten
  Untersuchungseinheit
* $n =$ Anzahl der Untersuchungseinheiten

sind[@kuckartzStatistikVerstaendlicheEinfuehrung2013, S. 217].

Obwohl Noten nicht intervallskaliert sind, werden oft Korrelationen nach
Bravais-Pearson berechnet. Zur Überprüfung der Robustheit der Auswertung
wurde diese Berechnung ebenfalls vorgenommen.

$$
r = \frac{cov(x,y)}{s_x \cdot s_y}
$$

wobei

* $cov(x,y) =$ Kovarianz der Variablen $x$ und $y$
* $s_x$ und $s_y$ = Standardabweichungen der Variablen $x$ und $y$

sind[@kuckartzStatistikVerstaendlicheEinfuehrung2013]. In den
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
Untersuchungen.

### Begründung der Wahl der Methode

Damit die Arbeitshypothese überprüft werden kann, muss eine
Gegenüberstellung von Fähigkeiten in CT und solchen in der
Allgemeinbildung erfolgen. Wenn zwischen den Leistungen in den beiden
Bereichen eine positive Korrelation beobachtet werden kann, ist dies
eine Indiz für die Gültigkeit der Arbeitshypothese.

Wie in der Einleitung erwähnt, erwerben die Lernenden der IMS parallel
zu ihrer Ausbildung als Informatiker/in, Fachrichtung
Applikationsentwicklung, eine kaufmännische Berufsmatur. Angehende
Applikationsentwicklerinnen und Applikationsentwickler in der
betrieblich orientierten Grundbildung (BOG) erwerben, wenn sie das den
wollen, in der Regel eine Berufsmatur mit technischer
Ausrichtung[@sbfiBerufsmaturitaet]. Diese Besonderheit hat sich ergeben,
weil sich die IMS aus historischen Gründen sehr stark am Modell der
Handelsmittelschule im Kanton Zürich orientiert.

Als weitere Besonderheit findet in der IMS per Ende eines jeden
Semesters eine promotionswirksame Beurteilung statt. Dabei kommt der
Leistung in der Berufsbildung lediglich ein Gewicht von etwas mehr als
10% zu. Die so gesetzte Anreizstruktur führt gelegentlich dazu, dass die
Lernenden die Prioritäten eher auf die Fächer der BMS legen. Das heisst
allerdings nicht, dass sie in beruflicher Hinsicht schlecht qualifiziert
wären. Die Lernenden der IMS belegen überdurchschnittlich oft
Spitzenplätze bei der kantonalen Rangierung aller Lernenden in den
ICT-Berufen. 

Diese Ausgangslage hat es erst ermöglicht, Leistungen im Fachbereich
Informatik mit Leistungen im Bereich Allgemeinbildung zu korrelieren.
An der für die Berufsausbildung zuständigen Berufsschule wurden
insgesamt 31 Module unterrichtet.
Damit standen aus der Berufsausbildung 31 Noten zur Verfügung. 15
davon stammen aus Modulen, welche Fähigkeiten in CT erfordern. 16 Noten
sind in Modulen vergeben worden, welche allgemeine berufliche
Fähigkeiten von Informatiker/innen, Fachrichtung
Applikationsentwicklung, vermitteln. Das Berufsmaturzeugnis beinhaltet
neun Noten. Diese Noten Gruppieren sich in Grundlagenbereich (erste
Landessprache, zweite Landessprache, dritte Sprache, Mathematik; Art.
8 Abs. 1 Verordnung über die eidgenössische Berufsmaturität, BMV),
Schwerpunktbereich (Finanz- und Rechnungswesen,
Wirtschaft und Recht; Art. 9 Abs. 2 und 3 BMV) und den Ergänzungsbereich
(Geschichte und Politik sowie Technik und Umwelt; Art. 10 Abs. 2 und
3 BMV). Ausserdem gibt es noch eine Note für interdisziplinäres Arbeiten
(Art. 11 BMV).
Eine Begründung
für die Einteilung der Module in solche mit starkem CT-Bezug und solche
mit ausschliesslich berufsspezifischen Inhalten erfolgt im Abschnitt mit
der Auswertung der Resultate.

Die Möglichkeit, CT-spezifische Fähigkeiten mit allgemeinbildenden
Fächern zu korrelieren, ist der Grund für die Wahl des Vorgehens.

### Beschreibung der Vorgehensweise

