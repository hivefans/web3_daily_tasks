from utils import formatted_time,get_active_proposals
import time
from supabase import create_client, Client

url: str = "supabase address"
key: str = "supabase secret key"
supabase: Client = create_client(url, key)

space_set = ["ens.eth","aave.eth","stgdao.eth","arbitrumfoundation.eth","opcollective.eth","punklens.eth"]
timestamp = int(time.time())
last_1h = timestamp - 3600
active_props = get_active_proposals(space_set,last_1h)
for prop in active_props:
    proposal_title = prop['title']
    proposal_start = formatted_time(prop['start'])
    proposal_url = "https://snapshot.org/#/" + prop['space']['id'] + "/proposal/" + prop['id']
    print(proposal_title, proposal_start, proposal_url)
    if len(proposal_title) > 0:
        supabase.table('articles').insert({"title": proposal_title, "code": proposal_url,"category": "snapshot投票"}).execute()
