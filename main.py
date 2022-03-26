import boto3
import botocore
from flask import Flask, request

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")

def Test_data(info):
    info = str(info)[1:-1]
    list_of_error_chars = ['<','>','{','}','$','=','/',chr(92)] ## chr(92) is '\'
    for char in list_of_error_chars:
        if char in info:
            return False
    return True

s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
obj = s3.Object('shaygefbucket','data.json')
app = Flask(__name__)
@app.route('/api/endpoint1', methods=["POST"])
def post():
    data = request.json
    if Test_data(data):
        try:
            data.update({}) ## check if the data is dict
            response = obj.put(Body=bytes(str(data),'utf-8'))
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return "The data was updated successfully"
            else:
                return "The data was not updated"

        except AttributeError:
            return "The data is not Dict type"
    else:
        return "Invalid value"

@app.route('/api/endpoint1', methods=["GET"])
def get():
    try:
        Get_data = obj.get()['Body'].read().decode("utf-8")
        return Get_data

    except botocore.exceptions.ClientError as e:
        status_code = e.response['ResponseMetadata']['HTTPStatusCode']
        return {"Error": status_code,
                "message": "something went wrong"}


if __name__ == '__main__':
    app.run(debug=True ,port=8080 ,host="0.0.0.0")