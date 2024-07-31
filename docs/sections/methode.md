# Methode

In diesem Abschnitt wird dargelegt, wie die Arbeitshypothese überprüft
wird. Aus der Arbeitshypothese ergibt sich folgende Frage:

Ist Computational Thinking eine hilfreiche Grundlage für das Lernen im
Allgemeinen?

Um diese Frage zu beantworten, wurden drei methodische Ansätze
verwendet.

1. Ein natürliches Experiment, in welchem die Auswirkungen von CT auf
   den Lernerfolg von Schulklassen überprüft wird.
2. Leitfadeninterviews, mit welchen erhoben wird, wie Schülerinnen
   und Schüler die Auswirkungen von CT auf den Lernerfolg beurteilen.
3. Die Gegenüberstellung von Noten aus der beruflichen Grundbildung und
   solchen aus der Allgemeinbildung von Lernenden des Berufes
   Informatiker/in, Fachrichtung Applikationsentwicklung.

## Natürliche Experimente 

Grundsätzlich wäre es wünschenswert, wenn die Arbeitshypothese mit einem
Experiment überprüft werden könnte.

>However, experiments tend to be expensive, and may be impossible for
>ethical reasons. Then statisticans turn to observational
>studies.[@freedmanStatisticalModelsTheory2009, S. 18]

Eine Form einer beobachtenden Studie ist das natürliche Experiment.
Dabei ist ein natürliches Experiment eine
Situation, in welcher sich eine Population zufällig in eine
Behandlungs- und eine Kontrollgruppe
aufteilen[@dunningNaturalExperimentsSocial2012,
S. 15 f; @gerringAppliedSocialScience2017, S. 208 f]. Die Bedingungen
werden vom Beobachter dabei grundsätzlich nicht beeinflusst. Das
bedeutet, dass natürliche Experimente nicht durchgeführt werden können.
Natürliche Experimente werden
entdeckt[@dunningNaturalExperimentsSocial2012, 39 ff].

### Entdeckte natürliche Experimente

An der Kantonsschule Büelrain wurden zwei Situationen gefunden, die sich
als natürliche Experimente zur Beantwortung der Forschungsfrage
eigneten. Die Kantonsschule Büelrain ist eine Zürcher Mittelschule, an
welcher zum Zeitpunkt der Verfassung des vorliegenden Textes drei
Schultypen unterrichtet wurden:

1. Das Wirtschaftsgymnasium (WG)
   
   Das WG führt über vier Jahre zu einer gymnasialen
   Matur mit dem Schwerpunktfach Wirtschaft und Recht. Das WG wird mit
   fünf bis sechs Parallelklassen geführt.

2. Die Handelsmittelschule (HMS)
   
   Die HMS führt nach drei Jahren Vollzeitunterricht und
   einem anschliessenden betrieblichen Praktikum in einer kaufmännischen
   Tätigkeit zu einem Eidgenössischen Fähigkeitszeugnis (EFZ) als
   Kauffrau bzw. Kaufmann mit kaufmännischer Berufsmatur. Die HMS wird
   in der Regel mit zwei Parallelklassen geführt.

3. Die Informatikmittelschule (IMS)
   
   Die IMS führt ebenfalls nach drei Jahren Vollzeitschule und einem
   anschliessenden betrieblichen Praktikum in einem
   Informatikunternehmen zu einem EFZ als Informatiker/in, Fachrichtung
   Applikationsentwicklung, mit kaufmännischer Berufsmatur. Die IMS wird
   in der Regel mit einer Klasse pro Jahrgang geführt.

Die Parallelklassen werden in Fächern mit hohen Stundendotaionen
(drei Lektionen pro Woche und mehr) nach  Möglichkeit von
unterschiedlichen Fachlehrpersonen unterrichtet. Als Parallelklassen
gelten Klassen des gleichen Schultyps im Gleichen Schuljahr.  
Das bedeutet, dass beispielsweise das Fach Mathematik in jeder
dritten WG Klasse von jemand anderem unterrichtet wird. In Fächern mit
tiefen Stundendotationen kann dieser Grundsatz nicht aufrecht erhalten
werden.  
Weil an Zürcher Mittelschulen eine ausgeprägte Methodenfreiheit gilt,
führt das in den einzelnen Klassen zu beträchtlichen Unterschieden
darin, wie bestimmte Inhalte vermittelt werden. Diese Varianz hat die
folgenden natürlichen Experimente ergeben.

