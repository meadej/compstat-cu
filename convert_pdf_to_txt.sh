#!/bin/bash
for filename in pdfs/*.pdf; do
    echo $filename
    java -jar pdfbox-app-2.0.8.jar ExtractText $filename -encoding UTF-8 -sort
done
