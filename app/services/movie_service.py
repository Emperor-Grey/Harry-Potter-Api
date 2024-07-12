from flask import jsonify

from app.models.Movie import movies, Movie


class MovieService:

    def get_all_movies(self):
        return jsonify([vars(movie) for movie in movies])

    def get_movie_by_id(self, id):
        for movie in movies:
            if movie.id == id:
                return vars(movie)
        return None

    def create_movie(self, name, director):
        new_id = max([movie.id for movie in movies]) + 1
        new_movie = Movie(new_id, name, director)
        return vars(new_movie)

    def update_movie(self, name, director):
        for movie in movies:
            if movie.id == id:
                movie.name = name
                movie.director = director
                return movie
        return None

    def delete_movie(self, id):
        for index, movie in enumerate(movies):
            if movie.id == id:
                del movies[index]
                return {"success": "success"}
        return None


movie_service = MovieService()
