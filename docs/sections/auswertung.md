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
@sec:modulcharakter gezeigt, streuen die Modulnoten stärker als die
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
