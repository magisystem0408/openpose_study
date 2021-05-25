# Unity側
## ビルド時、設定コマンド

- build settings>othersettings>auto graphics api for windowsのチェックを外す

# python側
## 実行時に必要なコマンド

-   仮想環境をanaconda上で立ち上げる
-   以下のコマンドを実行する
> python test_openpose --net_resolution "-1x256"

> ※ 01_body_from_image.pyは実行したいファイル名に書き換える

- 個々のファイルのディレクトリ先のパス
- C:\openpose\build\examples\tutorial_api_python



# 次のtodo
- vscodeでanaconda仮想環境に入れるようにする
- アニメーション・りぎんぐ処理リギング