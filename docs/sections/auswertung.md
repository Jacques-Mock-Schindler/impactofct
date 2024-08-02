# Korrelation zwischen Noten der Berufsausbildung und der BMS

Die Darstellung in [@fig:mittelwerte] zeigt eine starke Korrelation
zwischen den durchschnittlichen Leistungen in der Berufsausbildung und
jenen in der BMS.
Spearman's $\rho$
liegt bei 0.623 und Pearson's $r$ gar bei 0.693.

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/scatterplot_mittelwerte.png}
\caption[Korrelation mittlere Noten Berufsausbildung - BMS]{Korrelation
zwischen den Durchschnittsnoten der Berufsausbildung und der
Durchschnittsnotne der BMS. Die rote Linie zeigt die Regressionslinie.
Der blassrote Schatten um die Regresseionslinie zeigt das
Konfidenzintervall von 95\% an.}
\label{fig:mittelwerte}
\end{figure}

Wie bei Betrachtungen von Mittelwerten zu erwarten, hat die Streuung
gegenüber den Rohdaten deutlich abgenommen.

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/verteilung_durchschnitte.png}
\caption[Übersicht über die Verteilung der Durchschnittsnoten in BMS und
Berufsausbildung.]{Übersicht über die Verteilung der Durchschnittsnoten
in BMS und Berufsausbildung. Die rote Linie zeigt den Median.}
\label{fig:mittelwerte_boxplot}
\end{figure}

Der Effekt ist in @fig:mittelwerte_boxplot gut zu sehen.
Anders als in den Rohdaten gibt es keine Ausreisser nach unten. Der minimale Wert in der
BMS liegt bei 3.75 jener in der Berufsausbildung bei 3.76. Im Gegenzug
ist auch das Maximum etwas tiefer ausgefallen. In der BMS liegt das
Maximum bei 5.79 und in der Berufsausbildung bei 5.86. Diese Regression
zur Mitte[@freedmanStatistics2007, S. 170] ist in der Statistik ein
bekanntes Phänomen.

In der Betrachtung von Mittelwerten gehen Details verloren. Dies liegt
in der Natur der Sache, soll doch in einem Mittelwert eine ganze
Stichprobe in einer Zahl zusammengefasst werden.
Entsprechend zeigt die Gegenüberstellung der Mittelwerte lediglich, 
dass starke Lernende nicht ausschliesslich in einem der beiden
einander gegenübergestellten Ausbildungsgänge gute Leistungen erbringen.
Aus diesem Grund wird in den kommenden Abschnitten die Gegenüberstellung
auf Stufe einzelnes Modul bzw. einzelnes Fach ausgedehnt.

## Übersicht über die Detailauswertung

