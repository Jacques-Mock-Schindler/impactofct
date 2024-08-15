# Methoden {#sec:methode}

In diesem Abschnitt wird dargelegt, wie die Arbeitshypothese überprüft
werden soll. Damit dies einfacher möglich ist, kann die Arbeitshypothese
in die folgende Forschungsfrage umformuliert werden:

>Hilft die Anwendung von Computational Thinking beim Lernen?

Um diese Frage zu beantworten, wurde auf drei unterschiedliche
methodische Ansätze abgestellt.

1. Ein natürliches Experiment, mit welchem versucht wurde die
   Auswirkungen von Computational Thinking auf den Lernerfolg von
   Schulklassen zu überprüfen.

2. Leitfadeninterviews, mit welchen versucht wurde zu erheben, wie
   Schülerinnen und Schüler die Auswirkungen von Computational Thinking
   auf den Lernerfolg beurteilen.

3. Eine statistische Auswertung der Noten aus der Berufsausbildung und
   solchen aus der Allgemeinbildung von Lernenden des Berufes
   Informatiker/in, Fachrichtung Applikationsentwicklung. Damit soll
   festgestellt werden, ob die Leistungen aus den beiden Teilbereichen
   miteinander korrelieren.

## Natürliche Experimente {#sec:nat_exp}

Grundsätzlich wäre es wünschenswert, wenn die Arbeitshypothese mit einem
Experiment überprüft werden könnte.

>However, experiments tend to be expensive, and may be impossible for
>ethical reasons. Then statisticans turn to observational
>studies.[@freedmanStatisticalModelsTheory2009, S. 18]

Eine Form einer beobachtenden Studie ist das natürliche Experiment.
Dabei ist ein natürliches Experiment eine
Situation, in welcher sich eine Population zufällig in eine
Test- und eine Kontrollgruppe
aufteilen[@dunningNaturalExperimentsSocial2012,
S. 15 f; @gerringAppliedSocialScience2017, S. 208 f]. Die Bedingungen
werden vom Beobachter dabei grundsätzlich nicht beeinflusst. Das
bedeutet, dass natürliche Experimente nicht durchgeführt werden können.
Natürliche Experimente werden
entdeckt[@dunningNaturalExperimentsSocial2012, 39 ff] und dann
beobachtet.

### Entdeckte natürliche Experimente

An der Kantonsschule Büelrain wurden zwei Situationen gefunden, die sich
als natürliche Experimente zur Beantwortung der Forschungsfrage
grundsätzlich eigneten. 
Damit die Rahmenbedingungen der entdeckten Experimente nachvollzogen
werden können, werden hier die Eckdaten der Kantonsschule
Büelrain kurz beschrieben.

Die Kantonsschule Büelrain ist eine Zürcher Mittelschule mit ungefähr
750 Schülerinnen und Schülern. Zum Zeitpunkt der Verfassung des
vorliegenden Textes wurden an der Kantonsschule Büelrain drei
Schultypen unterrichtet:

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
   Informatikunternehmen oder der Informatikabteilung eines Unternehmens
   aus einer anderen Branche zu einem EFZ als Informatiker/in,
   Fachrichtung Applikationsentwicklung, mit kaufmännischer Berufsmatur.
   Die IMS wird in der Regel mit einer Klasse pro Jahrgang geführt.

Die Parallelklassen werden in Fächern mit hohen Stundendotaionen
(drei Lektionen pro Woche und mehr) nach  Möglichkeit von
unterschiedlichen Fachlehrpersonen unterrichtet. Als Parallelklassen
gelten Klassen des gleichen Schultyps im gleichen Schuljahr.  
Das bedeutet, dass beispielsweise das Fach Mathematik in jeder
WG Klasse im dritten Schuljahr von jemand anderem unterrichtet wird. In
Fächern mit
tiefen Stundendotationen kann dieser Grundsatz nicht aufrecht erhalten
werden.

