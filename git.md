# emoji_prefix.md

commit message template

`:emoji: Reason; Specification; Issue`

```
# 🌱 :seedling: Initial commit.
# 🔥 :fire: Update some features.
# ✨ :sparkles: Introduce new features.
# ♻️ :recycle: Refactor code.
# 🐛 :bug: Fix a bug.
# 🎨 :art: Improve design accessibility.
# 📚 :books: Add or update documentation.
# 🔧 :wrench: Add or edit configuration files.
# 🚨 :rotating_light: Fix compiler or linter warnings.
# ⚡️ :zap: Improve performance.
# 💚 :green_heart: Add or fix CI/CD Build.
# 📦️ :package: Add or update compiled files or packages.
# 🚀 :rocket: Deploy stuff.
# 🔀 :twisted_rightwards_arrows: Merge branches.
```

```
# example
:seedling: init README.md
:bug: up→down / main.c swap for main.c sort
:wrench: delete secrets / setting.py / issue #3
```

[emoji_prefix.md](https://gist.github.com/jpnykw/2be2d751e9aabb3b364c70e5a95b56cc)

# git指南書

基本的な使い方と、よくやらかしがちな問題の対処方法

## :beginner: 基本操作編

## add

特定のファイルのみを追加したい場合はファイル名を引数に渡します
複数のファイルを渡すことも可能です

```
$ git add ファイル名1 ファイル名2
```

ファイル名にはワイルドカードを使用することができます
例えば `.tsx` ファイルをまとめて追加したい場合は以下のように書けます

```
$ git add *.tsx
```

### ・all

変更を加えたファイルを全てステージングに追加します

```
$ git add -A
```

カレントディレクトリ直下にある変更ファイルを全て追加したい場合にはパスを使用します

```
$ git add .
```

### ・update

実は削除したファイルはそのままではステージングに追加されないので `-u` オプションを使用します

```
$ git add -u ファイル名
```

## commit

### ・m

ステージングに追加した変更をまとめてcommitします

```
$ git commit -m "コミットメッセージ"
```

### ・allow-empty

空のコミットをしたい時に使います
e.g. - 初期化時、CIを再実行したい場合（GUIで解決できる場合があります）、等

```
$ git commit --allow-empty
```

### ・amend

直前のコミット内容を編集したい時に使います
e.g. - ソースコードのタイプミス修正、コミットメッセージの修正等

```
$ git commit --amend
```

## stash

現在のブランチに影響する変更差分を一時的に退避させます

```
$ git stash
```

`-u` オプションを付け加えることでuntrackedファイルごと退避させることができます

```
$ git stash -u
```

### ・pop

退避させた変更を取り出す時に使います
以下のコマンドで退避したファイルを現在のブランチに呼び戻します
その際にはstashからは退避した内容が削除されます

```
$ git stash pop
```

### ・apply

stashにも残したまま取り出したい場合は `pop` の代わりに `apply` を使用します

```
$ git stash apply
```

## branch

### ・ブランチの切り替え
```
$ git checkout ブランチ名
```

### ・ブランチを切る
```
$ git checkout -b 自分の作りたいブランチ名
作業後↓
$ git add .
$ git commit
$ git push -u origin 自分の作ったブランチ名
```

## :warning: やらかし編

### ・間違えて `git add` しちゃったとき

以下のコマンドで特定ファイルをステージングから取り除くことができます

```
$ git reset HEAD ファイル名
```

### ・間違えて `git commit` しちゃった時

直前のコミットを取り消したい場合はソフトリセットを行えば解決できます

```
$ git reset --soft HEAD^
```

### ・過去のコミットメッセージを変更したい時

直前のコミットメッセージを編集する場合は `--amend` オプションで解決できます
以下のどちらかのコマンドを一度実行し、メッセージを修正します

```
$ git commit --amend
$ git commit --amend -m "新しいメッセージ"
```

その後pushする際はforceオプションが必須になります
対象ブランチによってはできない場合があるので注意が必要です

```
$ git push origin ブランチ名 -f
```

### ・間違えて違うブランチで作業しちゃった時

一旦変更差分をstashして退避させます

```
$ git stash
```

次にブランチを切り替えて変更差分を取り出します

```
$ git checkout ブランチ名
$ git stash pop
```

# LICENSE

this repo was forked from [git.md](https://gist.github.com/jpnykw/73c60e29b7cb49c5b4763974b1cd0d13) witten by [jpnykw](https://gist.github.com/jpnykw)

# nock

```
title: 意外と知らない？ Gitコマンド 100本ノック
tags: Git GitHub 初心者 新人プログラマ応援
author: ueki05
slide: false
```

# 概要

みなさん、Git使ってますか？
もしくは、使いこなしていますか？

独習Gitを読んで、思いの外Gitコマンドが多かったので、
タイトルの通り、Gitコマンドで100本ノックをまとめてみました。

Gitの環境構築が終わっている状態からを想定しています。
`git init`でローカルにリポジトリを用意してください。

問題に対して、直後に回答を載せる形式にしています。
Git初心者の方も、目を通して知らないオプションをググれば勉強になると思います。

# 参考文献

独習Git
<a target="_blank"  href="https://www.amazon.co.jp/gp/product/4798144614/ref=as_li_tl?ie=UTF8&camp=247&creative=1211&creativeASIN=4798144614&linkCode=as2&tag=ueki0e-22&linkId=9ef7d3413434b3de4b052b4827d2cf40"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=JP&ASIN=4798144614&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=ueki0e-22" ></a><img src="//ir-jp.amazon-adsystem.com/e/ir?t=ueki0e-22&l=am2&o=9&a=4798144614" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# 100本ノック

## Gitに馴染む

###  1. メールアドレスをGitのグローバル設定に追加
`git config --global user.email "Your E-mail@example.com"`
###  2. user.nameの設定値を表示
`git config user.name`
###  3. user.emailの設定値を表示
`git config user.email`
###  4. Gitヘルプシステムのヘルプ
`git help help`
###  5. Gitで利用できる全コマンドのリスト
`git help -a`
###  6. すべてのGitコマンドをページで表示
`git --paginate help -a`
###  7. すべてのGitガイドを表示
`git help -g`
###  8. Gitの用語集（glossary）を表示
`git help glossary`

## リポジトリの作り方と使い方

###  9. カレントディレクトリ内のGitリポジトリを初期化
`git init`
###  10. Gitに関するカレントディレクトリの状態を表示
`git status`
###  11. ファイルをGitに追跡させる（ファイルはステージングエリアに追加される）
`git add FILE`
###  12. 変更をGitリポジトリにコミットし、メッセージを付ける
`git commit -m "Message"`
###  13. Gitリポジトリのログ（ヒストリー）を表示
`git log`
###  14. ログとともに、変更されたファイルを表示する
`git log --stat`
###  15. リポジトリ内のファイルをリスト表示
`git ls-files`

## ファイルの追跡と更新

###  16. カレントディレクトリ内で追跡されているファイルと、リポジトリ内のファイルとの間に変更があれば、それを示す
`git diff`
###  17. git addを実行してから、ログメッセージとともにgit commitを実行する
`git commit -a -m "Message"`
###  18. ステージングエリアとリポジトリの間に変更があれば、それを示す
`git diff --staged`
###  19. git addで何が実行されるかを示す
`git add --dry-run .`
###  20. カレントディレクトリ内の新しいファイルをすべて追加する
`git add .`
###  21. 履歴をコミットごとに1行で表示し、各コミットで変更されたファイルのリストを1行で表示する
`git log --shortstat --oneline`

## 変更箇所をコミットする

###  22. ファイルを作業ディレクトリとステージングエリアから削除（remove）する
`git rm FILE`
###  23. 作業ディレクトリとステージングエリアで、FILE1の名前をFILE2に変更する
`git mv FILE1 FILE2`
###  24. ステージングエリアに追加（add）すべき変更部分を手作業で選択（pick）する
`git add -p`
###  25. ステージングエリアをリセット（reset）して、ファイルをコミット予定から外す
`git reset FILE`
###  26. ファイルの「最後にコミットしたバージョン」をチェックアウトして、localの作業ディレクトリに入れる
※まだcommitしていないファイルの差分が消えます
`git checkout FILE`

## Gitというタイムマシン

###  27. ヒストリー表示。個々のコミットで、親コミットのSHA1 IDも表示する。
`git log --parents`
###  28. ヒストリー表示。個々のコミットで、親コミットのSHA1 IDも短縮表示する。
`git log --parents --abbrev-commit`
###  29. ヒストリーを簡潔に（各コミットを1行で）表示する
`git log --oneline`
###  30. ヒストリー表示。個々のコミットにおけるファイルの差分を示す。
`git log --patch`
###  31. SHA1_IDにタグを付ける。タグ名にTAG_NAME、メッセージにTAG_MESSAGEを使う
`git tag -a TAG_NAME -m TAG_MESSAGE SHA1_ID`
###  32. ヒストリー表示。patchとstatの出力を組み合わせる。
`git log --patch-with-stat`
###  33. ブランチ名を、特定のSHA1 IDに変換する（tagでもできる）
`git rev-parse BRANCH`
###  34. 作業ディレクトリを、YOUR_SHA1_IDで指定されたバージョンと一致するものに変更する
`git checkout YOUR_SHA1_ID`
###  35. YOUR_SHA1IDを参照するTAG_NAMEという名のタグを作る。このタグには短いメッセージ（MESSAGE）が割り当てられる
`git tag TAG_NAME -m "MESSAGE" YOUR_SHA1ID`
###  36. すべてのタグのリストを出力する
`git tag`
###  37. TAG_NAMEというタグに関する情報を示す
`git show TAG_NAME`

## ブランチ（支線）を辿る

###  38. すべてのブランチのリストを表示
`git branch`
###  39. BRANCHという名前のブランチを新規に作成する
`git branch BRANCH`
###  40. 作業ディレクトリを変更して、BRANCHという名前のブランチを反映させる
`git checkout BRANCH`
###  41. リポジトリの履歴をすべてのブランチを通じて閲覧する
`git log --graph --decorate --pretty=oneline --all --abbrev-commit`
###  42. git logコマンドのためにlolという名前の別名（alias）を作る（logのオプションは任意）
`git config --global alias.lol "log --graph --decorate --pretty=oneline --all --abbrev-commit"`
###  43. すべてのブランチのリストをSHA1ID情報を付けて表示
`git branch -v`
###  44. YOUR_SHA1IDを開始地点としてブランチNEW_BRANCHを作る
`git branch NEW_BRANCH YOUR_SHA1ID`
###  45. BRANCH_BASEを開始地点としてBRANCH_NEWを作り、即座にチェックアウトする
`git checkout -b BRANCH_NEW BRANCH_BASE`
###  46. これまでに（git checkoutやgit reset等によって）行ったブランチ切替のすべての記録を表示する
`git reflog`
###  47. 現在進行中の作業（WIP）をスタッシュ（安全な隠し場所）に入れて、git checkoutを実行できるようにする
`git stash`
###  48. スタッシュに対比させたWIPのリストを表示
`git stash list`
###  49. 最後にスタッシュに入れた内容を現在の作業ディレクトリに反映させ、スタッシュから消去する
`git stash pop`

## ブランチをマージ（統合）する

###  50. 2本のブランチ間の差分を最初に違いが現れた場所から相対的に示す
```
---X---------BRANCH1
    ＼
     --------BRANCH2
```
`git diff BRANCH1...BRANCH2`
###  51. YOUR_SHA1_IDを開始地点としてブランチNEW_BRANCHを作る
`git branch NEW_BRANCH YOUR_SHA1_ID`
###  52. BRANCHを現在の（カレント）ブランチにマージする
`git merge BRANCH`
###  53. git log -n 1の短縮形（最新のコミットだけを表示する）
`git log -1`
###  54. BRANCH1とBRANCH2に共通するベースコミットを表示する
`git merge-base BRANCH1 BRANCH2`

## クローン（複製）を作る

###  55. ソースの位置にあるGitリポジトリのクローンを、複製先ディレクトリに作る
`git clone SOURCE DESTINATION_DIR`
###  56. すべてのブランチから、すべてのコミットログエントリを表示する（通常のgit logは、カレントブランチからのエントリだけを表示する）
`git log --oneline --all`
###  57. ローカルブランチだけでなく、リモート追跡ブランチも表示する
`git branch --all`
###  58. SOURCEにあるGitリポジトリのクローンを、複製先ディレクトリに、ペアリポジトリとして作る（複製先ディレクトリの名前は、規約に従って .gitで終わるようにする）
`git clone --bare SOURCE DESTINATION_DIR`
###  59. HEADのすべてのファイルを表示する
`git ls-tree HEAD`

## リモートとの共同作業

###  60. masterブランチをチェックアウトする。現在のブランチに変更があれば、それらは破棄される。
`git checkout -f master`
###  61. 現在のリポジトリにあるリモートの名前を表示する
`git remote`
###  62. リモートの名前を、対応するリモートURLとともに表示する
`git remote -v show`
###  63. BOBという名前のリモートを追加する。そのリモートは、ローカルリポジトリ../math.bobを指し示す。
`git remote add BOB ../math.bob`
###  64. リモートリポジトリREMOTEのリファレンスを表示する（現在のローカルリポジトリを指定するには、REMOTEとして . を使う）
`git ls-remote REMOTE`
###  65. リモートとのネットワーク通信の内容を表示する
`GIT_TRACE_PACKET=1 git ls-remote REMOTE`

## 変更をプッシュ（送出）する

###  66. masterブランチをoriginという名前のリモートにプッシュする
`git push origin master`
###  67. 現在のブランチを、デフォルトのリモート追跡ブランチにプッシュする。デフォルトは、git checkoutまたはgit push --set-upstreamにより設定される
`git push`
###  68. ORIGINという名前のリモートにあるNEW_BRANCHへのリモート追跡ブランチを作成する
`git push --set-upstream ORIGIN NEW_BRANCH`
###  69. 名前にBRANCHという言葉が含まれているGit構成設定のリストを表示する
`git config --get-regexp BRANCH`
###  70. BRANCHという名前のローカルブランチを削除する
`git branch -d BRANCH`
###  71. REMOTE_BRANCHという名前のリモートブランチを、originという名前のリモートから削除する
`git push origin :REMOTE_BRANCH`
###  72. SHA1IDにタグを付ける。タグ名にTAG_NAME、メッセージにTAG_MESSAGEを使う
`git tag -a TAG_NAME -m TAG_MESSAGE SHA1ID`
###  73. TAGNAMEという名前のタグを、originという名前のリモートにプッシュする
`git push origin TAGNAME`
###  74. すべてのタグをデフォルトのリモートにプッシュする
`git push --tags`
###  75. originという名前のリモートから、TAGNAMEという名前のタグを削除する
`git push origin :TAGNAME`
###  76. ローカルリポジトリから、TAGNAMEという名前のタグを削除する
`git tag -d TAGNAME`
###  77. Git構成のpush.defaultを、simpleという値に設定する。これは、アクセスできるすべてのリポジトリに（グローバルに）設定される
`git config --global push.default simple`

## 同期を保つ（プル）

###  78. リポジトリと上流リポジトリと同期させる（git fetchとgit mergeの2つで構成される)
`git pull`
###  79. リモートリポジトリから新しいコミットが取り込まれ、リモート追跡ブランチが更新される
`git fetch`
###  80. FETCH_HEADからの新しいコミットを、カレントブランチにマージする
`git merge FETCH_HEAD`
###  81. --ff-onlyスイッチを指定すると、FETCH_HEADがカレントブランチの子孫である場合に限り、マージが許可される（fast-forwardマージ)
`git pull --ff-only`

## ソフトウェア考古学（ログ）

###  82. マージの結果であるコミットのリストを表示
`git log --merges`
###  83. FILEに影響を与えたコミットのリストを表示
`git log --oneline FILE`
###  84. コミットメッセージがSTRINGを含んでいるコミットのリストを表示
`git log --grep=STRING`
###  85. 2つの日付の間に作られたコミットのリストを表示
`git log --since MM/DD/YYYY --until MM/DD/YYYY`
###  86. 著者名によるコミットの要約
`git shortlog`
###  87. 著者名によるコミットの要約で、メールアドレスも表示する
`git shortlog -e`
###  88. AUTHORを著者とするコミットのリスト（名前とメールアドレスを表示）
`git log --author=AUTHOR`
###  89. 現在のコミットと、その親の間にあるコミット（と、そのファイル）のリスト
`git log --stat HEAD^..HEAD`
###  90. 現在のコミットと、その親の間にあるコミット（と、テキストの変更）のリスト
`git log --patch HEAD^..HEAD`
###  91. すべてのブランチのリストをコラムに分けて表示する
`git branch --column`
###  92. 指定したSHA1_IDの名前を最も近いブランチをベースとして表示する
`git name-rev SHA1_ID`
###  93. 指定のSHA1_IDを含む、すべてのブランチを識別する（-rはリモート追跡ブランチを指定する。これを略すとローカルブランチだけが表示される）
`git branch -r --contains SHA1_ID`
###  94. STRINGを含む、すべてのファイルを探し出す
`git grep STRING`
###  95. FILEのblame出力をコマンドラインで表示する
`git blame FILE`
※ @culage 様より、 `git gui blame FILE` を使うと見やすいそうです！
###  96. FILEのblame出力をコマンドラインで、FILE-annotateに保存する
`git --no-pager blame FILE > FILE-annotate`

## git rebaseを理解する

###  97. masterブランチの先で、BRANCHブランチまでにあるコミットを表示
`git log --oneline master..BRANCH`
###  98. カレントブランチをmasterの最新コミットにリベースする
`git rebase master`
###  99. HEAD@{n}によって表現されるSHA1_IDを指し示すように、HEADをステージングエリアと作業ディレクトリの両方でリセットする
`git reset --hard HEAD@{n}`
###  100. masterの最新コミットをカレントブランチに、対話処理でリベースする。これによってエディタが開き、どのコミットをリベースに含めるかの取捨選択が可能となる
`git rebase --interactive master`
###  101. 指定のコミットをカレントブランチにコピーする
`git cherry-pick SHA1_ID`

## ワークフローとブランチの規約

###  102. ファイルの追加なしにコミットを作る
`git commit --allow-empty -m "initial commit"`
###  103. BRANCHをカレントブランチにマージし、たとえfast-forwardであっても、マージコミットを作成する
`git merge --no-ff BRANCH`

## Gitを研ぎ澄ませる

###  104. ローカル（リポジトリ固有の）Git構成をリストで表示
`git config --local --list`
###  105. グローバル（ユーザー固有の）Git構成をリストで表示
`git config --global --list`
###  106. システム（サーバー全体の）Git構成をリストで表示
`git config --system --list`
###  107. 相対的な日付フォーマットで最後の２つのコミットを表示
`git -c log.date=relative log -n 2`
###  108. 相対的な日付フォーマットをローカルGit構成に保存
`git config --local log.date relative`
###  109. ローカル（リポジトリ固有の）Git構成を編集する
`git config --local --edit`
###  110. グローバル（ユーザー固有の）Git構成を編集する
`git config --global --edit`
###  111. システム（サーバー全体の）Git構成を編集する
`git config --system --edit`
###  112. ローカルGit構成ファイルの名前をプリントする
`git -c core.editor=echo config --local --edit`
###  113. ローカルGit構成vimで編集する
`git -c core.editor=vim config --local --edit`
###  114. Git構成core.excludesfileの設定値をプリントする
`git config core.excludesfile`

# 最後に
100本ノックといいながら114本用意してしまいました。
