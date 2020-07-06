-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_chat_table`
--

DROP TABLE IF EXISTS `piano_chat_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_chat_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `who_receive` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `time` datetime(6) NOT NULL,
  `who_send_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piano_chat_table_who_send_id_ddbd48c0_fk_piano_users_id` (`who_send_id`),
  CONSTRAINT `piano_chat_table_who_send_id_ddbd48c0_fk_piano_users_id` FOREIGN KEY (`who_send_id`) REFERENCES `piano_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_chat_table`
--

LOCK TABLES `piano_chat_table` WRITE;
/*!40000 ALTER TABLE `piano_chat_table` DISABLE KEYS */;
INSERT INTO `piano_chat_table` VALUES (1,'John','Hello','2020-06-11 05:23:21.000000',1),(3,'Judy','Hi, Judy','2020-06-12 15:23:21.000000',1),(4,'Ann','Hi, Ann','2020-06-15 08:23:21.000000',3),(6,'John','It\'s hot','2020-06-12 04:30:21.000000',3),(8,'John','Hello','2020-06-05 15:23:41.000000',1),(9,'Judy','Hello! Judy','2020-06-12 10:23:41.000000',1),(10,'Ann','Hello, Ann','2020-06-11 15:23:41.000000',2);
/*!40000 ALTER TABLE `piano_chat_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:24:18
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_comments`
--

DROP TABLE IF EXISTS `piano_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comments` varchar(255) NOT NULL,
  `time` datetime(6) NOT NULL,
  `discuss_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piano_comments_discuss_id_ddec8bf9_fk_piano_discuss_id` (`discuss_id`),
  KEY `piano_comments_user_id_941f2bbd_fk_piano_users_id` (`user_id`),
  CONSTRAINT `piano_comments_discuss_id_ddec8bf9_fk_piano_discuss_id` FOREIGN KEY (`discuss_id`) REFERENCES `piano_discuss` (`id`),
  CONSTRAINT `piano_comments_user_id_941f2bbd_fk_piano_users_id` FOREIGN KEY (`user_id`) REFERENCES `piano_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_comments`
--

LOCK TABLES `piano_comments` WRITE;
/*!40000 ALTER TABLE `piano_comments` DISABLE KEYS */;
INSERT INTO `piano_comments` VALUES (1,'This is good!','2020-05-21 16:54:31.000000',1,1),(2,'Hi','2020-06-05 11:12:40.000000',2,2),(3,'Hello!','2020-06-04 14:23:16.000000',3,3),(4,'It\'s good!','2020-06-24 06:35:33.000000',9,1),(5,'I Love This!','2020-06-24 07:17:39.000000',1,1);
/*!40000 ALTER TABLE `piano_comments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:25:06
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_discuss`
--

DROP TABLE IF EXISTS `piano_discuss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_discuss` (
  `id` int NOT NULL AUTO_INCREMENT,
  `discuss_type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `time` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piano_discuss_user_id_a016c95c_fk_piano_users_id` (`user_id`),
  CONSTRAINT `piano_discuss_user_id_a016c95c_fk_piano_users_id` FOREIGN KEY (`user_id`) REFERENCES `piano_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_discuss`
--

LOCK TABLES `piano_discuss` WRITE;
/*!40000 ALTER TABLE `piano_discuss` DISABLE KEYS */;
INSERT INTO `piano_discuss` VALUES (1,'music','Popular Songs','This is a list of songs that have peaked at number one on the Billboard Hot 100 and the magazine\'s national singles charts that preceded it.','2020-05-11 05:28:31.000000',1),(2,'finance','stock','I love play Stock. And you ?','2020-03-25 08:35:21.000000',3),(3,'sports','tennis','I love play tennis. And you ?','2020-04-11 15:07:21.000000',2),(4,'entertainments','pop stars','I love play Jay. And you ?','2020-06-25 15:07:21.000000',1),(6,'music','Slow songs','I love slow songs. And you ?','2020-01-25 17:07:21.000000',2),(7,'sports','FootBall','Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. Unqualified, the word football normally means the form of football that is the most popular where the word is used.','2020-02-18 18:07:21.000000',3),(8,'music','Jazz','Jazz is good','2020-02-23 12:20:34.000000',1),(9,'entertainment','Show','Welcome to see the show!','2020-06-24 06:19:33.000000',1);
/*!40000 ALTER TABLE `piano_discuss` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:26:18
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_shoplist`
--

DROP TABLE IF EXISTS `piano_shoplist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_shoplist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `img_src` varchar(255) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_shoplist`
--

LOCK TABLES `piano_shoplist` WRITE;
/*!40000 ALTER TABLE `piano_shoplist` DISABLE KEYS */;
INSERT INTO `piano_shoplist` VALUES (1,'jack','/image/jacket.jpg','This is Jack',300),(2,'neckless','/image/necklace.jpg','This is shoplist items.',300),(3,'shoes','/image/shoes.jpg','This is shoes.',900),(4,'sweater','/image/sweater.jpg','This is sweater.',700),(5,'coat','/image/coat.jpg','This is coat.',1100);
/*!40000 ALTER TABLE `piano_shoplist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:26:36
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_usershopitem`
--

DROP TABLE IF EXISTS `piano_usershopitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_usershopitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `color` varchar(100) NOT NULL,
  `size` varchar(100) NOT NULL,
  `shoplist_id` int NOT NULL,
  `users_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piano_usershopitem_shoplist_id_be87abd0_fk_piano_shoplist_id` (`shoplist_id`),
  KEY `piano_usershopitem_users_id_4f2f30b0_fk_piano_users_id` (`users_id`),
  CONSTRAINT `piano_usershopitem_shoplist_id_be87abd0_fk_piano_shoplist_id` FOREIGN KEY (`shoplist_id`) REFERENCES `piano_shoplist` (`id`),
  CONSTRAINT `piano_usershopitem_users_id_4f2f30b0_fk_piano_users_id` FOREIGN KEY (`users_id`) REFERENCES `piano_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_usershopitem`
--

LOCK TABLES `piano_usershopitem` WRITE;
/*!40000 ALTER TABLE `piano_usershopitem` DISABLE KEYS */;
INSERT INTO `piano_usershopitem` VALUES (1,'pink','L',1,1),(2,'pink','L',2,1),(3,'pink','L',3,2),(4,'pink','L',4,3),(5,'pink','L',4,2),(6,'pink','L',1,3),(7,'pink','L',5,2),(8,'pink','L',4,1),(9,'pink','L',5,3),(10,'pink','L',2,1),(11,'blue','M',3,2),(12,'pink','M',3,3),(13,'blue','L',5,3),(14,'pink','M',1,1),(15,'pink','M',3,3),(16,'blue','L',5,3);
/*!40000 ALTER TABLE `piano_usershopitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:27:09
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: testDB
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `piano_users`
--

DROP TABLE IF EXISTS `piano_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piano_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `guide` varchar(255) NOT NULL,
  `hobby` varchar(255) NOT NULL,
  `job` varchar(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `piano_users_password_fd7c7f6a_uniq` (`password`),
  UNIQUE KEY `piano_users_username_dab0ff7a_uniq` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piano_users`
--

LOCK TABLES `piano_users` WRITE;
/*!40000 ALTER TABLE `piano_users` DISABLE KEYS */;
INSERT INTO `piano_users` VALUES (1,'Ann','ann123','Taiwan','girl','Hello!','Piano','F2E','/home/ann/Code/GitLab/React/Photos/Ann.jpg'),(2,'John','john123','Taiwan','boy','Hello','tennis','teacher','/home/ann/Code/GitLab/React/Photos/John.jpg'),(3,'Judy','judy123','Japan','girl','I\'m Judy','play ball','postman','/home/ann/Code/GitLab/React/Photos/Judy.jpg');
/*!40000 ALTER TABLE `piano_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-28 14:26:52
