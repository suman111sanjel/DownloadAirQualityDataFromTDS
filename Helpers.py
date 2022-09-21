import xml.etree.ElementTree as ET
import requests
import datetime
import os
import urllib.request

baseUr = 'http://smog.icimod.org:8080'


def create_if_not_exists(path):
    if (not os.path.exists(path)):
        os.makedirs(path)

    return path


def CatalogFiles(url, data_ext):
    '''
    Args:
        url: catalog url
        data_ext: file extension

    Returns: list of files
    '''

    tree = ET.fromstring(requests.get(url).text)
    list = []

    for c in tree.iter():
        l = c.get('name')
        list.append(l)

    new = [x for x in list if (x is None) == False]
    new_list = []
    for l in filter(lambda x: x[-3:] == data_ext, new):
        new_list.append(l)
    final = new_list
    final.sort()
    return final


def SliceFromDateCatalog(url, startDate, endDate):
    '''
    Args:
        url: catalog url
        startDate: start date for slice
        endDate: end date for slice

    Returns: list of sliced
    '''

    tree = ET.fromstring(requests.get(url).text)
    list = []

    for c in tree.iter():
        l = c.get('name')
        list.append(l)

    new = [x for x in list if (x is None) == False]
    new_list = []
    for l in filter(lambda x: x[0:2] == '20', new):
        new_list.append(l)
    final = []
    if (startDate[-9] == '-' and endDate[-9] == '-'):
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d-%H-%M')
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d-%H-%M')
    elif (startDate[-9] == '-'):
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d-%H-%M')
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    elif (endDate[-9] == '-'):
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d-%H-%M')
    else:
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')

    for i in range(len(new_list)):
        x = datetime.datetime.strptime(new_list[i], '%Y%m%d')
        if (x >= startDate and x <= endDate):
            y = new_list[i]
            final.append(y)
    final.sort()
    return final


def downloadModelData(url, downloadFolder, sd, ed):
    '''
    This downloads tha model data
    :param url: catalog url
    :param downloadFolder: saving path
    :param sd: start date
    :param ed: end date
    :return: None
    '''
    selectedDates = SliceFromDateCatalog(url, sd, ed)
    ListOfFilesToDownload = []
    for i in selectedDates:
        curDateURL = url.replace('/catalog.xml', '/' + i + '/catalog.xml')
        NcfilesNames = CatalogFiles(curDateURL, '.nc')
        Savingpath = os.path.join(downloadFolder, i)
        create_if_not_exists(Savingpath)
        for j in NcfilesNames:
            DownloadUrl = curDateURL.replace('/catalog/', '/fileServer/')
            DownloadUrl = DownloadUrl.replace('/catalog.xml', '/' + j)
            obj = {'url': DownloadUrl, 'Savingpath': os.path.join(Savingpath, j)}
            ListOfFilesToDownload.append(obj)

    for ik in ListOfFilesToDownload:
        urllib.request.urlretrieve(ik['url'], ik['Savingpath'])
        print("Download " + "Complete for " + ik['Savingpath'])


def downloadWRFCHEMNepal(downloadFolder, sd, ed):
    '''
    Downloads WRF-Chem data for Nepal
    :param downloadFolder: saving path
    :param sd:start date
    :param ed:end date
    :return: None
    '''
    url = baseUr + '/thredds/catalog/HKHAirQualityWatch/Forecast/WRF_Chem/d2_NP/catalog.xml'
    downloadModelData(url, downloadFolder, sd, ed)


def downloadWRFCHEMHKH(downloadFolder, sd, ed):
    '''
    Downloads WRF-Chem data for HKH
    :param downloadFolder: saving path
    :param sd:start date
    :param ed:end date
    :return: None
    '''
    url = baseUr + '/thredds/catalog/HKHAirQualityWatch/Forecast/WRF_Chem/d1_HKH/catalog.xml'
    downloadModelData(url, downloadFolder, sd, ed)


# list of geos Pollutant
PollutantList = ['CO', 'NO2', 'O3', 'PM', 'SO2']


def downloadGEOSData(downloadFolder, Pollutant, sd, ed):
    '''
    Download GEOS Data
    :param download Folder: saving path
    :param Pollutant: Pollutant string  ['CO', 'NO2', 'O3', 'PM', 'SO2']
    :param sd:start date
    :param ed:end date
    :return:
    '''
    if Pollutant in PollutantList:
        url = baseUr + '/thredds/catalog/HKHAirQualityWatch/Forecast/' + Pollutant + '/GEOS-' + Pollutant + '/catalog.xml'
        downloadModelData(url, downloadFolder, sd, ed)
    else:
        print('Invalid pollutant!!! Please give a valid pollutant. \n Following are the valid pollutants \n',
              ','.join(PollutantList))
