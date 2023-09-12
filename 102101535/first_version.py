import requests
import re
from openpyxl import Workbook

def main():

    workbook = Workbook()
    sheet = workbook.active
    headers = {
        'cookie': 'buvid3=AF7E4336-683D-2AEB-5667-5FB21535E67187193infoc; i-wanna-go-back=-1; _uuid=F93E3C87-10382-23AD-824B-27A193361E8E66199infoc; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; buvid_fp=2ba3ad7f6acb16191f1ca49ffc5c66b3; home_feed_column=5; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(u))kkYu|Ru0J\'uY))m~YRl); DedeUserID=527426084; DedeUserID__ckMd5=00b587f1778e1e7b; b_ut=5; LIVE_BUVID=AUTO5716894257275090; CURRENT_QUALITY=80; SESSDATA=430f2148%2C1705238175%2C979d2%2A72xoe6cwW6v8CmqC2s1IXhkMwzPMZyCx5XdhwFHZX-XN4sTGTJxXrWqVh2aK1s569jWiUxbQAAVAA; bili_jct=40f034f73101fa664a3d63ef89673470; sid=6wb18330; b_nut=1689748974; buvid4=7A0E5B98-695A-4A87-3965-0F4C57AE23D188249-023072016-Mk4wjKcJQ46e8fG6nCNzkDivye7Qm5pptEQXu4qFguaYYVRWkzj5LQ%3D%3D; PVID=1; browser_resolution=1528-750; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQyNDQ0NTIsImlhdCI6MTY5Mzk4NTI1MiwicGx0IjotMX0.hSJQoBvDe4fdw9gOlHh_94WTswnSf8dKbaUs8rjfyfk; bili_ticket_expires=1694244452; b_lsid=75EC3556_18A69B52964',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/video/BV1yF411C7ZJ/?spm_id_from=333.337.search-card.all.click&vd_source=e5ea948412c2a8820992ad19400de8ab',
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=1245133831&date=2023-09-06'
    response = requests.get(url=url,headers=headers)
    data = re.findall('.*?([\u4e00-\u9fa5]+).*',response.text)
    for index in data:
        print(index)
        sheet.append([index])
    workbook.save('弹幕.xlsx')

main()





