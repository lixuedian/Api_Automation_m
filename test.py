import requests
import json

utl = 'http://test-user.ekeguan.com/sem/addSemUser'
url = 'http://test-shijuan.ekeguan.com'
data = {
    "businessId": 2,
    "mobilestyle": 'pc',
    "sourceType": '42',
    "graduateTime": '202207',
    "degree": '本科',
    'phone': 18500352554,
    'smsCode': 8272
       }
header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'projectId': '1',
    'appFlag': '1',
    'deviceType': 'HUAWEI_EML-AL00_29',
    'deviceId': 'e77f7bcd-97ad-87f3-c79b-fbe7ffbffbaa',
    'platformVersion': 'Andriod:4.1+',
    'platform': 'android-Android',
    'EagleEye-TraceId': 'd26865ea-b22b-441d-d26865ea-b22b-441d',
    'timestamp': '1603198276',
    'appVersion': 'v4.1.7',
    'source': '1100'
}
data1 = {
    "businessId": 2,
    "phone": '18500352554'
}
# response = requests.post(url=url, headers=header, data=data1)
# print(response.json())
response = requests.post(url=utl, headers=header, data=data)
print(response.json())
