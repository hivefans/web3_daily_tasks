import json,requests,time
from datetime import datetime

def format_time(time):
    if time != None:
        time = int(time)
        dt = datetime.fromtimestamp(time)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return "no time"

def query_galaxy(payload, timeout=30, authorization='null'):
    url = "https://graphigo.prd.galaxy.eco/query"
    headers = {
        'Host': 'graphigo.prd.galaxy.eco',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'authorization': authorization,
        'content-type': 'application/json',
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://galaxy.eco',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://galaxy.eco/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload, timeout=timeout)
        resp_json = response.json()
        data = resp_json.get('data', {})
    except Exception as e:
        return False, str(e)
    else:
        return True, data

def campaign_latest(timeout=30,authorization='null'):
    query = '''query CampaignsLatest($input: ListCampaignInput!) {
                campaigns(input: $input) {
                    list {
                    __typename
                    id
                    numberID
                    type
                    name
                    status
                    gasType
                    chain
                    startTime
                    endTime
                    numNFTMinted
                    childrenCampaigns {
                        id
                        type
                        rewardName
                        __typename
                    }
                    creds {
                        __typename
                    }
                    space {
                        __typename
                        alias
                        name
                    }
                    }
                }
                }'''
    payload = json.dumps({
        "query":query,
        "variables":{
            "input":{
                "listType":"Newest",
                "types": ["Airdrop","Token","MysteryBox"],
                "gasTypes":["Gasless","Gas"],
                "statuses": ["Active"],
                "first":30,
                "after":"-1"
                }
                },
        "operationName":"CampaignsLatest"
        })
    status, data = query_galaxy(payload, timeout=timeout, authorization=authorization)
    if not status:
        print(f"获取活动信息失败, 报错: {data}")
        return False, {}
    else:
        campaign_info = data.get('campaigns', {}).get('list', {})
        print("获取活动最新信息成功")
        return True, campaign_info 


       
