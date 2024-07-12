from flask import Blueprint

from app.services.movie_service import MovieService

movie_bp = Blueprint("movies", __name__, url_prefix="/api/movies")
movie_service = MovieService()


@movie_bp.route("/", methods=["GET"])
def get_all_movies():
    return movie_service.get_all_movies()
