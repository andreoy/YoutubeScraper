import requests
import json
import csv
from datetime import date


def retrieveData(key,clickTrackingParams,continuation):

    url = "https://www.youtube.com/youtubei/v1/browse"

    querystring = {"key":key}

    payload = "{\"context\":{\"client\":{\"hl\":\"en\",\"gl\":\"ID\",\"remoteHost\":\"103.105.31.64\",\"deviceMake\":\"\",\"deviceModel\":\"\",\"visitorData\":\"CgtWdjFwdVV6cjl4WSiFzKyQBg%3D%3D\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0,gzip(gfe)\",\"clientName\":\"WEB\",\"clientVersion\":\"2.20220214.00.00\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"originalUrl\":\"https://www.youtube.com/c/RansEntertainment/videos\",\"platform\":\"DESKTOP\",\"clientFormFactor\":\"UNKNOWN_FORM_FACTOR\",\"configInfo\":{\"appInstallData\":\"CIXMrJAGEIDqrQUQt8utBRCY6q0FEOfR_RIQ2L6tBRCR-PwS\"},\"timeZone\":\"Asia/Bangkok\",\"browserName\":\"Firefox\",\"browserVersion\":\"88.0\",\"screenWidthPoints\":1366,\"screenHeightPoints\":178,\"screenPixelDensity\":1,\"screenDensityFloat\":1,\"utcOffsetMinutes\":420,\"userInterfaceTheme\":\"USER_INTERFACE_THEME_LIGHT\",\"mainAppWebInfo\":{\"graftUrl\":\"https://www.youtube.com/c/RansEntertainment/videos\",\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\",\"isWebNativeShareAvailable\":false}},\"user\":{\"lockedSafetyMode\":false},\"request\":{\"useSsl\":true,\"internalExperimentFlags\":[],\"consistencyTokenJars\":[]},\"clickTracking\":{\"clickTrackingParams\":\""+clickTrackingParams+"\"},\"adSignalsInfo\":{\"params\":[{\"key\":\"dt\",\"value\":\"1644897803395\"},{\"key\":\"flash\",\"value\":\"0\"},{\"key\":\"frm\",\"value\":\"0\"},{\"key\":\"u_tz\",\"value\":\"420\"},{\"key\":\"u_his\",\"value\":\"2\"},{\"key\":\"u_h\",\"value\":\"768\"},{\"key\":\"u_w\",\"value\":\"1366\"},{\"key\":\"u_ah\",\"value\":\"728\"},{\"key\":\"u_aw\",\"value\":\"1366\"},{\"key\":\"u_cd\",\"value\":\"24\"},{\"key\":\"bc\",\"value\":\"31\"},{\"key\":\"bih\",\"value\":\"178\"},{\"key\":\"biw\",\"value\":\"1349\"},{\"key\":\"brdim\",\"value\":\"-8,-8,-8,-8,1366,0,1382,744,1366,178\"},{\"key\":\"vis\",\"value\":\"1\"},{\"key\":\"wgl\",\"value\":\"true\"},{\"key\":\"ca_type\",\"value\":\"image\"}],\"bid\":\"ANyPxKqU5MaYGz2IJ0wSysemhy1ZYJI6D_7_ykiTSKA5nJSJRd016S3HQlNk-_qucHoCd8j-61k-VWk9jdxkVLT4gOO4e5krzA\"}},\"continuation\":\""+continuation+"\"}"
    headers = {
    
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    data = response.json()['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']

    for datum in data:
        try:
            print("Video ID:",datum['gridVideoRenderer']['videoId'],"-",datum['gridVideoRenderer']['title']['runs'][0]['text'],"-",datum['gridVideoRenderer']['publishedTimeText']['simpleText'],"-",datum['gridVideoRenderer']['viewCountText']['simpleText'])
            with open('youtube.csv','a',newline='',encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow([datum['gridVideoRenderer']['videoId'], datum['gridVideoRenderer']['title']['runs'][0]['text'], datum['gridVideoRenderer']['publishedTimeText']['simpleText'], datum['gridVideoRenderer']['viewCountText']['simpleText'], date.today()])
        except:
            print("error")
        
    next_continuation = data[30]['continuationItemRenderer']['continuationEndpoint']

    clickTrackingParams_new = next_continuation['clickTrackingParams']
    continuation_new = next_continuation['continuationCommand']['token']

    print("clickTrancking:",clickTrackingParams_new)
    print("continuation:",continuation_new)

    retrieveData(key,clickTrackingParams_new,continuation_new)

    return 0

channel = "RockyGerungOfficial2021"
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

for datum in data:
    
    print("Video ID:",datum['gridVideoRenderer']['videoId'],"-",datum['gridVideoRenderer']['title']['runs'][0]['text'],"-",datum['gridVideoRenderer']['publishedTimeText']['simpleText'],"-",datum['gridVideoRenderer']['viewCountText']['simpleText'])
    with open(channel+'.csv','a',newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([datum['gridVideoRenderer']['videoId'], datum['gridVideoRenderer']['title']['runs'][0]['text'], datum['gridVideoRenderer']['publishedTimeText']['simpleText'], datum['gridVideoRenderer']['viewCountText']['simpleText'], date.today()])


next_continuation = data[30]['continuationItemRenderer']['continuationEndpoint']

clickTrackingParams = next_continuation['clickTrackingParams']
continuation = next_continuation['continuationCommand']['token']

print("clickTracking:", clickTrackingParams)
print("continuation:", continuation)
retrieveData(key,clickTrackingParams,continuation)


