
api-token-auth

| HTTP Method | Input                            | Processing                | Output                             | Functionality                                |
|-------------|----------------------------------|---------------------------|------------------------------------|----------------------------------------------|
| POST        | `username`, `password` (JSON)    | Validate user credentials | `token` (JSON) on success          | Log in and obtain authentication token       |


| API エンドポイント             | HTTP メソッド | 機能                          |
|------------------------------|------------|-----------------------------|
| /sns_app/posts/              | GET        | 投稿一覧を取得                  |
| /sns_app/posts/              | POST       | 新規投稿を作成                  |
| /sns_app/posts/{id}/         | GET        | 特定の投稿情報を取得              |
| /sns_app/posts/{id}/         | PUT        | 特定の投稿情報を更新              |
| /sns_app/posts/{id}/         | DELETE     | 特定の投稿情報を削除              |
| /sns_app/likes/              | GET        | いいね一覧を取得                 |
| /sns_app/likes/              | POST       | 新規いいねを作成                 |
| /sns_app/likes/{id}/         | GET        | 特定のいいね情報を取得             |
| /sns_app/likes/{id}/         | DELETE     | 特定のいいね情報を削除             |
| /sns_app/comments/           | GET        | コメント一覧を取得               |
| /sns_app/comments/           | POST       | 新規コメントを作成               |
| /sns_app/comments/{id}/      | GET        | 特定のコメント情報を取得           |
| /sns_app/comments/{id}/      | PUT        | 特定のコメント情報を更新           |
| /sns_app/comments/{id}/      | DELETE     | 特定のコメント情報を削除           |
| /sns_app/follows/            | GET        | フォロー一覧を取得               |
| /sns_app/follows/            | POST       | 新規フォローを作成               |
| /sns_app/follows/{id}/       | GET        | 特定のフォロー情報を取得           |
| /sns_app/follows/{id}/       | DELETE     | 特定のフォロー情報を削除           |
| /sns_app/profiles/           | GET        | プロフィール一覧を取得            |
| /sns_app/profiles/{id}/      | GET        | 特定のプロフィール情報を取得       |
| /sns_app/profiles/{id}/      | PUT        | 特定のプロフィール情報を更新       |
| /sns_app/profiles/{id}/      | DELETE     | 特定のプロフィール情報を削除       |