Weil an Zürcher Mittelschulen eine ausgeprägte Methodenfreiheit gilt,
führt diese Organisation in den einzelnen Klassen zu beträchtlichen
Unterschieden,
wie bestimmte Inhalte vermittelt werden. Diese Unterschiede haben
die folgenden natürlichen Experimente ergeben.

### Beschreibung der natürlichen Experimente

In allen drei oben dargestellten Schultypen bilden wirtschaftliche
Inhalte ein Schwerpunkt.
Teil des Unterrichts in diesem Schwerpunkt ist das Fach Rechnungswesen.
Im WG findet der Unterricht im Rechnungswesen als Teil des Faches
Wirtschaft und Recht (WR) statt. In den beiden Schultypen HMS und IMS
wird Rechnungswesen in einem eigenen Fach, Finanz- und Rechnungswesen
(FRW), unterrichtet.  
Für das natürliche Experiment ist ausserdem von Bedeutung, dass im WG in
den ersten zwei Jahren das obligatorische Fach Informatik (OFI)
unterrichtet wird. 

Im Rechnungswesen ist kaufmännisches Rechnen Teil des Curriculums.
Kaufmännisches Rechnen ist im Wesentlichen Zinsrechnen. Dabei wird
insbesondere die deutsche Zinsusanz
eingeführt[@hischerKaufmaennischesRechnenWichtigsten2018, S. 102]. Die
deutsche Zinsusanz ist eine Vereinfachung der Zinsberechnung. In dieser
Methode wird mit zwölf Monaten à 30 Tagen und einem Jahr mit 360 Tagen
gerechnet.
Üblicherweise wird die deutsche Zinsusanz zuerst theoretisch eingeführt
und anschliessend mit Anwendungsübungen vertieft.

Die konkreten Experimente bestanden darin, dass die Testklassen als
Anwendungsübung einen Programmierauftrag zur deutschen Zinsusanz
bearbeiteten. Der Auftrag hat vorgesehen, dass ein Kontokorrentkonto
objektorientiert modelliert wurde. Dabei sollte das Kontokorrentkonto
Methoden zur Verfügung stellen, um tagegenau den Zins auf dem jeweiligen
Saldo des Kontokorrentkontos zu berechnen. Das Konzept des
Programmierauftrags kann dem UML-Klassendiagramm in [@fig:uml] entnommen
werden.

```{=latex}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/uml_kontokorrentkonto.png}
\caption[UML Diagramm Kontokorrentkotno]{Das UML Diagramm zeigt das
Klassendiagramm, das im natürlichen Experiment implementiert werden
sollte. Das Design wurde so gestaltet, damit das Problem zergliedert
werden musste. Die Vererbung Konto $\leftarrow$ Bilanzkonto $\leftarrow$
Kontokorrentkonto erzwang darüber hinaus eine gewisse Verallgemeinerung.
Die grau hinterlegte Klasse Erfolgskonto soll lediglich andeuten, dass
weitere Kontenklassen implementiert werden könnten.}
\label{fig:uml}
\end{figure}
```

Zur Überprüfung der Auswirkung der zusätzlichen Anwendungsübung wurden
die Prüfungsergebnisse von Aufgaben zum Zinsrechnen aus Prüfungen der
Testklassen mit solchen aus Kontrollklassen verglichen.

Da im WG parallel zum WR-Unterricht das OFI unterrichtet wird, bot dies
die Möglichkeit, im Rahmen des OFI die deutsche Zinsusanz in
Pyhton zu implementieren. Hier wurde von den Grundsätzen des natürlichen
Experiments insofern abgewichen, als dass diese Anwendungsübung bewusst
im Hinblick auf die Beantwortung der Forschungsfrage angelegt worden
ist. Dies war im Rahmen der Methodenfreiheit zu verantworten.  
Als Kontrollklasse diente eine WG Klasse, welche im OFI andere
Anwendungsübungen zur objektorientierten Programmierung gemacht hat.

