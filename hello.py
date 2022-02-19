import requests
import time
from flask import Flask

# db creds
myDbUser = "access_logs_rw"
myDBPwd = "89d7fvjrljf489"

# aws creds (just random strings)
AWS_ACCESS_ID = "jef984u3rhfc89343r"
AWS_ACCESS_KEY = "48re98gf745t5dasfrtewfreyg74reg"

app = Flask(__name__)

@app.route("/")
def serve_jokes():
    timestamp = str(time.asctime(time.gmtime(time.time())))

    print("\nHello traveller. Here is a joke for you fetched from https://sv443.net/jokeapi/v2/ API: \n  ")
    response = requests.get(  "https://v2.jokeapi.dev/joke/Any", 
                              params = { 'blacklistFlags':'nsfw,sexist', 'format':'txt'} 
                            )
    
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('API error: '. response.status_code)
    
    print(response.text)

    return "<h3>" + "\nHello traveller. Here is a joke for you fetched from https://sv443.net/jokeapi/v2/ API at :" + timestamp + "</h3>" + "<br><br> <p>" + response.text + "</p>"
    logTheDetails(response, timestamp)


# open a conncection to fdb, log the user's details
def logTheDetails(response, timestamp):
    pass; 


def main():
    app.run()


if __name__ == "__main__":
    main()




