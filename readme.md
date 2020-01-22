# measure_handler

Sigfox cloudとデータベースの間を接続するミドルウェア

## 依存関係のインストール

```shell
poetry install
```

### 環境変数

以下の環境変数をすべて設定しないと正常に動作しません。

Sigfox関係

```shell
$SIGFOX_ID="Sigfox APIのID"
$SIGFOX_PW="Sigfox APIのPW"
```

データベース関係

```shell
$MEASUREH_DB_HOST="DBのホスト名 (www.example.com, 127.0.0.1, etc..)"
$MEASUREH_DB_PORT="DBのポート番号"
$MEASUREH_DB_USER="DBのユーザ名"
$MEASUREH_DB_PASS="DBのパスワード"
$MEASUREH_DB_NAME="DBの名前"
```

## 実行

```shell
poetry run python -m measureh
```
