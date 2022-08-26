import json
import requests


def lambda_handler(event, context):
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(r.status_code)
    return {
        'statusCode': 200,
        'body': json.dumps('Mi lambda de project dev')
    }
