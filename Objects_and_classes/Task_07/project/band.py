from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:
            album = next(filter(lambda album: album.name == album_name, self.albums))
            if not album.published:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
            return "Album has been published. It cannot be removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + "\n".join(album.details() for album in self.albums)