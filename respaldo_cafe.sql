-- MySQL dump 10.13  Distrib 5.5.34, for Linux (x86_64)
--
-- Host: localhost    Database: sacracin_cafe
-- ------------------------------------------------------
-- Server version	5.5.34-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add Pais',8,'add_pais'),(23,'Can change Pais',8,'change_pais'),(24,'Can delete Pais',8,'delete_pais'),(25,'Can add departamento',9,'add_departamento'),(26,'Can change departamento',9,'change_departamento'),(27,'Can delete departamento',9,'delete_departamento'),(28,'Can add municipio',10,'add_municipio'),(29,'Can change municipio',10,'change_municipio'),(30,'Can delete municipio',10,'delete_municipio'),(31,'Can add comunidad',11,'add_comunidad'),(32,'Can change comunidad',11,'change_comunidad'),(33,'Can delete comunidad',11,'delete_comunidad'),(34,'Can add migration history',12,'add_migrationhistory'),(35,'Can change migration history',12,'change_migrationhistory'),(36,'Can delete migration history',12,'delete_migrationhistory'),(37,'Can add Entrevistado',13,'add_entrevistado'),(38,'Can change Entrevistado',13,'change_entrevistado'),(39,'Can delete Entrevistado',13,'delete_entrevistado'),(40,'Can add Dueño Finca',14,'add_duenofinca'),(41,'Can change Dueño Finca',14,'change_duenofinca'),(42,'Can delete Dueño Finca',14,'delete_duenofinca'),(43,'Can add Organizacion',15,'add_organizacion'),(44,'Can change Organizacion',15,'change_organizacion'),(45,'Can delete Organizacion',15,'delete_organizacion'),(46,'Can add recolector',16,'add_recolector'),(47,'Can change recolector',16,'change_recolector'),(48,'Can delete recolector',16,'delete_recolector'),(49,'Can add encuesta',17,'add_encuesta'),(50,'Can change encuesta',17,'change_encuesta'),(51,'Can delete encuesta',17,'delete_encuesta'),(52,'Can add socio organizacion',18,'add_socioorganizacion'),(53,'Can change socio organizacion',18,'change_socioorganizacion'),(54,'Can delete socio organizacion',18,'delete_socioorganizacion'),(55,'Can add Beneficio',19,'add_beneficios'),(56,'Can change Beneficio',19,'change_beneficios'),(57,'Can delete Beneficio',19,'delete_beneficios'),(58,'Can add credito',20,'add_creditoe'),(59,'Can change credito',20,'change_creditoe'),(60,'Can delete credito',20,'delete_creditoe'),(61,'Can add Organizaciones que dan credito',21,'add_dequien'),(62,'Can change Organizaciones que dan credito',21,'change_dequien'),(63,'Can delete Organizaciones que dan credito',21,'delete_dequien'),(64,'Can add quien financia',22,'add_quienfinancia'),(65,'Can change quien financia',22,'change_quienfinancia'),(66,'Can delete quien financia',22,'delete_quienfinancia'),(67,'Can add vive familia',23,'add_vivefamilia'),(68,'Can change vive familia',23,'change_vivefamilia'),(69,'Can delete vive familia',23,'delete_vivefamilia'),(70,'Can add composicion',24,'add_composicion'),(71,'Can change composicion',24,'change_composicion'),(72,'Can delete composicion',24,'delete_composicion'),(73,'Can add EnergiaFinca',25,'add_energiafinca'),(74,'Can change EnergiaFinca',25,'change_energiafinca'),(75,'Can delete EnergiaFinca',25,'delete_energiafinca'),(76,'Can add Combustible en la cocina',26,'add_combustible'),(77,'Can change Combustible en la cocina',26,'change_combustible'),(78,'Can delete Combustible en la cocina',26,'delete_combustible'),(79,'Can add Disponibilidad de agua en la finca',27,'add_aguafinca'),(80,'Can change Disponibilidad de agua en la finca',27,'change_aguafinca'),(81,'Can delete Disponibilidad de agua en la finca',27,'delete_aguafinca'),(82,'Can add servicios basicos',28,'add_serviciosbasicos'),(83,'Can change servicios basicos',28,'change_serviciosbasicos'),(84,'Can delete servicios basicos',28,'delete_serviciosbasicos'),(85,'Can add tenecia',29,'add_tenecia'),(86,'Can change tenecia',29,'change_tenecia'),(87,'Can delete tenecia',29,'delete_tenecia'),(88,'Can add necesidad alimento',30,'add_necesidadalimento'),(89,'Can change necesidad alimento',30,'change_necesidadalimento'),(90,'Can delete necesidad alimento',30,'delete_necesidadalimento'),(91,'Can add meses',31,'add_meses'),(92,'Can change meses',31,'change_meses'),(93,'Can delete meses',31,'delete_meses'),(94,'Can add tiempos crisis',32,'add_tiemposcrisis'),(95,'Can change tiempos crisis',32,'change_tiemposcrisis'),(96,'Can delete tiempos crisis',32,'delete_tiemposcrisis'),(97,'Can add seguridad',33,'add_seguridad'),(98,'Can change seguridad',33,'change_seguridad'),(99,'Can delete seguridad',33,'delete_seguridad');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$Z6rYZ1MYO77O$Y+2R8SYFnG66SSFGh/llMYjyzaxJT7cZ7M1V8GrZxQo=','2013-11-25 10:25:48',1,'crocha','','','carlos@simas.org',1,1,'2013-11-19 03:24:35');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=383 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-11-19 03:25:37',1,15,'1','ECOM',1,''),(2,'2013-11-19 03:25:49',1,15,'2','CISA',1,''),(3,'2013-11-19 03:26:05',1,15,'3','Banco Atlantida',1,''),(4,'2013-11-19 03:26:12',1,15,'4','SOPPEXCCA',1,''),(5,'2013-11-19 03:26:30',1,18,'1','Cooperativa',1,''),(6,'2013-11-19 03:26:50',1,18,'2','Asociación',1,''),(7,'2013-11-19 03:26:58',1,18,'3','Empresa',1,''),(8,'2013-11-19 03:27:06',1,18,'4','Grupo',1,''),(9,'2013-11-19 03:27:12',1,18,'5','Ninguno',1,''),(10,'2013-11-19 03:27:37',1,19,'1','Obtener crédito para la producción',1,''),(11,'2013-11-19 03:27:46',1,19,'2','Suministro de semilla',1,''),(12,'2013-11-19 03:27:59',1,19,'3','Tener servicio de asistencia técnica ',1,''),(13,'2013-11-19 03:28:08',1,19,'4','Tener servicio de capacitaciones',1,''),(14,'2013-11-19 03:28:20',1,19,'5','Fondos para retención de cosecha',1,''),(15,'2013-11-19 03:28:31',1,19,'6','Comercializar mejor y obtener mejor precio',1,''),(16,'2013-11-19 03:28:40',1,19,'7','Obtener mejores beneficios familiares',1,''),(17,'2013-11-19 03:28:52',1,19,'8','Proyectos sociales',1,''),(18,'2013-11-19 03:29:03',1,19,'9','Proyectos productivos',1,''),(19,'2013-11-19 03:29:18',1,20,'1','Corto plazo',1,''),(20,'2013-11-19 03:29:27',1,20,'2','Mediano plazo',1,''),(21,'2013-11-19 03:29:39',1,20,'3','Largo plazo',1,''),(22,'2013-11-19 03:29:58',1,21,'1','Empresa Ex',1,''),(23,'2013-11-19 03:30:09',1,21,'2','ONG',1,''),(24,'2013-11-19 03:30:17',1,21,'3','MF',1,''),(25,'2013-11-19 03:30:25',1,21,'4','Banco',1,''),(26,'2013-11-19 03:30:34',1,21,'5','Coop',1,''),(27,'2013-11-19 03:30:46',1,21,'6','PP',1,''),(28,'2013-11-19 03:31:18',1,23,'1','Viven en la finca',1,''),(29,'2013-11-19 03:31:29',1,23,'2','Viven en pueblo cerca de finca',1,''),(30,'2013-11-19 03:31:43',1,23,'3','Vive en ciudad lejos de la finca',1,''),(31,'2013-11-19 03:31:55',1,23,'4','Pasa tiempo en la finca y tiempo en casa',1,''),(32,'2013-11-19 03:32:22',1,25,'1','Electricidad',1,''),(33,'2013-11-19 03:32:35',1,25,'2','No hay',1,''),(34,'2013-11-19 03:32:48',1,25,'3','La red',1,''),(35,'2013-11-19 03:32:58',1,25,'4','Planta eléctrica',1,''),(36,'2013-11-19 03:33:08',1,25,'5','Panel Solar',1,''),(37,'2013-11-19 03:33:17',1,25,'6','Molino de viento',1,''),(38,'2013-11-19 03:33:29',1,25,'7','Candil',1,''),(39,'2013-11-19 03:33:38',1,25,'8','Combustible en la cocina',1,''),(40,'2013-11-19 03:33:51',1,25,'9','Gas',1,''),(41,'2013-11-19 03:34:02',1,25,'10','Leña de la finca',1,''),(42,'2013-11-19 03:34:11',1,25,'11','Leña comprada',1,''),(43,'2013-11-19 03:34:19',1,25,'12','Carbón',1,''),(44,'2013-11-19 03:35:13',1,26,'1','Gas',1,''),(45,'2013-11-19 03:35:24',1,26,'2','Leña de la finca',1,''),(46,'2013-11-19 03:35:37',1,26,'3','Leña comprada',1,''),(47,'2013-11-19 03:35:47',1,26,'4','Carbón',1,''),(48,'2013-11-19 03:36:10',1,27,'1','Río',1,''),(49,'2013-11-19 03:36:34',1,27,'2','Ojo de agua',1,''),(50,'2013-11-19 03:36:45',1,27,'3','Quebrada',1,''),(51,'2013-11-19 03:37:05',1,27,'4','Pozo comunitario',1,''),(52,'2013-11-19 03:37:17',1,27,'5','Pozo propio',1,''),(53,'2013-11-19 03:37:36',1,27,'6','Agua entubada',1,''),(54,'2013-11-19 03:38:36',1,25,'12','Carbón',3,''),(55,'2013-11-19 03:38:36',1,25,'11','Leña comprada',3,''),(56,'2013-11-19 03:38:36',1,25,'10','Leña de la finca',3,''),(57,'2013-11-19 03:38:36',1,25,'9','Gas',3,''),(58,'2013-11-19 03:38:36',1,25,'8','Combustible en la cocina',3,''),(59,'2013-11-19 03:40:19',1,30,'1','Poca tierra para producción de alimento',1,''),(60,'2013-11-19 03:40:36',1,30,'2','Falta de empleo o ingreso de la finca',1,''),(61,'2013-11-19 03:40:48',1,30,'3','Familia numerosa',1,''),(62,'2013-11-19 03:40:58',1,30,'4','Rendimientos de maíz y frijol bajos',1,''),(63,'2013-11-19 03:41:12',1,30,'5','Bajo producción de café',1,''),(64,'2013-11-19 03:41:21',1,30,'6','Bajo precio de café',1,''),(65,'2013-11-19 03:41:35',1,31,'1','Ene',1,''),(66,'2013-11-19 03:41:46',1,31,'2','Feb',1,''),(67,'2013-11-19 03:41:53',1,31,'3','Mar',1,''),(68,'2013-11-19 03:42:00',1,31,'4','Abr',1,''),(69,'2013-11-19 03:42:07',1,31,'5','May',1,''),(70,'2013-11-19 03:42:14',1,31,'6','Jun',1,''),(71,'2013-11-19 03:42:21',1,31,'7','Jul',1,''),(72,'2013-11-19 03:42:27',1,31,'8','Ago',1,''),(73,'2013-11-19 03:42:34',1,31,'9','Sep',1,''),(74,'2013-11-19 03:42:41',1,31,'10','Oct',1,''),(75,'2013-11-19 03:42:49',1,31,'11','Nov',1,''),(76,'2013-11-19 03:42:57',1,31,'12','Dic',1,''),(77,'2013-11-19 03:43:09',1,32,'1','Venta de Mano de obra',1,''),(78,'2013-11-19 03:43:18',1,32,'2','Venta de Ganado mayor',1,''),(79,'2013-11-19 03:43:27',1,32,'3','Venta de Ganado menor',1,''),(80,'2013-11-19 03:43:36',1,32,'4','Venta de equipo y herramienta',1,''),(81,'2013-11-19 03:43:48',1,32,'5','Venta de la tierra',1,''),(82,'2013-11-19 03:43:58',1,32,'6','Busco Préstamo',1,''),(83,'2013-11-19 03:44:08',1,32,'7','Prendo mi cosecha futura del café',1,''),(84,'2013-11-19 03:44:17',1,32,'8','Compra alimento fiado',1,''),(85,'2013-11-19 03:44:27',1,32,'9','Migró a otros lugares o países',1,''),(86,'2013-11-19 03:44:37',1,32,'10','Utilizó mi ahorros',1,''),(87,'2013-11-19 03:46:10',1,34,'1','Área total',1,''),(88,'2013-11-19 03:46:22',1,34,'2','Bosque',1,''),(89,'2013-11-19 03:46:34',1,34,'3','Tacotales',1,''),(90,'2013-11-19 03:46:45',1,34,'4','Cultivos anuales',1,''),(91,'2013-11-19 03:46:59',1,34,'5','Plantaciones  forestal',1,''),(92,'2013-11-19 03:47:08',1,34,'6','Áreas de pastos abierto',1,''),(93,'2013-11-19 03:47:20',1,34,'7','Áreas de pastos con árboles',1,''),(94,'2013-11-19 03:47:28',1,34,'8','Cultivos perennes',1,''),(95,'2013-11-19 03:47:44',1,35,'1','Enriquecimiento de los bosques',1,''),(96,'2013-11-19 03:47:54',1,35,'2','Protección de fuentes de agua',1,''),(97,'2013-11-19 03:48:07',1,35,'3','Establecimiento de cercas viva',1,''),(98,'2013-11-19 03:48:17',1,35,'4','Plantaciones forestales',1,''),(99,'2013-11-19 03:48:31',1,35,'5','Siembra de árboles en potrero',1,''),(100,'2013-11-19 03:48:40',1,35,'6','Siembra de árboles en cafetales',1,''),(101,'2013-11-19 03:48:50',1,35,'7','Establecimiento de viveros de árboles',1,''),(102,'2013-11-19 03:49:03',1,35,'8','Parcelas frutales',1,''),(103,'2013-11-19 03:49:12',1,35,'9','Huerto de Patio',1,''),(104,'2013-11-19 03:49:22',1,35,'10','Establecimiento de cultivo agroforestales',1,''),(105,'2013-11-19 03:49:42',1,36,'1','Vacas paridas',1,''),(106,'2013-11-19 03:49:52',1,36,'2','Vaca Seca',1,''),(107,'2013-11-19 03:49:59',1,36,'3','Vaquillas',1,''),(108,'2013-11-19 03:50:14',1,36,'4','Ternero de desarrollo',1,''),(109,'2013-11-19 03:50:22',1,36,'5','Novillos',1,''),(110,'2013-11-19 03:50:30',1,36,'6','Bueyes',1,''),(111,'2013-11-19 03:50:37',1,36,'7','Toros',1,''),(112,'2013-11-19 03:50:47',1,36,'8','Pelibuey',1,''),(113,'2013-11-19 03:50:55',1,36,'9','Cerdos',1,''),(114,'2013-11-19 03:51:05',1,36,'10','Aves de corral',1,''),(115,'2013-11-19 03:51:17',1,36,'11','Colmenas',1,''),(116,'2013-11-19 03:51:25',1,36,'12','Bestias',1,''),(117,'2013-11-19 03:51:47',1,37,'1','Arroz',1,''),(118,'2013-11-19 03:51:58',1,37,'2','Cacao',1,''),(119,'2013-11-19 03:52:13',1,37,'3','Café',1,''),(120,'2013-11-19 03:52:28',1,37,'4','Frijol',1,''),(121,'2013-11-19 03:52:45',1,37,'5','Guineo',1,''),(122,'2013-11-19 03:53:07',1,37,'6','Maíz',1,''),(123,'2013-11-19 03:53:21',1,37,'7','Malanga',1,''),(124,'2013-11-19 03:53:41',1,37,'8','Plátano',1,''),(125,'2013-11-19 03:53:52',1,37,'9','Quequisque',1,''),(126,'2013-11-19 03:54:02',1,37,'10','Yuca',1,''),(127,'2013-11-19 03:54:22',1,37,'11','Tomate',1,''),(128,'2013-11-19 03:54:55',1,37,'12','Repollo',1,''),(129,'2013-11-19 03:56:01',1,38,'1','Mango',1,''),(130,'2013-11-19 03:56:16',1,38,'2','Pejibeye',1,''),(131,'2013-11-19 03:56:29',1,38,'3','Aguacate',1,''),(132,'2013-11-19 03:56:49',1,38,'4','Citricos',1,''),(133,'2013-11-19 03:57:27',1,38,'3','Aguacate',2,'Modificado/a unidad.'),(134,'2013-11-19 04:00:11',1,39,'1','Arroz',1,''),(135,'2013-11-19 04:00:29',1,39,'2','Aves',1,''),(136,'2013-11-19 04:00:45',1,39,'3','Cacao',1,''),(137,'2013-11-19 04:00:59',1,39,'4','Café',1,''),(138,'2013-11-19 04:01:19',1,39,'5','Cuajada',1,''),(139,'2013-11-19 04:01:33',1,39,'6','Frijol',1,''),(140,'2013-11-19 04:01:45',1,39,'7','Guineo',1,''),(141,'2013-11-19 04:01:59',1,39,'8','Huevos',1,''),(142,'2013-11-19 04:02:15',1,39,'9','Leche',1,''),(143,'2013-11-19 04:02:36',1,39,'10','Maíz',1,''),(144,'2013-11-19 04:02:53',1,39,'11','Malanga',1,''),(145,'2013-11-19 04:03:14',1,39,'12','Mango',1,''),(146,'2013-11-19 04:03:30',1,39,'13','Naranja',1,''),(147,'2013-11-19 04:03:51',1,39,'14','Plátano',1,''),(148,'2013-11-19 04:04:02',1,39,'15','Quequisque',1,''),(149,'2013-11-19 04:04:15',1,39,'16','Queso',1,''),(150,'2013-11-19 04:04:29',1,39,'17','Ternero en desarrollo',1,''),(151,'2013-11-19 04:04:42',1,39,'18','Vaca',1,''),(152,'2013-11-19 04:04:53',1,39,'19','Yuca',1,''),(153,'2013-11-19 04:05:05',1,39,'20','Gallina',1,''),(154,'2013-11-19 04:05:23',1,39,'21','Leña',1,''),(155,'2013-11-19 04:05:45',1,39,'22','Madera aserrada',1,''),(156,'2013-11-19 04:06:02',1,39,'23','Crema',1,''),(157,'2013-11-19 04:06:32',1,39,'24','Cerdos',1,''),(158,'2013-11-19 04:06:53',1,39,'25','Pejibaye',1,''),(159,'2013-11-19 04:07:05',1,39,'26','Tomate',1,''),(160,'2013-11-19 04:07:17',1,39,'27','Repollo',1,''),(161,'2013-11-19 04:07:40',1,40,'1','Salarios',1,''),(162,'2013-11-19 04:07:48',1,40,'2','Negocios',1,''),(163,'2013-11-19 04:07:58',1,40,'3','Remesas',1,''),(164,'2013-11-19 04:08:07',1,40,'4','Alquiler',1,''),(165,'2013-11-19 04:08:28',1,41,'1','Area total de café',1,''),(166,'2013-11-19 04:08:39',1,41,'2','AREA EN RENOVACION',1,''),(167,'2013-11-19 04:08:47',1,41,'3','Area de café en desarrollo',1,''),(168,'2013-11-19 04:08:58',1,41,'4','Area de café en producción',1,''),(169,'2013-11-19 04:09:07',1,41,'5','Areá de café en recepo',1,''),(170,'2013-11-19 04:09:17',1,41,'6','Producción total de la finca en qq pergamino SECO',1,''),(171,'2013-11-19 04:09:30',1,41,'7','Producción total de finca en qq oro',1,''),(172,'2013-11-19 04:09:53',1,42,'1','C',1,''),(173,'2013-11-19 04:10:02',1,42,'2','CT',1,''),(174,'2013-11-19 04:10:10',1,42,'3','CM',1,''),(175,'2013-11-19 04:10:19',1,42,'4','B',1,''),(176,'2013-11-19 04:10:30',1,42,'5','P',1,''),(177,'2013-11-19 04:10:39',1,42,'6','H',1,''),(178,'2013-11-19 04:11:35',1,43,'1','Seleccion CATURRA',1,''),(179,'2013-11-19 04:11:48',1,43,'2','Lineas de CATIMORES',1,''),(180,'2013-11-19 04:12:00',1,43,'3','Hibridas',1,''),(181,'2013-11-19 04:12:08',1,43,'4','OTRAS',1,''),(182,'2013-11-19 04:12:31',1,44,'1','La misma finca',1,''),(183,'2013-11-19 04:12:43',1,44,'2','Fincas vecinas',1,''),(184,'2013-11-19 04:12:57',1,44,'3','Vivero Cooperativa',1,''),(185,'2013-11-19 04:13:07',1,44,'4','Vivero Empresa',1,''),(186,'2013-11-19 04:13:55',1,45,'1','Precio de la planta',1,''),(187,'2013-11-19 04:14:04',1,45,'2','Recomendaciones',1,''),(188,'2013-11-19 04:14:14',1,45,'3','Experiencia',1,''),(189,'2013-11-19 04:14:22',1,45,'4','Disponibilidad',1,''),(190,'2013-11-19 04:14:34',1,46,'1','La altitud',1,''),(191,'2013-11-19 04:14:43',1,46,'2','El clima',1,''),(192,'2013-11-19 04:14:51',1,46,'3','El rendimiento',1,''),(193,'2013-11-19 04:15:00',1,46,'4','Calidad de grano',1,''),(194,'2013-11-19 04:15:08',1,46,'5','Resistencia a enfermedades',1,''),(195,'2013-11-19 04:15:16',1,46,'6','La calidad de la taza',1,''),(196,'2013-11-19 04:15:47',1,47,'1','B',1,''),(197,'2013-11-19 04:15:59',1,47,'2','R',1,''),(198,'2013-11-19 04:16:08',1,47,'3','M',1,''),(199,'2013-11-19 04:16:17',1,47,'4','T',1,''),(200,'2013-11-19 04:16:26',1,47,'5','V',1,''),(201,'2013-11-19 04:16:34',1,47,'6','A',1,''),(202,'2013-11-19 04:16:43',1,47,'7','N',1,''),(203,'2013-11-19 04:17:27',1,48,'1','Fungicidas',1,''),(204,'2013-11-19 04:17:38',1,48,'2','Insecticidas',1,''),(205,'2013-11-19 04:17:48',1,48,'3','Herbicidas',1,''),(206,'2013-11-19 04:17:56',1,48,'4','Nematicidas',1,''),(207,'2013-11-19 04:18:06',1,48,'5','Fertilizantes en suelo',1,''),(208,'2013-11-19 04:18:18',1,48,'6','Abono orgánico',1,''),(209,'2013-11-19 04:18:27',1,48,'7','Fertilizantes foliares',1,''),(210,'2013-11-19 04:18:56',1,49,'1','Biofertilzantes',1,''),(211,'2013-11-19 04:19:06',1,49,'2','Compost',1,''),(212,'2013-11-19 04:19:15',1,49,'3','Roca Minerales',1,''),(213,'2013-11-19 04:19:26',1,49,'4','Insecticida natural',1,''),(214,'2013-11-19 04:19:36',1,49,'5','Fungicida natural',1,''),(215,'2013-11-19 04:19:47',1,49,'6','Cerca viva ',1,''),(216,'2013-11-19 04:19:55',1,49,'7','Cortina rompe viento',1,''),(217,'2013-11-19 04:20:05',1,49,'8','Abonos verdes',1,''),(218,'2013-11-19 04:20:13',1,49,'9','Siembra en Curva a nivel',1,''),(219,'2013-11-19 04:20:29',1,49,'10','Acequia',1,''),(220,'2013-11-19 04:20:41',1,49,'11','Barrera viva',1,''),(221,'2013-11-19 04:20:52',1,49,'12','Barrera muerta',1,''),(222,'2013-11-19 04:21:01',1,49,'13','Cosecha de agua',1,''),(223,'2013-11-19 04:21:38',1,49,'14','Cultivo asociado',1,''),(224,'2013-11-19 04:21:51',1,49,'15','Incorporación de rastrojo',1,''),(225,'2013-11-19 04:22:03',1,49,'16','Manejo selectivo de malas hierbas',1,''),(226,'2013-11-19 04:22:13',1,49,'17','Siembra de coberturas',1,''),(227,'2013-11-19 04:22:28',1,49,'18','Uso de trampa para la broca',1,''),(228,'2013-11-19 04:22:41',1,49,'19','Uso de Beauveria bassiana para broca',1,''),(229,'2013-11-19 04:22:51',1,49,'20','Siembra de plantas injertadas',1,''),(230,'2013-11-19 04:23:00',1,49,'21','Diversificación de los cafetales',1,''),(231,'2013-11-19 04:25:14',1,50,'1','Alta temperatura que daño las plantas y cosecha',1,''),(232,'2013-11-19 04:25:25',1,50,'2','Baja temperatura que daño las plantas y cosecha',1,''),(233,'2013-11-19 04:25:39',1,50,'3','Exceso de lluvia que daño las plantas y cosecha',1,''),(234,'2013-11-19 04:25:51',1,50,'4','Inundaciones que daño las plantas y cosecha',1,''),(235,'2013-11-19 04:26:00',1,50,'5','Falta de lluvia que daño las plantas y cosecha',1,''),(236,'2013-11-19 04:26:12',1,50,'6','Vientos muy fuertes que daño las plantas',1,''),(237,'2013-11-19 04:26:23',1,50,'7','Deslizamiento de tierra que daño los plantíos',1,''),(238,'2013-11-19 04:26:33',1,50,'8','El clima se descontrolo para hacer un buen manejo',1,''),(239,'2013-11-19 04:26:42',1,50,'9','El clima se descontrolo para hacer un buen corte',1,''),(240,'2013-11-19 04:26:53',1,50,'10','Hubo demasiada humedad que afecto las plantas y cosecha',1,''),(241,'2013-11-19 04:27:03',1,50,'11','Hubo poca humedad y afecto las plantas y cosecha',1,''),(242,'2013-11-19 04:27:34',1,51,'1','2013',1,''),(243,'2013-11-19 04:27:44',1,51,'2','2012',1,''),(244,'2013-11-19 04:28:09',1,51,'3','2011',1,''),(245,'2013-11-19 04:28:16',1,51,'4','2010',1,''),(246,'2013-11-19 04:28:23',1,51,'5','2009',1,''),(247,'2013-11-19 04:31:07',1,52,'1','A',1,''),(248,'2013-11-19 04:31:23',1,52,'2','M',1,''),(249,'2013-11-19 04:31:33',1,52,'3','B',1,''),(250,'2013-11-19 04:31:45',1,52,'4','T',1,''),(251,'2013-11-19 04:31:57',1,52,'5','V',1,''),(252,'2013-11-19 04:32:07',1,52,'6','A',1,''),(253,'2013-11-19 04:32:15',1,52,'7','N',1,''),(254,'2013-11-19 04:33:16',1,54,'1','Aspectos agrícolas',1,''),(255,'2013-11-19 04:33:28',1,53,'1','Aspectos agrícolas - Las variedades no son adecuada',1,''),(256,'2013-11-19 04:33:43',1,53,'2','Aspectos agrícolas - Hay Falta de semilla',1,''),(257,'2013-11-19 04:33:56',1,53,'3','Aspectos agrícolas - Las semillas con de mala calidad',1,''),(258,'2013-11-19 04:34:10',1,53,'4','Aspectos agrícolas - Manejo de cultivo no adecuado',1,''),(259,'2013-11-19 04:34:20',1,53,'5','Aspectos agrícolas - Fertilización no adecuada',1,''),(260,'2013-11-19 04:34:33',1,53,'6','Aspectos agrícolas - Muchos daños de plagas y enfermedades',1,''),(261,'2013-11-19 04:34:48',1,54,'2','Aspectos productivos',1,''),(262,'2013-11-19 04:35:03',1,53,'7','Aspectos productivos - Producción de café baja',1,''),(263,'2013-11-19 04:35:37',1,53,'8','Aspectos productivos - Poca floración',1,''),(264,'2013-11-19 04:36:05',1,53,'9','Aspectos productivos - Mucho abono',1,''),(265,'2013-11-19 04:37:48',1,53,'10','Aspectos productivos - Mucha caída de frutos',1,''),(266,'2013-11-19 04:39:05',1,53,'11','Aspectos productivos - Marcada bianualidad',1,''),(267,'2013-11-19 04:39:18',1,53,'12','Aspectos productivos - Mala recolección de frutos',1,''),(268,'2013-11-19 04:39:29',1,53,'13','Aspectos productivos - Falta de mano de obra para el  corte',1,''),(269,'2013-11-19 04:39:40',1,53,'14','Aspectos productivos - Beneficiado húmedo no adecuado',1,''),(270,'2013-11-19 04:39:54',1,54,'3','Aspectos  del mercado',1,''),(271,'2013-11-19 04:40:06',1,53,'15','Aspectos  del mercado - Bajo precio de café',1,''),(272,'2013-11-19 04:40:22',1,53,'16','Aspectos  del mercado - Falta de venta',1,''),(273,'2013-11-19 04:40:33',1,53,'17','Aspectos  del mercado - Estafa de contrato',1,''),(274,'2013-11-19 04:40:44',1,53,'18','Aspectos  del mercado - Mala calidad de café',1,''),(275,'2013-11-19 04:40:55',1,53,'19','Aspectos  del mercado - Pagos atrasados',1,''),(276,'2013-11-19 04:41:08',1,53,'20','Aspectos  del mercado - Problema de traslado de cosecha',1,''),(277,'2013-11-19 04:41:23',1,54,'4','Aspectos de financiamiento',1,''),(278,'2013-11-19 04:41:36',1,53,'21','Aspectos de financiamiento - Disponibilidad de crédito de corto plazo',1,''),(279,'2013-11-19 04:42:48',1,53,'22','Aspectos de financiamiento - Disponibilidad de crédito mediano plazo',1,''),(280,'2013-11-19 04:43:02',1,53,'23','Aspectos de financiamiento - Disponibilidad de crédito largo plazo',1,''),(281,'2013-11-19 04:43:13',1,53,'24','Aspectos de financiamiento - Altos interés de los crédito',1,''),(282,'2013-11-19 04:43:24',1,55,'1','Siempre',1,''),(283,'2013-11-19 04:43:34',1,55,'2','A veces',1,''),(284,'2013-11-19 04:44:24',1,55,'3','Nunca',1,''),(285,'2013-11-19 04:44:38',1,55,'4','Si',1,''),(286,'2013-11-19 04:44:43',1,55,'5','No',1,''),(287,'2013-11-19 04:48:24',1,56,'1','Área total de café en producción mz',1,''),(288,'2013-11-19 04:49:43',1,56,'2','Área de café altamente afectada por roya  (más de 30% de plantas)',1,''),(289,'2013-11-19 04:52:11',1,56,'3','Área  de café medianamente afectada por roya  (entre 10-30% plantas afectadas)',1,''),(290,'2013-11-19 04:52:21',1,56,'4','Área rea de café altamente afectada por roya  (menos de 10% plantas afectadas)',1,''),(291,'2013-11-19 04:52:33',1,56,'5','% reducción de la cosecha por la roya del café',1,''),(292,'2013-11-19 04:52:44',1,56,'6','Área totalmente pérdida y que tenía que renovar',1,''),(293,'2013-11-19 05:01:20',1,57,'1','Otros productores',1,''),(294,'2013-11-19 05:01:31',1,57,'2','Técnico de la cooperativa o asociación',1,''),(295,'2013-11-19 05:01:43',1,57,'3','Directivo de cooperativa',1,''),(296,'2013-11-19 05:01:57',1,57,'4','Vendedor de Agroquímicos',1,''),(297,'2013-11-19 05:02:22',1,57,'5','Técnicos de la empresas comercializadora',1,''),(298,'2013-11-19 05:02:33',1,57,'6','Otros',1,''),(299,'2013-11-19 05:21:45',1,58,'1','Variedades de café',1,''),(300,'2013-11-19 05:21:57',1,58,'2','Manejo de  semillero y vivero',1,''),(301,'2013-11-19 05:22:06',1,58,'3','Establecimiento y manejo de café',1,''),(302,'2013-11-19 05:22:15',1,58,'4','Manejo de cosecha de café',1,''),(303,'2013-11-19 05:22:25',1,58,'5','Manejo de plagas y enfermedades de café',1,''),(304,'2013-11-19 05:22:37',1,58,'6','Manejo de roya del café',1,''),(305,'2013-11-19 05:22:55',1,58,'7','Planificación de la finca',1,''),(306,'2013-11-19 05:23:06',1,58,'8','Diversificación de la fina y cafetales',1,''),(307,'2013-11-19 05:23:18',1,59,'1','Ch',1,''),(308,'2013-11-19 05:23:27',1,59,'2','VF',1,''),(309,'2013-11-19 05:23:40',1,59,'3','G',1,''),(310,'2013-11-19 05:23:47',1,59,'4','Pr',1,''),(311,'2013-11-19 05:27:23',1,60,'2','Contabilidad básica y administración',1,''),(312,'2013-11-19 05:27:33',1,60,'3','Manejo de créditos',1,''),(313,'2013-11-19 05:27:44',1,60,'4','Administración de pequeños negocios',1,''),(314,'2013-11-19 05:27:53',1,60,'5','Gestión empresarial',1,''),(315,'2013-11-19 05:28:05',1,60,'6','Registro de datos de la finca',1,''),(316,'2013-11-19 05:28:14',1,60,'7','Certificación de cafe',1,''),(317,'2013-11-19 05:28:46',1,61,'1','Org',1,''),(318,'2013-11-19 05:28:53',1,61,'2','Quim',1,''),(319,'2013-11-19 05:29:04',1,61,'3','Quim+Org',1,''),(320,'2013-11-19 05:29:13',1,61,'4','Biof',1,''),(321,'2013-11-19 05:29:20',1,61,'5','RM',1,''),(322,'2013-11-19 05:29:38',1,62,'1','Q Prev',1,''),(323,'2013-11-19 05:29:49',1,62,'2','Q Sist',1,''),(324,'2013-11-19 05:30:01',1,62,'3','Orgánico',1,''),(325,'2013-11-23 20:32:57',1,16,'1','Falguni Guharay',1,''),(326,'2013-11-23 20:33:23',1,13,'1','Luciano López Blandón',1,''),(327,'2013-11-23 20:35:51',1,14,'1','Luciano López Blandón',1,''),(328,'2013-11-23 20:36:12',1,8,'1','Nicaragua',1,''),(329,'2013-11-23 20:36:53',1,9,'1','Nueva Segovia',1,''),(330,'2013-11-23 20:37:22',1,10,'0','Nueva Segovia - Dipilto',1,''),(331,'2013-11-23 20:37:38',1,11,'1','Volcán',1,''),(332,'2013-11-23 20:41:54',1,19,'10','Ninguno',1,''),(333,'2013-11-23 20:42:18',1,17,'1','Luciano López Blandón',1,''),(334,'2013-11-23 20:50:13',1,63,'1','Sinai',1,''),(335,'2013-11-23 20:53:50',1,63,'2','Lote',1,''),(336,'2013-11-23 20:55:22',1,42,'7','No hay',1,''),(337,'2013-11-23 21:05:08',1,31,'13','No aplica',1,''),(338,'2013-11-23 21:05:38',1,64,'1','Topacio',1,''),(339,'2013-11-23 21:06:30',1,64,'2','Fungomac',1,''),(340,'2013-11-23 21:07:10',1,64,'3','Glifosato',1,''),(341,'2013-11-23 21:08:18',1,64,'4','Gramoxone',1,''),(342,'2013-11-23 21:08:41',1,31,'14','No aplico',1,''),(343,'2013-11-23 21:09:25',1,64,'5','8-5-10',1,''),(344,'2013-11-23 21:10:10',1,64,'6','20-20-20',1,''),(345,'2013-11-23 21:10:34',1,17,'1','Luciano López Blandón',2,'Añadido/a \"Luciano López Blandón\" composicion. Añadido/a \"None\" servicios basicos. Añadido/a \"None\" tenecia. Añadido/a \"None\" seguridad. Añadido/a \"UsoTierra object\" uso tierra. Añadido/a \"UsoTierra object\" uso tierra. Añadido/a \"Siembra de árboles en cafetales\" reforestacion. Añadido/a \"None\" area cafe. Añadido/a \"None\" area cafe. Añadido/a \"None\" area cafe. Añadido/a \"None\" area cafe. Añadido/a \"None\" area cafe. Añadido/a \"None\" variedad edad roya. Añadido/a \"None\" variedad edad roya. Añadido/a \"None\" produccion vivero. Añadido/a \"None\" manejo cafetales. Añadido/a \"None\" meses manejo cafe. Añadido/a \"None\" uso insumos. Añadido/a \"None\" uso insumos. Añadido/a \"None\" uso insumos. Añadido/a \"None\" uso insumos. Añadido/a \"None\" uso insumos.'),(346,'2013-11-23 21:16:31',1,73,'1','Beneficio Balladares',1,''),(347,'2013-11-23 21:16:49',1,74,'1','Tasa de Excelencia',1,''),(348,'2013-11-23 21:32:24',1,17,'1','Luciano López Blandón',2,'Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" uso opciones agroecologica. Añadido/a \"None\" beneficiado. Añadido/a \"None\" comercializacion. Añadido/a \"None\" comercializacion. Añadido/a \"None\" comercializacion. Añadido/a \"None\" credito. Añadido/a \"None\" credito. Añadido/a \"None\" credito. Añadido/a \"None\" 4.1 El Clima. Añadido/a \"None\" 4.1 El Clima. Añadido/a \"None\" 4.1 El Clima. Añadido/a \"None\" 4.2 El suelo y fertilidad.'),(349,'2013-11-23 21:33:22',1,52,'7','Ningún plantio',2,'Modificado/a nombre.'),(350,'2013-11-23 21:33:44',1,52,'6','Algunos plantios',2,'Modificado/a nombre.'),(351,'2013-11-23 21:33:57',1,52,'5','Varios Plantios',2,'Modificado/a nombre.'),(352,'2013-11-23 21:34:09',1,52,'4','Todos los plations',2,'Modificado/a nombre.'),(353,'2013-11-23 21:34:27',1,52,'3','Baja incidencia',2,'Modificado/a nombre.'),(354,'2013-11-23 21:34:37',1,52,'2','Media incidencia',2,'Modificado/a nombre.'),(355,'2013-11-23 21:34:46',1,52,'1','Alta incidencia',2,'Modificado/a nombre.'),(356,'2013-11-23 21:48:37',1,17,'1','Luciano López Blandón',2,'Añadido/a \"None\" 4.3. Las plagas. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"OtroRiesgos object\" otro riesgos. Añadido/a \"None\" 4.5 Mitigación de los riesgos . Añadido/a \"None\" impacto roya. Añadido/a \"None\" impacto roya. Añadido/a \"None\" impacto roya. Añadido/a \"None\" impacto roya. Añadido/a \"None\" impacto roya.'),(357,'2013-11-23 21:49:50',1,56,'5','Reducción de la cosecha por la roya en qq pergamino comparado con cosecha de tres años',2,'Modificado/a nombre.'),(358,'2013-11-23 22:00:44',1,85,'1','Poda Sanitaria',1,''),(359,'2013-11-23 22:01:06',1,85,'2','Poda Selectiva',1,''),(360,'2013-11-23 22:01:20',1,85,'3','Poda Selectiva',1,''),(361,'2013-11-23 22:02:04',1,86,'1','Caturra',1,''),(362,'2013-11-23 22:02:13',1,86,'2','Catimor',1,''),(363,'2013-11-23 22:02:38',1,87,'1','30% regulada Guaba',1,''),(364,'2013-11-23 22:03:31',1,87,'2','30% Regulada Guaba',1,''),(365,'2013-11-23 22:05:00',1,88,'1','15-15-15',1,''),(366,'2013-11-23 22:05:11',1,88,'2','8-5-10',1,''),(367,'2013-11-23 22:05:39',1,89,'1','Alto 10',1,''),(368,'2013-11-23 22:05:46',1,89,'2','Topacio',1,''),(369,'2013-11-23 22:06:42',1,90,'1','Topacio',1,''),(370,'2013-11-23 22:07:03',1,90,'2','Fungomac',1,''),(371,'2013-11-23 22:08:10',1,91,'1','Caturra',1,''),(372,'2013-11-23 22:08:18',1,91,'2','Pacamara',1,''),(373,'2013-11-23 22:08:29',1,91,'3','Catimor',1,''),(374,'2013-11-23 22:08:54',1,92,'1','No aplica',1,''),(375,'2013-11-23 22:09:19',1,93,'1','Mejor manejo de café',1,''),(376,'2013-11-23 22:09:31',1,94,'1','No aplica',1,''),(377,'2013-11-23 22:14:27',1,17,'1','Luciano López Blandón',2,'Añadido/a \"None\" poda cafetos. Añadido/a \"None\" renovacion cafetales. Añadido/a \"None\" manejo sombra. Añadido/a \"None\" manejo fertilizacion. Añadido/a \"None\" aplicacion fungicida. Añadido/a \"None\" oriento. Añadido/a \"None\" nuevos productos. Añadido/a \"None\" nuevos productos. Añadido/a \"None\" nivel finca. Añadido/a \"None\" si le gusta.'),(378,'2013-11-23 22:15:25',1,104,'1','Sinai',1,''),(379,'2013-11-23 22:19:38',1,104,'2','Lote',1,''),(380,'2013-11-23 22:20:38',1,17,'1','Luciano López Blandón',2,'Añadido/a \"None\" detalle incidencia roya. Añadido/a \"None\" detalle incidencia roya.'),(381,'2013-11-23 22:42:47',1,17,'1','Luciano López Blandón',2,'Modificados doce, trece y catorce para \"None\" impacto roya.'),(382,'2013-11-23 22:43:43',1,56,'5','% reducción de la cosecha en comparación con año base 2011-12',2,'Modificado/a nombre.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=106 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'Pais','lugar','pais'),(9,'departamento','lugar','departamento'),(10,'municipio','lugar','municipio'),(11,'comunidad','lugar','comunidad'),(12,'migration history','south','migrationhistory'),(13,'Entrevistado','encuesta','entrevistado'),(14,'Dueño Finca','encuesta','duenofinca'),(15,'Organizacion','encuesta','organizacion'),(16,'recolector','encuesta','recolector'),(17,'encuesta','encuesta','encuesta'),(18,'socio organizacion','encuesta','socioorganizacion'),(19,'Beneficio','encuesta','beneficios'),(20,'credito','encuesta','creditoe'),(21,'Organizaciones que dan credito','encuesta','dequien'),(22,'quien financia','encuesta','quienfinancia'),(23,'vive familia','encuesta','vivefamilia'),(24,'composicion','encuesta','composicion'),(25,'EnergiaFinca','encuesta','energiafinca'),(26,'Combustible en la cocina','encuesta','combustible'),(27,'Disponibilidad de agua en la finca','encuesta','aguafinca'),(28,'servicios basicos','encuesta','serviciosbasicos'),(29,'tenecia','encuesta','tenecia'),(30,'necesidad alimento','encuesta','necesidadalimento'),(31,'meses','encuesta','meses'),(32,'tiempos crisis','encuesta','tiemposcrisis'),(33,'seguridad','encuesta','seguridad'),(34,'uso','produccion_finca','uso'),(35,'actividad','produccion_finca','actividad'),(36,'animales','produccion_finca','animales'),(37,'productos','produccion_finca','productos'),(38,'productos patio','produccion_finca','productospatio'),(39,'rubros','produccion_finca','rubros'),(40,'fuentes','produccion_finca','fuentes'),(41,'estado actual','produccion_cafe_finca','estadoactual'),(42,'Variedad','produccion_cafe_finca','variedades'),(43,'resistente roya','produccion_cafe_finca','resistenteroya'),(44,'semilla','produccion_cafe_finca','semilla'),(45,'decide sembrar','produccion_cafe_finca','decidesembrar'),(46,'criterios','produccion_cafe_finca','criterios'),(47,'Manejos','produccion_cafe_finca','manejos'),(48,'tipos insumos','produccion_cafe_finca','tiposinsumos'),(49,'Opciones','produccion_cafe_finca','opciones'),(50,'Tipo Clima','vulnerabilidades_finca','tipoclima'),(51,'Tipo Clima','vulnerabilidades_finca','tipoyear'),(52,'Plagas','vulnerabilidades_finca','plagas'),(53,'opciones','vulnerabilidades_finca','opciones'),(54,'causa','vulnerabilidades_finca','causa'),(55,'respuestas','vulnerabilidades_finca','respuestas'),(56,'impactos','roya','impactos'),(57,'combatir','roya','combatir'),(58,'tipo capacitaciones','roya','tipocapacitaciones'),(59,'metodologia','roya','metodologia'),(60,'temas sociales','roya','temassociales'),(61,'tipo fertilizacion','roya','tipofertilizacion'),(62,'tipo fungicida','roya','tipofungicida'),(63,'Plantio','produccion_cafe_finca','plantio'),(64,'Nombre Tipos','produccion_cafe_finca','nombretipos'),(65,'uso tierra','produccion_finca','usotierra'),(66,'reforestacion','produccion_finca','reforestacion'),(67,'area cafe','produccion_cafe_finca','areacafe'),(68,'variedad edad roya','produccion_cafe_finca','variedadedadroya'),(69,'produccion vivero','produccion_cafe_finca','produccionvivero'),(70,'manejo cafetales','produccion_cafe_finca','manejocafetales'),(71,'meses manejo cafe','produccion_cafe_finca','mesesmanejocafe'),(72,'uso insumos','produccion_cafe_finca','usoinsumos'),(73,'beneficio seco','produccion_cafe_finca','beneficioseco'),(74,'calidad cafe','produccion_cafe_finca','calidadcafe'),(75,'uso opciones agroecologica','produccion_cafe_finca','usoopcionesagroecologica'),(76,'beneficiado','produccion_cafe_finca','beneficiado'),(77,'comercializacion','produccion_cafe_finca','comercializacion'),(78,'credito','produccion_cafe_finca','credito'),(79,'4.1 El Clima','vulnerabilidades_finca','elclima'),(80,'4.2 El suelo y fertilidad','vulnerabilidades_finca','suelofertilidad'),(81,'4.3. Las plagas','vulnerabilidades_finca','lasplagas'),(82,'otro riesgos','vulnerabilidades_finca','otroriesgos'),(83,'4.5 Mitigación de los riesgos ','vulnerabilidades_finca','mitigacion'),(84,'impacto roya','roya','impactoroya'),(85,'tipo cafetos','roya','tipocafetos'),(86,'tipo variedad','roya','tipovariedad'),(87,'tipo sombra','roya','tiposombra'),(88,'fertilizacion','roya','fertilizacion'),(89,'tipo aplicacion fungicida','roya','tipoaplicacionfungicida'),(90,'productos','roya','productos'),(91,'variedades','roya','variedades'),(92,'igual','roya','igual'),(93,'mas','roya','mas'),(94,'menos','roya','menos'),(95,'poda cafetos','roya','podacafetos'),(96,'renovacion cafetales','roya','renovacioncafetales'),(97,'manejo sombra','roya','manejosombra'),(98,'manejo fertilizacion','roya','manejofertilizacion'),(99,'aplicacion fungicida','roya','aplicacionfungicida'),(100,'oriento','roya','oriento'),(101,'nuevos productos','roya','nuevosproductos'),(102,'nivel finca','roya','nivelfinca'),(103,'si le gusta','roya','silegusta'),(104,'Plantio','roya','plantio'),(105,'detalle incidencia roya','roya','detalleincidenciaroya');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('e0nqv3643i3all1m6zpp2vk9pgupbsqs','NmI2ZmIyNDZlMGViY2JmYThlNTI1NDRhZTliZDZhYTI3YWRmZjgwOTqAAn1xAS4=','2013-12-05 22:38:20'),('ii20g43p1io9qni3lvyjb53iies7uffy','NTQwZjdhMmVhYzAwOGI0OTk4ZTJmOTEzMmZmM2Y1MGVlMDUzYmI3ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-12-03 05:32:17'),('6ylrff7bq9nesgsovcoefyl3w00kovju','NTQwZjdhMmVhYzAwOGI0OTk4ZTJmOTEzMmZmM2Y1MGVlMDUzYmI3ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-12-06 00:55:30'),('f512tmyhe8hjz4m8gxlzq1k01wsh16fr','NTQwZjdhMmVhYzAwOGI0OTk4ZTJmOTEzMmZmM2Y1MGVlMDUzYmI3ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-12-09 10:25:48'),('vt06cetaun6enu87cemhsockni5xotaz','NmI2ZmIyNDZlMGViY2JmYThlNTI1NDRhZTliZDZhYTI3YWRmZjgwOTqAAn1xAS4=','2013-12-07 22:50:10'),('2tvlg2ueg56pndmjwcnplyr09zgw2zug','YWIxZjkwY2JkZmNmOWRlMzQ3ZjE4ZGIwNDFkMTU4YzEyOGJmYjYyNjqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-12-08 15:47:04'),('gugddaxch436jvk7efl2fy2dk2eolcmc','NmI2ZmIyNDZlMGViY2JmYThlNTI1NDRhZTliZDZhYTI3YWRmZjgwOTqAAn1xAS4=','2013-12-08 17:51:00');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_aguafinca`
--