Wie in der Methodenbeschreibung in [@sec:effektive_methode] dargelegt,
wurden die Noten der BMS mit
jenen der Berufsausbildungsmodule korreliert. Dazu wurde Spearman's
$\rho$ berechnet und die Resultate in einer Heatmap dargestellt.
Obwohl die Arbeitshypothese 
die Frage nach den Auswirkungen von CT auf das Lernen im
allgemeinen stellt, werden die BMS Fächer auf der x-Achse und die
Module aus der Berufsausbildung auf der y-Achse dargestellt. Dies ist
zwar gegenüber der üblichen Darstellung von unabhängigen und abhängigen
Variablen vertauscht. In dieser Darstellung ist aber der Effekt besser
zu erkennen.

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/spearmankorrelationen_heatmap.png}
\caption[Heatmap mit den Korrelationen zwischen den Noten der
Berufsausbildung und jenen der BMS (Spearman's $\rho$).]{Heatmap mit den Korrelationen
zwischen den Noten der Berufsausbildung und jenen der BMS. Die
Korrelation wird mit Spearman's $\rho$ ausgedrückt. Die Noten der BMS
sind aufsteigend nach der mittleren Korrelation sortiert. Die Noten der
Berufsausbildung sind ebenfalls aufsteigend nach der mittleren
Korrelation sortiert. Die CT relevanten Module sind rot beschriftet.}
\label{fig:spearman}
\end{figure}

Die Modul-BMS Korrelationen mit einem Wert von über 0.3 sind grün
eingefärbt. Je höher der Wert, desto intensiver die gründe Färbung. Dies
lässt nur schon optisch gut erkennen, dass die Korrelation zwischen den
Noten der Module der Berufsausbildung und jener der BMS nicht sehr stark
ist. Optisch etwas weniger gut zu erkennen ist, dass nur die drei Fächer
Mathematik, Finanz- und Rechnungswesen sowie interdisziplinäres Arbeiten
im Mittel über alle Module den Wert von 0.3 überschreiten.  
Die als besonders CT relevanten qualifizierten Module verteilen sich
gleichmässig über die y-Achse der Heatmap. Dies zeigt, dass die CT
relevanten Module keine statistische Auffälligkeiten zeigen.

Trotzdem lassen sich die Resultate grob in drei Gruppen unterteilen:

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

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/korrelationen_heatmap.png}
\caption[Heatmap mit den Korrelationen zwischen den Noten der
Berufsausbildung und jenen der BMS (Pearson's $r$).]{Heatmap mit den
Korrelationen zwischen den Noten der Berufsausbildung und jenen der BMS.
Die Korrelation wird mit Pearson's $r$ ausgedrückt. Die Noten der BMS
sind aufsteigend nach der mittleren Korrelation sortiert. Die Noten der
Berufsausbildung sind ebenfalls aufsteigend nach der mittleren
Korrelation sortiert. Die CT relevanten Module sind rot beschriftet.}
\label{fig:pearson}
\end{figure}

Die Korrelationen nach Bravais-Pearson führt bezüglich der Sortierung
der Noten der BMS zum gleichen Resultat. Verschiebungen gibt es in der
Reihenfolge der Module. Die Bravais-Pearson Korrelation reagiert stärker
auf Streuungen als die Korrelation nach Separman. Wie in
[@sec:modulcharakter] gezeigt, streuen die Modulnoten stärker als die
Noten der BMS. Damit dürfte die Verschiebung in der Reihenfolge der
Modulnoten auf die grössere Streuung zurückzuführen sein.

Die Übereinstimmung der Sortierreihenfolge der BMS Fächer zeigt aber
trotzdem, dass
die Reihenfolge der Sortierung robust ist.

## Ursachen für die Gruppierung {#sec:gruppierung}

Die Fächergruppe mit der schwächsten Korrelation besteht ausschliesslich
aus Fächern, welche den Geisteswissenschaften zugeordnet werden.  
Die mittlere Fächergruppe kann den Sozialwissenschaften zugeordnet
werden.  
Die Fächergruppe mit der stärksten Korrelation ist heterogener
Zusammengesetzt. Mathematik und Finanz- und Rechnungswesen sind
Disziplinen, welche ein hohes Abstraktionsvermögen erfordern. Beim
interdisziplinären Arbeiten in den Fächern steht die Projektarbeit im
Vordergrund.

Die Fächergruppen stellen unterschiedliche Anforderungen an die
Lernenden. Diese Anforderungen sollen nun genauer betrachtet werden.
Anhand dieser Betrachtung wird erläutert, warum sich die Korrelationen
so deutlich gruppieren lassen. Die folgende Erklärung basiert auf diesen
fachspezifischen Anforderungen.

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
ist zwar kein vollständiges Ausblenden der realen Welt aber doch eine sehr starke
Abstrahierung davon.  
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

#### Interdisziplinäres Arbeiten in den Fächern

Die Note im interdisziplinären Arbeiten in den Fächern basiert auf
mehreren Projektarbeiten, welche die Lernenden im Verlauf der
dreijährigen Schuldauer erstellen. Projektunterricht ist eine Methode,
welche auch an der Berufsschule in der Berufsausbildung häufig zur
Anwendung kommt. Die Korrelation der Leistungen des interdisziplinären
Arbeiten in den Fächern mit jenen der Berufsausbildung dürfte mit der
Übereinstimmung der Methoden zu erklären sein.

## Vergleich von Spearman's $\rho$ in den Fächergruppen

Die Begründung in [@sec:gruppierung] würde erwarten lassen, dass die
nach zunehmender mittlerer Korrelation sortierten Module pro Gruppe eine
zunehmende Konzentration von CT relevanten Modulen aufweisen - von
Geisteswissenschaften über Sozialwissenschaften hin zu den abstrakten
Wissenschaften.  Wie [@fig:verschiebungen] entnommen
werden kann, entspricht dies nicht den beobachteten Resultaten.

\begin{figure}[ht!]
\includegraphics[width=\textwidth]{docs/graphics/verschiebung.png}
\caption[Darstellung der durchschnittlichen Korrelation nach Spearman
nach Fächergruppe.]{Darstellung der durchschnittlichen Korrelation nach
Spearman nach Fächergruppe. Je weiter unten in der Grafik ein Modul
steht, desto stärker ist die Korrelation. Grün dargestellt sind die CT
relevanten Module.}
\label{fig:verschiebungen}
\end{figure}

Die Veränderung der Verteilung der CT relevanten
Module von Fächergruppe zu Fächergruppe lässt kein Muster erkennen. Die
Verteilung mutet vielmehr völlig zufällig an.

## Gegenüberstellung von Arbeitshypothese und Datenauswertung

Die Auswertung der Daten zeigen keinen Zusammenhang zwischen CT und
allgemeinem Lernerfolg. Es zeigt sich lediglich, dass die Leistungen in der
Berufsausbildung stärker mit jenen in den abstrakten Disziplinen der BMS
korrelieren als in den Geistes- und Sozialwissenschaften. Dieser Effekt
gilt allerdings nur generell. Den als speziell CT relevant
identifizierten Modulen
kommt keine besondere Bedeutung zu.

Die im [@sec:arbeitshypothese] aufgestellte Arbeitshypothese lässt sich
somit nicht halten.

Im Umkehrschluss kann daher festgehalten werden, dass CT keine
überlegene Lehr- und Lernmethode darstellt. Dies bedeutet allerdings
nicht, dass CT als Methode im Unterricht keine Bedeutung zukommen soll.
Sie ist allerdings lediglich eine Methode unter anderen. Sie soll im
Rahmen der Methodenvielfalt dort eingesetzt werden, wo sie aufgrund
ihrer spezifischen Stärken einen Mehrwert generieren kann.
