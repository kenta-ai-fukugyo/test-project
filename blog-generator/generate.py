import os
import anthropic

def generate_blog_article(theme: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""以下のテーマでブログ記事を書いてください。

テーマ: {theme}

条件:
- 日本語で書く
- 文字数は約1000文字
- ブログ記事らしく、タイトル・導入・本文・まとめの構成にする
- 読みやすく、わかりやすい文体にする

記事のみを出力してください（余計な説明は不要です）。""",
            }
        ],
    )

    return response.content[0].text


def main():
    print("=== ブログ記事自動生成ツール ===\n")
    theme = input("テーマを入力してください: ").strip()

    if not theme:
        print("エラー: テーマが入力されていません。")
        return

    print("\n記事を生成中...\n")
    print("-" * 50)

    article = generate_blog_article(theme)
    print(article)

    print("-" * 50)
    print(f"\n文字数: {len(article)} 文字")


if __name__ == "__main__":
    main()
