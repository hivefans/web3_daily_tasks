from utils import format_time,campaign_latest
import time
from supabase import create_client, Client

url: str = "supabase address"
key: str = "supabase secret key"
supabase: Client = create_client(url, key)

result,campaigns_list = campaign_latest()
timestamp = int(time.time())
last_1h = timestamp - 3600
if result:
    for campaign in campaigns_list:
        campaign_url = f"https://galxe.com/{campaign['space']['alias']}/campaign/{campaign['id']}"
        campaign_name = campaign['name']
        campaign_type = campaign['type']
        campaign_chain = campaign['chain']
        campaign_status = campaign['status']
        campaign_starttime = campaign['startTime']
        campaign_info = f"活动时间: {format_time(campaign_starttime)}\n活动名称: {campaign_name}\ngas类型: 免费\n活动链接: {campaign_url}\n活动类型: {campaign_type} \n活动链: {campaign_chain}"
        if campaign_starttime != None:
            if campaign_starttime >= last_1h and campaign_starttime <= timestamp:
                supabase.table('articles').insert({"title": campaign_name, "code": campaign_info,"category": "银河任务"}).execute()
