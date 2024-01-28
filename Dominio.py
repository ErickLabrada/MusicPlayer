class Song():
    def __init__(self, name, artist,url):
         self.__name = name
         self.__artist = artist
         self.__url = url

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist
    
    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def __eq__(self, other):
        if isinstance(other, Song):
            return (
                self._Song__name == other._Song__name and
                self._Song__artist == other._Song__artist and
                self._Song__url == other._Song__url
            )
        return False
    def __str__(self):
        return f"{self._Song__name}|{self._Song__artist}"




class Playlist():
    def __init__(self, name):
         self.__name = name
         self.__songs = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_songs(self):
        return self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def delete_song(self, song):
        self.__songs.remove(song)

    def __str__(self):
        return f"{self.get_name()}"