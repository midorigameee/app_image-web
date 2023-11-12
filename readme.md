# About
DockerでFlaskアプリを動かすためのリポジトリ

# Development policy
（個人開発だけどせっかくだしポリシーを作ってみる）

- ブランチの使い分け
  - masterブランチには常に確実に動作するソースを置くようにする。
  - その他開発はfeature/hogehogeを使用する。
- 新しい機能を実装するとき
  - masterからfeature/hogehogeというトピックブランチを作成する。
  - 開発環境でトピックブランチで動作確認完了後にプルリクを出してmasterにマージする。

以下のページを参考にしました。
>　https://solodev.io/git-flow/



# Development environment
ローカルはAnacondaで仮想環境を作成して挙動を確認する。

## Anaconda infomation
Anacondaのversionは以下の通り
> $ conda --version  
> conda 4.6.14

仮想環境は以下のコマンドで生成した。
> $ conda create -name py38_flask python=3.8

パッケージはpip、condaそれぞれ以下のコマンドで出力した。
> $ pip freeze > requirements.txt
> $ conda list > conda_list.txt