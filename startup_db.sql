-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: startup
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `document_upload_details`
--

DROP TABLE IF EXISTS `document_upload_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_upload_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(250) NOT NULL,
  `document_path` varchar(250) NOT NULL,
  `type` varchar(250) NOT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `document_id` (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_upload_details`
--

LOCK TABLES `document_upload_details` WRITE;
/*!40000 ALTER TABLE `document_upload_details` DISABLE KEYS */;
INSERT INTO `document_upload_details` VALUES (1,'6ae1b56cebf211e8adb97440bb2fa689','kratos_god_of_war.jpg','image/jpeg','2018-11-19 17:27:30'),(2,'67ed993aec2311e8adb97440bb2fa689','kratos_god_of_war.jpg','image/jpeg','2018-11-19 23:17:54'),(3,'97299ddaed5d11e8aa587440bb2fa689','kratos_god_of_war.jpg','image/jpeg','2018-11-21 12:43:37'),(4,'9427baf8ed5e11e8aa587440bb2fa689','kratos_god_of_war.jpg','image/jpeg','2018-11-21 12:55:04'),(5,'e539b23eed5e11e8aa587440bb2fa689','kratos_god_of_war.jpg','image/jpeg','2018-11-21 12:57:18');
/*!40000 ALTER TABLE `document_upload_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `otp`
--

DROP TABLE IF EXISTS `otp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `otp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actor_id` varchar(250) NOT NULL,
  `otp` varchar(250) NOT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otp`
--

LOCK TABLES `otp` WRITE;
/*!40000 ALTER TABLE `otp` DISABLE KEYS */;
INSERT INTO `otp` VALUES (1,'341948871367','829014','2018-11-19 17:27:30');
/*!40000 ALTER TABLE `otp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_credentials`
--

DROP TABLE IF EXISTS `password_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `password_credentials` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actor_id` varchar(250) DEFAULT NULL,
  `password` varchar(250) NOT NULL,
  `created_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `actor_id` (`actor_id`),
  CONSTRAINT `password_credentials_ibfk_1` FOREIGN KEY (`actor_id`) REFERENCES `registrations` (`actor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_credentials`
--

LOCK TABLES `password_credentials` WRITE;
/*!40000 ALTER TABLE `password_credentials` DISABLE KEYS */;
INSERT INTO `password_credentials` VALUES (1,'341948871367','MTIzNDU2','2018-11-19 17:27:30','2018-11-19 17:27:30');
/*!40000 ALTER TABLE `password_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_comments`
--

DROP TABLE IF EXISTS `post_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` varchar(250) DEFAULT NULL,
  `comment` varchar(250) NOT NULL,
  `poster` varchar(250) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  KEY `poster` (`poster`),
  CONSTRAINT `post_comments_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post_details` (`post_id`),
  CONSTRAINT `post_comments_ibfk_2` FOREIGN KEY (`poster`) REFERENCES `registrations` (`actor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_comments`
--

LOCK TABLES `post_comments` WRITE;
/*!40000 ALTER TABLE `post_comments` DISABLE KEYS */;
INSERT INTO `post_comments` VALUES (1,'5c827550ebfd11e8adb97440bb2fa689','This is amazing brother. Will definitely support you.','341948871367','2018-11-19 21:57:57'),(2,'5c827550ebfd11e8adb97440bb2fa689','This is amazing brother. Will definitely support you.','341948871367','2018-11-19 22:01:06'),(3,'5c827550ebfd11e8adb97440bb2fa689','This is amazing brother. Will definitely support you.','341948871367','2018-11-19 22:01:50'),(4,'5c827550ebfd11e8adb97440bb2fa689','This is amazing brother. Will definitely support you.','341948871367','2018-11-19 22:02:41');
/*!40000 ALTER TABLE `post_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_details`
--

DROP TABLE IF EXISTS `post_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poster` varchar(250) DEFAULT NULL,
  `post_id` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `description` text,
  `created_date` varchar(250) DEFAULT NULL,
  `modified_date` varchar(250) DEFAULT NULL,
  `type` enum('GENERAL','MY_FEED','GROUP') DEFAULT 'GENERAL',
  PRIMARY KEY (`id`),
  UNIQUE KEY `post_id` (`post_id`),
  KEY `poster` (`poster`),
  CONSTRAINT `post_details_ibfk_1` FOREIGN KEY (`poster`) REFERENCES `registrations` (`actor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_details`
--

LOCK TABLES `post_details` WRITE;
/*!40000 ALTER TABLE `post_details` DISABLE KEYS */;
INSERT INTO `post_details` VALUES (1,'341948871367','75236d86ebf211e8adb97440bb2fa689','Minister in Modi Government Was Also Bribed, CBI Officer Alleges in SC Petition','Calling for an SIT to take over the case, Manish Kumar Sinha says there is a pressing need to fix a timeline for investigation in corruption so that premier investigating agencies dont become the \"Centre for Bogus Investigation\" and \"Extortion Directorate\".','2018-11-19 17:27:30','2018-11-19 17:27:30','GENERAL'),(2,'341948871367','ee300400ebf211e8adb97440bb2fa689','PM Modi Rakes Up CWG Scam as He Inaugurates KMP Expressway, Flags Off Mujesar Metro Line','With a design speed of 120 kmph for light vehicles and 100 kmph for heavy ones, the Western Peripheral Expressway is finally opening today, November 19.','2018-11-19 17:27:30','2018-11-19 17:27:30','GENERAL'),(3,'341948871367','ff24e55aebf211e8adb97440bb2fa689','AMU Postpones Play After Posters Showing Parts of J&K Missing From India\'s Map Spark Outrage','The play, penned by famous Hindi playwright Asghar Wajahat and scheduled for Sunday evening at the AMU drama club, was put off after objection was raised over its publicity posters carrying the erroneous map.','2018-11-19 17:27:30','2018-11-19 17:27:30','GENERAL'),(4,'341948871367','0c29a9deebf311e8adb97440bb2fa689','Sarfraz Ahmed Blames Poor Shot Selection For Loss Against Kiwis at Abu Dhabi','Pakistan captain Sarfraz Ahmed attributed lack of runs and poor shot selection from the lower order as reason for four-run loss against New Zealand on Monday.','2018-11-19 17:27:30','2018-11-19 17:27:30','GENERAL'),(5,'341948871367','1d875eceebf311e8adb97440bb2fa689','Pathetic How Sabarimala Pilgrims Are Being Treated','The Union minister visited Nilackal, the base camp, Pamba and Sannidhanam Monday morning, hours after police removed around 200-odd people who had gathered at the temple complex late on Sunday night.','2018-11-19 17:27:30','2018-11-19 17:27:30','GENERAL'),(6,'341948871367','5c827550ebfd11e8adb97440bb2fa689','Google News may shut down in EU over link tax','According to the new copyright directive, adopted by the European Parliament on September 12, tech giants must pay for work of artists and journalists which they use.','2018-11-20 18:48:14','2018-11-19 18:44:30','GENERAL');
/*!40000 ALTER TABLE `post_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_document_mapping`
--

DROP TABLE IF EXISTS `post_document_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post_document_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` varchar(250) DEFAULT NULL,
  `document_id` varchar(250) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  KEY `document_id` (`document_id`),
  CONSTRAINT `post_document_mapping_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post_details` (`post_id`),
  CONSTRAINT `post_document_mapping_ibfk_2` FOREIGN KEY (`document_id`) REFERENCES `document_upload_details` (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_document_mapping`
--

LOCK TABLES `post_document_mapping` WRITE;
/*!40000 ALTER TABLE `post_document_mapping` DISABLE KEYS */;
INSERT INTO `post_document_mapping` VALUES (1,'75236d86ebf211e8adb97440bb2fa689','6ae1b56cebf211e8adb97440bb2fa689','2018-11-19 17:27:30');
/*!40000 ALTER TABLE `post_document_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_likes`
--

DROP TABLE IF EXISTS `post_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post_likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` varchar(250) DEFAULT NULL,
  `liked_by` varchar(250) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  KEY `liked_by` (`liked_by`),
  CONSTRAINT `post_likes_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post_details` (`post_id`),
  CONSTRAINT `post_likes_ibfk_2` FOREIGN KEY (`liked_by`) REFERENCES `registrations` (`actor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_likes`
--

LOCK TABLES `post_likes` WRITE;
/*!40000 ALTER TABLE `post_likes` DISABLE KEYS */;
INSERT INTO `post_likes` VALUES (4,'5c827550ebfd11e8adb97440bb2fa689','341948871367','2018-11-19 22:25:37');
/*!40000 ALTER TABLE `post_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrations`
--

DROP TABLE IF EXISTS `registrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actor_id` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `mdn` int(11) NOT NULL,
  `channel` varchar(250) NOT NULL,
  `status` enum('ACTIVE','INACTIVE','ACTIVATION_PENDING') DEFAULT NULL,
  `document_id` varchar(250) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `actor_id` (`actor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrations`
--

LOCK TABLES `registrations` WRITE;
/*!40000 ALTER TABLE `registrations` DISABLE KEYS */;
INSERT INTO `registrations` VALUES (1,'341948871367','Deepak Gupta',1000000016,'web','ACTIVE','67ed993aec2311e8adb97440bb2fa689','2018-11-19 23:19:22','2018-11-19 17:27:30');
/*!40000 ALTER TABLE `registrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-21 12:58:04
