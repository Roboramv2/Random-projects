import requests

url = "https://www.fast2sms.com/dev/bulk"

headers = {
'authorization': "__INSERT FAST2SMS AUTHORIZATION__",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}


def sendSMS(mobileNo,accountNo,price):

    
    text="__ENTER TEXT FOR SMS__"

    payload = "sender_id=FSTSMS&message="+str(text)+"&language=english&route=p&numbers="+str(mobileNo)

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

