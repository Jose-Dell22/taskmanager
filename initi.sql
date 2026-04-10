CREATE TABLE IF NOT EXISTS tasks (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(100) NOT NULL,

    description TEXT,

    status VARCHAR(50)

);