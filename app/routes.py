from app import app

@app.route('/')
@app.route('/index')
def index(): #because the base page of websites is conventionally index.html?
    return "Hello, World!"