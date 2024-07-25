# Gegenüberstellung der Noten der Berufsausbildung und solchen aus der Berufsmittelschule

Als Reaktion auf die beiden gescheiterten Versuche, die Arbeitshypothese
zu bestätigen oder zu verwerfen, wurde in einem nächsten Schritt die
Noten der Berufsausbildung und der Berufsmittelschule (BMS) der
Lernenden der IMS ausgewertet.

## Beschreibung der Methode

Damit ein Verfahren für die statistische Auswertung der Noten festgelegt
werden konnte, wurde in einem ersten Schritt mit dem Shapiro-Wilk-Test,
dem Kolmogorov-Smirnov-Test und dem D'Agostino's K$^2$ Test überprüft,
ob die Noten der Stichprobe normal verteilt sind. Diese Überprüfung hat
schon für die Noten der BMS ergeben, dass nicht garantiert ist, dass die
Noten normal verteilt sind.

Anschliessend wurden die Noten jedes Moduls der Berufsausbildung 
den Noten jedes Fachs der BMS gegenübergestellt und die Korrelation
zwischen diesen Notenpaaren berechnet.  
Oft werden Korrelationen nach Bravais-Pearson berechnet. Das setzt
allerdings voraus, dass es sich um normalverteilte intervallskalierte
Daten handelt[@KorrelationNachBravaisPearsona]. Die einleitende
Überprüfung der Daten hat jedoch ergeben, dass sie nicht normalverteilt
sind.
Zudem sind Noten nicht zwingend intervallskaliert. Das wäre nur dann der
Fall, wenn ein streng linearer Massstab angelegt worden wäre und
zusätzlich tatsächlich jeder vergebene Punkt in einer Prüfung gleich
viel wert wäre. Dies kann jedoch nicht garantiert werden. Dies
begründet, warum Noten ordinal skaliert
sind.
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

Zur Auswertung der Resultate wurden die Ergebnisse in einer Heatmap
visualisiert. Da in den Sozialwissenschaften Ursache und Wirkung nicht
im gleichen Mass isoliert werden können wie in den Naturwissenschaften,
wurde die Schwelle für eine starke Korrelation wurde bei 0.3 angesetzt.

*Begründung der Schwelle von 0.3*

## Beschreibung der Vorgehensweise

## Begründung, weshalb die Methode erfolgreich war
Es hat sich gezeigt, dass die Auswertung von Noten von Absolventinnen und Absolventen der
Informatikmittelschule den grössten Erkenntnisgewinn ergeben.

In der Informatikmittelschule (IMS) werden in der schulisch
orientierten Grundbildung (SOG) Lernende zu
Informatiker/innen EFZ, Fachrichtung Applikationsentwicklung,
ausgebildet.
Der Lehrgang orientiert sich aus historischen Gründen sehr stark am
Modell der Handelsmittelschule im Kanton Zürich. Dies hat zur Folge,
dass parallel eine Berufsausbildung als Applikationsentwickler und eine
Berufsmittelschule mit einer Berufsmatur Ausrichtung Wirtschaft
absolviert werden. Diese Kombination einer technischen Berufslehre und
einer kaufmännischen Berufsmatur stellt eine Besonderheit dar. Angehende
Applikationsentwicklerinnen und Applikationsentwickler
in der betrieblich orientierten Grundbildung (BOG) erwerben, wenn sie
das den wollen, in der Regel eine Berufsmatur mit technischer
Ausrichtung[@sbfiBerufsmaturitaet].   

Als weitere Besonderheit findet in der IMS per Ende eines jeden
Semesters eine promotionswirksame Beurteilung statt. Dabei kommt der
Leistung in der Berufsbildung lediglich ein Gewicht von etwas mehr als
10% zu. Die so gesetzte Anreizstruktur führt gelegentlich dazu, dass die
Lernenden die Prioritäten eher auf die Fächer der BMS legen. Das heisst
allerdings nicht, dass sie in beruflicher Hinsicht schlecht qualifiziert
wären. Die Lernenden der IMS belegen überdurchschnittlich oft
Spitzenplätze bei der kantonalen Rangierung aller Lernenden in den
ICT-Berufen. 


Diese Ausgangslage
ermöglicht es, Leistungen im Fachbereich Informatik mit Leistungen im
Bereich Allgemeinbildung zu korrelieren. Dazu stehen aus der
Berufsausbildung (Berufsschule) 15 Noten aus Modulen mit einer
grossen Nähe zu dem, was CT ausmacht, und 16 Noten mit allgemeinen
beruflichen Inhalten sowie aus der
Allgemeinbildung (BMS) 7 Noten aus dem Grundlagenbereich
und zwei Noten aus kaufmännischen Fächern zur Verfügung.

Von besonderem Interesse sind die Korrelationen zwischen den Noten der
CT Module und den Noten des Grundlagenbereichs der BMS. Wenn die
Noten hier korrelieren, ist das ein Indiz für die Gültigkeit der
Arbeitshypothese. Wenn keine Korrelation festgestellt werden kann, muss
die Arbeitshypothese verworfen werden.
