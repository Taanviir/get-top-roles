from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allowing all routes and origins

mock_data = {
    "students": {
        "1": {
            "name": "Alice",
            "recommended_roles": [
                "Developer",
                "Data Scientist",
                "UX Designer",
                "Analyst",
                "Product Manager",
            ],
        },
        "2": {
            "name": "Bob",
            "recommended_roles": [
                "Marketing Specialist",
                "Sales Executive",
                "HR Manager",
                "Copywriter",
                "Event Planner",
            ],
        },
    }
}


@app.route("/get-top-roles", methods=["GET"])
def get_top_roles():
    student_id = request.args.get("student_id")
    if not student_id:
        return jsonify({"error": "Missing student_id parameter"}), 400

    student_data = mock_data["students"].get(student_id)
    if not student_data:
        return jsonify({"error": f"No data found for student: {student_id}"}), 404

    return (
        jsonify(
            {
                "student_id": student_id,
                "student_name": student_data["name"],
                "top_roles": student_data["recommended_roles"],
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
