from typing import Tuple
from project.song import Song

class Album:
    def __init__(self, name: str, *args: Tuple[Song]):
        self.name = name
        self.songs = [*args]
        self.published: bool = False

    def add_song(self, song: Song):
        if not self.published:
            if not song.single:
                if song not in self.songs:
                    self.songs.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."
                return "Song is already in the album."
            return f"Cannot add {song.name}. It's a single"
        return f"Cannot add songs. Album is published."

    def remove_song(self, song_name: str):
        if not self.published:
            try:
                song = next(filter(lambda song: song.name == song_name, self.songs))
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."
            except StopIteration:
                return "Song is not in the album."

        return f"Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join(f"== {song.get_info()}" for song in self.songs)





