from flask import Flask, jsonify,render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient("<connection string>")
db = client.get_database('<db>') 
records = db.studentData


# we are using mailgun to send mail notification
def mail_response(response,sub):
    # response is response we created which conatin all user's name and response code from google code:200 means success code:500 means client error
    #sub indicates which end point is called
    return requests.post(
        "Mailgun api call url",
        auth=("api", "<api key>"),
        data={"from": "attendance@<domain>",
              "to": ["to get notification"],
              "subject": sub + 'attendance filled',
              "text": response})



@app.route('/endpoint1', methods=['GET'])
def fillAJlect():
    url = '<formlink ending with response>'
    # https://docs.google.com/forms/u/0/d/e/******************************/formResponse
    data = list(records.find())
    response = [{'url':'<form link ending with viewform>'}]
    # https://docs.google.com/forms/d/e/**********************************/viewform
    for stu in data:
        form_data = {
            'entry.<your entry point>':stu['name'],
            'entry.<your entry point>':stu['enroll'],
            'draftResponse':[],
            'pageHistory':0}
        user_agent = {'Referer':response[0]['url'],'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        response.append({'name':stu['name'],'code':requests.post(url, data=form_data,headers=user_agent).status_code})
    mail_response(str(response),'used for mail notification subject name')
    return jsonify(response),200

@app.route('/endpoint2',methods=['GET'])
def fillAADlect():
    url= '<formlink ending with response>'
    # https://docs.google.com/forms/u/0/d/e/******************************/formResponse
    data = list(records.find())
    response =[{'url':'<form link ending with viewform>'}]
    for stu in data:
        form_data = {
            'entry.595650876':stu['name'],
            'entry.878245842':stu['enroll'],
            'draftResponse':[],
            'pageHistory':0}
        user_agent = {'Referer':response[0]['url'],'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        response.append({'name':stu['name'],'code':requests.post(url, data=form_data,headers=user_agent).status_code})
    mail_response(str(response),'Advance Java')
    return jsonify(response),200


@app.route('/endpoint3',methods=['GET'])
def fillWNS():
    url= '<formlink ending with response>'
    # https://docs.google.com/forms/u/0/d/e/******************************/formResponse
    data = list(records.find())
    response =[{'url':'<form link ending with viewform>'}]
    for stu in data:
        form_data = {
            'entry.359062664':stu['name'],
            'entry.501364324':stu['enroll'],
            'entry.1292587064':'6',
            'draftResponse':[],
            'pageHistory':0}
        user_agent = {'Referer':response[0]['url'],'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        response.append({'name':stu['name'],'code':requests.post(url, data=form_data,headers=user_agent).status_code})
    mail_response(str(response),'Advance Java')
    return jsonify(response),200


# this is test form i have created
@app.route('/test',methods=['GET']) 
def test():
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeH7oiXdmY9w_UUAH1ljcMXOkRTRUEYh4oX0TT5o9XnYuunrA/formResponse'
    
    data = list(records.find())
    response = [{'url':url}]
    for stu in data:
        form_data = {
            'entry.1162833800':stu['name'],
            'entry.227471117':stu['enroll'],
            'entry.51347225':'6',
            'entry.213055577':stu['email'],
            'draftResponse':[],
            'pageHistory':0}
        user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSeH7oiXdmY9w_UUAH1ljcMXOkRTRUEYh4oX0TT5o9XnYuunrA/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        response.append({'name':stu['name'],'code':requests.post(url, data=form_data,headers=user_agent).status_code})

    return jsonify(response),200


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()