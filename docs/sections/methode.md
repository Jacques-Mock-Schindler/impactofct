# Methode

In diesem Abschnitt wird dargelegt, wie die Arbeitshypothese überprüft
wird. Aus der Arbeitshypothese ergibt sich folgende Frage:

Ist Computational Thinking eine hilfreiche Grundlage für das Lernen im
Allgemeinen?

Um diese Frage zu beantworten, wurden drei methodische Ansätze
verwendet.

1. Ein natürliches Experiment, in welchem die Auswirkungen von CT auf
   den Lernerfolg von Schulklassen überprüft wird.
2. Qualitative Interviews, mit welchen erhoben wird, wie Schülerinnen
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
Kontokorrentkonto](docs/graphics/uml_konotkorrentkonto.svg){#fig:uml}

Als Kontrollgruppe konnte im WG eine der Parallelklassen verwendet
werden, welche das Zinsrechnen auf konventionellem Weg erarbeitet hat.
In der IMS musste in Ermangelung von Paralleklassen auf eine Klasse der
HMS als Kontrollgruppe zurückgegriffen werden. Dass die Kontrollgruppe
für die IMS aus einem anderen Schultyp stammte, war nicht so schlimm,
weil beide Schultypen im Wirtschaftsunterricht über das selbe Curriculum
verfügten.

### Begründung für die Wahl des natürlichen Experiments

Weil es eigentlich wünschenwsert wäre, die Gültigkeit einer
Arbeitshypothese experimentell zu überprüfen, liegt es auf der Hand,
entdeckte natürliche Experimente zu verwenden.

Neben der Verfügbarkeit sprachen aber auch die inhaltliche Ausgestaltung
des natürlichen Experiments für dessen Auswahl. Flossen doch
alle Aspekte von CT in den Unterricht
ein.  
Wie das geschehen ist, kann mit dem Klassendiagramm illustriert
werden (vgl. @fig:uml). Die Aufgabe, ein Kontokorrentkonto zu
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

Die Stichprobem
waren in beiden Teilexperimenten (WG bzw. IMS/HMS) zu klein, um
statistisch signifikatnte Aussagen zuzulassen.

*Wie gross müsste die Stichprobe sein?*

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

Die Resultate waren damit nicht so, wie sie erwartet worden sind.

Dass das natürliche Experiment dazu geführt hat, dass die Testklassen
schlechter abgeschnitten haben, als die Kontrollklassen scheint trotz
der Resultate wenig plausibel. Wahrscheinlicher ist, dass die
Störvariabeln doch einen viel grösseren Einfluss haten, als das zu
Beginn vermutet worden ist. Das würde lediglich bestätigen, dass die
Varianz in der Leistung zwischen Klassen oft gross ist, oft sogar
grösser als die Varianz zwischen einzelnene
Schulen[@wurstersebastianSchulUndUnterrichtsqualitaet2022, S. 28].


## Qualitatives Interview

Qualitative Interviews entsprechen nicht der gängigen Vorstellung von
Interviews, wie man sie aus den Medien kennt. Qualitative Interviews
sind eher durch den Interviewer moderierte Erzählungen des Interviewten.  

>Der grösste Fehler qualitativer Interviewführung liegt [denn auch]
>darin, zu viel vorzugeben und abzufragen
>[...][@helfferichLeitfadenUndExperteninterviews2022, S. 878].

Das bedeutet allerdings nicht, dass das qualitative Interview völlig
unstrukturiert ist. Es bedarf der gleich sorgfältigen Planung, wie jedes
andere Interview.

### Planung der qualitativen Interviews

>Je stärker das Forschungsinteresse auf konkrete, offen erhobene
>Informationen ausgerichtet ist, desto mehr Strukturierung verträgt das
>Interview und desto mehr Vorgaben sind
>gerechtfertigt[@helfferichLeitfadenUndExperteninterviews2022, S. 880]. 

Um dem qualitativen Interview Struktur zu geben, wird ein Leitfaden für
das Interview verfasst. Dieser Leitfaden kann entweder aus einer Reihe
offener Fragen oder aus mehreren Erzählaufforderungen bestehen.
Verbreitet ist eine Kombination aus konkreten Fragen und
Erzählaufforderungen. Wichtig ist, dass die Fragen offen formuliert
sind, so dass der Interviewte von der eigenen Erfahrung und seinem
Empfinden erzählen kann[@misochQualitativeInterviews2019, S. 66].
Der Leitfaden dient in qualitativen Interviews nicht nur als
Gedankenstütze, er soll ebenso dazu beitragen den Fokus auf der
Forschungsfrage zu
behalten.[@helfferichLeitfadenUndExperteninterviews2022, S. 881;
@misochQualitativeInterviews2019, S. 66]
Damit eine vergleichende Auswertung mehrerer Interviews möglich ist,
wird in allen Interviews der gleiche Leitfaden verwendet.

Konkret wurde für die durchgeführten Interviews eine Kombination aus
Erzählaufforderungen und ausformulierten Fragen (als Gedankenstützten)
erstellt. Für einen Themenbereich wurde ein UML-Klassendiagramm
erstellt, damit die Interviewpartner besser in der Lage waren, sich an
den Kontext der Frage zu erinnern.

### Durchführung der qualitativen Interviews

Es wurden insgesamt vier qualitative Interviews geführt. Alle vier
Interviews haben das gleiche Resultat hervorgebracht.  
Im Rahmen dieser Gespräche hat sich allerdings
gezeigt, dass das Gefälle zwischen Schülerinnen und Schülern auf der
einen Seite und einem Lehrer auf der anderen Seite zu gross war. Die
Schülerinnen und Schüler sind so stark darauf konditioniert, die
Erwartungen der Lehrerinnen und Lehrer zu erfüllen, dass keine freie
Erzählung ihrerseits erfolgt ist. Die Schülerinnen und Schüler haben
lieber auf konkrete Fragen gewartet. Diese haben sie bereitwillig
beantwortet. Sie haben sich dabei aber stehts bemüht, den Befrager mit
ihren Antworten zufrieden zu stellen.
Dies hat dazu geführt, dass die Arbeitshypothese zwar
bestätigt wurde, dass die Information aber als Antwort auf eine einzige
grosse Suggestivfrage zu verstehen ist.

Die Darstellung der Methoden gliedert sich in zwei Teile: jene Methode,
welche einen effektiven Erkenntnisgewinn ermöglichte und jene Methoden,
die keine greifbaren Resultate zeitigten.

## Auswertung von Noten von Absolventen der Informatikmittelschule

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


### Fazit zu den verworfenen Methoden

Es hätte sich um einen *Mixed Methods* Ansatz empirischer
Sozialforschung[@schreierMixedMethods2020, S. 164] gehandelt.
