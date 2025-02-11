from flask import Flask
import os 

app = Flask(__name__):


@app.route("/", methods =["GET"])
def home():
    return "Docker Experiment"




if name =="__main__":
    # provide host and port
    # host -> access local addrss and access host address 
    app.run(debug=True, host="0.0.0.0", port=5000)