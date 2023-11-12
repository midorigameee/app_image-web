# About
DockerでFlaskアプリを動かすためのリポジトリ

# Developing environment
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