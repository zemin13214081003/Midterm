from flask import Flask

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
    print("Here is your string: ")

#Create the flask app to accept a string argument on the POST curl
@app.route('/all', methods=['GET', 'POST'])
def post(string):
    parser = reqparse.Requestparser()
    parser.add_argument('string', required = TRUE, type = str)
    args = parser.parse_args()
    return{'NLP Service':args['string']}, 200

#NLP Service 1: to lower case:
@app.route('/1', methods=['POST'])
def NLPSERVICE1():
    string=request.args.get('string')
    input_str = string
    Service1Out = input_str.lower()
    return Service1Out

#NLPService 2: remove numbers:
@app.route('/2', methods=['POST'])
def NLPSERVICE2():
    import re
    input_str = string
    Service2Out = re.sub(r"\d+", "", input_str)
    return Service2Out


#NLP Service 3: extract the stream of tokens with the help of regular expressions
@app.route('/3', methods=['POST'])
def NLPSERVICE3():
    tk = RegexpTokenizer('\s+', gaps = True)
    input_str = string
    Service3Out = tk.tokenize(input_str)
    return Service3Out

#NLP Service 4: sentiment analysis
@app.route('/4', methods=['POST'])
def NLPSERVICE4():
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    Service4Out = [analyzer.polarity_scores(string)] 
    return Service4Out
             
#NLP Service 5

#NLP Service 6    
             
#Error Handling

             
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9776259)
