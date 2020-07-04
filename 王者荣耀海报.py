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
    try:
        skin_name = data['skin_name'].split('|')
    except Exception as e:
        print(e)
    #print(ename, cname, skin_name)
    
    #请求图片数据
    for skin_num in range (1, len(skin_name) + 1):
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(skin_num) + '.jpg'    
        #http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/525/525-bigskin-2.jpg
        #print(skin_url)
        skin_data = requests.get(skin_url, headers = headers).content
        
        #保存图片
        with open('HonorImage\\' + cname + '-' + skin_name[skin_num - 1] + '.jpg', 'wb') as f:
            print('正在下载海报', cname + '-' + skin_name[skin_num - 1])
            f.write(skin_data)
print("下载完成！感谢使用！")
