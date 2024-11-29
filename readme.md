Uge 7 Datasources

    pip install mysql-connector-python

Løsning: Main3.py

Data læses fra csv-filerne orders, products, restocks, start_inventory, suppliers

Laves til pandas dataframes
Dataframes laves til sql-tabeller vha DataFrame.to_sql()
Tabellerne behandles
Tabellerne skrives til sql vha pandas dataframe’s to_sql()
Og valideres med print(cursor.fetchall())

Med udgangspunkt i start_inventory er der indført en Inventory-tabel, for at kunne se
lagerstatus for et givet tidspunkt. Til dette mangler en funktion der behandler restocks og en
der behandler orders, og passende kald til begge.
