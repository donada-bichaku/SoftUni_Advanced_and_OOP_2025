from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user_to_update = next(filter(lambda user: user.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user_to_update.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"


        # if library.rented_books.get(user_to_update.username) != None:
        #     library.rented_books[new_username] = library.rented_books.pop(user_to_update.username)
        # used try-except below instead

        try:
            library.rented_books[new_username] = library.rented_books.pop(user_to_update.username)
        except KeyError:
            pass

        user_to_update.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
