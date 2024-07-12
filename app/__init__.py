from flask import Flask

from app.config.config import Config
from app.routes.character_routes import character_bp
from app.routes.movie_route import movie_bp

app = Flask(__name__)
app.config.from_object(Config)

# Routes
app.register_blueprint(character_bp)
app.register_blueprint(movie_bp)


@app.route('/', methods=['GET'])
def sayHello():
    return {"message": "The app starts from /api/"}


app.run(port=4000, host="0.0.0.0")
