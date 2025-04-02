from math import ceil
from typing import List


class PhotoAlbum:

    PHOTO_PER_PAGE = 4


    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List] = []
        self.photos = [[] for page in range(0, self.pages)]
        self.curr_page = 0
        self.curr_slot = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count/cls.PHOTO_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[-1]) == self.PHOTO_PER_PAGE:
            return "No more free slots"

        self.photos[self.curr_page].append(label)

        result = (f"{label} photo added successfully on "
                  f"page {self.curr_page+1} slot {self.curr_slot+1}") #correctly returns where the photo was added
        # and later we increment the next slot without affecting the result

        if self.curr_slot == self.PHOTO_PER_PAGE - 1:
            self.curr_slot = -1
            self.curr_page += 1

        self.curr_slot += 1

        return result

    def display(self):
        result = "-----------"

        for i in range(0, self.pages):
            result += "\n" + ("[] " * len(self.photos[i])).strip() + "\n"
            result += "-----------"

        return result

# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.photos)
# print(album.display())
# album = PhotoAlbum(1)
# album.add_photo("baby")
# album.add_photo("first grade")
# album.add_photo("eight grade")
# album.add_photo("party with friends")
# print(album.photos)
# print(album.display())






