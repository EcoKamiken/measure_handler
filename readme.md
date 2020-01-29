# sigr

Sigfox cloudからCallbackで送信されたデータを受信および解析し、
データベースに登録するサーバアプリケーション

## 依存関係のインストール

```shell
poetry install
```

### 環境変数

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
poetry run python -m sigr
```
