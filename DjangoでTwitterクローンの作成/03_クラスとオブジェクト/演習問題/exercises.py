# このファイルは演習問題の解答です。

# 1  expected 2 blank lines, found 1 = PEP8チェック。コメントの下には空白が必要


class UserScore:    # UserScoreクラスの作成
    def __init__(self, score):  # メソッドの作成。メソッドとはクラス内で定義されている関数。
        # メソッドの1番目の引数はselfという名前にする。'self'というのはクラスのインスタンス自身を指す。
        self.score = score  # self自体が'SampleClass'のインスタンスを指すので、nameと言うインスタンス変数を用意して引数nameを代入します。


u = UserScore({'english': 100, 'math': 49})
u1 = UserScore({'english': 80, 'math': 83})  # PEP8チェック。'：'の後にはスペースが必要。

print(u.score)
print(u1.score)

# 2


class User:  # Userクラスの作成。
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
    # 3

    def get_userinfo(self):
        print(self.username)
        print(self.email)


user1 = User(1, 'test', 'test@gmail.com')
user2 = User(2, 'test2', 'test2@gmail.com')

# 3

user1.get_userinfo()
user2.get_userinfo()



