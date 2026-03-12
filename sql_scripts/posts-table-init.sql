-- Create POSTS table
CREATE TABLE posts (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(75) NOT NULL,
    body VARCHAR(800) NOT NULL,
    image_path VARCHAR(200) NULL,
    timestamp DATETIME NOT NULL DEFAULT GETDATE(),
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- Insert sample article
INSERT INTO posts (title, author, body, image_path, user_id)
VALUES (
    'Lorem ipsum dolor sit amet',
    'John Smith',
    'Proin sit amet mi ornare, ultrices augue quis, facilisis tellus. Quisque neque dui, tincidunt sed volutpat quis, maximus sed est.',
    'https://cmsstoragejashan.blob.core.windows.net/images/sample.png',
    1
);