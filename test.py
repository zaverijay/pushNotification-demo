
## Install request module by running ->
#  pip3 install requests

# Replace the deviceToken key with the device Token for which you want to send push notification.
# Replace serverToken key with your serverKey from Firebase Console

# Run script by ->
# python3 fcm_python.py


import requests
import json
from flask.json import jsonify

# def denfPushNotification(deviceToken):
# def sendPushNotification(uid, dtoken):
def sendPushNotification():

    print("pointer is here")

    serverToken = 'AAAAHJcqDUc:APA91bEbUMOcz0FwzvLDTzweJrrhyzqu7fYwLHSPF0EnaRuCjwaTHDM3-RxGlnK_pWA2SZWFr1i5cN3u5jIh1q9pZ5Pi-imHfiOTzXYUbeCKTN4-6ixtfD1xHtaLaWizjNXwdSPUdN8I'
    # deviceToken = 'device token here'

    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

    body = {
            # 'notification': {'title': 'Sending push form python script',
            #                  'body': 'New Message'},
            "u_id": 2,
            "d_token": "dtoken"
            }

    # return jsonify({
    #     "u_id" : body.get("u_id"),
    #     "d_token": body.get("d_token")
    #     })
    # print(body.get("u_id"))
    # response = requests.post("https://fcm.googleapis.com/fcm/send", headers = headers, data=json.dumps(body))
    response = requests.post("http://127.0.0.1:5000/post", headers = headers, data=json.dumps(body))


    print(response.status_code)
    print(response.json())


# sendPushNotification()