# Midterm
MidtermHook.py README

All calls to this API will receive this print before the request is completed:
  'FE 595 Group 8: Zemin Li, Sherri Putnam, Spencer Tirella'

Create the flask app to accept a string argument on the POST curl
@app.route('/all', methods=['GET', 'POST'])
def post(string):
    parser = reqparse.Requestparser()
    parser.add_argument('string', required = TRUE, type = str)
    args = parser.parse_args()
    return{'NLP Service':args['string']}, 200

#NLP Service 1: to lower case:
@app.route("/1", methods=["POST"])

#NLPService 2: remove numbers:
@app.route('/2', methods=['POST'])

#NLP Service 3: extract the stream of tokens with the help of regular expressions
@app.route('/3', methods=['POST'])

#NLP Service 4: sentiment analysis
@app.route('/4', methods=['POST'])
             
#NLP Service 5
@app.route('/5', methods=['POST'])

#NLP Service 6
@app.route('/6', methods=['POST'])

  
#Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

Utilize the following Python curl call:

import requests
url = "http://3.21.158.149:789654/3"
response = requests.post(url, json={'string': 'MY TEST123'})
print(response.text)
print(response)
