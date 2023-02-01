from app import app

@app.route("/")
def index():
    return "index"

@app.route("/test")
def test():
    return "test"

app.run()