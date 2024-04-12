import json


def create_backup(self, backup_filename):
    with open(backup_filename, "w") as file:
        json.dump(self.books_collection, file, indent=4)