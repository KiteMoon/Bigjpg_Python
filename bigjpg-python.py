import requests
import json

url1 = input("请输入图片地址：")
mode = input("请输入图片类型（art/photo）：")
level = input("请输入图片降噪级别（-1/0/1/2/3)(数字越大级别越高）：")
multiple = input("请输入放大倍数（1/2/3/4）（分别为x2/x4/x6/x8)：")


data = {
    "style": mode,
    "noise": level,
    "x2": multiple,
    "input": url1,
}

r = requests.post(
    url='https://bigjpg.com/api/task/',
    headers={'X-API-KEY': "your key"},
    data={'conf': json.dumps(data)}
    )
print(r.json())
input("按任意键关闭")
#要不要加个睡眠进程呢。。。
