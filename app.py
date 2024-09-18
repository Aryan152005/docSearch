
from flask import Flask, request, jsonify
from search import search

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_endpoint():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    results = search(query)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
