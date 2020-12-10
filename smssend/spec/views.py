from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class PhoneNumber(APIView):
    def get(self,request):
        data = request.GET
        driver = data.get('driver_id')
        phone_number = data.get('phone_number')
        print('THIS IS DRIVER',driver)
        print('THIS IS PHONE NUMBER',phone_number)
        headers = {
            'api_key': '15b056aae8c5b037ff52ffa5b6cd1180',
            'Content-type': 'application/json'
        }
        driver_request = requests.get(f'http://0727-dmitrov.ligataxi.com/api/v1/drivers/{driver}/',headers=headers)
        driver_data=driver_request.json()
        print('THIS IS DRIVER DATAAAA',driver_data)
        car = driver_data.get('car')
        print('THIS IS CARRR',car)
        text = f'За вами приедет {car} '
        after_url = {'number':phone_number,
                     'text':text,
                     'sign':'Tach Taxi',
                     'channel':'DIRECT'}

        url = requests.get('https://agil.makhmudov@mail.ru:Q9BqK8I8HXoEx1hVIhcE4gRkBVa1@gate.smsaero.ru/v2/sms/send?',params=after_url)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',url.status_code)