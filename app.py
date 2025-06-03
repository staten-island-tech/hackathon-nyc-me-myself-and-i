from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory train positions
train_positions = {
    "A": {"x": 100, "y": 150},
    "B": {"x": 200, "y": 300}
}

@app.route("/")
def index():
    return render_template("index.html", trains=train_positions)

@app.route("/update_train_position", methods=["POST"])
def update_train_position():
    data = request.get_json()
    train_id = data.get("train_id")
    x = data.get("x")
    y = data.get("y")

    if train_id in train_positions:
        train_positions[train_id] = {"x": x, "y": y}
        return jsonify({"status": "updated"})
    else:
        return jsonify({"status": "error", "msg": "Invalid train ID"}), 400

if __name__ == "__main__":
    app.run(debug=True)