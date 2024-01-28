import mysql.connector

def createDatabase(database_name):
    with mysql.connector.connect(host="localhost", user="root", password="1234") as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))

def getConnection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="MusicPlayer"
    )
    return connection, connection.cursor()

def closeConnection(connection, cursor):
    cursor.close()
    connection.close()

def createTables():
    connection, cursor = getConnection()

    # Check if Song table exists before creating
    cursor.execute("SHOW TABLES LIKE 'Songs'")
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE Songs (
                ID_Song INT AUTO_INCREMENT,
                Name VARCHAR(255),
                Artist VARCHAR(255),
                URL VARCHAR(255),
                PRIMARY KEY(ID_Song)
            )
        """)

    # Check if Playlist table exists before creating
    cursor.execute("SHOW TABLES LIKE 'Playlists'")
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE Playlists (
                Name VARCHAR(255),
                ID_Playlist INT AUTO_INCREMENT,
                PRIMARY KEY(ID_Playlist)
            )
        """)

    # Check if PlaylistSong table exists before creating
    cursor.execute("SHOW TABLES LIKE 'PlaylistSongs'")
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE PlaylistSongs (
                ID_Song INT,
                ID_Playlist INT,
                FOREIGN KEY(ID_Song) REFERENCES Songs(ID_Song),
                FOREIGN KEY(ID_Playlist) REFERENCES Playlists(ID_Playlist)
            )
        """)

    connection.commit()
    closeConnection(connection, cursor)

def getDatabase():
    database_name = "MusicPlayer"
    try:
        connection, cursor = getConnection()
        # Check if the database exists
        cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        result = cursor.fetchone()
        if result:
            print("Database exists.")
        connection.commit()
        closeConnection(connection, cursor)
    except mysql.connector.Error as err:
        createDatabase(database_name)
        createTables()

def setUp():
    getDatabase()