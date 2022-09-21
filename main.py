from Helpers import downloadGEOSData, downloadWRFCHEMNepal, downloadWRFCHEMHKH

downloadFolderWRFCHEMNepal = '/home/suman/ThreddsDataServerDataset/AirQualityDataAutoDownloadPython'
downloadWRFCHEMNepal(downloadFolderWRFCHEMNepal, '2022-09-01', '2022-09-20')


downloadFolderWRFCHEMHKH = '/home/suman/ThreddsDataServerDataset/AirQualityDataAutoDownloadPython'
downloadWRFCHEMHKH(downloadFolderWRFCHEMHKH, '2022-09-01', '2022-09-20')

downloadFolderGEOS = '/home/suman/ThreddsDataServerDataset/AirQualityDataAutoDownloadPython'
downloadGEOSData(downloadFolderGEOS, '2022-09-01', '2022-09-20')
