"""データベースモジュール

* データベースとの通信

Todo:
    * None
"""

import os
import pymysql.cursors


class Database():
    """データベース接続

    Attributes:
        HOST (str): データベースホスト名
        USER (str): データベースユーザ名
        PASS (str): データベースパスワード
        PORT (int): データベースポート番号
        DB (str): データベース名
        CHARSET (str): 文字コード
        CURSOR_CLASS (str): カーソルの型
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
        """クエリ
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def parsed_data_insert_to_db(self, parsed_data):
        """ 解析済みのデータ(タプル)を受け取ってDBに登録する
        """
        with self.connection.cursor() as cursor:
            sql = """
            INSERT INTO
                sensors
                    (id, device_id, temperature, humidity, wattage, created_at)
                VALUES
                    (%s, %s, %s, %s, %s, %s)
            """
            try:
                cursor.execute(sql, (parsed_data[3], parsed_data[8], 0, 0,
                                     parsed_data[7], parsed_data[0]))
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e

    def __del__(self):
        self.connection.close()
