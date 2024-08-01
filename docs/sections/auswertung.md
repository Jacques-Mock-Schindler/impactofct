# Korrelation zwischen Noten der Berufsausbildung und der BMS

Die Auswertung der Mittelwerte der Berufsausbildung und der BMS zeigt,
wie in @fig:mittelwerte dargestellt,
eine starke Korrelation zwischen den beiden Leistungen. Spearman's $\rho$
liegt bei 0.623 und Pearson's $r$ gar bei 0.693.

![Korrelation zwischen den Durchschnittsnoten der Berufsausbildung (EFZ)
und der Durchschnittsnoten der BMS. Die rote Linie zeigt die
Regressionslinie. Der blassrote Schatten um die Regressionslinie zeigt
das Konfidenzintervall von 95%
an.](docs/graphics/scatterplot_mittelwerte.svg){#fig:mittelwerte}

Wie bei Betrachtungen von Mittelwerten zu erwarten, hat die Streuung
gegenüber den Rohdaten deutlich abgenommen.

![Visualisierung der Verteilung der Durchschnittsnoten in der BMS und in
der Berufsausbildung. Die rote Linie zeigt den
Median.](docs/graphics/verteilung_durchschnitte.svg){#fig:mittelwerte_boxplot}

Der Effekt ist in @fig:mittelwerte_boxplot gut zu sehen.
Anders als in den Rohdaten gibt es keine Ausreisser nach unten mehr. Der minimale Wert in der
BMS liegt bei 3.75 jener in der Berufsausbildung bei 3.76. Im Gegenzug
ist auch das Maximum etwas tiefer ausgefallen. In der BMS liegt das
Maximum bei 5.79 und in der Berufsausbildung bei 5.86. Diese Regression
zur Mitte[@freedmanStatistics2007, S. 170] ist in der Statistik ein
bekanntes Phänomen. Die Gegenüberstellung von Mittelwerten zeigt daher
nur, dass generell starke Lernende eben tatsächlich generell starke
Lernende sind. Um diese Tautologie zu durchbrechen, wird in den
kommenden Abschnitten auf die Resultate der Gegenüberstellung der
einzelnen Module und Fachnoten eingegangen.

## Übersicht über die Detailauswertung

Wie in der Methodenbeschreibung dargelegt, wurden die Noten der BMS mit
jenen der Berufsausbildungsmodule korreliert. Dazu wurde Spearman's
$\rho$ berechnet und die Resultate in einer Heatmap dargestellt.
Obwohl
die Fragestellung nach den Auswirkungen von CT auf das Lernen im
allgemeinen stellt, werden die die BMS Fächer auf der x-Achse und die
Module aus der Berufsausbildung auf der y-Achse dargestellt. So ist der
Effekt besser lesbar.


![Heatmap mit den Korrelationen zwischen der Noten der Berufsausbildung
und der BMS. Die
Korrelation wird mit Spearman's $\rho$ ausgedrückt. Die Noten der BMS
sind nach steigender mittlerer Korrelation
sortiert. Die Noten der Berufsbildung sind ebenfalls nach steigender
mittlerer Korrelation sortiert. Die Module mit besonderem CT Bezug sind
rot
beschriftet.](docs/graphics/spearmankorrelationen_heatmap.svg){#fig:spearman}

Die Modul-BMS Korrelationen mit einem Wert über 0.3 sind grün
eingefärbt. Je höher der Wert, desto intensiver die gründe Färbung. Dies
lässt nur schon optisch gut erkennen, dass die Korrelation zwischen den
Noten der Module der Berufsausbildung und jener der BMS nicht sehr stark
ist. Optisch etwas weniger gut zu erkennen ist, dass nur die drei Fächer
Mathematik, Finanz- und Rechnungswesen sowie interdisziplinäres Arbeiten
im Mittel über alle Module den Wert von 0.3 überschreiten.  
Die als besonders CT spezifisch qualifizierten Module verteilen sich
gleichmässig über die y-Achse der Heatmap. Damit ist die entsprechende
Einteilung der Module statistisch bedeutungslos.

Insgesamt lassen sich die Resultate grob in drei Gruppen unterteilen:

1. Fächer, welche die Schwelle von 0.3 überschritten haben.
   
   Das sind die Fächer Mathematik, Finanz- und Rechnungswesen sowie das
   interdisziplinäre Arbeiten in den Fächern.
2. Fächer welche die Schwelle knapp verfehlt haben (mittlere
   Korrelationen von 0.25 bis 0.3).

   Das sind die beiden Fächer Wirtschaft und recht sowie Technik und
   Umwelt.
3. Fächer mit einer schwachen Korrelation (weniger als 0.25).

   Das sind die Fächer Deutsch, Geschichte und Politik, Englisch und
   Französisch.

Ein ähnliches, wenn auch nicht ganz identisches Resultat ergibt sich,
wenn statt Spearman's $\rho$ auf Pearson's $r$ abgestellt wird.

![Heatmap mit den Korrelationen zwischen der Noten der Berufsausbildung
und der BMS. Die
Korrelation wird mit Pearson's $r$ ausgedrückt. Die Noten der BMS
sind nach steigender mittlerer Korrelation
sortiert. Die Noten der Berufsbildung sind ebenfalls nach steigender
mittlerer Korrelation sortiert. Die Module mit besonderem CT Bezug sind
rot
beschriftet.](docs/graphics/korrelationen_heatmap.svg){#fig:pearson}

Die Korrelationen nach Bravais-Pearson führt bezüglich der Sortierung
der Noten der BMS zum gleichen Resultat. Verschiebungen gibt es in der
Reihenfolge der Module. Die Bravais-Pearson Korrelation reagiert stärker
auf Streuungen als die Korrelation nach Perason. Wie in
[@sec:modulcharakter] gezeigt, streuen die Modulnoten stärker als die
Noten der BMS. Damit dürfte die Verschiebung in der Reihenfolge der
Modulnoten auf die grössere Streuung zurückzuführen sein.

Die Übereinstimmung der Sortierreihenfolge der BMS Fächer zeigt, dass
die Reihenfolge robust ist.

## Ursachen für die Gruppierung

Die Fächergruppe mit der Schwächsten Korrelation besteht ausschliesslich
aus Fächern, welche den Geisteswissenschaften zugeordnet werden.  
Die mittlere Fächergruppe kann den Sozialwissenschaften zugeordnet
werden.  
Die Fächergruppe mit der stärksten Korrelation ist heterogener
Zusammengesetzt. Mathematik und Finanz- und Rechnungswesen sind
Disziplinen, welche ein hohes Abstraktionsvermögen erfordern. Beim
interdisziplinären Arbeiten in den Fächern steht die Projektarbeit im
Vordergrund.

Im folgenden soll erläutert werden, weshalb sich die Korrelationen so
klar gruppieren lassen.

### Anforderungen der Geisteswissenschaften an Lernende

Der zentrale Werkstoff der Geisteswissenschaften ist der Text.
Entsprechend ist die wichtigste Tätigkeit einer Geisteswissenschafterin
bzw. eines Geisteswissenschafters die Auseinandersetzung mit Texten.  
Das verlangt von Lernenden in Fächern, die den Geisteswissenschaften
zugeordnet werden, dass sie viel Geduld und Konzentration aufbringen.
Sie müssen bereit sein, Fragen an Texte zu stellen und diese aus den
Texten heraus selber zu beantworten.

Dabei wird eine andere Art von Problemlösung geschult, als dies bei CT
der Fall ist. CT verlangt zum Überwinden von Verständnisproblemen
geradezu, dass man das Problem recherchiert. Aufgrund des hohen
Aktualitätsdruckes am besten online. Dies steht in einem gewissen
Gegensatz zur Vorgehensweise in den Geisteswissenschaften. Natürlich
soll auch in den Geisteswissenschaften Wissen aus allen verfügbaren
Quellen geschöpft werden. Aber zentral bleibt die Auseinandersetzung mit
dem Ursprungstext.

Auch wenn auf Hochschulstufe in den Geisteswissenschaften vermehrt
quantitative Methoden und damit naturwissenschaftliche Ansätze
Verwendung finden, ändert das nichts daran, dass Geisteswissenschaften
eher an qualitativen Erkenntnissen interessiert sind. Insbesondere auf
Mittelschulstufe dominiert nach wie vor das qualitative
Erkenntnisinteresse. CT verlangt
dagegen eher formal logisches und algorithmisches Denken.

Damit verlangen die Geisteswissenschaften eine andere Art von Geduld und
Konzentrationsfähigkeit als das in CT geschult wird.

Diese unterschiedlichen Arbeitsweisen sind ein möglicher Grund für die
schwache Korrelation der Noten aus der Berufsausbildung und jenen der
geisteswissenschaftlichen BMS Fächern.

### Anforderungen der Sozialwissenschaften an Lernende

Die Sozialwissenschaften befinden sich in vielerlei Hinsicht an der
Schnittstelle zwischen Geistes- und Naturwissenschaften. Die Inhalte
haben viele Berührungspunkte mit den Geisteswissenschaften und die
Methoden stammen oft aus den Naturwissenschaften.

In den den Sozialwissenschaften zuzuordnenden Fächern an Mittelschulen
werden viele Inhalte durch Texte vermittelt. Ausserdem ist es weit
verbreitete Praxis, die Lernenden selber Texte verfassen oder
erarbeitete Erkenntnisse präsentieren zu lassen. Ebenfalls Teil des
Unterrichtes ist es, die Lernenden bereits aufbereitete Statistiken
interpretieren zu lassen.

Die von CT geforderte algorithmische Vorgehensweise hat daher
bescheidenen Parallelen
zu den Methoden in den Sozialwissenschaften. Dies erklärt zum Teil,
weshalb die Korrelation zwischen den Noten der Berufsbildenden Fächer
und jenen der BMS stärker ist als in den Geisteswissenschaften aber doch
nicht so stark, dass die Schwelle von 0.3 überschritten wird.

### Anforderungen der Abstrakten Disziplinen an die Lernenden

Die Unterschiede in dieser Fächergruppe sind gross. Aus diesem Grund
wird diese Fächergruppe in Mathematik sowie Finanz- und
Rechnungswesen einerseits und das interdisziplinäre Arbeiten in den
Fächern andererseits aufgeteilt.

#### Mathematik und Finanz- und Rechnungswesen

Der Zusammenhang zwischen Mathematik und Finanz- und Rechnungswesen ist
grösser, als dies auf den ersten Blick den Anschein macht. Historisch
gesehen ist dies jedoch keine Überraschung. Luciano Pacioli, der
Erfinder des Rechnungswesens, hat sich als Mathematiker verstanden. Er
hat ein System entwickelt, in dem Einnahmen und Ausgaben einander
gegenübergestellt werden können, ohne dass negative Vorzeichen verwendet
werden müssen. Damit handelt es sich beim Finanz- und Rechnungswesen im
Kern um ein System für umfangreiche Additionen und Subtraktionen.  
Darüber hinaus wird sowohl in der Mathematik wie auch im Finanz- und
Rechnungswesen sehr stark von der realen Welt abstrahiert. Die
Mathematik ist eine theoretische Disziplin, die ohne Bezug zur realen
Welt auskommt. Im Finanz- und Rechnungswesen wird ebenfalls so stark
abstrahiert, dass das gleiche System auf so unterschiedliche Unternehmen
wie multinationale Grosskonzerne oder die lokale Bäckerei passen. Dies
ist kein totaler Verzicht auf die reale Welt aber doch eine sehr starke
Abstrahierung.  
Ausserdem weisen Mathematik und Finanz- und Rechnungswesen starke
Parallelen in der Problemlösung auf. In beiden Disziplinen werden
Probleme in kleinere Teilprobleme zerlegt, die einfacher zu lösen sind.  
Zu guter Letzt ist darauf hinzuweisen, dass in beiden Disziplinen eine
stark regelbasierte Arbeitsweise vorherrscht.

Zusammenfassend werden sowohl in der Mathematik als auch im Finanz- und
Rechnungswesen die gleichen Fähigkeiten geschult, die auch in CT
erforderlich sind. Dies dürfte die verhältnismässig starke Korrelation
der Leistungen in Mathematik und Finanz- und Rechnungswesen auf der
einen Seite sowie den Leistungen in der Berufsausbildung auf der anderen
Seite erklären.
