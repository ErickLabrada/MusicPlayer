import DatabaseManager as DB
class SongDAO():
    
    def getSongs(IDs_Songs):
        connection, cursor = DB.getConnection()
        sql = "select URL from Songs WHERE ID_Playlist = %s;"
        val = (ID_Playlist,)
        cursor.execute(sql,val)
        songs = (cursor.fetchall())
        DB.closeConnection(connection, cursor)
        return songs

    def getSongByNameAndArtist(name, artist):
        connection, cursor = DB.getConnection()
        sql = "SELECT * FROM Songs WHERE Name = %s AND Artist = %s;"
        val = (name, artist,)
        cursor.execute(sql,val)
        songs = (cursor.fetchone())
        DB.closeConnection(connection, cursor)
        return songs

    def getAllSongs():
        connection, cursor = DB.getConnection()
        sql = "select * from Songs;"
        cursor.execute(sql)
        songs = (cursor.fetchall())
        DB.closeConnection(connection, cursor)
        return songs

    def insertSongs(song):
        connection, cursor = DB.getConnection()
        sql = "INSERT INTO Songs (Name, Artist,URL) VALUES (%s, %s,%s)"
        val = (song.get_name(), song.get_artist(),song.get_url())
        cursor.execute(sql, val)
        connection.commit()
        DB.closeConnection(connection, cursor)

    def deleteUser(url):
    
        connection, cursor = DB.getConnection()

        sql = "DELETE FROM Songs WHERE URL = %s"
        val = (url)
        cursor.execute(sql, val)

        connection.commit()
        DB.closeConnection(connection, cursor)

    
class PlayListDAO():
    def getPlaylist(name):
        connection, cursor = DB.getConnection()
        sql = "select * from Playlists WHERE Name = %s;"
        val = (name,)
        cursor.execute(sql,val)
        songs = (cursor.fetchall())
        DB.closeConnection(connection, cursor)
        return songs

    def insertPlaylist(name):
        connection, cursor = DB.getConnection()
        sql = "INSERT INTO Playlists (Name) VALUES (%s)"
        val = (name,)
        cursor.execute(sql, val)
        connection.commit()
        DB.closeConnection(connection, cursor)

    def deletePlaylist(name):
    
        connection, cursor = DB.getConnection()

        sql = "DELETE FROM Playlists WHERE Name = %s"
        val = (name,)
        cursor.execute(sql, val)

        connection.commit()
        DB.closeConnection(connection, cursor)

    def getAllPlaylists():
        connection, cursor = DB.getConnection()
        sql = "SELECT * FROM Playlists;"
        cursor.execute(sql)
        playlists = cursor.fetchall()
        DB.closeConnection(connection, cursor)
        return playlists

class PlayListSongDAO():
    
    def getPlaylistSongs(playlistName):
        connection, cursor = DB.getConnection()

        # Retrieve the ID_Playlist based on the playlistName
        cursor.execute("SELECT ID_Playlist FROM Playlists WHERE Name = %s", (playlistName,))
        result = cursor.fetchone()

        if result:
            ID_Playlist = result[0]
            # Adjust the SQL query to fetch the required columns
            sql = "SELECT Songs.Name, Songs.Artist, Songs.URL FROM Songs " \
      "JOIN PlaylistSongs ON Songs.ID_Song = PlaylistSongs.ID_Song " \
      "JOIN Playlists ON PlaylistSongs.ID_Playlist = Playlists.ID_Playlist " \
      "WHERE Playlists.ID_Playlist = %s;"

            val = (ID_Playlist,)
            cursor.execute(sql, val)
            playlist = cursor.fetchall()
        else:
            print(f"Playlist '{playlistName}' not found.")
            playlist = []

        DB.closeConnection(connection, cursor)
        return playlist



    
    def insertSongIntoPlaylist(songName, playlistName):
        connection, cursor = DB.getConnection()

        # Retrieve the ID_Song based on the songName
        cursor.execute("SELECT ID_Song FROM Songs WHERE Name = %s", (songName,))
        result = cursor.fetchone()

        if result:
            ID_Song = result[0]

            # Retrieve the ID_Playlist based on the playlistName
            cursor.execute("SELECT ID_Playlist FROM Playlists WHERE Name = %s", (playlistName,))
            result = cursor.fetchone()

            if result:
                ID_Playlist = result[0]
                sql = "INSERT INTO PlaylistSongs (ID_Song, ID_Playlist) VALUES (%s, %s)"
                val = (ID_Song, ID_Playlist)
                cursor.execute(sql, val)
                connection.commit()
            else:
                print(f"Playlist '{playlistName}' not found.")
        else:
            print(f"Song '{songName}' not found.")

        DB.closeConnection(connection, cursor)

    def deleteSongFromPlaylist(ID_Song, ID_Playlist):
        connection, cursor = DB.getConnection()
        sql = "DELETE FROM PlaylistSongs WHERE (ID_Song, ID_Playlist) = %s,%s"
        val = (ID_Song, ID_Playlist)
        cursor.execute(sql, val)

        connection.commit()
        DB.closeConnection(connection, cursor)

    