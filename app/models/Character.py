class Character:

    def __init__(self, id: int, name: str, role: str, actor_name: str) -> None:
        self.id = id
        self.name = name
        self.role = role
        self.actor_name = actor_name


characters = [
    Character(1, "Harry Potter", "Protagonist", "Daniel Radcliffe"),
    Character(2, "Hermione Granger", "Supporting Character", "Emma Watson"),
    Character(3, "Ron Weasley", "Supporting Character", "Rupert Grint"),
    Character(4, "Albus Dumbledore", "Supporting Character", "Richard Harris/Michael Gambon"),
    Character(5, "Severus Snape", "Supporting Character", "Alan Rickman")
]
