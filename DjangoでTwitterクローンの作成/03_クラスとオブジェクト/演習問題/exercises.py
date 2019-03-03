# このファイルは演習問題の解答です。

# 1  expected 2 blank lines, found 1 = PEP8チェック。コメントの下のは2行の空白が必要


class UserScore:    # UserScoreクラスの作成
    def __init__(self, score):  # メソッドの作成。メソッドとはクラス内で定義されている関数。
        # メソッドの1つ目の引数にはselfを入れる。'self'というのはクラスのインスタンス自身を指す。
        self.score = score  # self自体が'SampleClass'のインスタンスをさしますので、nameと言うインスタンス変数を用意して引数nameを代入します。


u = UserScore({'english': 100, 'math': 49})
u1 = UserScore({'english': 80, 'math': 83})  # PEP8チェック。'：'の後にはスペースが必要。

print(u.score)
print(u1.score)



