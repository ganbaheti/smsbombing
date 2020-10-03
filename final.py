import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# for getting request the code is : 
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# for response
response = sendPostRequest(URL, 'api key', 'secret key', 'for testing put: stage', 'mobile no.', 'email id', 'text message' )

# for api : sms4 india only gives 25 sms per day. Use a Private DNS for more SMS.

