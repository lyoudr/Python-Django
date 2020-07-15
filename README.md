# Introduction

This website contains common applications such as clothes shops, chat rooms, blogs, etc.

# Techniques used

### Python & Django
(1) Designed each table data Model and used Many-to-many or Foreign key fields to establish the relation between tables.

(2) Used ORM syntax to communicate with DB. Besides, I use database migration to do version control of database schema.

(3) Dispatched URL, and processed various requests in View, 

(4) Did Error handling if there were exceptions.

(5) Used Session to record user login status, and use the Redis cache server to optimize performance.

### MySQL
(1) Designed table schema and define relationships between table using Foreign Key.

(2) Used database normalization to avoid repeated data and redundancy.

### Nginx
(1) Used the Load Balancer to spread traffic to each Backend server.

(2) Used Reverse Proxy to deliver requests to the real Backend server.

(3) Used Nginx to provide static file rendering services.

### Docker & CI/CD
(1) Used Docker to package the code, build into images, and start the container on different platforms, and use 

(2) Docker-compose to run several containers at once.

(3) Used the GitLab CI/CD mechanism to auto-deploy to the cloud, such as AWS EC2, and use Docker-compose to run three containers (Backend, MySQL, Nginx) at one time.

### Architechture

Following is my project architechture diagram.

https://user-images.githubusercontent.com/42345166/87497034-4ba1c900-c687-11ea-8c4a-b272d7f1c566.jpg