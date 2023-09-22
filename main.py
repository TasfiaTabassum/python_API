# here flask will be the server which will be running our API

from flask import Flask, request, jsonify
#Flask: This is the main class of the Flask framework. It's used to create Flask web applications.
#request: This module allows you to access incoming request data, such as form data or JSON payloads, from the client
# jsonify - to convert python dictionary to json object

# flask applicaction 
app = Flask(__name__)

# get route , path parameter
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200


# post route
@app.route("/create-user" , methods = ["POST"])
def create_user():
    #if request.method == "POST" :
    data = request.get_json()
    
    return jsonify(data), 201


# flask application start
if __name__ == "__main__" :
    app.run(debug=True)