In der IMS wurde die gleiche Anwendungsübung im Rahmen des Unterrichts
im Fach FRW durchgeführt. Hier stellte das Programmieren einfach eine
methodische Variante zu den konventionellen Anwendungsübungen aus dem
Lehrmittel dar. Weil die Lernenden der IMS in ihrer
beruflichen Ausbildung das Programmieren in Java lernen, erfolgte die
Implementation in Java.  
Weil die IMS keine Parallelklasse hat, diente eine Klasse der HMS als
Kontrollklasse.

### Begründung für die Wahl des natürlichen Experiments {#sec:begr_nat_exp}

Weil es eigentlich wünschenswert wäre, die Gültigkeit einer
Arbeitshypothese experimentell zu überprüfen, liegt es auf der Hand,
entdeckte natürliche Experimente zu verwenden.

Neben der Verfügbarkeit sprachen aber auch die inhaltliche Ausgestaltung
des natürlichen Experiments für dessen Auswahl. Die Anwendungsübung hat
alle Aspekte von Computational Thinking in den Unterricht einfliessen
lassen.

Wie das geschehen ist, kann mit dem UML Klassendiagramm aus [@fig:uml]
illustriert
werden. Die Aufgabe, ein Kontokorrentkonto zu
modellieren, musste in Teilprobleme zerlegt werden. Die Teilprobleme
entsprechen dabei den Klassen. Die Klassen mussten weiter analysiert und
mit Attributen und Methoden versehen werden. Durch die Modellierung des
Problems in Klassen und Unterklassen mit Attributen und Methoden musste
ausserdem von konkreten Beispielen abstrahiert werden. Nur dieses auf
das Notwendige reduzierte Modell eignete sich, wiederkehrende Probleme
zu erkennen und diese einer durch einen Algorithmus gesteuerten Lösung
zuzuführen. Die Implementierung in den Programmiersprachen Python bzw.
Java stellte dann die konkretisierte algorithmische Lösung dar.  
Ausserdem war die Unterrichtseinheit selbstüberprüfend. Wenn es den
Schülerinnen und Schülern nach der Implementierung in Python oder Java
möglich war, Zinsberechnungen durchzuführen, war die Aufgabenstellung
offensichtlich erfolgreich gelöst worden.

### Stärken und Schwächen der Untersuchungsanlage

Das Experiment liess erwarten, dass die Prüfungsleistungen im
kaufmännischen Rechnen der beiden Klassen, welche diese
Unterrichtseinheit durchlaufen haben, besser ausfallen würden, als jene
ihrer jeweiligen Kontrollklassen. Ein wesentlicher Vorteil des
Experiments lag daher in der einfachen Auswertung des Resultates. Es
mussten lediglich die Prüfungsleistungen der Test- mit jener der
Kontrollklasse
verglichen werden.

Dem standen allerdings mehrere Schwächen gegenüber.

