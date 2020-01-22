import os
import pymysql.cursors


class Database():
    """データベースとの接続を管理する
    """
    HOST = os.environ["MEASUREH_DB_HOST"]
    USER = os.environ["MEASUREH_DB_USER"]
    PASS = os.environ["MEASUREH_DB_PASS"]
    PORT = int(os.environ["MEASUREH_DB_PORT"])
    DB = os.environ["MEASUREH_DB_NAME"]
    CHARSET = "utf8mb4"
    CURSOR_CLASS = pymysql.cursors.DictCursor

    def __init__(self):
        self.connection = pymysql.connect(host=self.HOST, user=self.USER,
                                          password=self.PASS, database=self.DB,
                                          port=self.PORT, charset=self.CHARSET,
                                          cursorclass=self.CURSOR_CLASS)

    def query(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            self.connection.close()


if __name__ == '__main__':
    d = Database()
    print(d.query("SELECT * FROM sites"))
