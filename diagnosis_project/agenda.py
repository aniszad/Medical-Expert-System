class Agenda:
    def __init__(self):
        self.agenda = {}

    def add_to_agenda(self, key, value):
        self.agenda[key] = value

    def remove_from_agenda(self, pos):
        return self.agenda.pop(pos)

    def assign_agenda(self, new_agenda):
        self.agenda = new_agenda