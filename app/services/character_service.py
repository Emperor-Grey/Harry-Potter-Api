from flask import jsonify

from app.models.Character import characters, Character


class CharacterService:

    def get_characters(self):
        return jsonify([vars(character) for character in characters])

    def get_character_by_id(self, id):
        for character in characters:
            if character.id == id:
                return jsonify(vars(character))

        return jsonify({"message": "The Id doesn't exist"})

    def create_character(self, name, role, actor_name):
        new_id = max([character.id for character in characters]) + 1
        new_character = Character(new_id, name, role, actor_name)
        characters.append(new_character)
        return jsonify(vars(new_character))

    def update_character(self, id, name, role, actor_name):
        for character in characters:
            if character.id == id:
                character.name = name
                character.role = role
                character.actor_name = actor_name

                return jsonify(vars(character))

        return jsonify({"message": "The id mentioned does not exist"})

    def delete_character(self, id):
        for index, character in enumerate(characters):
            if character.id == id:
                del characters[index]
                return jsonify({"message": "Successfully deleted"})

        return jsonify({"message": "The id mentioned does not exist"})


character_service = CharacterService()
