import requests
import json


reqUrl = "http://127.0.0.1:5000/post"

serverToken = 'AAAAHJcqDUc:APA91bEbUMOcz0FwzvLDTzweJrrhyzqu7fYwLHSPF0EnaRuCjwaTHDM3-RxGlnK_pWA2SZWFr1i5cN3u5jIh1q9pZ5Pi-imHfiOTzXYUbeCKTN4-6ixtfD1xHtaLaWizjNXwdSPUdN8I'

headersList = {
                "Content-Type": "application/json",
                "Authorization": "key=" + serverToken,
                }

payload = json.dumps({
                        "u_id": 18,
                        "d_token": "anish bazmi"
                        })

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)

