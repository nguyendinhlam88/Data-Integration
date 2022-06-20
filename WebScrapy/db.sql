-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.7-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for oto-db
CREATE DATABASE IF NOT EXISTS `oto-db` /*!40100 DEFAULT CHARACTER SET utf16 COLLATE utf16_unicode_ci */;
USE `oto-db`;

-- Dumping structure for table oto-db.oto
CREATE TABLE IF NOT EXISTS `oto` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `domain` varchar(512) COLLATE utf16_unicode_ci DEFAULT NULL,
  `crawled_date` datetime DEFAULT NULL,
  `ten` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `gia_ban` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `xuat_xu` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tinh_trang` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `dong_xe` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `so_km_da_di` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `mau_ngoai_that` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `mau_noi_that` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `so_cua` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `so_cho_ngoi` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `nhien_lieu` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `he_thong_nap_nhien_lieu` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `hop_so` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `dan_dong` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tieu_thu_nhien_lieu` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `dung_tich_xi_lanh` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table oto-db.oto: ~1 rows (approximately)
/*!40000 ALTER TABLE `oto` DISABLE KEYS */;
INSERT INTO `oto` (`id`, `domain`, `crawled_date`, `ten`, `gia_ban`, `xuat_xu`, `tinh_trang`, `dong_xe`, `so_km_da_di`, `mau_ngoai_that`, `mau_noi_that`, `so_cua`, `so_cho_ngoi`, `nhien_lieu`, `he_thong_nap_nhien_lieu`, `hop_so`, `dan_dong`, `tieu_thu_nhien_lieu`, `dung_tich_xi_lanh`) VALUES
	(1, 'domain', NULL, 'ten', '1000', 'xuat_xu', 'tinh_trang', 'dong_xe', 'so_km_da_di', 'mau_ngoai_that', 'mau_noi_that', 'so_cua', '4', 'nhien_lieu', 'he_thong_nap_nhien_lieu', 'hop_so', 'dan_dong', 'tieu_thu_nhien_lieu', 'dung_tich_xi_lanh'),
	(2, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Dothanh IZ65	2022	- 400 Triệu', '2 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Dầu	2.8 L', 'Số tay', '3 chỗ', 'Truck', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(3, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Volvo XC40	R-DESIGN	2022	- 1 Tỷ 750 Triệu', '5 cửa', 'Xe mới', 'Nhập khẩu', '0 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(4, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Toyota Fortuner	2.4L 4x2 AT	2022	- 1 Tỷ 80 Triệu', '5 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Dầu	2.4 L', 'Số tự động', '7 chỗ', 'SUV', 'NULL', 'Đen', 'NULL', 'NULL', 'NULL'),
	(5, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Kia Seltos	Premium 1.4 AT	2022	- 749 Triệu', '5 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	1.4 L', 'Số tự động', '5 chỗ', 'Crossover', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(6, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Kia Seltos	Luxury 1.4 AT	2022	- 659 Triệu', '5 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	1.4 L', 'Số tự động', '5 chỗ', 'Crossover', 'NULL', 'Vàng', 'NULL', 'NULL', 'NULL'),
	(7, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	Mazda CX5	2.5 AT 2WD	2018	- 720 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	2.5 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Xanh', 'NULL', 'NULL', 'NULL'),
	(8, 'NULL', '2022-06-16 08:44:41', 'NULL', 'Xe	VinFast Fadil	Cao cấp 1.4 AT	2022	- 409 Triệu', '5 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	1.4 L', 'Số tự động', '5 chỗ', 'Hatchback', 'NULL', 'Xám', 'NULL', 'NULL', 'NULL'),
	(9, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Hyundai SantaFe	Cao cấp 2.5L HTRAC	2022	- 1 Tỷ 220 Triệu', '5 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	2.5 L', 'Số tự động', '7 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(10, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Ford Ranger	Raptor 2.0L 4x4 AT	2022	- 1 Tỷ 202 Triệu', '4 cửa', 'Xe mới', 'Nhập khẩu', '0 Km', 'NULL', 'Dầu	2.0 L', 'Số tự động', '5 chỗ', 'Bán tải / Pickup', 'NULL', 'Xanh', 'NULL', 'NULL', 'NULL'),
	(11, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Chevrolet Spark	LT 0.8 AT	2009	- 148 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '100,000 Km', 'NULL', 'Xăng	0.8 L', 'Số tự động', '5 chỗ', 'Hatchback', 'NULL', 'Xanh', 'NULL', 'NULL', 'NULL'),
	(12, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Honda Civic	G 1.5 AT	2022	- 770 Triệu', '4 cửa', 'Xe mới', 'Nhập khẩu', '0 Km', 'NULL', 'Xăng	1.5 L', 'Số tự động', '5 chỗ', 'Sedan', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(13, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Mercedes Benz GLC	300 4Matic	2019	- 2 Tỷ 450 Triệu', '5 cửa', 'Xe đã dùng', 'Nhập khẩu', '20,000 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(14, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Mercedes Benz E class	E300 AMG	2022	- 2 Tỷ 950 Triệu', '4 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '5 chỗ', 'Sedan', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(15, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Ford Everest	Titanium 2.0L 4x2 AT	2022	- 1 Tỷ 200 Triệu', '5 cửa', 'Xe mới', 'Nhập khẩu', '0 Km', 'NULL', 'Dầu	2.0 L', 'Số tự động', '7 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(16, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Mazda 3	Luxury	2020	- 625 Triệu', '4 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '26,000 Km', 'NULL', 'Xăng	1.5 L', 'Số tự động', '5 chỗ', 'Sedan', 'NULL', 'Đỏ', 'NULL', 'NULL', 'NULL'),
	(17, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Mitsubishi Outlander	2.0 CVT	2019	- 700 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '42,000 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '7 chỗ', 'SUV', 'NULL', 'Đỏ', 'NULL', 'NULL', 'NULL'),
	(18, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Mercedes Benz GLC	250 4Matic	2017	- 1 Tỷ 450 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '65,000 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(19, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Honda City	G 1.5 AT	2021	- 529 Triệu', '4 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	1.5 L', 'Số tự động', '5 chỗ', 'Sedan', 'NULL', 'Đen', 'NULL', 'NULL', 'NULL'),
	(20, 'NULL', '2022-06-16 08:44:42', 'NULL', 'Xe	Toyota Vios	G 1.5 CVT	2022	- 576 Triệu', '4 cửa', 'Xe mới', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng	1.5 L', 'Số tự động', '5 chỗ', 'Sedan', 'NULL', 'Đen', 'NULL', 'NULL', 'NULL'),
	(21, 'NULL', '2022-06-16 08:44:43', 'NULL', 'Xe	Mazda 3	1.5L Sport Luxury	2019	- 605 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '30,000 Km', 'NULL', 'Xăng	1.5 L', 'Số tự động', '5 chỗ', 'Hatchback', 'NULL', 'Đỏ', 'NULL', 'NULL', 'NULL'),
	(22, 'NULL', '2022-06-16 08:44:45', 'NULL', 'Xe	Suzuki Vitara	1.6 AT	2016	- 608 Triệu', '5 cửa', 'Xe đã dùng', 'Nhập khẩu', '0 Km', 'NULL', 'Xăng	1.6 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Xanh', 'NULL', 'NULL', 'NULL'),
	(23, 'NULL', '2022-06-16 08:44:45', 'NULL', 'Xe	Toyota Venza	2.7	2009	- 685 Triệu', '5 cửa', 'Xe đã dùng', 'Nhập khẩu', '21,000 Km', 'NULL', 'Xăng	2.7 L', 'Số tự động', '5 chỗ', 'Crossover', 'NULL', 'Nâu', 'NULL', 'NULL', 'NULL'),
	(24, 'NULL', '2022-06-16 08:44:45', 'NULL', 'Xe	Toyota Zace	2005	- 250 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '0 Km', 'NULL', 'Xăng', 'Số tay', '7 chỗ', 'SUV', 'NULL', 'Bạc', 'NULL', 'NULL', 'NULL'),
	(25, 'NULL', '2022-06-16 08:44:45', 'NULL', 'Xe	VinFast Lux SA 2.0	Plus 2.0 AT	2021	- 1 Tỷ 30 Triệu', '5 cửa', 'Xe đã dùng', 'Lắp ráp trong nước', '20,000 Km', 'NULL', 'Xăng	2.0 L', 'Số tự động', '7 chỗ', 'SUV', 'NULL', 'Trắng', 'NULL', 'NULL', 'NULL'),
	(26, 'NULL', '2022-06-16 08:44:45', 'NULL', 'Xe	Porsche Cayenne	3.0 V6	2018	- 5 Tỷ 450 Triệu', '5 cửa', 'Xe đã dùng', 'Nhập khẩu', '40,000 Km', 'NULL', 'Xăng	3.0 L', 'Số tự động', '5 chỗ', 'SUV', 'NULL', 'Đen', 'NULL', 'NULL', 'NULL');
/*!40000 ALTER TABLE `oto` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
