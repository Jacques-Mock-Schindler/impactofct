# Materialien auf GitHub {#sec:github}

Die vorliegende Arbeit wurde mit git versioniert und auf GitHub
abgelegt. Das Repository reicht allerdings nicht bis an den Anfang der
Entstehung der Arbeit zurück. Zum einen war die Struktur des
ursprünglichen Repositorys sehr unübersichtlich und zum anderen wurde
dort zu Beginn mit den nicht anonymisierten Rohdaten gearbeitet. Aus
diesen beiden Gründen wurde im Juli 2024 ein neues Repository angelegt.

## Datengrundlage

Der Arbeit liegen die folgenden Datentabellen zu Grunde:

* [personalien.csv](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/data/personalien.csv)
* [noten_bm.csv](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/data/noten_bm.csv)
* [noten_efz.csv](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/data/noten_efz.csv)

Alle Datentabellen (Rohdaten sowie abgeleitete Datentabellen) finden sich in anonymisierter
Form im GitHub Repositroy
[https://github.com/Jacques-Mock-Schindler/impactofct](https://github.com/Jacques-Mock-Schindler/impactofct/tree/main/docs/data)
(der Link führt direkt in den Unterordner mit den Tabellen).

## Für die Auswertung verwendete Python Scripts

Wie in [@sec:effektive_methode] (Beschreibung der Methode) erwähnt,
erfolgte die Auswertung der Daten mit Hilfe von Python Scripts. Hier
eine Auflistung der erstellten Scripts:

* [00_anonymisierung.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/00_anonymisierung.py)
* [01_normalverteilung_bm_visuell.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/01_normalverteilung_bm_visuell.py)
* [02_normalverteilung_efz_visuell.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/02_normalverteilung_efz_visuell.py)
* [03_margin_of_error.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/03_margin_of_error.py)
* [04_normalverteilung_rechnerisch.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/04_normalverteilung_rechnerisch.py)
* [05_signifikanz.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/05_signifikanz.py)
* [06_visualisierung_notenuebersicht.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/06_visualisierung_notenuebersicht.py)
* [07_visualisierung_efz_semesternoten.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/07_visualisierung_efz_semesternoten.py)
* [08_visualisierung_mittlere_korrelation.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/08_visualisierung_mittlere_korrelation.py)
* [09_korrelation_detailliert.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/09_korrelation_detailliert.py)
* [10_barcode.py](https://github.com/Jacques-Mock-Schindler/impactofct/blob/main/docs/code/240813_barcode.py)

Alle Scripts finden sich im GitHub Repository
[https://github.com/Jacques-Mock-Schindler/impactofct](https://github.com/Jacques-Mock-Schindler/impactofct/tree/main/docs/code)
(der Link führt direkt in den Unterordner mit den Scripts).
