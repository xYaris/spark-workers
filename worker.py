from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

def get_api_key() -> str:
    secret = os.environ.get("COMPUTE_API_KEY")
    print(os.environ.keys())
    if secret:
        return secret
      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave3' #testing +str(request.form['num'])
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/spark-371009/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      return "Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
