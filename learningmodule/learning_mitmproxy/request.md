# HTTP请求和响应示例

## GET请求

### 请求
```http request
GET /api/items?id=123 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (compatible; MyBrowser/1.0)
Accept: application/json
```

- **请求行**: `GET /api/items?id=123 HTTP/1.1` 指定了请求方法、请求路径和HTTP版本。
- **请求头**: 包含客户端信息、接受的数据类型等。
- **请求体**: GET请求通常没有请求体。

### 响应
```http response
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
"id": 123,
"name": "Sample Item",
"description": "This is a sample item."
}
```
   
    
- **状态行**: `HTTP/1.1 200 OK` 表示请求成功。
- **响应头**: 包含内容类型和内容长度。
- **响应体**: 返回的JSON格式数据。

## POST请求

### 请求
```http request
POST /api/items HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (compatible; MyBrowser/1.0)
Accept: application/json
Content-Type: application/json
Content-Length: 43

{
"name": "New Item",
"description": "This is a new item."
}
```

- **请求行**: `POST /api/items HTTP/1.1` 指定了请求方法和路径。
- **请求头**: 包含客户端信息、接受的数据类型、内容类型和内容长度。
- **请求体**: 包含要创建的新项目的JSON数据。


### 响应
```http response
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 123

{
"id": 456,
"name": "New Item",
"description": "This is a new item."
}
```


- **状态行**: `HTTP/1.1 201 Created` 表示资源被成功创建。
- **响应头**: 包含内容类型和内容长度。
- **响应体**: 返回新创建的项目的JSON格式数据。

## PUT请求

### 请求
```http request
PUT /api/items/123 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (compatible; MyBrowser/1.0)
Accept: application/json
Content-Type: application/json
Content-Length: 60

{
"name": "Updated Item",
"description": "This item has been updated."
}

```


- **请求行**: `PUT /api/items/123 HTTP/1.1` 指定了请求方法和资源标识符。
- **请求头**: 包含客户端信息、接受的数据类型、内容类型和内容长度。
- **请求体**: 包含更新资源的JSON数据。

### 响应
```http response
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
"id": 123,
"name": "Updated Item",
"description": "This item has been updated."
}
```
- **状态行**: `HTTP/1.1 200 OK` 表示资源被成功更新。
- **响应头**: 包含内容类型和内容长度。
- **响应体**: 返回更新后的资源的JSON格式数据。

## DELETE请求

### 请求
```http request
DELETE /api/items/123 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (compatible; MyBrowser/1.0)
Accept: application/json
```
- **请求行**: `DELETE /api/items/123 HTTP/1.1` 指定了请求方法和资源标识符。
- **请求头**: 包含客户端信息和接受的数据类型。
- **请求体**: DELETE请求通常没有请求体。

### 响应
```http response
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0

```
- **状态行**: `HTTP/1.1 204 No Content` 表示资源被成功删除，且响应体为空。
- **响应头**: 包含内容类型，但内容长度为0，因为没有返回数据。