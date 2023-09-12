from flask import Flask, request, jsonify
import llm_chain

app = Flask(__name__)

@app.route('/llm_chain', methods=['POST'])
def llm_chain_api():
    user_input = request.json['user_input']
    response = llm_chain.run(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run()