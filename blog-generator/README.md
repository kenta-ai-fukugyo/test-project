# ブログ記事自動生成ツール

テーマを入力するだけで、約1000文字の日本語ブログ記事を自動生成するツールです。

---

## 必要なもの

- Python 3.8 以上
- Anthropic の API キー（[こちら](https://console.anthropic.com/)から取得できます）

---

## セットアップ手順

### 1. このフォルダに移動する

```bash
cd blog-generator
```

### 2. ライブラリをインストールする

```bash
pip install -r requirements.txt
```

### 3. API キーを設定する

ターミナルで以下を実行してください（`sk-ant-...` の部分を自分の API キーに置き換えてください）。

**Mac / Linux の場合:**
```bash
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxxxxx"
```

**Windows の場合:**
```cmd
set ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

---

## 使い方

```bash
python generate.py
```

実行すると「テーマを入力してください:」と表示されるので、好きなテーマを入力してください。

### 実行例

```
=== ブログ記事自動生成ツール ===

テーマを入力してください: 朝のルーティンを整えるメリット

記事を生成中...

--------------------------------------------------
# 朝のルーティンを整えるメリット

（記事が表示されます...）
--------------------------------------------------

文字数: 1023 文字
```

---

## ファイル構成

```
blog-generator/
├── generate.py       # メインスクリプト
├── requirements.txt  # 必要なライブラリ一覧
└── README.md         # この説明書
```

---

## よくある質問

**Q: `ANTHROPIC_API_KEY` が設定されていないとエラーになります**
A: 上記の「API キーを設定する」手順を再確認してください。ターミナルを閉じると設定がリセットされるので、毎回設定が必要です。

**Q: 毎回 API キーを設定するのが面倒です**
A: `.zshrc`（Mac）や `.bashrc`（Linux）に `export ANTHROPIC_API_KEY="..."` を追記すると、ターミナルを開くたびに自動で設定されます。

**Q: 生成される記事の長さを変えたいです**
A: `generate.py` の `content` 内にある「文字数は約1000文字」の部分を書き換えてください。
