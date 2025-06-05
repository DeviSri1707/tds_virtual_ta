from flask import Flask, request, jsonify
from answer_generator import generate_answer

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def answer():
    data = request.get_json()
    question = data.get("question")
    image = data.get("image")

    answer, links = generate_answer(question, image)

    return jsonify({
        "answer": answer,
        "links": links
    })

if __name__ == "__main__":
    app.run(debug=True)
