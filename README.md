# Introduction

This website contains common applications, such as clothes shops, chat rooms, blogs, etc.

# Techniques used

### Python & Django
(1) There were Users Model, ShopList Model, UserShopItem Model, and Discuss Model which records information     about users, products, products purchased by users, and discussion posts on my website.

(2) I processed each request in view, used ORM syntax to communicate with DB, and used database migration to do version control of database schema. 

(3) For Cache implementation, I used the Redis cache server to catch discussion posts.

(4) For algorithm implementation, I used Bellman Ford to count the shortest path between two points.

(5) For the login system, I applied Authenticate Middleware to verify the access token of each request and used Session to record user login status

(6) For the Chat Room application, I implemented ASGI as a channel layer and used Redis as a channel layer server. When users connected through Websocket and established a channel in ASGI, they were joined to the group automatically.

### MySQL
(1) I used Foreign Key to define the Many-to-One relation between UserShopItem and Users Table.

(2) I got information on commodities purchased by users and buyer's information through Foreign Key.

(2) I applied transaction decorator on queries, such as recording items purchased by users and decreasing the amount of stock, to avoid race conditions.

(3) I used database normalization to avoid repeated data and redundancy.

### Nginx
(1) I used the Load Balancer to spread traffic to each Backend server started as a Docker container.

(2) I used Nginx to reverse proxy the URL started with "/api" to the real Backend server.

(3) I used Nginx to provide static files, such as JS, CSS, HTML, etc.

### Docker & CI/CD
(1) I used Docker to package the code, build into images, and start the container on different platforms. 

(2) I used the GitLab CI/CD mechanism to auto-deploy to the cloud, such as AWS EC2, and use Docker-compose to run three containers (Backend, MySQL, Nginx) at one time.

### Architechture

Below is my project architecture diagram.

https://user-images.githubusercontent.com/42345166/87497034-4ba1c900-c687-11ea-8c4a-b272d7f1c566.jpg