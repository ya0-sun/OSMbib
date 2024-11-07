# OSMbib

This repo contains research data and interactive visualization of the OSM review paper. 


## Interactive visualization 

🠊 ${\color{red}Click\space on \space \color{lightBlue}the \space Figures \space \color{lightgreen}to \space Explore \space Networks \space \color{orange}Interactively}$


### [Network clusters of keywords](https://app.vosviewer.com/?json=https%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1EbZDFNeOB0pFYYCwtFcOSIrvx6kGutQO)

*416 keywords out of 6,264 (both author keywords and key-words plus) with a minimum of 5 occurrences.*

* Two most frequent keywords- “openstreetmap”（816 occurrences) and “volunteered geographic information” (225 occurrences) were excluded to avoid overshadowing other keywords
* A total of 414 keywords were analyzed.

[![Network clusters of keywords:](https://github.com/user-attachments/assets/317d612f-38c6-46ef-890b-fc4df0081b86 'Network clusters of keywords')](https://app.vosviewer.com/?json=https%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1EbZDFNeOB0pFYYCwtFcOSIrvx6kGutQO)


### [Organizations' co-authorship network](https://app.vosviewer.com/?json=https\%3A\%2F\%2Fdrive.google.com\%2Fuc\%3Fid\%3D1CXvU7ZT3QXlY-hxaguZ5xd0mdVmgTJE5)

*67 organizations are selected with a minimum threshold of 10 documents.*

[![Organizations' Co-Authorship Network:](https://github.com/ya0-sun/OSMbib/blob/main/img/organization.png 'Organizations Co-Authorship Network')](https://app.vosviewer.com/?json=https%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CXvU7ZT3QXlY-hxaguZ5xd0mdVmgTJE5)


### [Co-authorship network](https://app.vosviewer.com/?json=https%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1BZZPj4WQq477UoeBQhTDaV09ll5_daAl)

*92 authors are selected with a minimum threshold of 5 documents per author.*

[![Co-Authorship Network:](https://github.com/ya0-sun/OSMbib/blob/main/img/co-authorship.png 'Co-Authorship Network')](https://app.vosviewer.com/?json=https%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1BZZPj4WQq477UoeBQhTDaV09ll5_daAl)

## [Data](https://github.com/ya0-sun/OSMbib/tree/main/data) 

### WoS 

The directory contains WoS data used in this work: 
* [original data downloaded from WoS](https://github.com/ya0-sun/OSMbib/tree/main/data/wos/wos_download)
* [merged data](https://github.com/ya0-sun/OSMbib/blob/main/data/wos/wos_merged_mod.txt)
* rules and examples for disambiguation [authors](https://github.com/ya0-sun/OSMbib/blob/main/data/wos/names_change.txt) and [affiliations](https://github.com/ya0-sun/OSMbib/blob/main/data/wos/affiliation_change.txt). 

### SotM 

The directory contains SotM data used in this work:
* [SotM websites](https://github.com/ya0-sun/OSMbib/blob/main/data/sotm/sotm_websites.md)
* [curated data of talks in each year](https://github.com/ya0-sun/OSMbib/blob/main/data/sotm/sotm_TI_AU_PY_merged.xlsx)
* [key players info webpage from OSM](https://github.com/ya0-sun/OSMbib/blob/main/data/sotm/keyFigures_infoList.md)
* [merged data list with Title-Author-Year](https://github.com/ya0-sun/OSMbib/blob/main/data/sotm/sotm_TI_AU_PY_merged.xlsx)

## [Analysis](https://github.com/ya0-sun/OSMbib/tree/main/analysis)
including research data for: 
* 0-documents_country_year
* 1-affiliations
* 2-author_affiliations
* 3-coauthorship
* 4-keywords
* 5-history
* 6-trendTopics
