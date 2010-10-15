-- MySQL dump 10.13  Distrib 5.1.49, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: simasnio_fed
-- ------------------------------------------------------
-- Server version	5.1.49-1ubuntu8

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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=115 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=163 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `encuesta_accionefectuadadocumento`
--

DROP TABLE IF EXISTS `encuesta_accionefectuadadocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionefectuadadocumento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cantidad` int(11),
  `participantes` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionefectuadadocumento_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionefectuadamedio`
--

DROP TABLE IF EXISTS `encuesta_accionefectuadamedio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionefectuadamedio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cantidad` int(11),
  `participantes` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionefectuadamedio_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionefectuadaregion`
--

DROP TABLE IF EXISTS `encuesta_accionefectuadaregion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionefectuadaregion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cantidad` int(11),
  `participantes` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionefectuadaregion_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionfortalececapacidad`
--

DROP TABLE IF EXISTS `encuesta_accionfortalececapacidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionfortalececapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `acciones` int(11),
  `participantes` int(11),
  `acciones_efectivas` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionfortalececapacidad_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionfortalececapadmitiva`
--

DROP TABLE IF EXISTS `encuesta_accionfortalececapadmitiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionfortalececapadmitiva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `mejorar_sistema` int(11),
  `mejorar_plan` int(11),
  `mejorar_apoyo` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionfortalececapadmitiva_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionimpulsadagrupo`
--

DROP TABLE IF EXISTS `encuesta_accionimpulsadagrupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionimpulsadagrupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `acciones_emprendidas_sex` int(11),
  `acciones_cambio_sex` int(11),
  `acciones_emprendidas_discapa` int(11),
  `acciones_cambio_discapa` int(11),
  `acciones_emprendidas_etnia` int(11),
  `acciones_cambio_etnia` int(11),
  `acciones_emprendidas_jovenes` int(11),
  `acciones_cambio_jovenes` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionimpulsadagrupo_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionimpulsadaorg`
--

DROP TABLE IF EXISTS `encuesta_accionimpulsadaorg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionimpulsadaorg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `acciones_emprendidas` int(11),
  `acciones_cambios_actitud` int(11),
  `acciones_impulsadas_masculinidad` int(11),
  `acciones_cambios_masculinidad` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionimpulsadaorg_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionobservatorio`
--

DROP TABLE IF EXISTS `encuesta_accionobservatorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionobservatorio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cantidad_observatorios` int(11),
  `cantidad_acciones_realiz` int(11),
  `cantidad_acciones_web` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionobservatorio_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionpromuevenintercambio`
--

DROP TABLE IF EXISTS `encuesta_accionpromuevenintercambio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionpromuevenintercambio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `acciones_org_part` int(11),
  `participantes` int(11),
  `acciones_efectivas` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionpromuevenintercambio_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionrealizadareflexion`
--

DROP TABLE IF EXISTS `encuesta_accionrealizadareflexion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionrealizadareflexion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `mujeres` int(11),
  `hombres` int(11),
  `jovenes` int(11),
  `div_sexual` int(11),
  `vih` int(11),
  `etnica` int(11),
  `discapacidad` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionrealizadareflexion_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_accionrelizadareflexionpersona`
--

DROP TABLE IF EXISTS `encuesta_accionrelizadareflexionpersona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_accionrelizadareflexionpersona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `mujeres` int(11),
  `hombres` int(11),
  `jovenes` int(11),
  `div_sexual` int(11),
  `vih` int(11),
  `etnica` int(11),
  `discapacidad` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_accionrelizadareflexionpersona_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_atencionvictima`
--