### Beschreibung der natürlichen Experimente

In allen drei oben dargestellten Schultypen bilden wirtschaftliche
Inhalte ein Schwerpunkt.
Teil des Unterrichts in diesem Schwerpunkt ist das Fach Rechnungswesen.
Im WG findet der Unterricht im Rechnungswesen als Teil des Faches
Wirtschaft und Recht (WR) statt. In den beiden Schultypen HMS und IMS
wird Rechnungswesen in einem eigenen Fach, Finanz- und Rechnungswesen
(FRW), unterrichtet.  
Im WG wird ausserdem in den ersten zwei Jahren das
obligatorische Fach Informatik (OFI) unterrichtet.

Im Rechnungswesen ist kaufmännisches Rechnen teil des Curriculums.
Kaufmännisches Rechnen ist im Wesentlichen Zinsrechnen. Dabei wird
insbesondere die deutsche Zinsusanz
eingeführt[@hischerKaufmaennischesRechnenWichtigsten2018, S. 102].
Üblicherweise wird die deutsche Zinsusanz zuerst theoretisch eingeführt
und anschliessen mit Anwendungsübungen vertieft.  
Da im WG parallel zum WR-Unterricht das OFI unterrichtet wird, hat dies
die Möglichkeit geboten, die deutsche Zinsusanz mit zusätzlichen
methodischen Ansätzen weiter zu vertiefen. Das
Thema wurde in eine Anwendungsübung für objektorientierte Programmierung
in Python integriert. Die Schülerinnen und Schüler sollten ein
Kontokorrentkonto modellieren und das Modell objektorientiert in Python
implementieren. Dabei sollte das Modell in der Lage sein, den Zins auf
den aktuellen Saldo unter Anwendung der deutschen Zinsusanz auf Tage
genau zu berechnen.  
In der IMS wurde die gleiche Anwendungsübung im Rahmen des Unterrichts
im Fach FRW durchgeführt. Weil die Lernenden der IMS in ihrer
beruflichen Ausbildung das Programmieren in Java lernen, erfolgte die
Implementation in Java.

Die Idee der Anwendungsübung kann in folgendem UML Klassendiagramm
dargestellt werden:

