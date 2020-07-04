import requests
import json

url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36'}
r = requests.get(url, headers = headers)
data_str = r.text
data_list = json.loads(data_str)

for data in data_list:
    cname = data['cname']
    ename = data['ename']
    
    skin_num = 1
    skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(skin_num) + '.jpg'
    skin_data = requests.get(skin_url, headers = headers)
    
    #请求图片数据
    while(skin_data.status_code != 404):
        with open('HonorImageTrue\\' + cname + '-皮肤' + str(skin_num) + '.jpg', 'wb') as f:
            print('正在下载海报', cname + '-皮肤' + str(skin_num))
            f.write(skin_data.content)
        skin_num += 1
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(skin_num) + '.jpg'    
        #http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/525/525-bigskin-2.jpg
        #print(skin_url)
        skin_data = requests.get(skin_url, headers = headers)
print('下载完成，感谢您的使用！')
