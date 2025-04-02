import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                # Slot number is the index in the page plus one (1-indexed)
                slot_number = len(page)
                return f"{label} photo added successfully on page {i + 1} slot {slot_number}"
        return "No more free slots"

    def display(self):
        result = []
        # For each page, start with the 11-dash separator
        for page in self.photos:
            result.append("-----------")
            # Represent each added photo with "[]"
            # If the page is empty, the row remains empty
            result.append(" ".join("[]" for _ in page))
        # Append the final dashed line at the end of the album
        result.append("-----------")
        return "\n".join(result)


# Example usage:
album = PhotoAlbum(2)
print(album.add_photo("MyHoliday"))
print(album.add_photo("Family"))
print(album.add_photo("Friends"))
print(album.add_photo("Selfie"))
print(album.add_photo("Landscape"))
print(album.display())
