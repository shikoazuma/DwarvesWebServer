from flask import Flask, jsonify
import requests
import simplejson
import json


webserver = Flask(__name__)
webserver.config['JSON_AS_ASCII'] = False
url = "https://thedwarves.pusherplatform.io/api/dwarves"
testResponse = requests.get(url)
answeredResponse = testResponse.text
data = json.loads(answeredResponse)


dwarves_list = []
dic = data['dwarves']
for personal_info in dic:
    dwarves_list.append(personal_info['name'])



@webserver.route("/api/dwarves")
def searchDwarves():
    output = {}
    
    output['dwarves'] = dwarves_list
    
    return jsonify(output)



@webserver.route("/api/dwarves/<string:dwarf>")
def searchDwarf(dwarf):
    output = {}

    if dwarf not in dwarves_list:
        return "Dwarf does not exist"

    else:
        for person in dic:
            if person['name'] == dwarf:
                output['dwarf'] = person
                break
        return jsonify(output)







if __name__ == "__main__":
    webserver.run(debug=True, host="127.0.0.1", port=8888)
