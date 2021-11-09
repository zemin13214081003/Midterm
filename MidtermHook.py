from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import json

app = Flask(__name__) # "__main__"

@app.route('/grp8', methods=['GET', 'POST'])
def flask_import():
  return """<html>
 
<body>
<h1>FA595 Midterm<h1><br><br>
<h2>Group 8: Zemin Li, Sherri Putnam, Spencer Tirella</h2>
<b>
<p>Deliverables:<br>
1. Created a flask end point accessible to the entire internet hosted on an AWS machine<br>
2. Able to accept cURL calls on one route and successfully return a 200 status when called<br>
3. Able to accept in a request with a payload including a string and a requested NLP service<br>
&nbsp;&nbsp&nbsp;&nbsp;Our project is capable of returning 2 services for each member of our group<br>
</p>
</body>
</html>
  """



@app.before_request
def before():
    print('Hello and welcome')

#Create the flask app to accept a string argument on the POST curl
@app.route('/all', methods=['GET', 'POST'])
def post(string):
    parser = reqparse.Requestparser()
    parser.add_argument('string', required = TRUE, type = str)
    args = parser.parse_args()
    return{'NLP Service':args['string']}, 200

#NLP Service 1: to lower case:
@app.route("/nlp1", methods=["POST"])
def nlp1():
    string={'string':request.json['string']}
    string2=json.dumps(string)
    string3=str.lower(string2)
    return jsonify({'string':string3})

#NLPService 2: remove numbers:
@app.route('/2', methods=['GET', 'POST'])
def NLPSERVICE2():
    import re
    input_str = string
    Service2Out = re.sub(r"\d+", "", input_str)
    return Service2Out

#NLP Service 3: extract the stream of tokens with the help of regular expressions
@app.route('/3', methods=['GET', 'POST'])
def NLPSERVICE3():
    tk = RegexpTokenizer('\s+', gaps = True)
    input_str = string
    Service3Out = tk.tokenize(input_str)
    return Service3Out

#NLP Service 4: sentiment analysis
@app.route('/4', methods=['GET', 'POST'])
def NLPSERVICE4():
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    Service4Out = [analyzer.polarity_scores(string)] 
    return Service4Out
             
#NLP Service 5
@app.route('/5', methods=['GET', 'POST'])
def NLPSERVICE5():
    str = request.form["request"]
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    com = re.split(pattern, str)
    lenth = len(com)
    strr = ["how many word ",lenth]
    return(strr)

#NLP Service 6
@app.route('/6', methods=['GET', 'POST'])
def NLPSERVICE6():
    com1 = request.form["request"]
    lenth = len(com1)
    strr = ["the length of words ", lenth]
    return(strr)
  
#Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=74747)
