import requests
import json
import csv
from datetime import date


def retrieveData(channel, key,clickTrackingParams,continuation):

    url = "https://www.youtube.com/youtubei/v1/browse"

    querystring = {"key":key}

    payload = "{\"context\":{\"client\":{\"hl\":\"en\",\"gl\":\"ID\",\"remoteHost\":\"103.105.31.64\",\"deviceMake\":\"\",\"deviceModel\":\"\",\"visitorData\":\"CgtWdjFwdVV6cjl4WSiFzKyQBg%3D%3D\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0,gzip(gfe)\",\"clientName\":\"WEB\",\"clientVersion\":\"2.20220214.00.00\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"originalUrl\":\"https://www.youtube.com/c/RansEntertainment/videos\",\"platform\":\"DESKTOP\",\"clientFormFactor\":\"UNKNOWN_FORM_FACTOR\",\"configInfo\":{\"appInstallData\":\"CIXMrJAGEIDqrQUQt8utBRCY6q0FEOfR_RIQ2L6tBRCR-PwS\"},\"timeZone\":\"Asia/Bangkok\",\"browserName\":\"Firefox\",\"browserVersion\":\"88.0\",\"screenWidthPoints\":1366,\"screenHeightPoints\":178,\"screenPixelDensity\":1,\"screenDensityFloat\":1,\"utcOffsetMinutes\":420,\"userInterfaceTheme\":\"USER_INTERFACE_THEME_LIGHT\",\"mainAppWebInfo\":{\"graftUrl\":\"https://www.youtube.com/c/RansEntertainment/videos\",\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\",\"isWebNativeShareAvailable\":false}},\"user\":{\"lockedSafetyMode\":false},\"request\":{\"useSsl\":true,\"internalExperimentFlags\":[],\"consistencyTokenJars\":[]},\"clickTracking\":{\"clickTrackingParams\":\""+clickTrackingParams+"\"},\"adSignalsInfo\":{\"params\":[{\"key\":\"dt\",\"value\":\"1644897803395\"},{\"key\":\"flash\",\"value\":\"0\"},{\"key\":\"frm\",\"value\":\"0\"},{\"key\":\"u_tz\",\"value\":\"420\"},{\"key\":\"u_his\",\"value\":\"2\"},{\"key\":\"u_h\",\"value\":\"768\"},{\"key\":\"u_w\",\"value\":\"1366\"},{\"key\":\"u_ah\",\"value\":\"728\"},{\"key\":\"u_aw\",\"value\":\"1366\"},{\"key\":\"u_cd\",\"value\":\"24\"},{\"key\":\"bc\",\"value\":\"31\"},{\"key\":\"bih\",\"value\":\"178\"},{\"key\":\"biw\",\"value\":\"1349\"},{\"key\":\"brdim\",\"value\":\"-8,-8,-8,-8,1366,0,1382,744,1366,178\"},{\"key\":\"vis\",\"value\":\"1\"},{\"key\":\"wgl\",\"value\":\"true\"},{\"key\":\"ca_type\",\"value\":\"image\"}],\"bid\":\"ANyPxKqU5MaYGz2IJ0wSysemhy1ZYJI6D_7_ykiTSKA5nJSJRd016S3HQlNk-_qucHoCd8j-61k-VWk9jdxkVLT4gOO4e5krzA\"}},\"continuation\":\""+continuation+"\"}"
    headers = {
    
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    data = response.json()['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']

    for datum in data[:-1]:
       
        print("Video ID:",datum['gridVideoRenderer']['videoId'],"-",datum['gridVideoRenderer']['title']['runs'][0]['text'],"-",datum['gridVideoRenderer']['publishedTimeText']['simpleText'],"-",datum['gridVideoRenderer']['viewCountText']['simpleText'])
        with open(channel+'.csv','a',newline='',encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([datum['gridVideoRenderer']['videoId'], datum['gridVideoRenderer']['title']['runs'][0]['text'], datum['gridVideoRenderer']['publishedTimeText']['simpleText'], datum['gridVideoRenderer']['viewCountText']['simpleText'], date.today()])

    try:    
        next_continuation = data[len(data)-1]['continuationItemRenderer']['continuationEndpoint']

        clickTrackingParams_new = next_continuation['clickTrackingParams']
        continuation_new = next_continuation['continuationCommand']['token']

        print("clickTrancking:",clickTrackingParams_new)
        print("continuation:",continuation_new)

        retrieveData(channel, key,clickTrackingParams_new,continuation_new)
    except:
        print("Last Data")

    return 0

def goToVideo(key):
    url='https://www.youtube.com/watch?v='+key

    headers={}

    response = requests.request("GET", url, headers=headers)
    
    INNERTUBE_API_KEY = response.text.split('INNERTUBE_API_KEY')[1].split('":"')[1].split('","')[0]

    continuation = response.text.split('"token":"')[1].split('","')[0]

    print (INNERTUBE_API_KEY)
    print (continuation)

def getComment(isFirst:bool,key, continuation):
    url='https://www.youtube.com/youtubei/v1/next?key='+key+'&prettyPrint=false'
    payload = json.dumps({
    "context": {
        "client": {
        "hl": "en",
        "gl": "ID",
        "remoteHost": "114.125.250.52",
        "deviceMake": "",
        "deviceModel": "",
        "visitorData": "Cgs5MzJ0a3Z5T2RkYyiGpZ2VBg%3D%3D",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0,gzip(gfe)",
        "clientName": "WEB",
        "clientVersion": "2.20220609.00.00",
        "osName": "Windows",
        "osVersion": "10.0",
        "screenPixelDensity": 2,
        "platform": "DESKTOP",
        "clientFormFactor": "UNKNOWN_FORM_FACTOR",
        "configInfo": {
            "appInstallData": "CIalnZUGEJje_RIQmIeuBRCUj64FENSDrgUQuIuuBRC3y60FEIKOrgUQmOqtBRD_ja4FEJH4_BIQ2L6tBQ%3D%3D"
        },
        "screenDensityFloat": 1.5,
        "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
        "timeZone": "Asia/Jakarta",
        "browserName": "Firefox",
        "browserVersion": "100.0",
        "screenWidthPoints": 1280,
        "screenHeightPoints": 337,
        "utcOffsetMinutes": 420,
        "mainAppWebInfo": {
            "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
            "isWebNativeShareAvailable": False
        }
        },
        "user": {
        "lockedSafetyMode": False
        },
        "request": {
        "useSsl": True,
        "internalExperimentFlags": [],
        "consistencyTokenJars": []
        }
    },
    "continuation": continuation
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if(isFirst):
        data = response.json()['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems']
    else:
        data = response.json()['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction']['continuationItems']

    # print(data)

    for datum in data[:-1]:
        comment=datum['commentThreadRenderer']['comment']['commentRenderer']
        author = comment['authorText']['simpleText']
        textComment = comment['contentText']['runs']

        print(author)
        # print(textComment)

    print(data[len(data)-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])


channel = "AdiHidayatOfficial"
url = "https://www.youtube.com/c/"+channel+"/videos"

headers = {

    }

response = requests.request("GET", url, headers=headers)

ytInitialData = response.text.split('ytInitialData')

json1=ytInitialData[1].split(';')[0].split('gridRenderer')[1].split('submenu')[0].split('targetId')[0]

key = response.text.split('INNERTUBE_API_KEY":"')[1].split('"')[0]

clickTrackingParams_MP = response.text.split('"clickTracking":{"clickTrackingParams":"')[1].split('"}},"INNERTUBE')[0]

continueation_token = response.text.split('"continuationCommand":{"token":"')[1].split('","request"')[0]

data_main = json.loads(response.text.split('var ytInitialData = ')[1].split(';')[0])
data=data_main['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']

print("len",len(data))
for i,datum in enumerate(data[:-1]):
    print (i)
    if "publishedTimeText" in datum['gridVideoRenderer']:
        print("Video ID:",datum['gridVideoRenderer']['videoId'],"-",datum['gridVideoRenderer']['title']['runs'][0]['text'],"-",datum['gridVideoRenderer']['publishedTimeText']['simpleText'],"-",datum['gridVideoRenderer']['viewCountText']['simpleText'])
        with open(channel+'.csv','a',newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([datum['gridVideoRenderer']['videoId'], datum['gridVideoRenderer']['title']['runs'][0]['text'], datum['gridVideoRenderer']['publishedTimeText']['simpleText'], datum['gridVideoRenderer']['viewCountText']['simpleText'], date.today()])


next_continuation = data[30]['continuationItemRenderer']['continuationEndpoint']

clickTrackingParams = next_continuation['clickTrackingParams']
continuation = next_continuation['continuationCommand']['token']

print("clickTracking:", clickTrackingParams)
print("continuation:", continuation)
retrieveData(channel,key,clickTrackingParams,continuation)

# goToVideo('jHS4ShVFjEY')

# getComment(True,'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8','Eg0SC2pIUzRTaFZGakVZGAYyJSIRIgtqSFM0U2hWRmpFWTAAeAJCEGNvbW1lbnRzLXNlY3Rpb24%3D')

# getComment(False,'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8','Eg0SC2pIUzRTaFZGakVZGAYy4AIKtgJnZXRfcmFua2VkX3N0cmVhbXMtLUNxWUJDSUFFRlJlMzBUZ2Ftd0VLbGdFSTJGOFFnQVFZQnlLTEFmdnRsMGQ3dngwWF9lSlV2MFFGSHlPVTZSV2ZvYUZwbTlIS0JHVGRUOFpSWnNySk1zMDFDSUtsWnliYXgtQmdlMmExU25DVG5WaXAzeWktZFJ6WUNtSld0U3RrcG5FWTNVMWlTLTlhcEpnX3VPR3hLNXhYWHBCZjlxVHptaWxlRjVrU0dmTEVqcWdLRGdVeEdtM0sxSDNOZGRVeUxESFVoVkU0ZTlJVUNZVzIyOEtDRmM1RFRmb0dPQU1RRkJJRkNJa2dHQUFTQlFpSElCZ0FFZ1VJaGlBWUFCSUZDSWdnR0FBU0J3aVhJQkFQR0FFU0J3aUZJQkFVR0FFWUFBIhEiC2pIUzRTaFZGakVZMAB4ASgUQhBjb21tZW50cy1zZWN0aW9u')





