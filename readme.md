# About
DockerでFlaskアプリを動かすためのリポジトリ  
（結局本番環境はPython直接動かしてるけど…）

# Development policy
（個人開発だけどせっかくだしポリシーを作ってみる）

- ブランチの使い分け
  - master
    - 確実に動作するソースを置くブランチ
    - リリースバージョンの管理を行う
  - develop
    - 直接コミット禁止
    - developで一旦動作確認する
  - feature
    - 機能開発を行うブランチ
    - 機能ごとにfeature/hogehogeという名前でブランチを切る
  - release
    - developで微調整を行うときのブランチ
  - hotfix
    - masterでバグが発生したときに緊急で対応するときのブランチ
- 新しい機能を実装するとき
  - masterからdevelopにブランチを切る
  - developからfeature/hogehogeというトピックブランチを切る
  - 開発環境でトピックブランチの動作確認を行い、完了後にプルリクを出してdevelopにマージする
  - 本番環境でも確実に動作することを確認したら、masterにVer.名でマージする
- 色々書いたけど…
 - とりあえず困ったらfeatureでブランチ切る
 - ミスってもドンマイ！

以下のページを参考にしました。
> https://solodev.io/git-flow/  
> https://qiita.com/y-okudera/items/0b57830d2f56d1d51692

# Development environment
ローカルでDockerでPython環境を立てて挙動を確認する。

## Docker information
コンテナの初回起動時はDockerfileを読み込み、imageを生成する。
そのときのDockerfileのコマンドが実行される。

2回目以降（イメージ生成済みでコンテナ起動）はDockerfileのコマンドは実行されず、docker-compose.ymlのコマンドのみが実行される。

# Production environment
[Render](https://render.com/)を使用する。

## Render information
Python環境を使用する。

- Environment
  - Key : PYTHON_VERSION
  - Value : 3.8.18
- Settings
  - Build & Deploy
    - Root Directory : src
    - Build Command : python -V; pip install --upgrade pip; pip install -r requirements.txt;  pip install -r requirements_pytorch.txt --find-links https://download.pytorch.org/whl/torch_stable.html
    - Start Command : $ python app.py

# ToDo management
Github Projectでissue切って管理する。粒度はいったん度外視する！

# Frequently used commands for me
## Docker
$ docker compose up -d  
$ docker compose ps
$ docker compoes exec [SERVICE NAME] bash  
    ex) $ docker compoes exec python3 bash  
$ docker compose down  
$ docker image ls  
$ docker imare rm [IMAGE ID]

## pip
$ pip freeze > requirements.txt

## git
### ブランチ操作
ブランチの確認(-a無しだとローカルのブランチだけ確認)
> $ git branch -a

ローカルブランチの削除(pushされていない差分無視なら-dじゃなくて-D)
> $ git branch -d hogehoge

リモートブランチの削除
> $ git push --delete origin hogehoge