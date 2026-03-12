import sqlite3

class DatabaseManager:
    def __init__(self, db_name='server_data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create a table for server settings
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS server_settings (
                id INTEGER PRIMARY KEY,
                setting_name TEXT NOT NULL,
                setting_value TEXT NOT NULL
            )
        ''')
        
        # Create a table for user data
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY,
                user_id TEXT NOT NULL,
                server_id TEXT NOT NULL,
                data TEXT
            )
        ''')
        
        self.connection.commit()

    def set_setting(self, name, value):
        self.cursor.execute('''
            INSERT OR REPLACE INTO server_settings (setting_name, setting_value)
            VALUES (?, ?)
        ''', (name, value))
        self.connection.commit()

    def get_setting(self, name):
        self.cursor.execute('''
            SELECT setting_value FROM server_settings WHERE setting_name = ?
        ''', (name,))
        return self.cursor.fetchone()

    def store_user_data(self, user_id, server_id, data):
        self.cursor.execute('''
            INSERT INTO user_data (user_id, server_id, data)
            VALUES (?, ?, ?)
        ''', (user_id, server_id, data))
        self.connection.commit()

    def get_user_data(self, user_id, server_id):
        self.cursor.execute('''
            SELECT data FROM user_data WHERE user_id = ? AND server_id = ?
        ''', (user_id, server_id))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()