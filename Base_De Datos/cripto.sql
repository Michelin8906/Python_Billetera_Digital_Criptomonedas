-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 30-11-2020 a las 05:10:06
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cripto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `code_cripto`
--

DROP TABLE IF EXISTS `code_cripto`;
CREATE TABLE IF NOT EXISTS `code_cripto` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Code` text NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `code_cripto`
--

INSERT INTO `code_cripto` (`Id`, `Code`) VALUES
(1, 'ATOM'),
(2, 'ATOM'),
(3, 'BAT'),
(4, 'BCH'),
(5, 'BNB'),
(6, 'BTC'),
(7, 'BUSD'),
(8, 'DASH'),
(9, 'EOS'),
(10, 'ETH'),
(11, 'LTC'),
(12, 'NANO'),
(13, 'PAX'),
(14, 'TRX'),
(15, 'TUSD'),
(16, 'USDT'),
(17, 'XLM'),
(18, 'XRP');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `criptomonedas`
--

DROP TABLE IF EXISTS `criptomonedas`;
CREATE TABLE IF NOT EXISTS `criptomonedas` (
  `Name_Crip` text,
  `Cant` int(11) DEFAULT NULL,
  `Cod_Usu` text,
  `Date` text
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `criptomonedas`
--

INSERT INTO `criptomonedas` (`Name_Crip`, `Cant`, `Cod_Usu`, `Date`) VALUES
('BNB', 16, 'Michael', '2020-05-18 00:27:41.163158'),
('BTC', 16, 'Michael', '2020-11-30 00:09:07.042112'),
('ETH', 19, 'Michael', '2020-05-17 17:30:01.847021'),
('BNB', 42, 'Betsy', '2020-05-17 23:52:54.640571'),
('BTC', 25, 'Betsy', '2020-11-30 00:09:09.269348'),
('ETH', 13, 'Betsy', '2020-04-16 22:58:53.741181'),
('LTC', 10, 'Betsy', '2020-01-16 22:58:53.741181'),
('ETH', 20, 'Carlos', '2020-05-17 17:28:05.381135'),
('BNB', 20, 'Carlos', '2020-05-18 00:27:50.291929'),
('BTC', 11, 'Carlos', '2020-02-01 22:58:53.741181'),
('LTC', 16, 'Carlos', '2020-04-16 22:58:53.741181'),
('BNB', 30, 'Diego', '2020-01-16 22:58:53.741181'),
('BTC', 12, 'Diego', '2020-04-16 22:58:53.741181'),
('ETH', 13, 'Diego', '2020-05-17 17:30:03.299829'),
('TRX', 19, 'Diego', '2020-02-01 22:58:53.741181'),
('LTC', 14, 'Diego', '2020-05-16 23:27:34.720913'),
('LTC', 5, 'Michael', '2020-05-16 23:27:36.978221');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

DROP TABLE IF EXISTS `historial`;
CREATE TABLE IF NOT EXISTS `historial` (
  `Nombre_Envia` text NOT NULL,
  `Nombre_Recibe` text NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `Nombre_Cripto` text NOT NULL,
  `Fecha_Envio` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `historial`
--

INSERT INTO `historial` (`Nombre_Envia`, `Nombre_Recibe`, `Cantidad`, `Nombre_Cripto`, `Fecha_Envio`) VALUES
('Michael', 'Betsy', 4, 'BTC', '2020-05-16 22:53:04.459467'),
('Diego', 'Michael', 5, 'LTC', '2020-05-16 23:27:36.978221'),
('Michael', 'Carlos', 5, 'ETH', '2020-05-17 17:28:05.381135'),
('Michael', 'Diego', 2, 'ETH', '2020-05-17 17:29:36.453484'),
('Michael', 'Diego', 2, 'ETH', '2020-05-17 17:29:49.452670'),
('Michael', 'Diego', 2, 'ETH', '2020-05-17 17:30:03.299829'),
('Michael', 'Betsy', 2, 'BNB', '2020-05-17 23:52:54.640571'),
('Michael', 'Carlos', 2, 'BNB', '2020-05-18 00:27:50.291929'),
('Michael', 'Betsy', 1, 'BTC', '2020-11-30 00:09:09.269348');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `ID_USU` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario` text,
  `Contraseña` text,
  PRIMARY KEY (`ID_USU`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`ID_USU`, `Usuario`, `Contraseña`) VALUES
(1, 'Michael', '1234'),
(2, 'Carlos', '1234'),
(3, 'Betsy', '1234'),
(4, 'Diego', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