![UML Diagramm
Kontokorrentkonto](../graphics/uml_konotkorrentkonto.svg){#fig-uml}

Als Kontrollgruppe konnte im WG eine der Parallelklassen verwendet
werden, welche das Zinsrechnen auf konventionellem Weg erarbeitet hat.
In der IMS musste in Ermangelung von Paralleklassen auf eine Klasse der
HMS als Kontrollgruppe zurückgegriffen werden. Dass die Kontrollgruppe
für die IMS aus einem anderen Schultyp stammte, war nicht so schlimm,
weil beide Schultypen im Wirtschaftsunterricht über das selbe Curriculum
verfügten.

### Begründung für die Wahl des natürlichen Experiments {#sec-begr_nat_exp}

Weil es eigentlich wünschenwsert wäre, die Gültigkeit einer
Arbeitshypothese experimentell zu überprüfen, liegt es auf der Hand,
entdeckte natürliche Experimente zu verwenden.

Neben der Verfügbarkeit sprachen aber auch die inhaltliche Ausgestaltung
des natürlichen Experiments für dessen Auswahl. Flossen doch
alle Aspekte von CT in den Unterricht
ein.  
Wie das geschehen ist, kann mit dem Klassendiagramm illustriert
werden (vgl. @fig-uml). Die Aufgabe, ein Kontokorrentkonto zu
modellieren, musste in Teilprobleme zerlegt werden. Die Teilprobleme
entsprechen dabei den Klassen. Die Klassen mussten weiter analysiert und
mit Attributen und Methoden versehen werden. Durch die Modellierung des
Problems in Klassen und Unterklassen mit Attributen und Methoden musste
ausserdem von konkreten Beispielen abstrahiert werden. Nur dieses auf
das Notwendige reduzierte Modell eignete sich, wiederkehrende Probleme
zu erkennen und diese einer durch einen Algorithmus gesteuerten Lösung
zuzuführen.  
Ausserdem war die Unterrichtseinheit selbstüberprüfend. Wenn es den
Schülerinnen und Schülern nach der Implementierung in Python oder Java
möglich war, Zinsberechnungen durchzufürhen, war die Aufgabenstellung
offensichtlich erfolgreich gelöst worden.

### Stärken und Schwächen der Untersuchungsanlage

Das Experiment liess erwarten, dass die Prüfungsleistungen im
kaufmännischen Rechnen der beiden Klassen, welche diese
Untrrichtseinheit durchlaufen haben, besser ausfallen würden, als jene
ihrer jeweiligen Kontrollklassen. Ein wesentlicher Vorteil des
Experiments lag daher in der einfachen Auswertung des Resultates. Es
mussten lediglich die Prüfungsleistungen der beteilligten Klassen
miteinander verglichen werden.

Dem standen allerdings mehrere Schwächen gegenüber.

Die Stichproben waren $n_{WG}=26$ und $n_{IMS}=10$. Dies ist viel zu
klein, um eine belastbare Aussage machen zu können. 
Ausgehend von der
allgemeinen für die Abschätzung der Stichprobengrösse verwendeten
Formel

 $$S = \frac{Z^2 \times P \times (1-P)}{M^2}$$

mit

* $S$ = Stichprobengrösse
* $Z$ = $Z$-Wert (hier 1.96 für 95%)
* $P$ = Populationsanteil (hier 0,5 weil unbekannt)
* $M$ = Fehlermarge (hier 0.05 für 5%)[@perenFormelsammlungWirtschaftsstatistikWissen2022]

hätte die Stichprobe $n=385$ sein müssen. Mit der aktuellen
Stichprobengrösse muss man im WG mit einer Fehlermarge von knapp 20% und
in der IMS gar mit einer solchen von etwas mehr als 30% rechnen.

Zudem gibt es verschiedene Störvariabeln, welche das Resultat
verfälschen. Zu nennen ist insbesondere die unterschiedliche
Klassenzusammensetzung. Dies hat nicht nur mit der Stichprobengrösse zu
tun. Jede Schulklasse hat eine eigene Gruppendynamik. Diese
Gruppendynamik kann den Lernerfolg massgeblich beeinflussen. Dieses
Phänomen beeinträchtigt die Aussagekraft des Vergleiches der
Parallelklassen des WG. Noch viel stärker kommt dieses Phänomen zum
Tragen beim Vergleich von Klassen zweier Schultypen. Die HMS und die IMS
haben wohl das selbe Curriculum im Wirtschaftsunterricht, sie stellen
aber ganzu unterschiedliche Soziotope dar. Eine kaufmännische Ausbildung
zieht eher kommunikative Menschen an wohingegen eine Ausbildung als
Applikationsentwickler/in eher technisch interessierte Menschen anzieht.
Dass es sich dabei nicht um ein blosses Cliché handelt, zeigt sich an
den Aufnahmebedingungen zu den beiden Schultypen. Für den Eintritt in
die HMS muss eine Aufnahmeprüfung nach der zweiten oder dritten
Sekundarklasse abgelegt werden. Für die Aufnahme an die IMS muss eine
Aufnahmeprüfung nach der dritten Sekundarklasse abgelegt werden sowie
zusätzlich ein Multichck "ICT Informatiker/in EFZ Fachricthung
Applikationsentwicklung" in den Bereichen "Potenzial" und
"berufsspezifische Fähigkeiten" mit mindestens 50 Punkten bestanden
werden[@ZentraleAufnahmepruefungFuer]. Die IMS richtet sich damit
erklärtermassen an eine spezifische Gruppe von Lernenden.  
Ausserdem ist auch die Methodenfreiheit, welche das Experiment
eigentlich erst ermöglicht hat, auch eine Störvariabel. Nicht allen
Lehrpersonen liegen alle Themen gleich gut. Der Einfluss dieses
Umstandes konnte im vorliegenden Experiment nicht isoliert werden.

Trotz der offensichtlichen Schwächen des natürlichen Experiments bestand
die Hoffnung, dass der Effekt so stark sein würde, dass er den Einfluss
der Störvariabeln überdecken würde.

### Durchführung der natürlichen Experimente

In der Klasse des WG fanden die Einführung ins Zinsrechnen und die
Informatikanwendungsübung dazu unabhängig voneinander statt. Die
Einführung ins Zinsrechnen erfolgte im WR Unterricht und die
Anwendungsübung im OFI. Da die beiden Unterrichtseinheiten mit
zeitlichem Abstand stattfanden, musste im OFI eine Repetition zum
Zinsrechnen stattfinden, bevor die Anwendungsübung zum Kontokorrentkonto
durchgeführt werden konnte.

Die Anwendungsübung zum Kontokorrenktonto bildete gleichzeitig den
Anlass zur Einführung in die objektiorientierte Programmierung in
Python. Mit der Idee den Schülerinnen und Schülern Unterstützung zu
bieten, wurde ihnen ein fertiges UML Klassendiagramm abgegeben. Anhand
dieses Diagrammes wurden sowohl die inhaltlichen Aspekte des
Kontokrrentkontos wie auch die technischen Aspekte der
objektkorientierten Programmierung besprochen.  
Anschliessend haben die Schülerinnen und Schüler eine Einführung in die
Programmierung von Klassen erhalten und haben versucht, die neuen
Kenntnisse am Beispiel des Kontokorrentkontos anzuwenden.

Es hat sich, im Rückblick wenig überraschend, gezeigt, dass die
Informatikkenntnisse der Schülerinnen und Schüler nicht gut genug waren,
um die Aufgabe lösen zu können. Die Komplexität des Werkzeuges
Informatik war so gross, dass es den Blick auf die Probleme der
Zinsrechnung verstellt hat.

In der Klasse der IMS konnte auf die Informatikkenntnissen der
Berufsausbildung zurückgegriffen werden. Die Lernenden der IMS hatten zu
diesem Zeitpunkt bereits sechs mal Mehr Informatikunterricht erhalten
als die Schülerinnen und Schüler des WG. In der IMS sind 12
Wochenlektionen für den Informatikunterricht vorgesehen, im WG 2. Die
Lernenden der IMS waren also mit den Grundzügen der objektorientierten
Programmierung bereits vertraut. Aussesrdem wird in der IMS
Programmieren mit Java unterrichtet.  
Obwohl also die Ausgangslage für das Untrrichtsmodul Kontokorrentkonto
deutlich besser waren als im WG, wurde das Klassendiagramm zusammen mit
den Lernenden entwickelt.  
Die Lernenden waren denn auch in der Lage, das Modell zu implementieren.
Nach Aussagen der Lernenden, hat ihnen die Implementation des Modells
den Blick für die Details des Zinsrechnens und die Grenzfälle der
Tageberechnung geschärft.

### Auswertung der Resultate des natürlichen Experiments

Nach der Durchführung des Experiments wurden trotz dessen
offensichtlicher Schwächen in Konzeption und Durchführung die Resultate
der Testklassen mit den Resultaten der jeweiligen Kontrollklassen
verglichen.

Die Schülerinnen und Schüler der WG Testklasse haben im Durschnitt 67.3%
der möglichen Punkte in der Aufgabe zum Zinsrechnen erreicht, die
Schülerinnen und Schüler der Kontrollklasse 80.4%. Die
Gegenüberstellungen der Leistungen von IMS und HMS haben die Lernenden
der IMS 77.1% und die Lernenden der HMS 80.4% erreicht.  

Aufgrund des durch die Stichprobe möglichen Fehlers wäre es möglich,
dass die Leistungen in der Gesamtpopulation durch die Anwendungsübung
tatsächlich verbessert werden könnte. Allerdings müssten Test- und
Kontrollgruppe sich im WG mit den erzielten Resultaten je am äussersten
Rand der jeweiligen Bandbreite an Resutlaten bewegen. In der IMS müsste
die Bandbreite aufgrund des grösseren Fehlers etwas weniger stark
ausgereizt worden sein.   
Unabhängig von dem, was statistisch denkbar wäre, entsprachen die
Resultate nicht den Erwartungen.

Dass das natürliche Experiment dazu geführt hat, dass die Testklassen
schlechter abgeschnitten haben, als die Kontrollklassen scheint trotz
der Resultate wenig plausibel. Wahrscheinlicher ist, dass die
Störvariabeln doch einen viel grösseren Einfluss haten, als das zu
Beginn vermutet worden ist. Das würde lediglich bestätigen, dass die
Varianz in der Leistung zwischen Klassen oft gross ist, oft sogar
grösser als die Varianz zwischen einzelnene
Schulen[@wurstersebastianSchulUndUnterrichtsqualitaet2022, S. 28].

Weil das Problem der Stichprobengrösse bereits in der Planung erkannt
worden ist, sollte das natürliche Experiment durch Leitfadenintervies
ergänzt werden.

## Leitfadeninterview

Leitfadeninterviews entsprechen nicht der gängigen Vorstellung von
Interviews, wie man sie aus den Medien kennt. Leitfadeninterviews
sind eher durch den Interviewer moderierte Erzählungen des Interviewten.  

>Der grösste Fehler qualitativer Interviewführung liegt [denn auch]
>darin, zu viel vorzugeben und abzufragen
>[...][@helfferichLeitfadenUndExperteninterviews2022, S. 878].

Das bedeutet allerdings nicht, dass das Leitfadeninterview völlig
unstrukturiert ist. Es bedarf wie jede andere wissenschaftliche
Befragung der sorgfältigen Planung.

### Planung der Leitfadeninterviews

>Je stärker das Forschungsinteresse auf konkrete, offen erhobene
>Informationen ausgerichtet ist, desto mehr Strukturierung verträgt das
>Interview und desto mehr Vorgaben sind
>gerechtfertigt[@helfferichLeitfadenUndExperteninterviews2022, S. 880]. 

Um dem Leitfadeninterview Struktur zu geben, wird vor der Durchführung
ein Leitfaden für das Interview verfasst. Dieser Leitfaden kann entweder
aus einer Reihe
offener Fragen oder aus mehreren Erzählaufforderungen bestehen.
Verbreitet ist eine Kombination aus konkreten Fragen und
Erzählaufforderungen. Wichtig ist, dass die Fragen offen formuliert
sind, so dass der Interviewte von der eigenen Erfahrung und seinem
Empfinden erzählen kann[@misochQualitativeInterviews2019, S. 66].
Der Leitfaden dient nicht nur als
Gedankenstütze, er soll ebenso dazu beitragen den Fokus auf der
Forschungsfrage zu
behalten[@helfferichLeitfadenUndExperteninterviews2022, S. 881;
@misochQualitativeInterviews2019, S. 66].
Der Leitfaden soll als Anleitung an den Gesprächsmoderatoren dienen.  
Damit eine vergleichende Auswertung mehrerer Interviews möglich ist,
wird in allen Interviews der gleiche Leitfaden verwendet.

Der Interviewleitfaden besteht aus einer Kombination von
Erzählaufforderungen und ausformulierten Fragen. Die ausformulierten
Fragen dienen als Gedächtnisstützen. Ausserdem sollen sie gestellt
werden können, falls die Erzählaufforderung sich als nicht zielführend
erweist. Da als Gesprächspartnerinnen bzw. Gesprächspartner nur
Schülerinnen und Schüler bzw. Lernende aus den beiden Testklassen in
Frage gekommen sind, wurde der Leitfaden mit dem UML Klassendiagramm
aus @fig-uml ergänzt. Dieses sollte den Befragten als
Erinnerungshilfe vorgelegt werden können.
Der für die Interviews verwendete Leitfaden findet sich im Anhang.

Wie bereits erwähnt, kamen als Gesprächspartnerinnen bzw.
Gesprächspartner nur Angehörige der Testklassen in Frage.
Interessentinnen bzw. Interessenten konnten sich direkt in einen Termin
in einem eigens dafür vorgesehenen Kalender eintragen. Dies sollte die
Diskretion unter den Angehörigen der Testklassen sicherstellen.

### Begründung für die Wahl von Leitfadeninterviews als Methode

Da Lernen ein psychologischer Prozess ist, der nicht direkt beobachtet
werden kann, muss der Vorgang des Lernens indirekt erschlossen werden.
Standardmässig gechieht dies durch die Kontrolle des Lernerfolges in
Prüfungen. Das hätte duch das natürliche Experiment ausgenutzt werden
sollen. Allerdings hätte dies lediglich ermöglicht, die Gültigkeit
der Arbeitshypothse zu belegen. Selbst wenn dies gelungen wäre, hätte
damit die Frage, warum die Arbeitshypothese bestätigt worden ist, nicht
beantwortet werden können. Dies ist eine qualitative Frage.

Um diese Frage beantworten zu können, muss auf das Erleben der
Schülerinnen und Schüler bzw. der Lernenden abgestellt werden. Da dieses
genausowenig direkt beobachtbar ist wie das Lernen, muss es erfragt
werden. Das Erleben einer Lernsituation ist allerdings zu individuell,
als das es mit einem standardisierten Fragebogen erhoben werden könnte.
Das Leitfadeninterview bietet hier eine Möglichkeit, diesem Umstand
zu begegnen. Mit dem Erfragen des Lernerlebnisses kann die
möglicherweise die Frage, weshalb die Arbeitshyptohese gilt, beantwortet
werden.

### Durchführung der Leitfadeninterviews

Die Rekrutierung von Gesprächspartnerinnen und Gesprächspartnern
gestaltete sich schwieriger als geplant. Auf die allgemeine Einladung
hat zuerst niemand reagiert. Erst auf gezielte Einladung haben sich
einzelne Schülerinnen und Lernende zu einem Gespräch bereit erklärt. Die
angestrebte Zahl an Gesprächspartnerinnen und Gesprächspartnern konnte
nicht erreicht werden. Insgesamt wurden lediglich vier Gespräche
geführt. Alle vier
Interviews haben das gleiche Resultat hervorgebracht.  

Im Rahmen dieser Gespräche hat sich allerdings
gezeigt, dass das Gefälle zwischen Schülerinnen und Schülern auf der
einen Seite und einem Lehrer auf der anderen Seite zu gross war. Die
Schülerinnen und Schüler sind so stark darauf konditioniert, die
Erwartungen der Lehrerinnen und Lehrer zu erfüllen, dass keine freie
Erzählung ihrerseits erfolgt ist. Dies dürfte nicht zuletzt ihrem  Alter
geschuldet sein[@helfferichLeitfadenUndExperteninterviews2022, S. 876].
Die Gesprächspartnerinnen und Gesprächspartner haben sich ehrlich
bemüht, die gewünschten Auskünfte zu erteilen. Sie haben aber lieber auf
konkrete Fragen gewartete, als dass sie von sich aus erzählt hätten.
Ausserdem war stets ihr Bemühen zu erkennen, den Befrager mit ihren
Antworten zufrieden zu stellen.

Nach der Durchführung ist beim Befrager der Eindruck zurückgeblieben, er
hätte eine einzige grosse Suggestivfrage gestellt.

### Auswertung der Interviews

Als Gesprächspartnerinnen bzw. Gesprächspartner standen zwei
Schülerinnen des WG und zwei Lernende der IMS zur Verfügung.
In den Interviews zeigte sich, dass Lernende der IMS über etwas mehr
vorschulische Programmiererfahrungen verfügten als die Schülerinnen
des WG. Übereinstimmend wurde festgehalten, dass durch
das Programmieren einer Lösung zu einem Problem, das Problem besser
verstanden würde. Insbesondere die Schülerinnen des WG
wiesen jedoch darauf hin, dass beträchtliche Programmierkenntnisse
vorhanden sein müssen, damit von diesem Effekt profitiert werden kann.

Die Aussagen deckten sich damit mit den Erwartungen.

Dies ist hier allerdings ein Grund, am Wert der Aussagen zu zweifeln.
Wie bei der Beschreibung der Durchführung bereits festgehalten, ist
keine spontane Erzählung zustande gekommen. Die Gesprächspartnerinnen
und Gesprächspartner waren zu stark darauf bedacht, zu erzählen, was der
Befrager hören wollte, dass den Aussagen kein eigener Wert zukommt. Sie
haben lediglich die der Arbeitshypothese zu Grunde liegenden Annahmen
verstärkt.

Aus den Interviews ergab sich daher kein Erkenntnisgewinn.  
Dies führte dazu, dass nach einer weiteren Möglichkeit gesucht wurde, um
die Arbeitshypothese zu überprüfen. Diese hat sich aus der Natur der
Ausbildung an der IMS ergeben.

## Fazit zu den verworfenen Methoden

Mit den verworfenen Methoden hätte ein sogenannter *Mixed Methods*
Ansatz empirischer Sozialforschung[@schreierMixedMethods2020, S. 164]
verfolgt werden sollen. Es hat sich allerdings gezeigt, dass der
Mittelansatz dazu unzureichend ist. Für das natürliche Experiment war
die Population zu klein und für die Leitfadeninterviews konnte keine
Gesprächssituation geschaffen werden, in welcher die
Gesprächspartnerinnen und Gesprächspartner unbeeinflusst vom Befrager
Auskunft geben konnten.

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

### Begründung der Wahl der Methode {#sec-kernbegruendung}

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
Die Noten der Module werden dabei als Ursache und jene der BMS als
Wirkung behandelt.  
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

Die ausgewerteten Daten stammen von einer Zürcher Mittelschule und sind
nicht öffentlich verfügbar. Möglicherweise hätten die Daten gestützt auf
§ 18 des Gesetzes über die Information und den Datenschutz (IDG) des
Kantons Zürich verfügbar gemacht werden können. Dieser Schritt war
vorliegend allerdings nicht erforderlich, da der Verfasser als
Mitarbeiter Zugriff auf den Datenbestand hatte.

Die Daten waren der IMS waren auf Papier, jene der HMS als PDF
archiviert. Damit jederzeit wieder auf die Daten der IMS zugegriffen
werden kann, wurden diese vor der eigentlichen Erfassung eingescannt.  
Die Form der Archivierung machte es in einem ersten Schritt nötig, die
relevanten Informationen abzuschreiben. Die manuelle Datenerfassung ist
Fehleranfällig und musste daher aus Konzentrationsgründen in mehrere
Phasen unterteilt werden. Ausserdem mussten die erfassten Daten
kontrolliert werden. Damit diese Kontrolle einfacher erfolgen konnte,
wurden die Namen und Klassen erst nach erfolgter Kontrolle gehasht. 

Die Daten wurden in CSV-Dateien zur Weiterverarbeitung abgespeichert. Es
wurden dazu die folgenden drei Tabellen erstellt:

* Personalien

    In dieser Tabelle wurden Name, Klasse, Gender und Alter erfasst. Aus
    Gründen des Persönlichkeitsschutzes wurden Namen und Klassen mit
    SHA256 gehasht und nur der Hashwert abgespeichert. Dies ermöglicht
    trotz Anonymisierung die Zuordnung der erfasste Noten zu einer
    Person. Ausserdem würde die Erfassung von Alter und Gender
    gegebenenfalls weitere Auswertungen zulassen.

* Noten der Berufsausbildung

    In dieser Tabelle wurden die Noten der Besuchten Module erfasst.  
    Der Hashwert dient dabei als Identifikator.

* Noten der BMS

    In  dieser Tabelle wurden die Noten der BMS Abschlussprüfungen
    erfasst.  
    Der Hashwert dient auch hier als Identifikator.

Die Aufteilung der Daten in drei Tabellen hatte zum Einen praktische
Gründe. Die Tabellen behielten überschaubare Dimensionen. Andererseits
brauchen die Daten bei der Analyse nicht nach Herkunft gefiltert zu
werden.

Eine Beurteilung der Qualität der Daten erfolgt im Abschnitt "Daten" vor
der Analyse der Resultate.

Die Auswertung der Daten erfolgte in einem Python Skript. In diesem
Skript wurden die Daten in pandas Datafram geladen. Die Analyse erfolgte
mit den durch SciPy.stats zur Verfügung gestellten Funktionen
`normaltest()`, `shapiro()` und `kstest()` sowie die durch pandas zur
Verfügung gestellten Funktionen `spearman()` und `df.corr()`.  

Die Visualisierung als Heatmap wurde mit Hilfe der Libraries matplotlib
und seaborn erstellt. Um die relevante Schwelle der Korrelation von 0.3
sichtbar zu machen, wurde ein eigenes Farbschema angelegt. Dieses
Farbschema wechselt von Grau zu Grün. Die Schwelle des für den Umschlag
der Farbe wurde dabei auf 0.3 festgelegt.

Das Skript wird im Anhang abgedruckt. Ebenfalls im Anhang findet sich
ein Abdruck der Ausgabe von pip freeze. Damit soll die
Nachvollziehbarkeit der Resultate sichergestellt werden.
