# Fixtures


| No. | モデル名   | フィクスチャファイル名   | ディレクトリ     | コマンド                                           |
| --- | ---------- | ------------------------ | ---------------- | -------------------------------------------------- |
| 1   | CustomUser | customuser_fixtures.json | api/fixtures     | python manage.py loaddata customuser_fixtures.json |
| 2   | Profile    | profile_fixtures.json    | sns_app/fixtures | python manage.py loaddata profile_fixtures.json    |
| 3   | Post       | post_fixtures.json       | sns_app/fixtures | python manage.py loaddata post_fixtures.json       |
| 4   | Comment    | comment_fixtures.json    | sns_app/fixtures | python manage.py loaddata comment_fixtures.json    |
| 5   | Like       | like_fixtures.json       | sns_app/fixtures | python manage.py loaddata like_fixtures.json       |
| 6   | Follow     | follow_fixtures.json     | sns_app/fixtures | python manage.py loaddata follow_fixtures.json     |

## Fixturesデータ

| No. | アプリケーション名 | モデル名   | フィクスチャファイル名  | JSONデータの例                                                 |
| --- | ------------------ | ---------- | ----------------------- | -------------------------------------------------------------- |
| 1   | api                | CustomUser | custom_users.json       | {"model": "custom_users.customuser", "pk": 1, "fields": {...}} |
| 2   | api                | Profile    | profiles.json           | {"model": "profiles.profile", "pk": 1, "fields": {...}}        |
| 3   | sns_app            | Post       | posts.json              | {"model": "sns_app.post", "pk": 1, "fields": {...}}            |
| 4   | sns_app            | Like       | likes.json              | {"model": "sns_app.like", "pk": 1, "fields": {...}}            |
| 5   | sns_app            | Comment    | comments.json           | {"model": "sns_app.comment", "pk": 1, "fields": {...}}         |
| 6   | sns_app            | Follow     | follows.json            | {"model": "sns_app.follow", "pk": 1, "fields": {...}}          |
| 7   | ec_app             | Product    | product_fixtures.json   | {"model": "ec_app.product", "pk": 1, "fields": {...}}          |
| 8   | ec_app             | Order      | order_fixtures.json     | {"model": "ec_app.order", "pk": 1, "fields": {...}}            |
| 9   | ec_app             | OrderItem  | orderitem_fixtures.json | {"model": "ec_app.orderitem", "pk": 1, "fields": {...}}        |


product_fixtures.json
order_fixtures.json
orderitem_fixtures.json

customuser_fixtures.json
[    {        "model": "api.customuser",        "pk": 1,        "fields": {            "username": "user1",            "email": "user1@example.com",            "first_name": "John",            "last_name": "Doe"        }    }]

profile_fixtures.json
[    {        "model": "sns_app.profile",        "pk": 1,        "fields": {            "custom_user": 1,            "display_name": "John Doe",            "bio": "Hello, I'm John Doe!"        }    }]

post_fixtures.json
[    {        "model": "sns_app.post",        "pk": 1,        "fields": {            "author": 1,            "content": "This is my first post!",            "created_at": "2023-04-01T10:00:00Z"        }    }]

comment_fixtures.json
[    {        "model": "sns_app.comment",        "pk": 1,        "fields": {            "custom_user": 1,            "post": 1,            "content": "Great post!",            "created_at": "2023-04-01T10:05:00Z",            "updated_at": "2023-04-01T10:05:00Z"        }    }]

like_fixtures.json
[    {        "model": "sns_app.like",        "pk": 1,        "fields": {            "custom_user": 1,            "post": 1,            "created_at": "2023-04-01T10:07:00Z"        }    }]

follow_fixtures.json
[    {        "model": "sns_app.follow",        "pk": 1,        "fields": {            "follower": 1,            "followed": 2,            "timestamp": "2023-04-01T10:10:00Z"        }    }]

product_fixtures.json
[    {        "model": "ec_app.product",        "pk": 1,        "fields": {            "name": "Sample Product",            "description": "This is a sample product.",            "price": 1000,            "stock": 10        }    }]

order_fixtures.json
[    {        "model": "ec_app.order",        "pk": 1,        "fields": {            "custom_user": 1,            "total_price": 1100,            "status": "processing",            "created_at": "2023-04-01T11:00:00Z"        }    }]

orderitem_fixtures.json
[    {        "model": "ec_app.orderitem",        "pk": 1,        "fields": {            "order": 1,            "product": 1,            "quantity": 1,            "price": 1000        }    }]

これらのフィクスチャは、それぞれプロジェクト内の関連するアプリケーションの fixtures ディレクトリに配置
