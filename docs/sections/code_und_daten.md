# Materialien auf GitHub

Die vorliegende Arbeit wurde mit git versioniert und auf GitHub
abgelegt. Das Repository reicht allerdings nicht bis an den Anfang der
Entstehung der Arbeit zurück. Zum einen war die Struktur des
ursprünglichen Repositorys sehr unübersichtlich und zum anderen wurde
dort zu Beginn mit den nicht anonymisierten Rohdaten gearbeitet. Aus
diesen beiden Gründen wurde im Juli 2024 ein neues Repository angelegt.

## Datengrundlage

Der Arbeit liegen die folgenden Daten Tabellen zu Grunde:

* personalien.csv
* noten_bm.csv
* noten_efz.csv

Aus diesen Rohdaten wurden die folgenden Daten Tabellen errechnet:

* korrelationen.csv
* normalverteilung_bm.csv
* normalverteilung_bm_zahlen.csv
* normalverteilung_efz_zahlen.csv
* pearson_signifikanztest.csv
* pearson.csv
* spearman.csv
* spearman_signifikanz.csv

Alle diese Daten Tabellen finden sich in anonymisierter
Form im GitHub Repositroy
[https://github.com/Jacques-Mock-Schindler/impactofct](https://github.com/Jacques-Mock-Schindler/impactofct/tree/main/docs/data)
(der Link führt direkt in den Unterordner mit den Tabellen).

## Für die Auswertung verwendete Python Scripts

Wie in [@sec:effektive_methode] (Beschreibung der Methode) erwähnt,
erfolgte die Auswertung der Daten mit Hilfe von Python Scripts. Hier
eine Auflistung der erstellten Scripts:


* anonymisierung.py
* csv2tex.py
* korrelation.py
* korrelationen_gruppiert.py
* mittlere_korrelation.py
* modul_signifikanz.py
* normalverteilung.py
* normalverteilung_visuell.py
* semesterwerte_efz.py
* signifikanz.py
* visualisierung_uebersicht.py

Alle Scripts finden sich im GitHub Repository
[https://github.com/Jacques-Mock-Schindler/impactofct](https://github.com/Jacques-Mock-Schindler/impactofct/tree/main/docs/code)
(der Link führt direkt in den Unterordner mit den Scripts).
