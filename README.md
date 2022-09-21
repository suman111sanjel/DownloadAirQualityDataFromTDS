## Downloading Air Quality Data from TDS (THREDDS Data Server)
clone this project using the following code

`git clone https://github.com/suman111sanjel/DownloadAirQualityDataFromTDS.git`

****

### This project helps to download air quality forecast data for THREDDS Data Server. The THREDDS Data server is hosted by ICIMOD. Use the link below to access the thredds data server.

http://smog.icimod.org:8080/thredds/catalog/catalog.html


##How to download the forecast data
Open main.py

There are three function `downloadGEOSData, downloadWRFCHEMNepal, downloadWRFCHEMHKH`

###downloadGEOSData function

This function helps to download the GEOS forecast data.

`
downloadGEOSData(folderCompletePathToSave, Pollutant, StartDate, EndDate)
`

_folderCompletePathToSave:_(String type) Example:'/home/username/downloadFolder'(incase of Linux). If you are using windows use 'E:\downloadFolder' (This is just a example. You use any partation or location)

_Pollutant_: (String type) Example 'NO2'. Note use following code for different pollutant ('CO', 'NO2', 'O3', 'PM', 'SO2')

_StartDate:_(String type) format 'YYYY-MM-DD' Example: '2022-09-01'

_EndDate:_(String type) format 'YYYY-MM-DD' Example: '2022-09-20'


###downloadWRFCHEMNepal and downloadWRFCHEMHKH
This function helps to download WRFChem model data for different domain(HKH, Nepal)

    downloadWRFCHEMHKH(folderCompletePathToSave, StartDate, EndDate)
    downloadWRFCHEMNepal(folderCompletePathToSave, StartDate, EndDate)

_folderCompletePathToSave:_(String type) Example:'/home/username/downloadFolder'(incase of Linux). If you are using windows use 'E:\downloadFolder' (This is just a example. You use any partation or location)


_StartDate:_(String type) format 'YYYY-MM-DD' Example: '2022-09-01'

_EndDate:_(String type) format 'YYYY-MM-DD' Example: '2022-09-20'


Note: If you get any problem downloading the date. Please write to suman.sanjel@icimod.org