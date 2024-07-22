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

In allen drei Schultypen werden Unterrichtsinhalte aus dem Fach
Rechnungswesen vermittelt. Im WG findet dieser Unterricht im Fach
Wirtschaft und Recht in den anderen beiden Schultypen in einem eigenen
Fach statt. Im WG wird ausserdem in den ersten zwei Jahren das
obligatorische Fach Informatik unterrichtet.

In dieser Situation war es möglich, in zwei Klassen als Lernhilfe für
das Zinsrechnen ein Kontokorrentkonto modellieren zu Lassen. Das
Kontokorrentkonto sollte einerseits Buchungen korrekt erfassen und
andererseits verschiedenen Zinsberechnungen vornehmen können. Dazu wurde
in der Klasse das folgende UML Diagramm erarbeitet:

![UML Diagramm Kontokorrentkonto]( docs/graphics/uml_konotkorrentkonto.svg )

1. In einer WG Klasse konnte diese Aufgabe im obligatorischen Fach
   Informatik gestellt werden.  
   Anschliessend konnten die Prüfungsleistungen im Zinsrechnen dieser
   Klasse mit den Prüfungsleistungen zum gleichen Thema einer Klasse
   verglichen werden, welche diese 
   Anwendungsübung im Informatikunterricht nicht bearbeitet hat.  
2. In der IMS hat sich eine ähnliche Gelegenheit ergeben. Dort wurde 
   die Aufgabe im Rahmen des Unterrichts im Fach Rechnungswesen
   bearbeitet.
   Als Kontrollgruppe diente dort eine Klasse aus der HMS.

Wenn die Leistungen der Klassen, welche das Kontokorrentkonto modelliert
haben signifikant besser sind, als die Leistungen der Kontrollklassen,
wäre das ein Indiz für die Korrektheit der Arbeitshypothese. Andernfalls
kann aufgrund der vielen Störvariablen keine Aussage gemacht werden und
es muss nach weiteren Methoden zur Prüfung der Arbeitshypothese gesucht
werden.  
Die Auswertung der Noten der involvierten Klassen hat in beiden Fällen
ergeben, dass die Klassen, welche das Kontokorrentkonto modelliert
haben, in den Prüfungen zum Zinsrechnen schlechter abgeschnitten haben,
als die Kontrollklassen.

Für die Resultate können verschiedene Gründe verantwortlich gemacht
werden. Diese sollen nach den beiden Experimenten getrennt dargestellt
werden. 

1. Im ersten Experiment wurden die Schwierigkeiten der Modellierung des
   Kontokorrentkontos in Python unterschätzt. Die Schülerinnen und
   Schüler waren von der Aufgabenstellung überfordert. Die
   Programmierung des Modells hat so viel Aufmerksamkeit verlangt, dass
   der inhaltliche Aspekt nicht mehr verarbeitet werden konnte.  
   Das Resultat wäre möglicherweise ein anderes gewesen, wenn die
   Schülerinnen und Schüler einerseits deutlich mehr
   Programmiererfahrung mitgebracht hätten und adererseits mehr Zeit zur
   Umsetzung des Auftrags zur Verfügung gestanden hätte.

2. In der IMS konnte die Aufgabenstellung grundsätzlich gelöst werden.  
   Die Resultate beim Vergleich der Leistungen einer Klasse der IMS mit
   einer Klasse der HMS dürften jdeoch nicht zu Letzt den sehr
   unterschiedlichen Charakteren der typischen Lernenden in den beiden
   Schultypen geschuldet sein.  
   Zum Einen handelt es sich bei der Klasse der IMS im Gegensatz zu
   jener der HMS um eine reine Männerklasse. Zum Anderen darf nicht
   vergessen werden, dass die Interessen der Schülerinnen und Schüler in
   IMS und HMS doch recht unterschiedlich sind. Lernende der IMS streben
   eine Tätigkeit als Programmiererinnen und Programmierer an, Lernende
   der HMS entsprechen eher dem traditionellen Bild eines KV Lernenden.

### Qualitatives Interview

Qualitative Interviews entsprechen nicht der gängigen Vorstellung von
Interviews, wie man sie aus den Medien kennt. Qualitative Interviews
sind eher durch den Interviewer moderierte Erzählungen des Interviewten.  

>Der grösste Fehler qualitativer Interviewführung liegt [denn auch]
>darin, zu viel vorzugeben und abzufragen
>[...][@helfferichLeitfadenUndExperteninterviews2022, S. 878].

Das bedeutet allerdings nicht, dass das qualitative Interview völlig
unstrukturiert ist. Es bedarf der gleich sorgfältigen Planung, wie jedes
andere Interview.

#### Planung der qualitativen Interviews

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

#### Durchführung der qualitativen Interviews

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
