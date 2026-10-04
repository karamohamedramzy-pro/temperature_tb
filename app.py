from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

# ===== البيانات الافتراضية (سيتم تعديلها لاحقاً / نقلها لقاعدة بيانات) =====
CAPITALS = [
    {
        "country": "Algeria",
        "capital": "Algiers",
        "temperature": 25,
        "image": "image/6f2a0f6471f01b68a3661bfca8c55f18d54ce9b4.jpg",
    },
    {
        "country": "Egypt",
        "capital": "Cairo",
        "temperature": 30,
        "image": "image/Cairo_From_Tower_(cropped).jpg",
    },
    {
        "country": "united arab emirates",
        "capital": "Abu Dhabi",
        "temperature": 33,
        "image": "https://images.unsplash.com/photo-1512632578888-169bbbc64f33",
    },
    {
        "country": "Saudi Arabia",
        "capital": "Riyadh",
        "temperature": 35,
        "image": "image/Riyadh_Skyline.jpg",
    },
    {
        "country": "Jordan",
        "capital": " Amman",
        "temperature": 28,
        "image": "image/download.jpg",
    },
]


def resolve_image(path):
    """الروابط الخارجية تبقى كما هي، والمحلية تتحول إلى رابط static."""
    if path.startswith(("http://", "https://")):
        return path
    return url_for("static", filename=path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/capitals")
def api_capitals():
    data = [{**c, "image": resolve_image(c["image"])} for c in CAPITALS]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)