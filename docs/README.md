# CompStat@CU
A mapping and statistics reporting tool for crime on the University of Colorado at Boulder campus.

## CompStat
CompStat@CU is a specialized set of data-analysis tools used to analyze crime and crime trends on CU Boulder's campus. While CompStat as a whole normally embodies a wide-ranging set of policing philosophies and methods (the DOJ recently did a neat report on its growth and development [here](https://www.bja.gov/publications/perf-compstat.pdf)), this tool is strictly an algorithim-driven piece of software. 

## Documentation
All documentation about this system can be found in the `/docs/` folder. Considering that this program is still in the early stages of development, there is not much there as of yet. 

## Data Sources
- Crime data is provided courtesy of the CUPD, which releases daily crime logs about incidents on campus [here](https://www.colorado.edu/police/records-reports/daily-crime-log).   
- Geocoding data, which allows us to turn street addresses into exact coordinates, is from the [US Census Bureau](https://www.census.gov/geo/maps-data/data/geocoder.html) and OpenStreetMap's nifty [Nominatim](https://wiki.openstreetmap.org/wiki/Nominatim) tool. 

## Future Features
Our team is currently working on many future features, including:
- A refacotred code-base that actually fits the principles of clean code
- Analysis of current crime trends and anamolous incidents using k-means clustering
- Mathematically-driven calculation of the most dangerous times/areas of the year on-campus
- Construction of predictive models to anticipate future crime developements 
- An API so that anybody can use the data we parsed

## Other tools
- Apache's [PDFBox](https://pdfbox.apache.org/) is used to transform the PDFs into easily-readable plaintext.   
- [Leaflet](http://leafletjs.com/) is used to display the data after going through processing.   

## License
This program is currently licensed under the MIT license, which can be found in the `/docs/` folder.

## Disclaimer
This data is as up to date as we can make it, however, it is **not** guaranteed to be 100% accurate or complete.
I am **not** officially affiliated with the University or the Police Department.


Feel free to get in touch with me at the email on my GitHub profile. I'm always down to talk more about this program and data analysis in general.


Also huge shoutout to the men and women of the CUPD who make CU a safe and secure place to live and study.