Die Stichproben waren $n_{WG}=26$ und $n_{IMS}=10$. Dies ist viel zu
klein, um eine belastbare Aussage machen zu können. 
Ausgehend von der
allgemeinen für die Abschätzung der Stichprobengrösse verwendeten
Formel

 $$n = \frac{Z^2 \times P \times (1-P)}{M^2}$$ {#eq:stichprobe}

mit

* $n$ = Stichprobengrösse
* $Z$ = $Z$-Wert (hier 1.96 für 95%)
* $P$ = Populationsanteil (hier 0,5 weil unbekannt)
* $M$ = Fehlermarge (hier 0.05 für 
    5%)[@perenFormelsammlungWirtschaftsstatistikWissen2022, S. 147]

hätte die Stichprobe $n=385$ sein müssen. 

Da die Stichprobe viel kleiner ist, soll hier der Fehlerbereich (Margin
of Error, MoE)
berechnet werden. Die Berechnung des Fehlerbereichs erfolgt nach der
Formel

$$
MoE = z \cdot \sqrt{\frac{p(1-p)}{n}\cdot \frac{N-n}{N-1}}
$$ {#eq:moe}

wobei

* $z =$ z-Wert für das Konfidenzniveau (für 95% ist z  1.96),
* $p =$ die geschätzte Erfolgswahrscheinlichkeit (wenn unbekannt, wird oft
  0.5 verwendet, da dies die maximale Variabilität darstellt),
* $n =$ die Stichprobengrösse ist,
* $N =$ die Populationsgröße ist[@ramachandranStatisticalEstimation2021, S. 223].

Mit der aktuellen
Stichprobengrösse muss man im WG mit einer Fehlermarge von knapp 19% und
in der IMS gar mit einer solchen von etwas mehr als 30% rechnen.

Zudem gibt es verschiedene Störvariabeln, welche das Resultat
verfälschen. Zu nennen ist insbesondere die unterschiedliche
Klassenzusammensetzung. Jede Schulklasse hat eine eigene Gruppendynamik. Diese
Gruppendynamik kann den Lernerfolg massgeblich beeinflussen. Dieses
Phänomen beeinträchtigt bereits die Aussagekraft des Vergleiches der
Parallelklassen im WG. Noch viel stärker kommt dieses Phänomen jedoch
beim Vergleich von Klassen zweier Schultypen zum Tragen. Die HMS und die IMS
haben wohl im Wirtschaftsunterricht das selbe Curriculum, sie stellen
aber ganz unterschiedliche Soziotope dar. Eine kaufmännische Ausbildung
zieht eher kommunikative Menschen an, wohingegen eine Ausbildung als
Applikationsentwickler/in eher technisch interessierte Menschen anzieht.
Dass es sich dabei um mehr als ein blosses Cliché handelt, zeigt sich an
den Aufnahmebedingungen zu den beiden Schultypen.  
Der Eintritt in die
HMS ist im Anschluss an die zweite oder dritte Klasse der Sekundarschule
möglich. Damit man zur Ausbildung an der HMS zugelassen wird, muss eine
Aufnahmeprüfung abgelegt werden. An dieser Aufnahmeprüfung werden die
Fächer Deutsch und Mathematik geprüft[@ZAPHMS]. Der Eintritt in die IMS
ist ausschliesslich nach der dritten Klasse der Sekundarschule möglich.
Auch für die Zulassung zu diesem Ausbildungsgang muss eine
Aufnahmeprüfung in den Fächern Deutsch und Mathematik abgelegt
werden[@ZAPIMS]. Zusätzlich muss für die Zulassung zur IMS 
ein Multicheck "ICT Informatiker/in EFZ Fachricthung
Applikationsentwicklung" in den Bereichen "Potenzial" und
"berufsspezifische Fähigkeiten" mit je mindestens 50 Punkten bestanden
werden[@ZAPIMS]. Die IMS richtet sich damit
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
Einführung ins Zinsrechnen erfolgte im WR-Unterricht und die
Anwendungsübung im OFI. Da die beiden Unterrichtseinheiten mit
zeitlichem Abstand stattfanden, musste im OFI eine Repetition zum
Zinsrechnen stattfinden, bevor die Anwendungsübung zum Kontokorrentkonto
durchgeführt werden konnte.

Die Anwendungsübung zum Kontokorrenktonto bildete gleichzeitig den
Anlass zur Einführung in die objektorientierte Programmierung in
Python. Mit der Idee, den Schülerinnen und Schülern Unterstützung zu
bieten, wurde ihnen ein fertiges UML Klassendiagramm abgegeben. Anhand
dieses Diagrammes wurden sowohl die inhaltlichen Aspekte des
Kontokrrentkontos wie auch die technischen Aspekte der
objektorientierten Programmierung besprochen. 
Anschliessend an die Einführung in die objektorientierte Programmierung
wurde deren Umsetzung in Python besprochen. Sowohl die Einführung in die
objektorientierte Programmierung wie auch die Einführung in deren
Umsetzung erfolgte in konventionellen Lehrgesprächen.
Im Anschluss an die Einführungen haben die Schülerinnen und Schüler
versucht, die neuen
Kenntnisse am Beispiel des Kontokorrentkontos anzuwenden.

Es hat sich, im Rückblick wenig überraschend, gezeigt, dass die
Informatikkenntnisse der Schülerinnen und Schüler nicht annähernd
ausreichend waren,
um die Aufgabe lösen zu können. Die Komplexität des "Werkzeugs"
objektorientierte Programmierung war so gross, dass das Werkzeug den
Blick auf die
Probleme der Zinsrechnung verstellt hat.

In der Klasse der IMS war die Ausgangslage deutlich günstiger. Hier
konnte auf die Informatikkenntnissen aus der
Berufsausbildung zurückgegriffen werden. Die Lernenden der IMS hatten zu
diesem Zeitpunkt bereits sechs mal mehr Informatikunterricht erhalten
als die Schülerinnen und Schüler des WG. In der IMS sind 12
Wochenlektionen für den Informatikunterricht bzw. die Berufsausbildung
vorgesehen, im WG zwei.
Darüber hinaus wird in der IMS
Programmieren mit Java unterrichtet. Für das Verständnis der
objektorientierten Programmierung weist Java gegenüber Python deutliche
didaktische Vorteile auf. Selbst in einem einfachen "Hello, World!"
Programm kommt in Java die Objektorientierung zum Ausdruck. Muss doch,
wie das folgende Listing zeigt, bereits dafür eine Klasse mit einer
`main`-Methode geschrieben werden.

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Im Gegensatz
dazu wird das gleiche Programm in Python in der Regel in einem einfachen
REPL (read-eval-print-loop) in einem Terminal ausgeführt.

```python
>>>print("Hello, World!")
```

Die Lernenden der IMS waren also mit den Grundzügen der
objektorientierten Programmierung bereits vertraut.

Obwohl die Ausgangslage für das Unterrichtsmodul Kontokorrentkonto
deutlich besser waren als im WG, wurde das Klassendiagramm zusammen mit
den Lernenden entwickelt. Dies hat zusätzlich zu einem besseren
Verständnis der Aufgabenstellung beigetragen. 
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
Schülerinnen und Schüler der Kontrollklasse 80.4%. In den
Gegenüberstellungen der Leistungen von IMS und HMS haben die Lernenden
der IMS 77.1% und die Lernenden der HMS 80.4% erreicht.  

Aufgrund der durch die Grösse der Stichprobe möglichen Fehlerspanne wäre es möglich,
dass die Leistungen in der Gesamtpopulation durch die Anwendungsübung
tatsächlich verbessert worden sind. Allerdings müssten sich Test- und
Kontrollgruppe im WG mit den erzielten Resultaten je am äussersten
Rand der jeweiligen Bandbreite der möglichen Resultate bewegen. In der IMS müsste
die Bandbreite aufgrund der grösseren Fehlerspanne etwas weniger stark
ausgereizt worden sein.

Ungeachtet dessen, was statistisch denkbar wäre, entsprachen die
Resultate nicht den Erwartungen.

Dass das natürliche Experiment ursächlich dafür war, dass die Testklassen
schlechter abgeschnitten haben als die Kontrollklassen, scheint trotz
der Resultate wenig plausibel. Wahrscheinlicher ist, dass die
Störvariabeln doch einen viel grösseren Einfluss hatten, als das zu
Beginn vermutet worden ist. Das würde lediglich bestätigen, dass die
Varianz in der Leistung zwischen Klassen oft gross ist, oft sogar
grösser als die Varianz zwischen einzelnen
Schulen[@wurstersebastianSchulUndUnterrichtsqualitaet2022, S. 28].

Weil das Problem der Stichprobengrösse bereits in der Planung erkannt
worden ist, sollte das natürliche Experiment durch Leitfadenintervies
ergänzt werden.

## Leitfadeninterview {#sec:leitfadeninterview}

Leitfadeninterviews entsprechen nicht der gängigen Vorstellung von
Interviews, wie man sie aus den Medien kennt. Leitfadeninterviews
sind eher durch den Interviewer moderierte Erzählungen des Interviewten.  

>"Der grösste Fehler qualitativer Interviewführung liegt [denn auch]
>darin, zu viel vorzugeben und abzufragen
>[...][@helfferichLeitfadenUndExperteninterviews2022, S. 878]."

Das bedeutet allerdings nicht, dass das Leitfadeninterview völlig
unstrukturiert ist. Es bedarf wie jede andere wissenschaftliche
Befragung der sorgfältigen Planung.

### Planung der Leitfadeninterviews

>"Je stärker das Forschungsinteresse auf konkrete, offen erhobene
>Informationen ausgerichtet ist, desto mehr Strukturierung verträgt das
>Interview und desto mehr Vorgaben sind
>gerechtfertigt[@helfferichLeitfadenUndExperteninterviews2022, S.
880]." 

Um dem Leitfadeninterview Struktur zu geben, wird vor der Durchführung
der dem Interviewtyp den Namen gebende Leitfaden für das Interview verfasst. Dieser Leitfaden kann entweder
aus einer Reihe
offener Fragen oder aus mehreren Erzählaufforderungen bestehen. Für die
im Rahmen dieser Arbeit durchgeführten Interviews wurde
eine Kombination aus konkreten Fragen und
Erzählaufforderungen vorbereitet. Dabei wurden die Fragen offen
formuliert,
so dass der Interviewte von der eigenen Erfahrung und seinem
Empfinden erzählen konnte[@misochQualitativeInterviews2019, S. 66].
Der Leitfaden diente dabei nicht nur als
Gedankenstütze, er sollte ebenso dazu beitragen, den Fokus auf der
Forschungsfrage zu
behalten[@helfferichLeitfadenUndExperteninterviews2022, S. 881;
@misochQualitativeInterviews2019, S. 66].
Der Leitfaden sollte als Anleitung an den Gesprächsmoderatoren dienen.  
Damit eine vergleichende Auswertung mehrerer Interviews möglich ist,
wurde in allen Interviews der gleiche Leitfaden verwendet.
Da als Gesprächspartnerinnen bzw. Gesprächspartner nur
Schülerinnen und Schüler bzw. Lernende aus den beiden Testklassen in
Frage gekommen sind, wurde der Leitfaden mit dem UML Klassendiagramm
aus @fig:uml ergänzt. Dieses sollte den Befragten als
Erinnerungshilfe vorgelegt werden können.
Der für die Interviews verwendete Leitfaden findet sich im Anhang.xxx

Wie bereits erwähnt, kamen als Gesprächspartnerinnen bzw.
Gesprächspartner nur Angehörige der Testklassen in Frage.
Interessentinnen bzw. Interessenten konnten sich direkt in einen Termin
in einem eigens dafür vorgesehenen Kalender eintragen. Dies sollte die
Diskretion unter den Angehörigen der Testklassen sicherstellen.

### Begründung für die Wahl von Leitfadeninterviews als Methode

Da Lernen ein psychologischer Prozess ist, der nicht direkt beobachtet
werden kann, muss der Vorgang des Lernens indirekt erschlossen werden.
Standardmässig geschieht dies durch die Kontrolle des Lernerfolges in
Prüfungen. Das hätte durch das natürliche Experiment ausgenutzt werden
sollen. Allerdings hätte dies lediglich ermöglicht, die Gültigkeit
der Arbeitshypothese zu belegen. Selbst wenn dies gelungen wäre, hätte
damit die Frage, warum die Arbeitshypothese bestätigt worden ist, nicht
beantwortet werden können. Die Frage nach der Begründung ist
qualitativer Natur.

Um diese Frage beantworten zu können, muss auf das Erleben der
Schülerinnen und Schüler bzw. der Lernenden abgestellt werden. Da dieses
genausowenig direkt beobachtbar ist wie das Lernen, muss es erfragt
werden. Das Erleben einer Lernsituation ist allerdings zu individuell,
als das es mit einem standardisierten Fragebogen erhoben werden könnte.
Das Leitfadeninterview bietet hier eine Möglichkeit, diesem Umstand
zu begegnen. Mit dem Erfragen des Lernerlebnisses besteht die
Möglichkeit, die Frage weshalb, die Arbeitshypothese gilt, beantworten
zu können.

### Durchführung der Leitfadeninterviews

Die Rekrutierung von Gesprächspartnerinnen und Gesprächspartnern
gestaltete sich schwieriger als erwartet. Auf die allgemeine Einladung,
an einem Leitfandeninterview teilzunehmen,
hat zuerst niemand reagiert. Erst auf gezielte Einladung hin haben sich
einzelne Schülerinnen und Lernende zu einem Gespräch bereit erklärt. Die
angestrebte Zahl an Gesprächspartnerinnen und Gesprächspartnern konnte
nicht erreicht werden. Insgesamt wurden lediglich vier Gespräche
geführt. Alle vier
Interviews haben zum gleichen Resultat geführt.  

Im Rahmen dieser Gespräche hat sich allerdings
gezeigt, dass das Gefälle zwischen Schülerinnen und Schülern auf der
einen Seite und einem Lehrer auf der anderen Seite zu gross war. Die
Schülerinnen und Schüler sind so stark darauf konditioniert, die
Erwartungen der Lehrerinnen und Lehrer zu erfüllen, dass keine freie
Erzählung ihrerseits erfolgt ist. Dies dürfte nicht zuletzt ihrem  Alter
geschuldet sein[@helfferichLeitfadenUndExperteninterviews2022, S. 876].
Die Gesprächspartnerinnen und Gesprächspartner haben sich ehrlich
bemüht, die gewünschten Auskünfte zu erteilen. Sie haben aber lieber auf
konkrete Fragen gewartet, als dass sie von sich aus erzählt hätten.
Ausserdem war stets ihr Bemühen zu erkennen, den Befrager mit ihren
Antworten zufriedenzustellen.

Nach der Durchführung ist beim Befrager der Eindruck zurückgeblieben, er
hätte eine einzige grosse Suggestivfrage gestellt. Dem hätte allenfalls
durch den Einsatz von geschulten externen Interviewern begegnet werden
können.

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

Dies ist hier allerdings eher ein Grund, am Wert der Aussagen zu zweifeln.
Wie bei der Beschreibung der Durchführung bereits festgehalten, ist
keine spontane Erzählung zustande gekommen. Die Gesprächspartnerinnen
und Gesprächspartner waren zu stark darauf bedacht, zu erzählen, was der
Befrager hören wollte. So kommt den Aussagen kein eigener Wert zu. Sie
haben lediglich die der Arbeitshypothese zu Grunde liegenden Annahmen
wiederholt.

Aus den Interviews ergab sich daher kein Erkenntnisgewinn.  

Dies führte dazu, dass nach einer weiteren Möglichkeit gesucht wurde, um
die Arbeitshypothese zu überprüfen. Wie im Folgenden zu zeigen sein
wird, hat sich eine solche Möglichkeit aus der Natur der
Ausbildung an der IMS ergeben.

## Fazit zu den verworfenen Methoden

Mit den verworfenen Methoden hätte ein sogenannter *Mixed Methods*
Ansatz empirischer Sozialforschung[@schreierMixedMethods2020, S. 164]
verfolgt werden sollen. Es hat sich allerdings gezeigt, dass der
Mittelansatz dazu unzureichend war. Für das natürliche Experiment war
die Population zu klein und für die Leitfadeninterviews konnte keine
Gesprächssituation geschaffen werden, in welcher die
Gesprächspartnerinnen und Gesprächspartner unbeeinflusst vom Befrager
Auskunft geben konnten.
