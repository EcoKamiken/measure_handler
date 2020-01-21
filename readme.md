# measure_handler

Sigfox cloudとデータベースの間を接続するミドルウェア

## 依存関係のインストール

```shell
poetry install
```

### 環境変数

以下の環境変数を設定しないとSigfox APIを使用できないので必ず設定する。

```shell
$SIGFOX_ID="Sigfox APIのID"
$SIGFOX_PW="Sigfox APIのPW"
```

## 実行

```shell
poetry run python -m measureh
```
