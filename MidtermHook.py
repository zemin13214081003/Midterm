from flask import Flask
from flask_restful import Resource, Api, regparse

app = Flask(__name__) # "__main__"
api = Api(app)

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

#Create the flask app to accept a string argument on the POST curl
def post(string):
    parser = reqparse.Requestparser()
    parser.add_argument('string', required = TRUE, type = str)
    args = parser.parse_args()
    return{'NLP Service':args['string']}, 200

#NLP Service 1: to lower case:
input_str = string
input_str = input_str.lower()

#NLPService 2: remove numbers:
import re
input_str = string
result = re.sub(r"\d+", "", input_str)

#NLP Service 3: extract the stream of tokens with the help of regular expressions
tk = RegexpTokenizer('\s+', gaps = True)
input_str = string
new_out = tk.tokenize(input_str)

#NLP Service 4: sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
df['compound'] = [analyzer.polarity_scores(string)['compound'] 
df['neg'] = [analyzer.polarity_scores(string)['neg'] 
df['neu'] = [analyzer.polarity_scores(string)['neu']
df['pos'] = [analyzer.polarity_scores(string)['pos'] 

#NLP Service 5

#NLP Service 6

#Combine all NLP outputs for POST response
Responseout=rbind(input_str,result,new_out,analyzer)       
             
#Error Handling
if args['string'] = '':
             return {
                 'message': f"No Input Provided"
             }, 409
        else print(Responseout)
            return {'string':print(Responseout)},200
             
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080
