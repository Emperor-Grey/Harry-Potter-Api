from flask import Blueprint, request, jsonify

from app.services.character_service import CharacterService

character_bp = Blueprint("character", __name__, url_prefix="/api/characters")

character_service = CharacterService()


@character_bp.route('/', methods=["GET"])
def get_characters():
    return character_service.get_characters(), 200


@character_bp.route("/<int:id>", methods=["GET"])
def get_character(id):
    if not id:
        return jsonify({"message": "Character ID is required"}), 400
    return character_service.get_character_by_id(id), 200


@character_bp.route("/", methods=["POST"])
def create_character():
    data = request.get_json()
    name = data["name"]
    role = data["role"]
    actor_name = data.get("actor_name")
    if not name or not role or not actor_name:
        return jsonify({"message": "Name, role, and actor_name are required"}), 400
    return character_service.create_character(name, role, actor_name), 201


@character_bp.route("/<int:id>", methods=["PUT"])
def update_character(id):
    if not id:
        return jsonify({"message": "The id must be passed as a requirement"}), 400

    data = request.get_json()
    name = data["name"]
    role = data["role"]
    actor_name = data["actor_name"]
    return character_service.update_character(id, name, role, actor_name), 200


@character_bp.route("/<int:id>", methods=["DELETE"])
def delete_character(id):
    if not id:
        return jsonify({"message": "The id is required"}), 400

    return character_service.delete_character(id), 200