DROP TABLE IF EXISTS `encuesta_atencionvictima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_atencionvictima` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `servicio_salud` int(11),
  `servicio_psicologia` int(11),
  `servicio_legal` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_atencionvictima_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_atencionvictimaalbergue`
--

DROP TABLE IF EXISTS `encuesta_atencionvictimaalbergue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_atencionvictimaalbergue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `mujeres` int(11),
  `jovenes` int(11),
  `ninos_ninas` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_atencionvictimaalbergue_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_denunciajuridica`
--

DROP TABLE IF EXISTS `encuesta_denunciajuridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_denunciajuridica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `persona_div_sexual` int(11),
  `persona_discapacidad` int(11),
  `persona_vih` int(11),
  `persona_racial` int(11),
  `persona_joven` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_denunciajuridica_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_denunciasocialefectiva`
--

DROP TABLE IF EXISTS `encuesta_denunciasocialefectiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_denunciasocialefectiva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `persona_div_sexual` int(11),
  `persona_discapacidad` int(11),
  `persona_vih` int(11),
  `persona_racial` int(11),
  `persona_joven` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_denunciasocialefectiva_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_denunciasocialrealizada`
--

DROP TABLE IF EXISTS `encuesta_denunciasocialrealizada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_denunciasocialrealizada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `persona_div_sexual` int(11),
  `persona_discapacidad` int(11),
  `persona_vih` int(11),
  `persona_racial` int(11),
  `persona_joven` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_denunciasocialrealizada_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_denunciaviolencia`
--

DROP TABLE IF EXISTS `encuesta_denunciaviolencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_denunciaviolencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `comisariato` int(11),
  `fiscalia` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_denunciaviolencia_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_encuesta`
--

DROP TABLE IF EXISTS `encuesta_encuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_encuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacion_id` int(11) NOT NULL,
  `proyecto_id` int(11) NOT NULL,
  `periodo` int(11) NOT NULL,
  `anio` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_encuesta_48753264` (`organizacion_id`),
  KEY `encuesta_encuesta_30b52635` (`proyecto_id`),
  KEY `encuesta_encuesta_403f60f` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_estadocapacidadadmitiva`
--

DROP TABLE IF EXISTS `encuesta_estadocapacidadadmitiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_estadocapacidadadmitiva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sistema` varchar(100),
  `plan` varchar(100),
  `organizaciones` varchar(100),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_estadocapacidadadmitiva_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_indicador`
--

DROP TABLE IF EXISTS `encuesta_indicador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_indicador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resultado_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `encuesta_indicador_e633356` (`resultado_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_organizacion`
--

DROP TABLE IF EXISTS `encuesta_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_corto` varchar(100) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `correo` varchar(75),
  `contacto` varchar(200),
  `telefono` varchar(200),
  `antecedentes` longtext NOT NULL,
  `nombre` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_participacioncomisionagenda`
--

DROP TABLE IF EXISTS `encuesta_participacioncomisionagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_participacioncomisionagenda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cat_instancias` int(11),
  `cant_acc_prom` int(11),
  `cant_acc_efec` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_participacioncomisionagenda_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_participacioncomisiondecision`
--

DROP TABLE IF EXISTS `encuesta_participacioncomisiondecision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_participacioncomisiondecision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `cantidad_instancias` int(11),
  `cantidad_acciones_promovidas` int(11),
  `cantidad_acciones_efectivas` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_participacioncomisiondecision_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_proyecto`
--

DROP TABLE IF EXISTS `encuesta_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_proyecto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacion_id` int(11) NOT NULL,
  `codigo` varchar(150),
  `cobertura` longtext NOT NULL,
  `duracion` varchar(30) NOT NULL,
  `monto` varchar(100),
  `monto2` varchar(100),
  `nombre` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_proyecto_48753264` (`organizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_referenciacontraref`
--

DROP TABLE IF EXISTS `encuesta_referenciacontraref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_referenciacontraref` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accion` varchar(100),
  `mujeres` int(11),
  `jovenes` int(11),
  `ninos_ninas` int(11),
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_referenciacontraref_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_resultado`
--

DROP TABLE IF EXISTS `encuesta_resultado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_resultado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_resultadotrabajado`
--

DROP TABLE IF EXISTS `encuesta_resultadotrabajado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_resultadotrabajado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resultado_id` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `encuesta_resultadotrabajado_e633356` (`resultado_id`),
  KEY `encuesta_resultadotrabajado_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `encuesta_resultadotrabajado_municipio`
--

DROP TABLE IF EXISTS `encuesta_resultadotrabajado_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encuesta_resultadotrabajado_municipio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resultadotrabajado_id` int(11) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resultadotrabajado_id` (`resultadotrabajado_id`,`municipio_id`),
  KEY `encuesta_resultadotrabajado_municipio_56d0d6eb` (`resultadotrabajado_id`),
  KEY `encuesta_resultadotrabajado_municipio_cebc556` (`municipio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=321 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `latitud` decimal(8,5),
  `longitud` decimal(8,5),
  `extension` decimal(10,2),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_779a4ea6` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-10-15 14:04:41
