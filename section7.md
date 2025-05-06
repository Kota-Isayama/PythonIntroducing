# 7. 入力と出力

## 7.1. 出力を見やすくフォーマットする

### 7.1.1. フォーマット済み文字列リテラル
問題1:
ユーザーの名前`name`と年齢`age`を受け取り、以下の形の`str`を返す関数`greet_user()`をf文字列を利用して作成してください。
- `Hello <name>, you are <age> years old.`
  - `<name>`と`<age>`にそれぞれ名前と年齢が入ります。

問題2:
商品名`item`、単価（税込前）`price`、個数`quantity`を受け取り、合計金額（税込）を含む注文内容を表す`str`を返す関数`format_order()`
をf文字列を利用して作成してください。ただし、注文内容は以下のフォーマットにし、税率は10%とします。
- `You orderd <個数> x <商品名>. Total with tax: <合計金額(税込)> JPY`


問題3:
幅`width`と高さ`height`を受け取り、f文字列を利用して、その面積を以下の形式の`str`で返す関数`describe_rectangle()`を作成してください。
- `A <幅> x <高さ> rectangle has an area of <面積>. (area=<面積>)`

問題4:
名前`name`とスコア`score`を受け取り、以下の形式の`str`を返す関数`score_format()`を作成してください。
- `<名前> scored <スコア> points.`
  - ただし、スコアはちょうど小数点第二位の数までが表示されるようにしてください。

問題5:
単語`word`を受け取り、以下の形式でf文字列内で中かっこ{}を挿入した`str`を返す関数`escape_example()`を作成してください。
- `Hello {単語}`
  - 例: 入力が`"world"`のとき、`"Hello {world}"`

### 7.1.2. 文字列のformat()メソッド
問題6:
ユーザーの名前`name`と年齢`age`を受け取り、以下の形の`str`を返す関数`greet_user_format()`をformatメソッドを利用して作成してください。
- `Hello <name>, you are <age> years old.`
  - `<name>`と`<age>`にそれぞれ名前と年齢が入ります。

問題7:
商品データ以下の形式で入った辞書`data`を受け取って、合計金額（税込）を含む注文内容を表す`str`を返す関数`format_order_dict()`をformatメソッドを利用して作成してください。
ただし税率は10%とします。
- 辞書の形式
  - `{"item": <商品名>, "price": <値段(税抜)>, "quantity": <個数>}`
- 返り値の形式
  - `You orderd <個数> x <商品名>. Total with tax: <合計金額(税込)> JPY`

問題8:
数字`number`を３桁になるようにゼロ埋めした`str`を返す関数`pad_number()`をformatメソッドを利用して作成してください。
- 例: `7` → `"007"`

問題9:
小数`score`を受け取り、それを%表示に直した`str`を返す関数`percentage()`をformatメソッドを利用して作成してください。
- 例: `0.876` → `"Score: 87.6%"`

問題10:
名前`name`と個数`count`を受け取り、以下の形式の`str`を返す`double_use()`関数をformatメソッドを利用して作成してください。
- `"There are <個数> <名前>(s). I repeat, <個数> <名前>(s)!`
