# django_rest_web_todo

- 概要
- 認証方式： JWT(Simple Json Web Token) token認証
  - 開発(Debug設定)　メールはコンソールに表示する。（ローカルでテスト）
  - 本番設定：settings.pyでメール、メールサーバーの設定を有効化すること。
- アカウント管理（account/)
- API(api/)
- データベース(docker/)
  - docker-compose: PostgreSQL(本ソフトデフォルト）
    - dockerフォルダー/postgresql でPostgreSQL選択可能。
    - dockerフォルダー/mysql で、MySQL選択可能。
- Todo-Webアプリ(todo_task/)
- Todo-API

### 概要

- Django REST Frameworkを使ったTODOアプリ
- JWT SimpleJWTによるtoken認証を利用
- Djoserパッケージの利用による

### (1) 認証・認可　API一覧


| 機能                       | URL                                                          |
| -------------------------- | ------------------------------------------------------------ |
| 1. アカウント仮登録        | http://localhost:8000/api/auth/users/                        |
| - tokenの取得              | http://localhost:8000/api/auth/jwt/create/                   |
| 2. アカウント本登録        | http://localhost:8000/api/auth/users/activation/             |
| 3. アカウント本登録再送信  | http://localhost:8000/api/auth/users/resend_activation/      |
| 4. ログイン                | http://localhost:8000/api/auth/jwt/create/                   |
| 5. リフレッシュトークン    | http://localhost:8000/api/auth/jwt/refresh/                  |
| 6. 認証チェック            | http://localhost:8000/api/auth/jwt/verify/                   |
| 7. ユーザー情報取得        | http://localhost:8000/api/auth/users/me/                     |
| 8. ユーザー情報変更        | http://localhost:8000/api/auth/users/me/                     |
| 9. ユーザーリスト取得      | http://localhost:8000/api/auth/users/                        |
| 10. メールアドレス変更     | (Djoserのデフォルトでは提供されていない)                     |
| 11. メールアドレス変更確認 | (Djoserのデフォルトでは提供されていない)                     |
| 12. パスワード変更         | http://localhost:8000/api/auth/users/set_password/           |
| 13. パスワードリセット     | http://localhost:8000/api/auth/users/reset_password/         |
| 14. パスワードリセット確認 | http://localhost:8000/api/auth/users/reset_password_confirm/ |
| 15. アカウント削除         | http://localhost:8000/api/auth/users/{username}/             |
| 16. アカウント削除確認     | (Djoserのデフォルトでは提供されていない)                     |

## 認証・認可　ユニットテスト