DROP TABLE IF EXISTS `encuesta_aguafinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_aguafinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_aguafinca`
--

LOCK TABLES `encuesta_aguafinca` WRITE;
/*!40000 ALTER TABLE `encuesta_aguafinca` DISABLE KEYS */;
INSERT INTO `encuesta_aguafinca` VALUES (1,'Río'),(2,'Ojo de agua'),(3,'Quebrada'),(4,'Pozo comunitario'),(5,'Pozo propio'),(6,'Agua entubada');
/*!40000 ALTER TABLE `encuesta_aguafinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_beneficios`
--

DROP TABLE IF EXISTS `encuesta_beneficios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_beneficios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_beneficios`
--

LOCK TABLES `encuesta_beneficios` WRITE;
/*!40000 ALTER TABLE `encuesta_beneficios` DISABLE KEYS */;
INSERT INTO `encuesta_beneficios` VALUES (1,'Obtener crédito para la producción'),(2,'Suministro de semilla'),(3,'Tener servicio de asistencia técnica '),(4,'Tener servicio de capacitaciones'),(5,'Fondos para retención de cosecha'),(6,'Comercializar mejor y obtener mejor precio'),(7,'Obtener mejores beneficios familiares'),(8,'Proyectos sociales'),(9,'Proyectos productivos'),(10,'Ninguno');
/*!40000 ALTER TABLE `encuesta_beneficios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_combustible`
--

DROP TABLE IF EXISTS `encuesta_combustible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_combustible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_combustible`
--

LOCK TABLES `encuesta_combustible` WRITE;
/*!40000 ALTER TABLE `encuesta_combustible` DISABLE KEYS */;
INSERT INTO `encuesta_combustible` VALUES (1,'Gas'),(2,'Leña de la finca'),(3,'Leña comprada'),(4,'Carbón');
/*!40000 ALTER TABLE `encuesta_combustible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_composicion`
--

DROP TABLE IF EXISTS `encuesta_composicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_composicion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adultos` int(11) NOT NULL,
  `adultas` int(11) NOT NULL,
  `jovenes_varones` int(11) NOT NULL,
  `jovenes_mujeres` int(11) NOT NULL,
  `ninos` int(11) NOT NULL,
  `ninas` int(11) NOT NULL,
  `permanente_hombres` int(11) NOT NULL,
  `permanente_mujeres` int(11) NOT NULL,
  `temporales_hombres` int(11) NOT NULL,
  `temporales_mujeres` int(11) NOT NULL,
  `tecnico_hombres` int(11) NOT NULL,
  `tecnico_mujeres` int(11) NOT NULL,
  `relacion_finca_vivienda_id` int(11) NOT NULL,
  `educacion_dueno` int(11) NOT NULL,
  `educacion_maxima_hombre` int(11) NOT NULL,
  `educacion_maxima_mujeres` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_composicion_748c8f3d` (`relacion_finca_vivienda_id`),
  KEY `encuesta_composicion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_composicion`
--

LOCK TABLES `encuesta_composicion` WRITE;
/*!40000 ALTER TABLE `encuesta_composicion` DISABLE KEYS */;
INSERT INTO `encuesta_composicion` VALUES (1,2,2,1,0,0,0,0,0,3,3,0,0,1,2,4,4,1);
/*!40000 ALTER TABLE `encuesta_composicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_creditoe`
--

DROP TABLE IF EXISTS `encuesta_creditoe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_creditoe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_creditoe`
--

LOCK TABLES `encuesta_creditoe` WRITE;
/*!40000 ALTER TABLE `encuesta_creditoe` DISABLE KEYS */;
INSERT INTO `encuesta_creditoe` VALUES (1,'Corto plazo'),(2,'Mediano plazo'),(3,'Largo plazo');
/*!40000 ALTER TABLE `encuesta_creditoe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_dequien`
--

DROP TABLE IF EXISTS `encuesta_dequien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_dequien` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_dequien`
--

LOCK TABLES `encuesta_dequien` WRITE;
/*!40000 ALTER TABLE `encuesta_dequien` DISABLE KEYS */;
INSERT INTO `encuesta_dequien` VALUES (1,'Empresa Ex'),(2,'ONG'),(3,'MF'),(4,'Banco'),(5,'Coop'),(6,'PP');
/*!40000 ALTER TABLE `encuesta_dequien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_duenofinca`
--

DROP TABLE IF EXISTS `encuesta_duenofinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_duenofinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_duenofinca`
--

LOCK TABLES `encuesta_duenofinca` WRITE;
/*!40000 ALTER TABLE `encuesta_duenofinca` DISABLE KEYS */;
INSERT INTO `encuesta_duenofinca` VALUES (1,'Luciano López Blandón');
/*!40000 ALTER TABLE `encuesta_duenofinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_encuesta`
--

DROP TABLE IF EXISTS `encuesta_encuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_encuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `recolector_id` int(11) NOT NULL,
  `nombre_id` int(11) NOT NULL,
  `cedula` varchar(50) NOT NULL,
  `dueno_id` int(11) NOT NULL,
  `sexo` int(11) NOT NULL,
  `finca` varchar(200) DEFAULT NULL,
  `pais_id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  `comunidad_id` int(11) NOT NULL,
  `longitud` double DEFAULT NULL,
  `latitud` double DEFAULT NULL,
  `altitud` varchar(50) DEFAULT NULL,
  `beneficiario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_encuesta_67cfeecd` (`recolector_id`),
  KEY `encuesta_encuesta_aa17bc3d` (`nombre_id`),
  KEY `encuesta_encuesta_383ad89a` (`dueno_id`),
  KEY `encuesta_encuesta_de1867db` (`pais_id`),
  KEY `encuesta_encuesta_cad1d7f2` (`departamento_id`),
  KEY `encuesta_encuesta_7a0809aa` (`municipio_id`),
  KEY `encuesta_encuesta_5cafe4bb` (`comunidad_id`),
  KEY `encuesta_encuesta_8b0fdfb6` (`beneficiario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_encuesta`
--

LOCK TABLES `encuesta_encuesta` WRITE;
/*!40000 ALTER TABLE `encuesta_encuesta` DISABLE KEYS */;
INSERT INTO `encuesta_encuesta` VALUES (1,'2013-11-22',1,1,'481-070166-0000D',1,1,'El Sinai',1,1,0,1,NULL,NULL,'1500',2);
/*!40000 ALTER TABLE `encuesta_encuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_energiafinca`
--

DROP TABLE IF EXISTS `encuesta_energiafinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_energiafinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_energiafinca`
--

LOCK TABLES `encuesta_energiafinca` WRITE;
/*!40000 ALTER TABLE `encuesta_energiafinca` DISABLE KEYS */;
INSERT INTO `encuesta_energiafinca` VALUES (1,'Electricidad'),(2,'No hay'),(3,'La red'),(4,'Planta eléctrica'),(5,'Panel Solar'),(6,'Molino de viento'),(7,'Candil');
/*!40000 ALTER TABLE `encuesta_energiafinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_entrevistado`
--

DROP TABLE IF EXISTS `encuesta_entrevistado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_entrevistado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_entrevistado`
--

LOCK TABLES `encuesta_entrevistado` WRITE;
/*!40000 ALTER TABLE `encuesta_entrevistado` DISABLE KEYS */;
INSERT INTO `encuesta_entrevistado` VALUES (1,'Luciano López Blandón');
/*!40000 ALTER TABLE `encuesta_entrevistado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_meses`
--

DROP TABLE IF EXISTS `encuesta_meses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_meses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_meses`
--

LOCK TABLES `encuesta_meses` WRITE;
/*!40000 ALTER TABLE `encuesta_meses` DISABLE KEYS */;
INSERT INTO `encuesta_meses` VALUES (1,'Ene'),(2,'Feb'),(3,'Mar'),(4,'Abr'),(5,'May'),(6,'Jun'),(7,'Jul'),(8,'Ago'),(9,'Sep'),(10,'Oct'),(11,'Nov'),(12,'Dic'),(13,'No aplica'),(14,'No aplico');
/*!40000 ALTER TABLE `encuesta_meses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_necesidadalimento`
--

DROP TABLE IF EXISTS `encuesta_necesidadalimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_necesidadalimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_necesidadalimento`
--

LOCK TABLES `encuesta_necesidadalimento` WRITE;
/*!40000 ALTER TABLE `encuesta_necesidadalimento` DISABLE KEYS */;
INSERT INTO `encuesta_necesidadalimento` VALUES (1,'Poca tierra para producción de alimento'),(2,'Falta de empleo o ingreso de la finca'),(3,'Familia numerosa'),(4,'Rendimientos de maíz y frijol bajos'),(5,'Bajo producción de café'),(6,'Bajo precio de café');
/*!40000 ALTER TABLE `encuesta_necesidadalimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_organizacion`
--

DROP TABLE IF EXISTS `encuesta_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_organizacion`
--

LOCK TABLES `encuesta_organizacion` WRITE;
/*!40000 ALTER TABLE `encuesta_organizacion` DISABLE KEYS */;
INSERT INTO `encuesta_organizacion` VALUES (1,'ECOM'),(2,'CISA'),(3,'Banco Atlantida'),(4,'SOPPEXCCA');
/*!40000 ALTER TABLE `encuesta_organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_quienfinancia`
--

DROP TABLE IF EXISTS `encuesta_quienfinancia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_quienfinancia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desde` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_quienfinancia_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_quienfinancia`
--

LOCK TABLES `encuesta_quienfinancia` WRITE;
/*!40000 ALTER TABLE `encuesta_quienfinancia` DISABLE KEYS */;
INSERT INTO `encuesta_quienfinancia` VALUES (1,3,1);
/*!40000 ALTER TABLE `encuesta_quienfinancia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_quienfinancia_beneficio_ser_socio`
--

DROP TABLE IF EXISTS `encuesta_quienfinancia_beneficio_ser_socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_quienfinancia_beneficio_ser_socio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quienfinancia_id` int(11) NOT NULL,
  `beneficios_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_quienfinancia_be_quienfinancia_id_77b6cc65f9636a7_uniq` (`quienfinancia_id`,`beneficios_id`),
  KEY `encuesta_quienfinancia_beneficio_ser_socio_d232b357` (`quienfinancia_id`),
  KEY `encuesta_quienfinancia_beneficio_ser_socio_d5b682ba` (`beneficios_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_quienfinancia_beneficio_ser_socio`
--

LOCK TABLES `encuesta_quienfinancia_beneficio_ser_socio` WRITE;
/*!40000 ALTER TABLE `encuesta_quienfinancia_beneficio_ser_socio` DISABLE KEYS */;
INSERT INTO `encuesta_quienfinancia_beneficio_ser_socio` VALUES (1,1,10);
/*!40000 ALTER TABLE `encuesta_quienfinancia_beneficio_ser_socio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_quienfinancia_de_quien`
--

DROP TABLE IF EXISTS `encuesta_quienfinancia_de_quien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_quienfinancia_de_quien` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quienfinancia_id` int(11) NOT NULL,
  `dequien_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_quienfinancia_d_quienfinancia_id_41faaffdf2320a42_uniq` (`quienfinancia_id`,`dequien_id`),
  KEY `encuesta_quienfinancia_de_quien_d232b357` (`quienfinancia_id`),
  KEY `encuesta_quienfinancia_de_quien_5288e76b` (`dequien_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_quienfinancia_de_quien`
--

LOCK TABLES `encuesta_quienfinancia_de_quien` WRITE;
/*!40000 ALTER TABLE `encuesta_quienfinancia_de_quien` DISABLE KEYS */;
INSERT INTO `encuesta_quienfinancia_de_quien` VALUES (1,1,1),(2,1,6);
/*!40000 ALTER TABLE `encuesta_quienfinancia_de_quien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_quienfinancia_socio`
--

DROP TABLE IF EXISTS `encuesta_quienfinancia_socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_quienfinancia_socio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quienfinancia_id` int(11) NOT NULL,
  `socioorganizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_quienfinancia_s_quienfinancia_id_15df7f86aa775476_uniq` (`quienfinancia_id`,`socioorganizacion_id`),
  KEY `encuesta_quienfinancia_socio_d232b357` (`quienfinancia_id`),
  KEY `encuesta_quienfinancia_socio_4f12d2bd` (`socioorganizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_quienfinancia_socio`
--

LOCK TABLES `encuesta_quienfinancia_socio` WRITE;
/*!40000 ALTER TABLE `encuesta_quienfinancia_socio` DISABLE KEYS */;
INSERT INTO `encuesta_quienfinancia_socio` VALUES (1,1,5);
/*!40000 ALTER TABLE `encuesta_quienfinancia_socio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_quienfinancia_tiene_credito`
--

DROP TABLE IF EXISTS `encuesta_quienfinancia_tiene_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_quienfinancia_tiene_credito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quienfinancia_id` int(11) NOT NULL,
  `creditoe_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_quienfinancia_ti_quienfinancia_id_74f370821f12726_uniq` (`quienfinancia_id`,`creditoe_id`),
  KEY `encuesta_quienfinancia_tiene_credito_d232b357` (`quienfinancia_id`),
  KEY `encuesta_quienfinancia_tiene_credito_9b77262d` (`creditoe_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_quienfinancia_tiene_credito`
--

LOCK TABLES `encuesta_quienfinancia_tiene_credito` WRITE;
/*!40000 ALTER TABLE `encuesta_quienfinancia_tiene_credito` DISABLE KEYS */;
INSERT INTO `encuesta_quienfinancia_tiene_credito` VALUES (1,1,1);
/*!40000 ALTER TABLE `encuesta_quienfinancia_tiene_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_recolector`
--

DROP TABLE IF EXISTS `encuesta_recolector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_recolector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_recolector`
--

LOCK TABLES `encuesta_recolector` WRITE;
/*!40000 ALTER TABLE `encuesta_recolector` DISABLE KEYS */;
INSERT INTO `encuesta_recolector` VALUES (1,'Falguni Guharay');
/*!40000 ALTER TABLE `encuesta_recolector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_seguridad`
--

DROP TABLE IF EXISTS `encuesta_seguridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_seguridad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compra_alimento` int(11) NOT NULL,
  `cubrir_necesidades` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_seguridad_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_seguridad`
--

LOCK TABLES `encuesta_seguridad` WRITE;
/*!40000 ALTER TABLE `encuesta_seguridad` DISABLE KEYS */;
INSERT INTO `encuesta_seguridad` VALUES (1,2,1,1);
/*!40000 ALTER TABLE `encuesta_seguridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_seguridad_meses_dificiles`
--

DROP TABLE IF EXISTS `encuesta_seguridad_meses_dificiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_seguridad_meses_dificiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seguridad_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_seguridad_meses_difi_seguridad_id_94322bc28eb8edd_uniq` (`seguridad_id`,`meses_id`),
  KEY `encuesta_seguridad_meses_dificiles_97b15ff3` (`seguridad_id`),
  KEY `encuesta_seguridad_meses_dificiles_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_seguridad_meses_dificiles`
--

LOCK TABLES `encuesta_seguridad_meses_dificiles` WRITE;
/*!40000 ALTER TABLE `encuesta_seguridad_meses_dificiles` DISABLE KEYS */;
INSERT INTO `encuesta_seguridad_meses_dificiles` VALUES (1,1,8),(2,1,6),(3,1,7);
/*!40000 ALTER TABLE `encuesta_seguridad_meses_dificiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_seguridad_porque_no_cubre`
--

DROP TABLE IF EXISTS `encuesta_seguridad_porque_no_cubre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_seguridad_porque_no_cubre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seguridad_id` int(11) NOT NULL,
  `necesidadalimento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_seguridad_porque_no__seguridad_id_912fb3f387c5d29_uniq` (`seguridad_id`,`necesidadalimento_id`),
  KEY `encuesta_seguridad_porque_no_cubre_97b15ff3` (`seguridad_id`),
  KEY `encuesta_seguridad_porque_no_cubre_43f65fd2` (`necesidadalimento_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_seguridad_porque_no_cubre`
--

LOCK TABLES `encuesta_seguridad_porque_no_cubre` WRITE;
/*!40000 ALTER TABLE `encuesta_seguridad_porque_no_cubre` DISABLE KEYS */;
INSERT INTO `encuesta_seguridad_porque_no_cubre` VALUES (1,1,5),(2,1,6);
/*!40000 ALTER TABLE `encuesta_seguridad_porque_no_cubre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_seguridad_soluciones_crisis`
--

DROP TABLE IF EXISTS `encuesta_seguridad_soluciones_crisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_seguridad_soluciones_crisis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seguridad_id` int(11) NOT NULL,
  `tiemposcrisis_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_seguridad_soluciones_seguridad_id_166f03254741e58_uniq` (`seguridad_id`,`tiemposcrisis_id`),
  KEY `encuesta_seguridad_soluciones_crisis_97b15ff3` (`seguridad_id`),
  KEY `encuesta_seguridad_soluciones_crisis_8b8d485a` (`tiemposcrisis_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_seguridad_soluciones_crisis`
--

LOCK TABLES `encuesta_seguridad_soluciones_crisis` WRITE;
/*!40000 ALTER TABLE `encuesta_seguridad_soluciones_crisis` DISABLE KEYS */;
INSERT INTO `encuesta_seguridad_soluciones_crisis` VALUES (1,1,8),(2,1,3);
/*!40000 ALTER TABLE `encuesta_seguridad_soluciones_crisis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_serviciosbasicos`
--

DROP TABLE IF EXISTS `encuesta_serviciosbasicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_serviciosbasicos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_serviciosbasicos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_serviciosbasicos`
--

LOCK TABLES `encuesta_serviciosbasicos` WRITE;
/*!40000 ALTER TABLE `encuesta_serviciosbasicos` DISABLE KEYS */;
INSERT INTO `encuesta_serviciosbasicos` VALUES (1,1);
/*!40000 ALTER TABLE `encuesta_serviciosbasicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_serviciosbasicos_agua_consumo_humano`
--

DROP TABLE IF EXISTS `encuesta_serviciosbasicos_agua_consumo_humano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_serviciosbasicos_agua_consumo_humano` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serviciosbasicos_id` int(11) NOT NULL,
  `aguafinca_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_serviciosbas_serviciosbasicos_id_6e539c009778cce7_uniq` (`serviciosbasicos_id`,`aguafinca_id`),
  KEY `encuesta_serviciosbasicos_agua_consumo_humano_62179f7d` (`serviciosbasicos_id`),
  KEY `encuesta_serviciosbasicos_agua_consumo_humano_1e88a6cb` (`aguafinca_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_serviciosbasicos_agua_consumo_humano`
--

LOCK TABLES `encuesta_serviciosbasicos_agua_consumo_humano` WRITE;
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_agua_consumo_humano` DISABLE KEYS */;
INSERT INTO `encuesta_serviciosbasicos_agua_consumo_humano` VALUES (1,1,2);
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_agua_consumo_humano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_serviciosbasicos_agua_trabajo_finca`
--

DROP TABLE IF EXISTS `encuesta_serviciosbasicos_agua_trabajo_finca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_serviciosbasicos_agua_trabajo_finca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serviciosbasicos_id` int(11) NOT NULL,
  `aguafinca_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_serviciosbas_serviciosbasicos_id_3da14171cef65260_uniq` (`serviciosbasicos_id`,`aguafinca_id`),
  KEY `encuesta_serviciosbasicos_agua_trabajo_finca_62179f7d` (`serviciosbasicos_id`),
  KEY `encuesta_serviciosbasicos_agua_trabajo_finca_1e88a6cb` (`aguafinca_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_serviciosbasicos_agua_trabajo_finca`
--

LOCK TABLES `encuesta_serviciosbasicos_agua_trabajo_finca` WRITE;
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_agua_trabajo_finca` DISABLE KEYS */;
INSERT INTO `encuesta_serviciosbasicos_agua_trabajo_finca` VALUES (1,1,2);
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_agua_trabajo_finca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_serviciosbasicos_combustible`
--

DROP TABLE IF EXISTS `encuesta_serviciosbasicos_combustible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_serviciosbasicos_combustible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serviciosbasicos_id` int(11) NOT NULL,
  `combustible_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_serviciosbas_serviciosbasicos_id_3316c5b2c52009cc_uniq` (`serviciosbasicos_id`,`combustible_id`),
  KEY `encuesta_serviciosbasicos_combustible_62179f7d` (`serviciosbasicos_id`),
  KEY `encuesta_serviciosbasicos_combustible_0c8e3b20` (`combustible_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_serviciosbasicos_combustible`
--

LOCK TABLES `encuesta_serviciosbasicos_combustible` WRITE;
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_combustible` DISABLE KEYS */;
INSERT INTO `encuesta_serviciosbasicos_combustible` VALUES (1,1,2);
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_combustible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_serviciosbasicos_electricidad`
--

DROP TABLE IF EXISTS `encuesta_serviciosbasicos_electricidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_serviciosbasicos_electricidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serviciosbasicos_id` int(11) NOT NULL,
  `energiafinca_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encuesta_serviciosbas_serviciosbasicos_id_32e2ed9efe310105_uniq` (`serviciosbasicos_id`,`energiafinca_id`),
  KEY `encuesta_serviciosbasicos_electricidad_62179f7d` (`serviciosbasicos_id`),
  KEY `encuesta_serviciosbasicos_electricidad_0be2a953` (`energiafinca_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_serviciosbasicos_electricidad`
--

LOCK TABLES `encuesta_serviciosbasicos_electricidad` WRITE;
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_electricidad` DISABLE KEYS */;
INSERT INTO `encuesta_serviciosbasicos_electricidad` VALUES (1,1,3);
/*!40000 ALTER TABLE `encuesta_serviciosbasicos_electricidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_socioorganizacion`
--

DROP TABLE IF EXISTS `encuesta_socioorganizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_socioorganizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_socioorganizacion`
--

LOCK TABLES `encuesta_socioorganizacion` WRITE;
/*!40000 ALTER TABLE `encuesta_socioorganizacion` DISABLE KEYS */;
INSERT INTO `encuesta_socioorganizacion` VALUES (1,'Cooperativa'),(2,'Asociación'),(3,'Empresa'),(4,'Grupo'),(5,'Ninguno');
/*!40000 ALTER TABLE `encuesta_socioorganizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_tenecia`
--

DROP TABLE IF EXISTS `encuesta_tenecia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_tenecia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` int(11) NOT NULL,
  `documento` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_tenecia_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_tenecia`
--

LOCK TABLES `encuesta_tenecia` WRITE;
/*!40000 ALTER TABLE `encuesta_tenecia` DISABLE KEYS */;
INSERT INTO `encuesta_tenecia` VALUES (1,5,1,1);
/*!40000 ALTER TABLE `encuesta_tenecia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_tiemposcrisis`
--

DROP TABLE IF EXISTS `encuesta_tiemposcrisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_tiemposcrisis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_tiemposcrisis`
--

LOCK TABLES `encuesta_tiemposcrisis` WRITE;
/*!40000 ALTER TABLE `encuesta_tiemposcrisis` DISABLE KEYS */;
INSERT INTO `encuesta_tiemposcrisis` VALUES (1,'Venta de Mano de obra'),(2,'Venta de Ganado mayor'),(3,'Venta de Ganado menor'),(4,'Venta de equipo y herramienta'),(5,'Venta de la tierra'),(6,'Busco Préstamo'),(7,'Prendo mi cosecha futura del café'),(8,'Compra alimento fiado'),(9,'Migró a otros lugares o países'),(10,'Utilizó mi ahorros');
/*!40000 ALTER TABLE `encuesta_tiemposcrisis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta_vivefamilia`
--

DROP TABLE IF EXISTS `encuesta_vivefamilia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_vivefamilia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta_vivefamilia`
--

LOCK TABLES `encuesta_vivefamilia` WRITE;
/*!40000 ALTER TABLE `encuesta_vivefamilia` DISABLE KEYS */;
INSERT INTO `encuesta_vivefamilia` VALUES (1,'Viven en la finca'),(2,'Viven en pueblo cerca de finca'),(3,'Vive en ciudad lejos de la finca'),(4,'Pasa tiempo en la finca y tiempo en casa');
/*!40000 ALTER TABLE `encuesta_vivefamilia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_comunidad`
--

DROP TABLE IF EXISTS `lugar_comunidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_comunidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio_id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lugar_comunidad_7a0809aa` (`municipio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_comunidad`
--

LOCK TABLES `lugar_comunidad` WRITE;
/*!40000 ALTER TABLE `lugar_comunidad` DISABLE KEYS */;
INSERT INTO `lugar_comunidad` VALUES (1,0,'Volcán');
/*!40000 ALTER TABLE `lugar_comunidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_departamento_de1867db` (`pais_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
INSERT INTO `lugar_departamento` VALUES (1,1,'Nueva Segovia','nueva-segovia',0.00);
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `latitud` decimal(8,5) DEFAULT NULL,
  `longitud` decimal(8,5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_cad1d7f2` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
INSERT INTO `lugar_municipio` VALUES (0,1,'Dipilto','dipilto',NULL,NULL,NULL);
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_pais`
--

DROP TABLE IF EXISTS `lugar_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_pais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_pais`
--

LOCK TABLES `lugar_pais` WRITE;
/*!40000 ALTER TABLE `lugar_pais` DISABLE KEYS */;
INSERT INTO `lugar_pais` VALUES (1,'Nicaragua');
/*!40000 ALTER TABLE `lugar_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_areacafe`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_areacafe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_areacafe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado_id` int(11) NOT NULL,
  `once` double NOT NULL,
  `doce` double NOT NULL,
  `trece` double NOT NULL,
  `catorse` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_areacafe_eeec61f0` (`estado_id`),
  KEY `produccion_cafe_finca_areacafe_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_areacafe`
--

LOCK TABLES `produccion_cafe_finca_areacafe` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_areacafe` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_areacafe` VALUES (1,1,3,3,3,3,1),(2,4,3,3,3,2,1),(3,5,0,0,0,1,1),(4,6,84,126,52,50,1),(5,7,42,63,26,25,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_areacafe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_beneficiado`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_beneficiado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_beneficiado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cortes` int(11) NOT NULL,
  `separan` int(11) NOT NULL,
  `despulpan_fermentan` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `calibran` int(11) NOT NULL,
  `revisan` int(11) NOT NULL,
  `despulpar` int(11) NOT NULL,
  `fermentan` int(11) NOT NULL,
  `orean` int(11) NOT NULL,
  `beneficiado_seco_id` int(11) NOT NULL,
  `calidad` int(11) NOT NULL,
  `determina_calidad_id` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `cuanto` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_beneficiado_d73e8f17` (`beneficiado_seco_id`),
  KEY `produccion_cafe_finca_beneficiado_c3e937ad` (`determina_calidad_id`),
  KEY `produccion_cafe_finca_beneficiado_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_beneficiado`
--

LOCK TABLES `produccion_cafe_finca_beneficiado` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_beneficiado` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_beneficiado` VALUES (1,1,2,1,2,2,2,1,3,1,1,1,1,1,30,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_beneficiado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_beneficioseco`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_beneficioseco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_beneficioseco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_beneficioseco`
--

LOCK TABLES `produccion_cafe_finca_beneficioseco` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_beneficioseco` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_beneficioseco` VALUES (1,'Beneficio Balladares');
/*!40000 ALTER TABLE `produccion_cafe_finca_beneficioseco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_calidadcafe`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_calidadcafe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_calidadcafe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_calidadcafe`
--

LOCK TABLES `produccion_cafe_finca_calidadcafe` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_calidadcafe` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_calidadcafe` VALUES (1,'Tasa de Excelencia');
/*!40000 ALTER TABLE `produccion_cafe_finca_calidadcafe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_comercializacion`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_comercializacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_comercializacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` int(11) NOT NULL,
  `p_total` double NOT NULL,
  `i_venta_cafe` double NOT NULL,
  `i_precio` double NOT NULL,
  `c_venta` double NOT NULL,
  `c_precio` double NOT NULL,
  `e_venta` double NOT NULL,
  `e_precio` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_comercializacion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_comercializacion`
--

LOCK TABLES `produccion_cafe_finca_comercializacion` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_comercializacion` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_comercializacion` VALUES (1,1,126,63,2450,0,0,63,2400,1),(2,2,52,26,1350,0,0,26,1300,1),(3,3,50,50,1150,0,0,0,0,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_comercializacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_credito`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_credito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` int(11) NOT NULL,
  `monto` double NOT NULL,
  `cobertura` double NOT NULL,
  `credito_mediano` double NOT NULL,
  `necesidad` double NOT NULL,
  `credito_largo` double NOT NULL,
  `cobertura_necesidad` double NOT NULL,
  `facilidad` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_credito_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_credito`
--

LOCK TABLES `produccion_cafe_finca_credito` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_credito` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_credito` VALUES (1,2,600,0,0,0,0,0,1,1),(2,3,1800,0,0,0,0,0,1,1),(3,3,850,0,0,0,0,0,1,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_criterios`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_criterios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_criterios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_criterios`
--

LOCK TABLES `produccion_cafe_finca_criterios` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_criterios` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_criterios` VALUES (1,'La altitud'),(2,'El clima'),(3,'El rendimiento'),(4,'Calidad de grano'),(5,'Resistencia a enfermedades'),(6,'La calidad de la taza');
/*!40000 ALTER TABLE `produccion_cafe_finca_criterios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_decidesembrar`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_decidesembrar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_decidesembrar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_decidesembrar`
--

LOCK TABLES `produccion_cafe_finca_decidesembrar` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_decidesembrar` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_decidesembrar` VALUES (1,'Precio de la planta'),(2,'Recomendaciones'),(3,'Experiencia'),(4,'Disponibilidad');
/*!40000 ALTER TABLE `produccion_cafe_finca_decidesembrar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_estadoactual`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_estadoactual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_estadoactual` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_estadoactual`
--

LOCK TABLES `produccion_cafe_finca_estadoactual` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_estadoactual` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_estadoactual` VALUES (1,'Area total de café'),(2,'AREA EN RENOVACION'),(3,'Area de café en desarrollo'),(4,'Area de café en producción'),(5,'Areá de café en recepo'),(6,'Producción total de la finca en qq pergamino SECO'),(7,'Producción total de finca en qq oro');
/*!40000 ALTER TABLE `produccion_cafe_finca_estadoactual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_manejocafetales_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales` VALUES (1,3,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_fertilizante_foliares`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_fertilizante_foliares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_fertilizante_foliares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_5f9751e28d7bf1a9_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_fertilizante_foliares_ee26` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_fertilizante_foliares_7603` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_fertilizante_foliares`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_fertilizante_foliares` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fertilizante_foliares` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_fertilizante_foliares` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fertilizante_foliares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_fertilizante_suelo`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_fertilizante_suelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_fertilizante_suelo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_2386dd8c533876b9_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_fertilizante_suelo_e26ac59` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_fertilizante_suelo_5451b1f` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_fertilizante_suelo`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_fertilizante_suelo` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fertilizante_suelo` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_fertilizante_suelo` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fertilizante_suelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_fungicidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_fungicidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_fungicidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_4d0df8caa7698354_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_fungicidas_e26532f4` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_fungicidas_5450fa53` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_fungicidas`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_fungicidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fungicidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_fungicidas` VALUES (1,1,2),(2,1,4);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_fungicidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_insecticidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_insecticidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_insecticidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_m_manejocafetales_id_83bcbb3503f4f28_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_insecticidas_e26532f4` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_insecticidas_5450fa53` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_insecticidas`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_insecticidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_insecticidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_insecticidas` VALUES (1,1,7);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_insecticidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_manejo_cafeto`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_manejo_cafeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_manejo_cafeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_64735991a232dd9f_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_manejo_cafeto_e26532f4` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_manejo_cafeto_5450fa53` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_manejo_cafeto`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_manejo_cafeto` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_manejo_cafeto` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_manejo_cafeto` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_manejo_cafeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_manejo_sombra`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_manejo_sombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_manejo_sombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_656b1cb0daadeb77_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_manejo_sombra_e26532f4` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_manejo_sombra_5450fa53` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_manejo_sombra`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_manejo_sombra` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_manejo_sombra` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_manejo_sombra` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_manejo_sombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejocafetales_nematicidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejocafetales_nematicidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejocafetales_nematicidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejocafetales_id` int(11) NOT NULL,
  `manejos_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__manejocafetales_id_444cc272bfafd460_uniq` (`manejocafetales_id`,`manejos_id`),
  KEY `produccion_cafe_finca_manejocafetales_nematicidas_e26532f4` (`manejocafetales_id`),
  KEY `produccion_cafe_finca_manejocafetales_nematicidas_5450fa53` (`manejos_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejocafetales_nematicidas`
--

LOCK TABLES `produccion_cafe_finca_manejocafetales_nematicidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_nematicidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejocafetales_nematicidas` VALUES (1,1,1),(2,1,5);
/*!40000 ALTER TABLE `produccion_cafe_finca_manejocafetales_nematicidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_manejos`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_manejos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_manejos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_manejos`
--

LOCK TABLES `produccion_cafe_finca_manejos` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_manejos` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_manejos` VALUES (1,'B'),(2,'R'),(3,'M'),(4,'T'),(5,'V'),(6,'A'),(7,'N');
/*!40000 ALTER TABLE `produccion_cafe_finca_manejos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe` VALUES (1,4,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_1cc7a3326a948e65_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliaf190` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_folia2ce6` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares` VALUES (1,1,11),(2,1,6);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_2214dbd0d4d488a3_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelod71a` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo0e5a` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo` VALUES (1,1,10),(2,1,6);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_49a0196dce3cea10_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas_41484e77` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas` VALUES (1,1,8),(2,1,11);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_fungicidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_47c9b134f3cb1304_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas_41484e77` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas` VALUES (1,1,13);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_insecticidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_756fe392cc3a6705_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto_41484e77` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto` VALUES (1,1,2),(2,1,3);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_m_mesesmanejocafe_id_51e257fe8028983_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra_41484e77` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra` VALUES (1,1,5),(2,1,6);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mesesmanejocafe_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca__mesesmanejocafe_id_167962d4819a2bf4_uniq` (`mesesmanejocafe_id`,`meses_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas_41484e77` (`mesesmanejocafe_id`),
  KEY `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas`
--

LOCK TABLES `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas` VALUES (1,1,9);
/*!40000 ALTER TABLE `produccion_cafe_finca_mesesmanejocafe_mes_nematicidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_nombretipos`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_nombretipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_nombretipos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_nombretipos`
--

LOCK TABLES `produccion_cafe_finca_nombretipos` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_nombretipos` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_nombretipos` VALUES (1,'Topacio'),(2,'Fungomac'),(3,'Glifosato'),(4,'Gramoxone'),(5,'8-5-10'),(6,'20-20-20');
/*!40000 ALTER TABLE `produccion_cafe_finca_nombretipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_opciones`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_opciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_opciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_opciones`
--

LOCK TABLES `produccion_cafe_finca_opciones` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_opciones` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_opciones` VALUES (1,'Biofertilzantes'),(2,'Compost'),(3,'Roca Minerales'),(4,'Insecticida natural'),(5,'Fungicida natural'),(6,'Cerca viva '),(7,'Cortina rompe viento'),(8,'Abonos verdes'),(9,'Siembra en Curva a nivel'),(10,'Acequia'),(11,'Barrera viva'),(12,'Barrera muerta'),(13,'Cosecha de agua'),(14,'Cultivo asociado'),(15,'Incorporación de rastrojo'),(16,'Manejo selectivo de malas hierbas'),(17,'Siembra de coberturas'),(18,'Uso de trampa para la broca'),(19,'Uso de Beauveria bassiana para broca'),(20,'Siembra de plantas injertadas'),(21,'Diversificación de los cafetales');
/*!40000 ALTER TABLE `produccion_cafe_finca_opciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_plantio`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_plantio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_plantio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_plantio`
--

LOCK TABLES `produccion_cafe_finca_plantio` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_plantio` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_plantio` VALUES (1,'Sinai'),(2,'Lote');
/*!40000 ALTER TABLE `produccion_cafe_finca_plantio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vivero_finca` int(11) NOT NULL,
  `plantas_vivero` double NOT NULL,
  `plantas_finca` double NOT NULL,
  `plantas_vender` double NOT NULL,
  `plantas_injertadas` double NOT NULL,
  `edad_planta` double NOT NULL,
  `costo_planta_caturra` double NOT NULL,
  `costo_planta_catimore` double NOT NULL,
  `costo_planta_hibridas` double NOT NULL,
  `pagar_caturra` double NOT NULL,
  `pagar_catimore` double NOT NULL,
  `pagar_hibrida` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_produccionvivero_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero` VALUES (1,1,2500,2500,0,0,7,0,0,0,5,5,0,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_consigue_semilla`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_consigue_semilla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_consigue_semilla` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `semilla_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_43d9dcfa76bc3c76_uniq` (`produccionvivero_id`,`semilla_id`),
  KEY `produccion_cafe_finca_produccionvivero_consigue_semilla_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_consigue_semilla_bff69d52` (`semilla_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_consigue_semilla`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_consigue_semilla` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_consigue_semilla` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_consigue_semilla` VALUES (1,1,2);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_consigue_semilla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_criterio`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_criterio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_criterio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `criterios_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_7fac55444a51f69d_uniq` (`produccionvivero_id`,`criterios_id`),
  KEY `produccion_cafe_finca_produccionvivero_criterio_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_criterio_b9014e1e` (`criterios_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_criterio`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_criterio` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_criterio` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_criterio` VALUES (1,1,3),(2,1,5);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_criterio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_decide`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_decide`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_decide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `decidesembrar_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_465b8ac997c087ae_uniq` (`produccionvivero_id`,`decidesembrar_id`),
  KEY `produccion_cafe_finca_produccionvivero_decide_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_decide_cf8e5353` (`decidesembrar_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_decide`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_decide` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_decide` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_decide` VALUES (1,1,3);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_decide` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_disponible`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_disponible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_disponible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `variedades_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_586f78414ebb3a40_uniq` (`produccionvivero_id`,`variedades_id`),
  KEY `produccion_cafe_finca_produccionvivero_disponible_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_disponible_ee5d6666` (`variedades_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_disponible`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_disponible` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_disponible` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_disponible` VALUES (1,1,7);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_disponible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_resistente_roya`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_resistente_roya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_resistente_roya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `resistenteroya_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_27c5b479c914fd79_uniq` (`produccionvivero_id`,`resistenteroya_id`),
  KEY `produccion_cafe_finca_produccionvivero_resistente_roya_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_resistente_roya_c1e8b9a6` (`resistenteroya_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_resistente_roya`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_resistente_roya` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_resistente_roya` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_resistente_roya` VALUES (1,1,2);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_resistente_roya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_produccionvivero_variedad`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_produccionvivero_variedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_produccionvivero_variedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produccionvivero_id` int(11) NOT NULL,
  `variedades_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_produccionvivero_id_5a33ee1d290daf81_uniq` (`produccionvivero_id`,`variedades_id`),
  KEY `produccion_cafe_finca_produccionvivero_variedad_fb9038be` (`produccionvivero_id`),
  KEY `produccion_cafe_finca_produccionvivero_variedad_ee5d6666` (`variedades_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_produccionvivero_variedad`
--

LOCK TABLES `produccion_cafe_finca_produccionvivero_variedad` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_variedad` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_produccionvivero_variedad` VALUES (1,1,3);
/*!40000 ALTER TABLE `produccion_cafe_finca_produccionvivero_variedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_resistenteroya`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_resistenteroya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_resistenteroya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_resistenteroya`
--

LOCK TABLES `produccion_cafe_finca_resistenteroya` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_resistenteroya` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_resistenteroya` VALUES (1,'Seleccion CATURRA'),(2,'Lineas de CATIMORES'),(3,'Hibridas'),(4,'OTRAS');
/*!40000 ALTER TABLE `produccion_cafe_finca_resistenteroya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_semilla`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_semilla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_semilla` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_semilla`
--

LOCK TABLES `produccion_cafe_finca_semilla` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_semilla` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_semilla` VALUES (1,'La misma finca'),(2,'Fincas vecinas'),(3,'Vivero Cooperativa'),(4,'Vivero Empresa');
/*!40000 ALTER TABLE `produccion_cafe_finca_semilla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_tiposinsumos`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_tiposinsumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_tiposinsumos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_tiposinsumos`
--

LOCK TABLES `produccion_cafe_finca_tiposinsumos` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_tiposinsumos` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_tiposinsumos` VALUES (1,'Fungicidas'),(2,'Insecticidas'),(3,'Herbicidas'),(4,'Nematicidas'),(5,'Fertilizantes en suelo'),(6,'Abono orgánico'),(7,'Fertilizantes foliares');
/*!40000 ALTER TABLE `produccion_cafe_finca_tiposinsumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_usoinsumos`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_usoinsumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_usoinsumos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_id` int(11) NOT NULL,
  `nombre_id` int(11) NOT NULL,
  `aplicaciones` double NOT NULL,
  `cantidad` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_usoinsumos_acf1eac4` (`tipo_id`),
  KEY `produccion_cafe_finca_usoinsumos_aa17bc3d` (`nombre_id`),
  KEY `produccion_cafe_finca_usoinsumos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_usoinsumos`
--

LOCK TABLES `produccion_cafe_finca_usoinsumos` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_usoinsumos` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_usoinsumos` VALUES (1,1,1,1,300,1),(2,1,2,1,250,1),(3,3,3,1,1,1),(4,5,5,1,2,1),(5,7,6,2,1,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_usoinsumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_usoinsumos_momento`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_usoinsumos_momento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_usoinsumos_momento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usoinsumos_id` int(11) NOT NULL,
  `meses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_usoin_usoinsumos_id_184d9bb6ab741cf1_uniq` (`usoinsumos_id`,`meses_id`),
  KEY `produccion_cafe_finca_usoinsumos_momento_34502c62` (`usoinsumos_id`),
  KEY `produccion_cafe_finca_usoinsumos_momento_6c2cfcdf` (`meses_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_usoinsumos_momento`
--

LOCK TABLES `produccion_cafe_finca_usoinsumos_momento` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_usoinsumos_momento` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_usoinsumos_momento` VALUES (1,1,8),(2,2,11),(3,3,7),(4,4,7),(5,5,11),(6,5,6);
/*!40000 ALTER TABLE `produccion_cafe_finca_usoinsumos_momento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_usoopcionesagroecologica`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_usoopcionesagroecologica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_usoopcionesagroecologica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `opcion_id` int(11) NOT NULL,
  `nivel` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_usoopcionesagroecologica_5566d6f7` (`opcion_id`),
  KEY `produccion_cafe_finca_usoopcionesagroecologica_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_usoopcionesagroecologica`
--

LOCK TABLES `produccion_cafe_finca_usoopcionesagroecologica` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_usoopcionesagroecologica` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_usoopcionesagroecologica` VALUES (1,7,2,1),(2,10,4,1),(3,11,2,1),(4,14,2,1),(5,15,4,1),(6,21,4,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_usoopcionesagroecologica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_variedadedadroya`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_variedadedadroya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_variedadedadroya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_plantio_id` int(11) NOT NULL,
  `area` double NOT NULL,
  `produccion_2012` double NOT NULL,
  `produccion_2013` double NOT NULL,
  `produccion_2014` double NOT NULL,
  `nivel_roya` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_cafe_finca_variedadedadroya_dfabaf28` (`nombre_plantio_id`),
  KEY `produccion_cafe_finca_variedadedadroya_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_variedadedadroya`
--

LOCK TABLES `produccion_cafe_finca_variedadedadroya` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_variedadedadroya` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_variedadedadroya` VALUES (1,1,1.5,0,0,40,50,1),(2,2,1.5,0,0,10,100,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_variedadedadroya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_variedadedadroya_variedades`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_variedadedadroya_variedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_variedadedadroya_variedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `variedadedadroya_id` int(11) NOT NULL,
  `variedades_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produccion_cafe_finca_variedadedadroya_id_3331c4927a67caab_uniq` (`variedadedadroya_id`,`variedades_id`),
  KEY `produccion_cafe_finca_variedadedadroya_variedades_26f76943` (`variedadedadroya_id`),
  KEY `produccion_cafe_finca_variedadedadroya_variedades_ee5d6666` (`variedades_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_variedadedadroya_variedades`
--

LOCK TABLES `produccion_cafe_finca_variedadedadroya_variedades` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_variedadedadroya_variedades` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_variedadedadroya_variedades` VALUES (1,1,1),(2,1,2),(3,2,1);
/*!40000 ALTER TABLE `produccion_cafe_finca_variedadedadroya_variedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_cafe_finca_variedades`
--

DROP TABLE IF EXISTS `produccion_cafe_finca_variedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_cafe_finca_variedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_cafe_finca_variedades`
--

LOCK TABLES `produccion_cafe_finca_variedades` WRITE;
/*!40000 ALTER TABLE `produccion_cafe_finca_variedades` DISABLE KEYS */;
INSERT INTO `produccion_cafe_finca_variedades` VALUES (1,'C'),(2,'CT'),(3,'CM'),(4,'B'),(5,'P'),(6,'H'),(7,'No hay');
/*!40000 ALTER TABLE `produccion_cafe_finca_variedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_actividad`
--

DROP TABLE IF EXISTS `produccion_finca_actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_actividad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_actividad`
--

LOCK TABLES `produccion_finca_actividad` WRITE;
/*!40000 ALTER TABLE `produccion_finca_actividad` DISABLE KEYS */;
INSERT INTO `produccion_finca_actividad` VALUES (1,'Enriquecimiento de los bosques'),(2,'Protección de fuentes de agua'),(3,'Establecimiento de cercas viva'),(4,'Plantaciones forestales'),(5,'Siembra de árboles en potrero'),(6,'Siembra de árboles en cafetales'),(7,'Establecimiento de viveros de árboles'),(8,'Parcelas frutales'),(9,'Huerto de Patio'),(10,'Establecimiento de cultivo agroforestales');
/*!40000 ALTER TABLE `produccion_finca_actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_animales`
--

DROP TABLE IF EXISTS `produccion_finca_animales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_animales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_animales`
--

LOCK TABLES `produccion_finca_animales` WRITE;
/*!40000 ALTER TABLE `produccion_finca_animales` DISABLE KEYS */;
INSERT INTO `produccion_finca_animales` VALUES (1,'Vacas paridas'),(2,'Vaca Seca'),(3,'Vaquillas'),(4,'Ternero de desarrollo'),(5,'Novillos'),(6,'Bueyes'),(7,'Toros'),(8,'Pelibuey'),(9,'Cerdos'),(10,'Aves de corral'),(11,'Colmenas'),(12,'Bestias');
/*!40000 ALTER TABLE `produccion_finca_animales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_animalesfinca`
--

DROP TABLE IF EXISTS `produccion_finca_animalesfinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_animalesfinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `animales_id` int(11) NOT NULL,
  `cantidad` double DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_animalesfinca_c3f404c4` (`animales_id`),
  KEY `produccion_finca_animalesfinca_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_animalesfinca`
--

LOCK TABLES `produccion_finca_animalesfinca` WRITE;
/*!40000 ALTER TABLE `produccion_finca_animalesfinca` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_animalesfinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_fuentes`
--

DROP TABLE IF EXISTS `produccion_finca_fuentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_fuentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_fuentes`
--

LOCK TABLES `produccion_finca_fuentes` WRITE;
/*!40000 ALTER TABLE `produccion_finca_fuentes` DISABLE KEYS */;
INSERT INTO `produccion_finca_fuentes` VALUES (1,'Salarios'),(2,'Negocios'),(3,'Remesas'),(4,'Alquiler');
/*!40000 ALTER TABLE `produccion_finca_fuentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_ingresofamiliar`
--

DROP TABLE IF EXISTS `produccion_finca_ingresofamiliar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_ingresofamiliar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rubro_id` int(11) NOT NULL,
  `cantidad` double DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `quien_vendio` int(11) DEFAULT NULL,
  `maneja_negocio` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_ingresofamiliar_9c7df5dd` (`rubro_id`),
  KEY `produccion_finca_ingresofamiliar_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_ingresofamiliar`
--

LOCK TABLES `produccion_finca_ingresofamiliar` WRITE;
/*!40000 ALTER TABLE `produccion_finca_ingresofamiliar` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_ingresofamiliar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_otrosingresos`
--

DROP TABLE IF EXISTS `produccion_finca_otrosingresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_otrosingresos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fuente_id` int(11) NOT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `meses` int(11) DEFAULT NULL,
  `ingreso` int(11) DEFAULT NULL,
  `tiene_ingreso` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_otrosingresos_407650da` (`fuente_id`),
  KEY `produccion_finca_otrosingresos_acf1eac4` (`tipo_id`),
  KEY `produccion_finca_otrosingresos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_otrosingresos`
--

LOCK TABLES `produccion_finca_otrosingresos` WRITE;
/*!40000 ALTER TABLE `produccion_finca_otrosingresos` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_otrosingresos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_productofinca`
--

DROP TABLE IF EXISTS `produccion_finca_productofinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_productofinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivo_id` int(11) DEFAULT NULL,
  `area` double NOT NULL,
  `total_produccion` double DEFAULT NULL,
  `consumo` double DEFAULT NULL,
  `venta` double DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_productofinca_db1e46c0` (`cultivo_id`),
  KEY `produccion_finca_productofinca_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_productofinca`
--

LOCK TABLES `produccion_finca_productofinca` WRITE;
/*!40000 ALTER TABLE `produccion_finca_productofinca` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_productofinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_productopatio`
--

DROP TABLE IF EXISTS `produccion_finca_productopatio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_productopatio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivo_id` int(11) DEFAULT NULL,
  `cantidad` double NOT NULL,
  `total_produccion` double DEFAULT NULL,
  `consumo` double DEFAULT NULL,
  `venta` double DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_productopatio_db1e46c0` (`cultivo_id`),
  KEY `produccion_finca_productopatio_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_productopatio`
--

LOCK TABLES `produccion_finca_productopatio` WRITE;
/*!40000 ALTER TABLE `produccion_finca_productopatio` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_productopatio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_productos`
--

DROP TABLE IF EXISTS `produccion_finca_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `unidad` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_productos`
--

LOCK TABLES `produccion_finca_productos` WRITE;
/*!40000 ALTER TABLE `produccion_finca_productos` DISABLE KEYS */;
INSERT INTO `produccion_finca_productos` VALUES (1,'Arroz','qq'),(2,'Cacao','qq'),(3,'Café','qq'),(4,'Frijol','qq'),(5,'Guineo','Cbz'),(6,'Maíz','qq'),(7,'Malanga','qq'),(8,'Plátano','Cbz'),(9,'Quequisque','qq'),(10,'Yuca','qq'),(11,'Tomate','Caja'),(12,'Repollo','Cabeza');
/*!40000 ALTER TABLE `produccion_finca_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_productospatio`
--

DROP TABLE IF EXISTS `produccion_finca_productospatio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_productospatio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `unidad` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_productospatio`
--

LOCK TABLES `produccion_finca_productospatio` WRITE;
/*!40000 ALTER TABLE `produccion_finca_productospatio` DISABLE KEYS */;
INSERT INTO `produccion_finca_productospatio` VALUES (1,'Mango','Saco de cien'),(2,'Pejibeye','Saco'),(3,'Aguacate','Docena'),(4,'Citricos','Saco de cien');
/*!40000 ALTER TABLE `produccion_finca_productospatio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_reforestacion`
--

DROP TABLE IF EXISTS `produccion_finca_reforestacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_reforestacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reforestacion_id` int(11) NOT NULL,
  `respuesta` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_reforestacion_5e93ee40` (`reforestacion_id`),
  KEY `produccion_finca_reforestacion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_reforestacion`
--

LOCK TABLES `produccion_finca_reforestacion` WRITE;
/*!40000 ALTER TABLE `produccion_finca_reforestacion` DISABLE KEYS */;
INSERT INTO `produccion_finca_reforestacion` VALUES (1,6,1,1);
/*!40000 ALTER TABLE `produccion_finca_reforestacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_rubros`
--

DROP TABLE IF EXISTS `produccion_finca_rubros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_rubros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `unidad` varchar(100) NOT NULL,
  `categoria` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_rubros`
--

LOCK TABLES `produccion_finca_rubros` WRITE;
/*!40000 ALTER TABLE `produccion_finca_rubros` DISABLE KEYS */;
INSERT INTO `produccion_finca_rubros` VALUES (1,'Arroz','qq',3),(2,'Aves','Unidad',NULL),(3,'Cacao','qq',NULL),(4,'Café','qq',NULL),(5,'Cuajada','Lb',NULL),(6,'Frijol','qq',3),(7,'Guineo','Cbz',NULL),(8,'Huevos','Docena',NULL),(9,'Leche','Lt',NULL),(10,'Maíz','qq',NULL),(11,'Malanga','qq',NULL),(12,'Mango','Cien',NULL),(13,'Naranja','Cien',NULL),(14,'Plátano','Cbz',NULL),(15,'Quequisque','qq',NULL),(16,'Queso','Lb',NULL),(17,'Ternero en desarrollo','Cabeza',NULL),(18,'Vaca','Cabeza',NULL),(19,'Yuca','qq',NULL),(20,'Gallina','Unidad',NULL),(21,'Leña','Manojo',NULL),(22,'Madera aserrada','Pie tablar',NULL),(23,'Crema','Lb',NULL),(24,'Cerdos','Unidad',NULL),(25,'Pejibaye','Racimo',NULL),(26,'Tomate','Caja',NULL),(27,'Repollo','Cabeza',NULL);
/*!40000 ALTER TABLE `produccion_finca_rubros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_tipotrabajo`
--

DROP TABLE IF EXISTS `produccion_finca_tipotrabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_tipotrabajo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_tipotrabajo`
--

LOCK TABLES `produccion_finca_tipotrabajo` WRITE;
/*!40000 ALTER TABLE `produccion_finca_tipotrabajo` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_finca_tipotrabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_uso`
--

DROP TABLE IF EXISTS `produccion_finca_uso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_uso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_uso`
--

LOCK TABLES `produccion_finca_uso` WRITE;
/*!40000 ALTER TABLE `produccion_finca_uso` DISABLE KEYS */;
INSERT INTO `produccion_finca_uso` VALUES (1,'Área total'),(2,'Bosque'),(3,'Tacotales'),(4,'Cultivos anuales'),(5,'Plantaciones  forestal'),(6,'Áreas de pastos abierto'),(7,'Áreas de pastos con árboles'),(8,'Cultivos perennes');
/*!40000 ALTER TABLE `produccion_finca_uso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_finca_usotierra`
--

DROP TABLE IF EXISTS `produccion_finca_usotierra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produccion_finca_usotierra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tierra_id` int(11) DEFAULT NULL,
  `area` double DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `produccion_finca_usotierra_977022e2` (`tierra_id`),
  KEY `produccion_finca_usotierra_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_finca_usotierra`
--

LOCK TABLES `produccion_finca_usotierra` WRITE;
/*!40000 ALTER TABLE `produccion_finca_usotierra` DISABLE KEYS */;
INSERT INTO `produccion_finca_usotierra` VALUES (1,1,3,1),(2,8,3,1);
/*!40000 ALTER TABLE `produccion_finca_usotierra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelanteaplicacionfungicida`
--

DROP TABLE IF EXISTS `roya_adelanteaplicacionfungicida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelanteaplicacionfungicida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2016_id` int(11) NOT NULL,
  `mz_2016` double NOT NULL,
  `dosis_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelanteaplicacionfungicida_9d0827ba` (`tipo_2016_id`),
  KEY `roya_adelanteaplicacionfungicida_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelanteaplicacionfungicida`
--

LOCK TABLES `roya_adelanteaplicacionfungicida` WRITE;
/*!40000 ALTER TABLE `roya_adelanteaplicacionfungicida` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelanteaplicacionfungicida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantefertilizacion`
--

DROP TABLE IF EXISTS `roya_adelantefertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantefertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantefertilizacion`
--

LOCK TABLES `roya_adelantefertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_adelantefertilizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantefertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantemanejofertilizacion`
--

DROP TABLE IF EXISTS `roya_adelantemanejofertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantemanejofertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2016_id` int(11) NOT NULL,
  `mz_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelantemanejofertilizacion_9d0827ba` (`tipo_2016_id`),
  KEY `roya_adelantemanejofertilizacion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantemanejofertilizacion`
--

LOCK TABLES `roya_adelantemanejofertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_adelantemanejofertilizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantemanejofertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantemanejosombra`
--

DROP TABLE IF EXISTS `roya_adelantemanejosombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantemanejosombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2016_id` int(11) NOT NULL,
  `mz_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelantemanejosombra_9d0827ba` (`tipo_2016_id`),
  KEY `roya_adelantemanejosombra_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantemanejosombra`
--

LOCK TABLES `roya_adelantemanejosombra` WRITE;
/*!40000 ALTER TABLE `roya_adelantemanejosombra` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantemanejosombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantepodacafetos`
--

DROP TABLE IF EXISTS `roya_adelantepodacafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantepodacafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2016_id` int(11) NOT NULL,
  `mz_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelantepodacafetos_9d0827ba` (`tipo_2016_id`),
  KEY `roya_adelantepodacafetos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantepodacafetos`
--

LOCK TABLES `roya_adelantepodacafetos` WRITE;
/*!40000 ALTER TABLE `roya_adelantepodacafetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantepodacafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelanterecepocafetos`
--

DROP TABLE IF EXISTS `roya_adelanterecepocafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelanterecepocafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mz_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelanterecepocafetos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelanterecepocafetos`
--

LOCK TABLES `roya_adelanterecepocafetos` WRITE;
/*!40000 ALTER TABLE `roya_adelanterecepocafetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelanterecepocafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelanterenovacioncafetales`
--

DROP TABLE IF EXISTS `roya_adelanterenovacioncafetales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelanterenovacioncafetales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2016_id` int(11) NOT NULL,
  `mz_2016` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_adelanterenovacioncafetales_9d0827ba` (`tipo_2016_id`),
  KEY `roya_adelanterenovacioncafetales_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelanterenovacioncafetales`
--

LOCK TABLES `roya_adelanterenovacioncafetales` WRITE;
/*!40000 ALTER TABLE `roya_adelanterenovacioncafetales` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelanterenovacioncafetales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantetipoaplicacionfungicida`
--

DROP TABLE IF EXISTS `roya_adelantetipoaplicacionfungicida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantetipoaplicacionfungicida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantetipoaplicacionfungicida`
--

LOCK TABLES `roya_adelantetipoaplicacionfungicida` WRITE;
/*!40000 ALTER TABLE `roya_adelantetipoaplicacionfungicida` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantetipoaplicacionfungicida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantetipocafetos`
--

DROP TABLE IF EXISTS `roya_adelantetipocafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantetipocafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantetipocafetos`
--

LOCK TABLES `roya_adelantetipocafetos` WRITE;
/*!40000 ALTER TABLE `roya_adelantetipocafetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantetipocafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantetiposombra`
--

DROP TABLE IF EXISTS `roya_adelantetiposombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantetiposombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantetiposombra`
--

LOCK TABLES `roya_adelantetiposombra` WRITE;
/*!40000 ALTER TABLE `roya_adelantetiposombra` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantetiposombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_adelantetipovariedad`
--

DROP TABLE IF EXISTS `roya_adelantetipovariedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_adelantetipovariedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_adelantetipovariedad`
--

LOCK TABLES `roya_adelantetipovariedad` WRITE;
/*!40000 ALTER TABLE `roya_adelantetipovariedad` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_adelantetipovariedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_aplicacionfungicida`
--

DROP TABLE IF EXISTS `roya_aplicacionfungicida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_aplicacionfungicida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2012_id` int(11) NOT NULL,
  `tipo_2014_id` int(11) NOT NULL,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `dosis_2012` double NOT NULL,
  `dosis_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_aplicacionfungicida_2dd071ed` (`tipo_2012_id`),
  KEY `roya_aplicacionfungicida_903101ab` (`tipo_2014_id`),
  KEY `roya_aplicacionfungicida_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_aplicacionfungicida`
--

LOCK TABLES `roya_aplicacionfungicida` WRITE;
/*!40000 ALTER TABLE `roya_aplicacionfungicida` DISABLE KEYS */;
INSERT INTO `roya_aplicacionfungicida` VALUES (1,1,2,1,2,300,300,1);
/*!40000 ALTER TABLE `roya_aplicacionfungicida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_capacitacionessociales`
--

DROP TABLE IF EXISTS `roya_capacitacionessociales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_capacitacionessociales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_id` int(11) NOT NULL,
  `cuantas` int(11) NOT NULL,
  `profesor_id` int(11) NOT NULL,
  `gratis` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  `nivel` int(11),
  PRIMARY KEY (`id`),
  KEY `roya_capacitacionessociales_acf1eac4` (`tipo_id`),
  KEY `roya_capacitacionessociales_56d46bd1` (`profesor_id`),
  KEY `roya_capacitacionessociales_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_capacitacionessociales`
--

LOCK TABLES `roya_capacitacionessociales` WRITE;
/*!40000 ALTER TABLE `roya_capacitacionessociales` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_capacitacionessociales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_capacitacionessociales_metodologia`
--

DROP TABLE IF EXISTS `roya_capacitacionessociales_metodologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_capacitacionessociales_metodologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `capacitacionessociales_id` int(11) NOT NULL,
  `metodologia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_capacitaci_capacitacionessociales_id_26775605ae9cc781_uniq` (`capacitacionessociales_id`,`metodologia_id`),
  KEY `roya_capacitacionessociales_metodologia_ad019498` (`capacitacionessociales_id`),
  KEY `roya_capacitacionessociales_metodologia_3619a378` (`metodologia_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_capacitacionessociales_metodologia`
--

LOCK TABLES `roya_capacitacionessociales_metodologia` WRITE;
/*!40000 ALTER TABLE `roya_capacitacionessociales_metodologia` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_capacitacionessociales_metodologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_capacitacionestecnicas`
--

DROP TABLE IF EXISTS `roya_capacitacionestecnicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_capacitacionestecnicas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_id` int(11) NOT NULL,
  `cuantas` int(11) NOT NULL,
  `profesor_id` int(11) NOT NULL,
  `gratis` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  `nivel` int(11),
  PRIMARY KEY (`id`),
  KEY `roya_capacitacionestecnicas_acf1eac4` (`tipo_id`),
  KEY `roya_capacitacionestecnicas_56d46bd1` (`profesor_id`),
  KEY `roya_capacitacionestecnicas_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_capacitacionestecnicas`
--

LOCK TABLES `roya_capacitacionestecnicas` WRITE;
/*!40000 ALTER TABLE `roya_capacitacionestecnicas` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_capacitacionestecnicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_capacitacionestecnicas_metodologia`
--

DROP TABLE IF EXISTS `roya_capacitacionestecnicas_metodologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_capacitacionestecnicas_metodologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `capacitacionestecnicas_id` int(11) NOT NULL,
  `metodologia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_capacitaci_capacitacionestecnicas_id_4eb0254adc0ad635_uniq` (`capacitacionestecnicas_id`,`metodologia_id`),
  KEY `roya_capacitacionestecnicas_metodologia_11ef61dc` (`capacitacionestecnicas_id`),
  KEY `roya_capacitacionestecnicas_metodologia_3619a378` (`metodologia_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_capacitacionestecnicas_metodologia`
--

LOCK TABLES `roya_capacitacionestecnicas_metodologia` WRITE;
/*!40000 ALTER TABLE `roya_capacitacionestecnicas_metodologia` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_capacitacionestecnicas_metodologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_capacitor`
--

DROP TABLE IF EXISTS `roya_capacitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_capacitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_capacitor`
--

LOCK TABLES `roya_capacitor` WRITE;
/*!40000 ALTER TABLE `roya_capacitor` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_capacitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_combatir`
--

DROP TABLE IF EXISTS `roya_combatir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_combatir` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_combatir`
--

LOCK TABLES `roya_combatir` WRITE;
/*!40000 ALTER TABLE `roya_combatir` DISABLE KEYS */;
INSERT INTO `roya_combatir` VALUES (1,'Otros productores'),(2,'Técnico de la cooperativa o asociación'),(3,'Directivo de cooperativa'),(4,'Vendedor de Agroquímicos'),(5,'Técnicos de la empresas comercializadora'),(6,'Otros');
/*!40000 ALTER TABLE `roya_combatir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_detalleincidenciaroya`
--

DROP TABLE IF EXISTS `roya_detalleincidenciaroya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_detalleincidenciaroya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plantio_id` int(11) NOT NULL,
  `area` double NOT NULL,
  `planta` int(11) NOT NULL,
  `edad` double NOT NULL,
  `variedad` int(11) NOT NULL,
  `sombra` int(11) NOT NULL,
  `nivel` double NOT NULL,
  `dosis` double NOT NULL,
  `aplicaciones` double NOT NULL,
  `afectadas` double NOT NULL,
  `hojas` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_detalleincidenciaroya_face79d8` (`plantio_id`),
  KEY `roya_detalleincidenciaroya_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_detalleincidenciaroya`
--

LOCK TABLES `roya_detalleincidenciaroya` WRITE;
/*!40000 ALTER TABLE `roya_detalleincidenciaroya` DISABLE KEYS */;
INSERT INTO `roya_detalleincidenciaroya` VALUES (1,1,1.5,2,15,2,3,30,2,2,100,60,1),(2,2,1.5,3,15,1,3,20,2,2,100,100,1);
/*!40000 ALTER TABLE `roya_detalleincidenciaroya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_detalleincidenciaroya_fertilizacion`
--

DROP TABLE IF EXISTS `roya_detalleincidenciaroya_fertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_detalleincidenciaroya_fertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detalleincidenciaroya_id` int(11) NOT NULL,
  `tipofertilizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_detalleinci_detalleincidenciaroya_id_5f5c518ee018fee5_uniq` (`detalleincidenciaroya_id`,`tipofertilizacion_id`),
  KEY `roya_detalleincidenciaroya_fertilizacion_c569a614` (`detalleincidenciaroya_id`),
  KEY `roya_detalleincidenciaroya_fertilizacion_81f99d85` (`tipofertilizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_detalleincidenciaroya_fertilizacion`
--

LOCK TABLES `roya_detalleincidenciaroya_fertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_detalleincidenciaroya_fertilizacion` DISABLE KEYS */;
INSERT INTO `roya_detalleincidenciaroya_fertilizacion` VALUES (1,1,2),(2,2,2);
/*!40000 ALTER TABLE `roya_detalleincidenciaroya_fertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_detalleincidenciaroya_fungicidas`
--

DROP TABLE IF EXISTS `roya_detalleincidenciaroya_fungicidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_detalleincidenciaroya_fungicidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detalleincidenciaroya_id` int(11) NOT NULL,
  `tipofungicida_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_detalleinci_detalleincidenciaroya_id_10233fd8b502ddd7_uniq` (`detalleincidenciaroya_id`,`tipofungicida_id`),
  KEY `roya_detalleincidenciaroya_fungicidas_c569a614` (`detalleincidenciaroya_id`),
  KEY `roya_detalleincidenciaroya_fungicidas_dddeeea8` (`tipofungicida_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_detalleincidenciaroya_fungicidas`
--

LOCK TABLES `roya_detalleincidenciaroya_fungicidas` WRITE;
/*!40000 ALTER TABLE `roya_detalleincidenciaroya_fungicidas` DISABLE KEYS */;
INSERT INTO `roya_detalleincidenciaroya_fungicidas` VALUES (1,1,2),(2,2,2);
/*!40000 ALTER TABLE `roya_detalleincidenciaroya_fungicidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_fertilizacion`
--

DROP TABLE IF EXISTS `roya_fertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_fertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_fertilizacion`
--

LOCK TABLES `roya_fertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_fertilizacion` DISABLE KEYS */;
INSERT INTO `roya_fertilizacion` VALUES (1,'15-15-15'),(2,'8-5-10');
/*!40000 ALTER TABLE `roya_fertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_igual`
--

DROP TABLE IF EXISTS `roya_igual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_igual` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_igual`
--

LOCK TABLES `roya_igual` WRITE;
/*!40000 ALTER TABLE `roya_igual` DISABLE KEYS */;
INSERT INTO `roya_igual` VALUES (1,'No aplica');
/*!40000 ALTER TABLE `roya_igual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_impactoroya`
--

DROP TABLE IF EXISTS `roya_impactoroya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_impactoroya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `impacto_id` int(11) NOT NULL,
  `doce` double NOT NULL,
  `trece` double NOT NULL,
  `catorce` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_impactoroya_6c9deeb9` (`impacto_id`),
  KEY `roya_impactoroya_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_impactoroya`
--

LOCK TABLES `roya_impactoroya` WRITE;
/*!40000 ALTER TABLE `roya_impactoroya` DISABLE KEYS */;
INSERT INTO `roya_impactoroya` VALUES (1,1,3,3,2,1),(2,2,0,2,1,1),(3,3,3,1,1,1),(4,5,100,58.7,60.3,1),(5,6,0,0,1,1);
/*!40000 ALTER TABLE `roya_impactoroya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_impactos`
--

DROP TABLE IF EXISTS `roya_impactos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_impactos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_impactos`
--

LOCK TABLES `roya_impactos` WRITE;
/*!40000 ALTER TABLE `roya_impactos` DISABLE KEYS */;
INSERT INTO `roya_impactos` VALUES (1,'Área total de café en producción mz'),(2,'Área de café altamente afectada por roya  (más de 30% de plantas)'),(3,'Área  de café medianamente afectada por roya  (entre 10-30% plantas afectadas)'),(4,'Área rea de café altamente afectada por roya  (menos de 10% plantas afectadas)'),(5,'% reducción de la cosecha en comparación con año base 2011-12'),(6,'Área totalmente pérdida y que tenía que renovar');
/*!40000 ALTER TABLE `roya_impactos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_manejofertilizacion`
--

DROP TABLE IF EXISTS `roya_manejofertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_manejofertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2012_id` int(11) NOT NULL,
  `tipo_2014_id` int(11) NOT NULL,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_manejofertilizacion_2dd071ed` (`tipo_2012_id`),
  KEY `roya_manejofertilizacion_903101ab` (`tipo_2014_id`),
  KEY `roya_manejofertilizacion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_manejofertilizacion`
--

LOCK TABLES `roya_manejofertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_manejofertilizacion` DISABLE KEYS */;
INSERT INTO `roya_manejofertilizacion` VALUES (1,1,2,4,2,1);
/*!40000 ALTER TABLE `roya_manejofertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_manejosombra`
--

DROP TABLE IF EXISTS `roya_manejosombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_manejosombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2012_id` int(11) NOT NULL,
  `tipo_2014_id` int(11) NOT NULL,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_manejosombra_2dd071ed` (`tipo_2012_id`),
  KEY `roya_manejosombra_903101ab` (`tipo_2014_id`),
  KEY `roya_manejosombra_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_manejosombra`
--

LOCK TABLES `roya_manejosombra` WRITE;
/*!40000 ALTER TABLE `roya_manejosombra` DISABLE KEYS */;
INSERT INTO `roya_manejosombra` VALUES (1,1,2,0,0,1);
/*!40000 ALTER TABLE `roya_manejosombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_mas`
--

DROP TABLE IF EXISTS `roya_mas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_mas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_mas`
--

LOCK TABLES `roya_mas` WRITE;
/*!40000 ALTER TABLE `roya_mas` DISABLE KEYS */;
INSERT INTO `roya_mas` VALUES (1,'Mejor manejo de café');
/*!40000 ALTER TABLE `roya_mas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_menos`
--

DROP TABLE IF EXISTS `roya_menos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_menos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_menos`
--

LOCK TABLES `roya_menos` WRITE;
/*!40000 ALTER TABLE `roya_menos` DISABLE KEYS */;
INSERT INTO `roya_menos` VALUES (1,'No aplica');
/*!40000 ALTER TABLE `roya_menos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_metodologia`
--

DROP TABLE IF EXISTS `roya_metodologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_metodologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_metodologia`
--

LOCK TABLES `roya_metodologia` WRITE;
/*!40000 ALTER TABLE `roya_metodologia` DISABLE KEYS */;
INSERT INTO `roya_metodologia` VALUES (1,'Ch'),(2,'VF'),(3,'G'),(4,'Pr');
/*!40000 ALTER TABLE `roya_metodologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_nivelfinca`
--

DROP TABLE IF EXISTS `roya_nivelfinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_nivelfinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` int(11) NOT NULL,
  `variedades` int(11) NOT NULL,
  `produccion` int(11) NOT NULL,
  `igual_id` int(11) NOT NULL,
  `mas_id` int(11) NOT NULL,
  `menos_id` int(11) NOT NULL,
  `otros_productos` int(11) NOT NULL,
  `respuesta` longtext,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_nivelfinca_863d7899` (`igual_id`),
  KEY `roya_nivelfinca_4970bc10` (`mas_id`),
  KEY `roya_nivelfinca_b74af729` (`menos_id`),
  KEY `roya_nivelfinca_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_nivelfinca`
--

LOCK TABLES `roya_nivelfinca` WRITE;
/*!40000 ALTER TABLE `roya_nivelfinca` DISABLE KEYS */;
INSERT INTO `roya_nivelfinca` VALUES (1,1,1,3,1,1,1,2,'',1);
/*!40000 ALTER TABLE `roya_nivelfinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_nivelfinca_cuales`
--

DROP TABLE IF EXISTS `roya_nivelfinca_cuales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_nivelfinca_cuales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nivelfinca_id` int(11) NOT NULL,
  `variedades_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_nivelfinca_cuales_nivelfinca_id_72f19f55f7bd92c8_uniq` (`nivelfinca_id`,`variedades_id`),
  KEY `roya_nivelfinca_cuales_6653efa7` (`nivelfinca_id`),
  KEY `roya_nivelfinca_cuales_ee5d6666` (`variedades_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_nivelfinca_cuales`
--

LOCK TABLES `roya_nivelfinca_cuales` WRITE;
/*!40000 ALTER TABLE `roya_nivelfinca_cuales` DISABLE KEYS */;
INSERT INTO `roya_nivelfinca_cuales` VALUES (1,1,1),(2,1,2),(3,1,3);
/*!40000 ALTER TABLE `roya_nivelfinca_cuales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_nolegusta`
--

DROP TABLE IF EXISTS `roya_nolegusta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_nolegusta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `porque` longtext NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_nolegusta_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_nolegusta`
--

LOCK TABLES `roya_nolegusta` WRITE;
/*!40000 ALTER TABLE `roya_nolegusta` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_nolegusta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_nolegusta_metodologia`
--

DROP TABLE IF EXISTS `roya_nolegusta_metodologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_nolegusta_metodologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nolegusta_id` int(11) NOT NULL,
  `metodologia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_nolegusta_metodologia_nolegusta_id_26d749219b1e2d6f_uniq` (`nolegusta_id`,`metodologia_id`),
  KEY `roya_nolegusta_metodologia_fc93c529` (`nolegusta_id`),
  KEY `roya_nolegusta_metodologia_3619a378` (`metodologia_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_nolegusta_metodologia`
--

LOCK TABLES `roya_nolegusta_metodologia` WRITE;
/*!40000 ALTER TABLE `roya_nolegusta_metodologia` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_nolegusta_metodologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_nuevosproductos`
--

DROP TABLE IF EXISTS `roya_nuevosproductos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_nuevosproductos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_id` int(11) NOT NULL,
  `frecuencia` double NOT NULL,
  `cantidad` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_nuevosproductos_1635d9bd` (`producto_id`),
  KEY `roya_nuevosproductos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_nuevosproductos`
--

LOCK TABLES `roya_nuevosproductos` WRITE;
/*!40000 ALTER TABLE `roya_nuevosproductos` DISABLE KEYS */;
INSERT INTO `roya_nuevosproductos` VALUES (1,1,1,300,1),(2,2,1,300,1);
/*!40000 ALTER TABLE `roya_nuevosproductos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_oriento`
--

DROP TABLE IF EXISTS `roya_oriento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_oriento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_oriento_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_oriento`
--

LOCK TABLES `roya_oriento` WRITE;
/*!40000 ALTER TABLE `roya_oriento` DISABLE KEYS */;
INSERT INTO `roya_oriento` VALUES (1,1);
/*!40000 ALTER TABLE `roya_oriento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_oriento_opcion`
--

DROP TABLE IF EXISTS `roya_oriento_opcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_oriento_opcion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oriento_id` int(11) NOT NULL,
  `combatir_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_oriento_opcion_oriento_id_55f6a31ac4d1b690_uniq` (`oriento_id`,`combatir_id`),
  KEY `roya_oriento_opcion_30dfbf50` (`oriento_id`),
  KEY `roya_oriento_opcion_129c6681` (`combatir_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_oriento_opcion`
--

LOCK TABLES `roya_oriento_opcion` WRITE;
/*!40000 ALTER TABLE `roya_oriento_opcion` DISABLE KEYS */;
INSERT INTO `roya_oriento_opcion` VALUES (1,1,4);
/*!40000 ALTER TABLE `roya_oriento_opcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_plantio`
--

DROP TABLE IF EXISTS `roya_plantio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_plantio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_plantio`
--

LOCK TABLES `roya_plantio` WRITE;
/*!40000 ALTER TABLE `roya_plantio` DISABLE KEYS */;
INSERT INTO `roya_plantio` VALUES (1,'Sinai'),(2,'Lote');
/*!40000 ALTER TABLE `roya_plantio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_podacafetos`
--

DROP TABLE IF EXISTS `roya_podacafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_podacafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2012_id` int(11) NOT NULL,
  `tipo_2014_id` int(11) NOT NULL,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_podacafetos_2dd071ed` (`tipo_2012_id`),
  KEY `roya_podacafetos_903101ab` (`tipo_2014_id`),
  KEY `roya_podacafetos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_podacafetos`
--

LOCK TABLES `roya_podacafetos` WRITE;
/*!40000 ALTER TABLE `roya_podacafetos` DISABLE KEYS */;
INSERT INTO `roya_podacafetos` VALUES (1,3,2,0,0,1);
/*!40000 ALTER TABLE `roya_podacafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_productos`
--

DROP TABLE IF EXISTS `roya_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_productos`
--

LOCK TABLES `roya_productos` WRITE;
/*!40000 ALTER TABLE `roya_productos` DISABLE KEYS */;
INSERT INTO `roya_productos` VALUES (1,'Topacio'),(2,'Fungomac');
/*!40000 ALTER TABLE `roya_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_recepocafetos`
--

DROP TABLE IF EXISTS `roya_recepocafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_recepocafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_recepocafetos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_recepocafetos`
--

LOCK TABLES `roya_recepocafetos` WRITE;
/*!40000 ALTER TABLE `roya_recepocafetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `roya_recepocafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_renovacioncafetales`
--

DROP TABLE IF EXISTS `roya_renovacioncafetales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_renovacioncafetales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_2012_id` int(11) NOT NULL,
  `tipo_2014_id` int(11) NOT NULL,
  `mz_2012` double NOT NULL,
  `mz_2014` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_renovacioncafetales_2dd071ed` (`tipo_2012_id`),
  KEY `roya_renovacioncafetales_903101ab` (`tipo_2014_id`),
  KEY `roya_renovacioncafetales_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_renovacioncafetales`
--

LOCK TABLES `roya_renovacioncafetales` WRITE;
/*!40000 ALTER TABLE `roya_renovacioncafetales` DISABLE KEYS */;
INSERT INTO `roya_renovacioncafetales` VALUES (1,1,2,0,0,1);
/*!40000 ALTER TABLE `roya_renovacioncafetales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_silegusta`
--

DROP TABLE IF EXISTS `roya_silegusta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_silegusta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `porque` longtext NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roya_silegusta_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_silegusta`
--

LOCK TABLES `roya_silegusta` WRITE;
/*!40000 ALTER TABLE `roya_silegusta` DISABLE KEYS */;
INSERT INTO `roya_silegusta` VALUES (1,'En la visita aldo en los lugares y veo como lo hacen',1);
/*!40000 ALTER TABLE `roya_silegusta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_silegusta_metodologia`
--

DROP TABLE IF EXISTS `roya_silegusta_metodologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_silegusta_metodologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `silegusta_id` int(11) NOT NULL,
  `metodologia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roya_silegusta_metodologia_silegusta_id_21ef2e1b5216a30d_uniq` (`silegusta_id`,`metodologia_id`),
  KEY `roya_silegusta_metodologia_7eb6384e` (`silegusta_id`),
  KEY `roya_silegusta_metodologia_3619a378` (`metodologia_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_silegusta_metodologia`
--

LOCK TABLES `roya_silegusta_metodologia` WRITE;
/*!40000 ALTER TABLE `roya_silegusta_metodologia` DISABLE KEYS */;
INSERT INTO `roya_silegusta_metodologia` VALUES (1,1,2);
/*!40000 ALTER TABLE `roya_silegusta_metodologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_temassociales`
--

DROP TABLE IF EXISTS `roya_temassociales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_temassociales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_temassociales`
--

LOCK TABLES `roya_temassociales` WRITE;
/*!40000 ALTER TABLE `roya_temassociales` DISABLE KEYS */;
INSERT INTO `roya_temassociales` VALUES (1,'Formación y fortalecimiento organizacional'),(2,'Contabilidad básica y administración'),(3,'Manejo de créditos'),(4,'Administración de pequeños negocios'),(5,'Gestión empresarial'),(6,'Registro de datos de la finca'),(7,'Certificación de cafe');
/*!40000 ALTER TABLE `roya_temassociales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipoaplicacionfungicida`
--

DROP TABLE IF EXISTS `roya_tipoaplicacionfungicida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipoaplicacionfungicida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipoaplicacionfungicida`
--

LOCK TABLES `roya_tipoaplicacionfungicida` WRITE;
/*!40000 ALTER TABLE `roya_tipoaplicacionfungicida` DISABLE KEYS */;
INSERT INTO `roya_tipoaplicacionfungicida` VALUES (1,'Alto 10'),(2,'Topacio');
/*!40000 ALTER TABLE `roya_tipoaplicacionfungicida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipocafetos`
--

DROP TABLE IF EXISTS `roya_tipocafetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipocafetos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipocafetos`
--

LOCK TABLES `roya_tipocafetos` WRITE;
/*!40000 ALTER TABLE `roya_tipocafetos` DISABLE KEYS */;
INSERT INTO `roya_tipocafetos` VALUES (1,'Poda Sanitaria'),(2,'Poda Selectiva'),(3,'Poda Selectiva');
/*!40000 ALTER TABLE `roya_tipocafetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipocapacitaciones`
--

DROP TABLE IF EXISTS `roya_tipocapacitaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipocapacitaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipocapacitaciones`
--

LOCK TABLES `roya_tipocapacitaciones` WRITE;
/*!40000 ALTER TABLE `roya_tipocapacitaciones` DISABLE KEYS */;
INSERT INTO `roya_tipocapacitaciones` VALUES (1,'Variedades de café'),(2,'Manejo de  semillero y vivero'),(3,'Establecimiento y manejo de café'),(4,'Manejo de cosecha de café'),(5,'Manejo de plagas y enfermedades de café'),(6,'Manejo de roya del café'),(7,'Planificación de la finca'),(8,'Diversificación de la fina y cafetales');
/*!40000 ALTER TABLE `roya_tipocapacitaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipofertilizacion`
--

DROP TABLE IF EXISTS `roya_tipofertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipofertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipofertilizacion`
--

LOCK TABLES `roya_tipofertilizacion` WRITE;
/*!40000 ALTER TABLE `roya_tipofertilizacion` DISABLE KEYS */;
INSERT INTO `roya_tipofertilizacion` VALUES (1,'Org'),(2,'Quim'),(3,'Quim+Org'),(4,'Biof'),(5,'RM');
/*!40000 ALTER TABLE `roya_tipofertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipofungicida`
--

DROP TABLE IF EXISTS `roya_tipofungicida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipofungicida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipofungicida`
--

LOCK TABLES `roya_tipofungicida` WRITE;
/*!40000 ALTER TABLE `roya_tipofungicida` DISABLE KEYS */;
INSERT INTO `roya_tipofungicida` VALUES (1,'Q Prev'),(2,'Q Sist'),(3,'Orgánico');
/*!40000 ALTER TABLE `roya_tipofungicida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tiposombra`
--

DROP TABLE IF EXISTS `roya_tiposombra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tiposombra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tiposombra`
--

LOCK TABLES `roya_tiposombra` WRITE;
/*!40000 ALTER TABLE `roya_tiposombra` DISABLE KEYS */;
INSERT INTO `roya_tiposombra` VALUES (1,'30% regulada Guaba'),(2,'30% Regulada Guaba');
/*!40000 ALTER TABLE `roya_tiposombra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_tipovariedad`
--

DROP TABLE IF EXISTS `roya_tipovariedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_tipovariedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_tipovariedad`
--

LOCK TABLES `roya_tipovariedad` WRITE;
/*!40000 ALTER TABLE `roya_tipovariedad` DISABLE KEYS */;
INSERT INTO `roya_tipovariedad` VALUES (1,'Caturra'),(2,'Catimor');
/*!40000 ALTER TABLE `roya_tipovariedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roya_variedades`
--

DROP TABLE IF EXISTS `roya_variedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roya_variedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roya_variedades`
--

LOCK TABLES `roya_variedades` WRITE;
/*!40000 ALTER TABLE `roya_variedades` DISABLE KEYS */;
INSERT INTO `roya_variedades` VALUES (1,'Caturra'),(2,'Pacamara'),(3,'Catimor');
/*!40000 ALTER TABLE `roya_variedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'encuesta','0001_initial','2013-11-19 03:24:45'),(2,'produccion_finca','0001_initial','2013-11-19 03:24:45'),(3,'vulnerabilidades_finca','0001_initial','2013-11-19 03:24:46'),(4,'produccion_cafe_finca','0001_initial','2013-11-19 03:24:47'),(5,'roya','0001_initial','2013-11-19 03:24:48'),(6,'roya','0002_auto__add_field_capacitacionessociales_nivel__add_field_capacitaciones','2013-11-19 05:15:13');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_causa`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_causa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_causa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_causa`
--

LOCK TABLES `vulnerabilidades_finca_causa` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_causa` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_causa` VALUES (1,'Aspectos agrícolas'),(2,'Aspectos productivos'),(3,'Aspectos  del mercado'),(4,'Aspectos de financiamiento');
/*!40000 ALTER TABLE `vulnerabilidades_finca_causa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_elclima`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_elclima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_elclima` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clima_id` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_elclima_f8f116f3` (`clima_id`),
  KEY `vulnerabilidades_finca_elclima_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_elclima`
--

LOCK TABLES `vulnerabilidades_finca_elclima` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_elclima` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_elclima` VALUES (1,2,1),(2,6,1),(3,10,1);
/*!40000 ALTER TABLE `vulnerabilidades_finca_elclima` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_elclima_fecha`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_elclima_fecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_elclima_fecha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `elclima_id` int(11) NOT NULL,
  `tipoyear_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_elclima__elclima_id_aa8ef6d4a663eb7_uniq` (`elclima_id`,`tipoyear_id`),
  KEY `vulnerabilidades_finca_elclima_fecha_313ffee9` (`elclima_id`),
  KEY `vulnerabilidades_finca_elclima_fecha_4395c05f` (`tipoyear_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_elclima_fecha`
--

LOCK TABLES `vulnerabilidades_finca_elclima_fecha` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_elclima_fecha` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_elclima_fecha` VALUES (1,1,3),(2,2,3),(3,3,1),(4,3,2);
/*!40000 ALTER TABLE `vulnerabilidades_finca_elclima_fecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_lasplagas_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas` VALUES (1,2013,1);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_antracnosis`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_antracnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_antracnosis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspla_lasplagas_id_75da3b9231e5eb8_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_antracnosis_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_antracnosis_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_antracnosis`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_antracnosis` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_antracnosis` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_antracnosis` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_antracnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_broca`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_broca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_broca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspl_lasplagas_id_3e3473fd756695cc_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_broca_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_broca_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_broca`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_broca` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_broca` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_broca` VALUES (1,1,7);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_broca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_gallo`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_gallo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_gallo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspl_lasplagas_id_4b4d67b180c155d0_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_gallo_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_gallo_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_gallo`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_gallo` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_gallo` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_gallo` VALUES (1,1,3),(2,1,6);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_gallo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_hierro`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_hierro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_hierro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspl_lasplagas_id_466e0e9f541aa821_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_hierro_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_hierro_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_hierro`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_hierro` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_hierro` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_hierro` VALUES (1,1,3),(2,1,5);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_hierro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_nematodos`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_nematodos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_nematodos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspl_lasplagas_id_2f58bb5d65d86595_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_nematodos_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_nematodos_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_nematodos`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_nematodos` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_nematodos` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_nematodos` VALUES (1,1,1),(2,1,5);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_nematodos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_lasplagas_roya`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_lasplagas_roya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_lasplagas_roya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lasplagas_id` int(11) NOT NULL,
  `plagas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_laspla_lasplagas_id_da91227a5452d9d_uniq` (`lasplagas_id`,`plagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_roya_63a28486` (`lasplagas_id`),
  KEY `vulnerabilidades_finca_lasplagas_roya_b949f61c` (`plagas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_lasplagas_roya`
--

LOCK TABLES `vulnerabilidades_finca_lasplagas_roya` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_roya` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_lasplagas_roya` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `vulnerabilidades_finca_lasplagas_roya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_mitigacion`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_mitigacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_mitigacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monitoreo_plagas` int(11) NOT NULL,
  `cada_cuanto` int(11) NOT NULL,
  `como_realiza` int(11) NOT NULL,
  `registro_monitoreo` int(11) NOT NULL,
  `recursos` int(11) NOT NULL,
  `falta_recursos` int(11) NOT NULL,
  `almacenamiento` int(11) NOT NULL,
  `forma_organizada` int(11) NOT NULL,
  `contrato` int(11) NOT NULL,
  `certificado` int(11) NOT NULL,
  `tipo_certificado` int(11) NOT NULL,
  `reconocida` int(11) NOT NULL,
  `infraestructura` int(11) NOT NULL,
  `plan_manejo` int(11) NOT NULL,
  `plan_negocio` int(11) NOT NULL,
  `plan_inversion` int(11) NOT NULL,
  `elaborar` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_mitigacion_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_mitigacion`
--

LOCK TABLES `vulnerabilidades_finca_mitigacion` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_mitigacion` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_mitigacion` VALUES (1,1,1,1,2,2,1,2,2,1,2,1,1,1,2,2,2,1,1);
/*!40000 ALTER TABLE `vulnerabilidades_finca_mitigacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_opciones`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_opciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_opciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `causa_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_opciones_5267e5b6` (`causa_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_opciones`
--

LOCK TABLES `vulnerabilidades_finca_opciones` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_opciones` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_opciones` VALUES (1,1,'Las variedades no son adecuada'),(2,1,'Hay Falta de semilla'),(3,1,'Las semillas con de mala calidad'),(4,1,'Manejo de cultivo no adecuado'),(5,1,'Fertilización no adecuada'),(6,1,'Muchos daños de plagas y enfermedades'),(7,2,'Producción de café baja'),(8,2,'Poca floración'),(9,2,'Mucho abono'),(10,2,'Mucha caída de frutos'),(11,2,'Marcada bianualidad'),(12,2,'Mala recolección de frutos'),(13,2,'Falta de mano de obra para el  corte'),(14,2,'Beneficiado húmedo no adecuado'),(15,3,'Bajo precio de café'),(16,3,'Falta de venta'),(17,3,'Estafa de contrato'),(18,3,'Mala calidad de café'),(19,3,'Pagos atrasados'),(20,3,'Problema de traslado de cosecha'),(21,4,'Disponibilidad de crédito de corto plazo'),(22,4,'Disponibilidad de crédito mediano plazo'),(23,4,'Disponibilidad de crédito largo plazo'),(24,4,'Altos interés de los crédito');
/*!40000 ALTER TABLE `vulnerabilidades_finca_opciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_otroriesgos`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_otroriesgos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_otroriesgos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `motivo_id` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_otroriesgos_590ecb5a` (`motivo_id`),
  KEY `vulnerabilidades_finca_otroriesgos_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_otroriesgos`
--

LOCK TABLES `vulnerabilidades_finca_otroriesgos` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_otroriesgos` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_otroriesgos` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,10,1),(11,11,1),(12,12,1),(13,13,1),(14,14,1),(15,15,1),(16,16,1),(17,17,1),(18,18,1),(19,19,1),(20,20,1),(21,21,1),(22,22,1),(23,23,1),(24,24,1);
/*!40000 ALTER TABLE `vulnerabilidades_finca_otroriesgos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_otroriesgos_respuesta`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_otroriesgos_respuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_otroriesgos_respuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `otroriesgos_id` int(11) NOT NULL,
  `respuestas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilidades_finca_otro_otroriesgos_id_3f293f2c05633a0_uniq` (`otroriesgos_id`,`respuestas_id`),
  KEY `vulnerabilidades_finca_otroriesgos_respuesta_234928c4` (`otroriesgos_id`),
  KEY `vulnerabilidades_finca_otroriesgos_respuesta_f66cc077` (`respuestas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_otroriesgos_respuesta`
--

LOCK TABLES `vulnerabilidades_finca_otroriesgos_respuesta` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_otroriesgos_respuesta` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_otroriesgos_respuesta` VALUES (1,1,5),(2,2,3),(3,3,3),(4,4,1),(5,5,1),(6,6,2),(7,7,1),(8,8,2),(9,9,2),(10,10,3),(11,11,1),(12,12,3),(13,13,3),(14,14,3),(15,15,2),(16,16,3),(17,17,3),(18,18,3),(19,19,3),(20,20,3),(21,21,1),(22,22,3),(23,23,3),(24,24,3);
/*!40000 ALTER TABLE `vulnerabilidades_finca_otroriesgos_respuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_plagas`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_plagas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_plagas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_plagas`
--

LOCK TABLES `vulnerabilidades_finca_plagas` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_plagas` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_plagas` VALUES (1,'Alta incidencia'),(2,'Media incidencia'),(3,'Baja incidencia'),(4,'Todos los plations'),(5,'Varios Plantios'),(6,'Algunos plantios'),(7,'Ningún plantio');
/*!40000 ALTER TABLE `vulnerabilidades_finca_plagas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_respuestas`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_respuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_respuestas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_respuestas`
--

LOCK TABLES `vulnerabilidades_finca_respuestas` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_respuestas` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_respuestas` VALUES (1,'Siempre'),(2,'A veces'),(3,'Nunca'),(4,'Si'),(5,'No');
/*!40000 ALTER TABLE `vulnerabilidades_finca_respuestas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_suelofertilidad`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_suelofertilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_suelofertilidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `textura` int(11) NOT NULL,
  `profundidad` int(11) NOT NULL,
  `presencia` int(11) NOT NULL,
  `abundancia` int(11) NOT NULL,
  `pendiente` int(11) NOT NULL,
  `drenaje` int(11) NOT NULL,
  `materia_organica` int(11) NOT NULL,
  `preparan` int(11) NOT NULL,
  `fertilidad` int(11) NOT NULL,
  `foliar` int(11) NOT NULL,
  `fertilizacion` int(11) NOT NULL,
  `conservacion` int(11) NOT NULL,
  `obra_conservacion` int(11) NOT NULL,
  `fertil` int(11) NOT NULL,
  `degrados` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vulnerabilidades_finca_suelofertilidad_6d5d17e3` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_suelofertilidad`
--

LOCK TABLES `vulnerabilidades_finca_suelofertilidad` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_suelofertilidad` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_suelofertilidad` VALUES (1,3,3,3,1,3,1,2,3,2,2,1,2,5,2,2,1);
/*!40000 ALTER TABLE `vulnerabilidades_finca_suelofertilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_tipoclima`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_tipoclima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_tipoclima` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_tipoclima`
--

LOCK TABLES `vulnerabilidades_finca_tipoclima` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_tipoclima` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_tipoclima` VALUES (1,'Alta temperatura que daño las plantas y cosecha'),(2,'Baja temperatura que daño las plantas y cosecha'),(3,'Exceso de lluvia que daño las plantas y cosecha'),(4,'Inundaciones que daño las plantas y cosecha'),(5,'Falta de lluvia que daño las plantas y cosecha'),(6,'Vientos muy fuertes que daño las plantas'),(7,'Deslizamiento de tierra que daño los plantíos'),(8,'El clima se descontrolo para hacer un buen manejo'),(9,'El clima se descontrolo para hacer un buen corte'),(10,'Hubo demasiada humedad que afecto las plantas y cosecha'),(11,'Hubo poca humedad y afecto las plantas y cosecha');
/*!40000 ALTER TABLE `vulnerabilidades_finca_tipoclima` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vulnerabilidades_finca_tipoyear`
--

DROP TABLE IF EXISTS `vulnerabilidades_finca_tipoyear`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerabilidades_finca_tipoyear` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades_finca_tipoyear`
--

LOCK TABLES `vulnerabilidades_finca_tipoyear` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades_finca_tipoyear` DISABLE KEYS */;
INSERT INTO `vulnerabilidades_finca_tipoyear` VALUES (1,'2013'),(2,'2012'),(3,'2011'),(4,'2010'),(5,'2009');
/*!40000 ALTER TABLE `vulnerabilidades_finca_tipoyear` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-11-25 22:11:25
