# Generate sheet of barcodes

Upon receiving a spredsheet with SKU and Antall, run the following:

```
ph open excel export.xlsx | ph columns SKU Antall | ph query Antall
```

Rewrite the commas to

```tex
\putnbarcodes{1}{1000}
```
