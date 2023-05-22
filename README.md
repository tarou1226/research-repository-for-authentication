## research-repository-for-authentication
認証の研究リポジトリ

### 実行環境
- macOS Ventura 13.3.1
- Python 3.11.3

### 想定状況
- 日本の人口は約1.3億人
- PINコードは英小文字/大文字、数字 = 62種類 これに記号を加えると、93種類ほどになる。(今後要検討)
    - 記号一覧:[!"#$%&'()=-^~\|@`[{;+:*]},<.>/?_]
    - 62種の場合、8桁で考えると、62 ** 8 == 218,340,105,584,896通りある

### テスト実行方法
```bash
# bash or zsh
$ pwd
/authenntication

$ ls
main.py test.py

$ python -m unittest test.py
OK
```

### PIN発行方法
```bash
# bash or zsh
$ pwd
/authenntication

$ ls
main.py test.py

$ python main.py
```

### 疑問・感想
- コーディング能力が低すぎる
- ランダムな数字列の生成する関数を作れたはいいが、テストの書き方が分からんすぎる
- ランダムなものってどうやってテストするねん(seedとか？)