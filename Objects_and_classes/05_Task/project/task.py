from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name != new_name:
            self.name = new_name
            return self.name
        else:
            return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        if self.due_date != new_date:
            self.due_date = new_date
            return self.due_date
        else:
            return "Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        try:
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        except IndexError:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
