# f_string_practice.py

# 問題1
# ユーザーの名前と年齢を受け取り、"Hello <name>, you are <age> years old." という形式のメッセージを返してください。
def greet_user(name: str, age: int) -> str:
    return ""  # ここをf文字列で実装してください

# def test_greet_user():
#     import pytest
#     @pytest.mark.parametrize("name,age,expected", [
#         ("Alice", 30, "Hello Alice, you are 30 years old."),
#         ("Bob", 22, "Hello Bob, you are 22 years old."),
#     ])
#     def test(name, age, expected):
#         assert greet_user(name, age) == expected


# 問題2
# 商品名、単価（税込前）、個数を受け取り、合計金額（税込）を含む注文内容を出力してください。
# 消費税は10%として、合計に対して課税してください。
def format_order(item: str, price: float, quantity: int) -> str:
    return ""  # f文字列で小数計算も含めて実装してください

# def test_format_order():
#     import pytest
#     @pytest.mark.parametrize("item,price,quantity,expected", [
#         ("apple", 100.0, 3, "You ordered 3 x apple. Total with tax: 330.0 JPY"),
#         ("banana", 200.0, 2, "You ordered 2 x banana. Total with tax: 440.0 JPY"),
#     ])
#     def test(item, price, quantity, expected):
#         assert format_order(item, price, quantity) == expected


# 問題3
# 幅と高さを受け取り、面積を2回表示するようなメッセージを返してください。
# 例: "A 4.0 x 5.0 rectangle has an area of 20.0. (area=20.0)"
def describe_rectangle(width: float, height: float) -> str:
    return ""  # 面積の変数を2回f文字列内で使ってください

# def test_describe_rectangle():
#     import pytest
#     @pytest.mark.parametrize("width,height,expected", [
#         (4.0, 5.0, "A 4.0 x 5.0 rectangle has an area of 20.0. (area=20.0)"),
#     ])
#     def test(width, height, expected):
#         assert describe_rectangle(width, height) == expected


# 問題4
# 名前とスコアを受け取り、f文字列内でformatメソッドを使ってスコアを小数第2位まで整形してください。
# 例: "Eve scored 87.46 points."
def nested_format(name: str, score: float) -> str:
    return ""  # f文字列の中で format() を使って小数の整形をしてください

# def test_nested_format():
#     import pytest
#     @pytest.mark.parametrize("name,score,expected", [
#         ("Eve", 87.456, "Eve scored 87.46 points."),
#     ])
#     def test(name, score, expected):
#         assert nested_format(name, score) == expected


# 問題5
# 文字列を受け取り、f文字列内で中括弧 `{}` を表示させてください。
# 例: 入力が "world" のとき → "Hello {world}"
def escape_example(word: str) -> str:
    return ""  # 中括弧のエスケープに注意してください

# def test_escape_example():
#     import pytest
#     @pytest.mark.parametrize("word,expected", [
#         ("world", "Hello {world}"),
#     ])
#     def test(word, expected):
#         assert escape_example(word) == expected


# format_method_practice.py

# 問題1
# 名前と年齢を受け取り、"Hello <name>, you are <age> years old." という形式で返してください。
def greet_user_format(name: str, age: int) -> str:
    return ""  # formatメソッドを使ってください

# def test_greet_user_format():
#     import pytest
#     @pytest.mark.parametrize("name,age,expected", [
#         ("Alice", 30, "Hello Alice, you are 30 years old."),
#         ("Bob", 22, "Hello Bob, you are 22 years old."),
#     ])
#     def test(name, age, expected):
#         assert greet_user_format(name, age) == expected


# 問題2
# 辞書で渡された商品データを使って、"You ordered <quantity> x <item> at <price> JPY each." を返してください。
# ヒント: formatメソッドに辞書を展開して渡しましょう。
def format_order_dict(data: dict) -> str:
    return ""  # format(**data) を活用

# def test_format_order_dict():
#     import pytest
#     @pytest.mark.parametrize("data,expected", [
#         ({"item": "apple", "price": 100.0, "quantity": 3}, "You ordered 3 x apple at 100.0 JPY each."),
#     ])
#     def test(data, expected):
#         assert format_order_dict(data) == expected


# 問題3
# 数字を3桁になるようにゼロ埋めしてください。
# 例: 7 → "007"
def pad_number(number: int) -> str:
    return ""  # formatでゼロ埋めを実現してください

# def test_pad_number():
#     import pytest
#     @pytest.mark.parametrize("number,expected", [
#         (7, "007"),
#         (42, "042"),
#     ])
#     def test(number, expected):
#         assert pad_number(number) == expected


# 問題4
# 小数をパーセント表示してください（例: 0.876 → "Score: 87.6%"）。
def percentage(score: float) -> str:
    return ""  # パーセント表示のフォーマット指定子を使ってください

# def test_percentage():
#     import pytest
#     @pytest.mark.parametrize("score,expected", [
#         (0.876, "Score: 87.6%"),
#     ])
#     def test(score, expected):
#         assert percentage(score) == expected


# 問題5
# 変数を複数回使用する文を format で作成してください。
# 例: "There are 2 cat(s). I repeat, 2 cat(s)!"
def double_use(name: str, count: int) -> str:
    return ""  # 同じ引数を2回以上使う例にしてください

# def test_double_use():
#     import pytest
#     @pytest.mark.parametrize("name,count,expected", [
#         ("cat", 2, "There are 2 cat(s). I repeat, 2 cat(s)!"),
#     ])
#     def test(name, count, expected):
#         assert double_use(name, count) == expected
