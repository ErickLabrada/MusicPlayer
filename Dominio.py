class Song():
    def __init__(self, name, artist, cover,url):
         self.__name = name
         self.__artist = artist
         self.__cover = cover
         self.__url = url

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_cover(self):
        return self.__cover

    def set_cover(self, cover):
        self.__cover = cover
    
    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

class playlist():
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