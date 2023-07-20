""" from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb", 27017)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def index():
    return "Hello, this is your Flask app!"

@app.route("/insert", methods=["POST"])
def insert_data():
    try:
        data = request.get_json()
        if data and "name" in data:
            collection.insert_one({"name": data["name"]})
            return jsonify({"status": "success", "name": "Data inserted successfully!"})
        else:
            return jsonify({"status": "error", "name": "Invalid data format!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/query")
def query_data():
    try:
        result = collection.find_one()
        if result:
            return jsonify({"status": "success", "data": result})
        else:
            return jsonify({"status": "success", "message": "No data found!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
 """



from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb", 27017)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def index():
    return "Hello, this is your Flask app!"

@app.route("/insert", methods=["POST"])
def insert_data():
    try:
        data = request.get_json()
        print(data)
        if data and "name" in data and "age" in data and "email" in data:
            # Insert data into the MongoDB collection
            collection.insert_one({
                "name": data["name"],
                "age": data["age"],
                "email": data["email"]
            })
            return jsonify({"status": "success", "message": "Data inserted successfully!"})
        else:
            return jsonify({"status": "error", "message": "Invalid data format!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    

@app.route("/query")
def query_data():
    try:
        # Use the find method with a filter to query documents where age is greater than 20
        results = collection.find({"age": {"$gt": 20}})

        # Convert the MongoDB Cursor to a list of dictionaries
        data_list = list(results)

        if data_list:
            return jsonify({"status": "success", "data": data_list})
        else:
            return jsonify({"status": "success", "message": "No data found!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/display")
def display_collection():
    try:
        # Retrieve all documents from the collection
        results = collection.find()

        # Convert the MongoDB Cursor to a list of dictionaries and handle ObjectId
        data_list = []
        for document in results:
            document["_id"] = str(document["_id"])  # Convert ObjectId to string
            data_list.append(document)

        if data_list:
            return jsonify({"status": "success", "data": data_list})
        else:
            return jsonify({"status": "success", "message": "No data found!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
