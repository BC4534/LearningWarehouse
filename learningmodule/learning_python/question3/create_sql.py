import sqlite3

# 连接到数据库
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 创建作者表
create_authors_table = '''
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL,
    email TEXT UNIQUE
);
'''
cursor.execute(create_authors_table)

# 创建分类表
create_categories_table = '''
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE
);
'''
cursor.execute(create_categories_table)

# 创建文章表
create_articles_table = '''
CREATE TABLE IF NOT EXISTS articles (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    publish_date DATE,
    author_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
'''
cursor.execute(create_articles_table)

# 插入作者数据
author_data = [
    ('John Doe', 'john.doe@example.com'),
    ('Jane Smith', 'jane.smith@example.com')
]
insert_author_query = "INSERT INTO authors (author_name, email) VALUES (?,?)"
cursor.executemany(insert_author_query, author_data)

# 插入分类数据
category_data = [
    ('Technology',),
    ('Lifestyle',)
]
insert_category_query = "INSERT INTO categories (category_name) VALUES (?)"
cursor.executemany(insert_category_query, category_data)

# 插入文章数据
article_data = [
    ('Introduction to Python', 'Python is a great programming language...', '2024-01-01', 1, 1),
    ('Healthy Living Tips', 'Here are some tips for a healthy lifestyle...', '2024-02-01', 2, 2)
]
insert_article_query = "INSERT INTO articles (title, content, publish_date, author_id, category_id) VALUES (?,?,?,?,?)"
cursor.executemany(insert_article_query, article_data)

# 提交更改
conn.commit()
# 关闭连接
conn.close()