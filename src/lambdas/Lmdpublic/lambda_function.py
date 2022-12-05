import json
import requests
import psycopg2


def lambda_handler(event, context):

    try:
        connection = psycopg2.connect(
            host="dev-project-mydata-dbinstance.c8id9eg6dyio.us-east-1.rds.amazonaws.com",
            user="postgres",
            password="uzjmWhB5HVpxBNOSx8b.54Uu5JQNat",
            database="mydata"
        )
        print("Conexión exitosa!!")
    except Exception as ex:
        print(ex)

    return {
        'statusCode': 200,
        'body': json.dumps('Mi lambda publica')
    }