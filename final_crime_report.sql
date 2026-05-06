-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2026 at 03:17 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `final_crime_report`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `case_assignment`
--

CREATE TABLE `case_assignment` (
  `assignment_id` int(11) NOT NULL,
  `fk_report_id` int(11) NOT NULL,
  `fk_invest_id` int(11) NOT NULL,
  `assigned_at` date NOT NULL,
  `assigned_status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `case_assignment`
--

INSERT INTO `case_assignment` (`assignment_id`, `fk_report_id`, `fk_invest_id`, `assigned_at`, `assigned_status`) VALUES
(6, 7, 3, '2026-03-12', 'Closed'),
(7, 8, 4, '2026-03-12', 'assigned'),
(8, 9, 3, '2026-03-12', 'assigned');

-- --------------------------------------------------------

--
-- Table structure for table `crime_category`
--

CREATE TABLE `crime_category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL,
  `category_dec` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crime_category`
--

INSERT INTO `crime_category` (`category_id`, `category_name`, `category_dec`) VALUES
(3, 'Robbery', 'The unlawful taking of property or valuables from a person through force, intimidation, or threat of violence.'),
(4, 'Assault', 'Intentionally causing physical harm or threatening to cause harm to another person.'),
(5, 'Cybercrime', 'Involves illegal activities carried out using computers, networks, or the internet such as hacking, identity theft, and online fraud.'),
(6, 'Kidnapping', 'The unlawful act of taking or detaining a person against their will, often for ransom or other illegal purposes.'),
(7, 'Domestic Violence', 'physical, emotional, or psychological abuse between family members or partners within a household.'),
(8, 'Vandalism', 'Intentional damage or destruction of public or private property.'),
(9, 'Drug Offense', 'Drug offenses involve the illegal possession, distribution, manufacturing, or trafficking of prohibited drugs.'),
(10, 'Murder', 'Unlawful and intentional killing of another person.'),
(11, 'Human Trafficking', 'Involves the illegal trade or exploitation of people for forced labor, slavery, or sexual exploitation.'),
(12, 'Harassment', 'Involves repeated unwanted behavior or threats that cause fear, distress, or emotional harm to another person.');

-- --------------------------------------------------------

--
-- Table structure for table `crime_evidence`
--

CREATE TABLE `crime_evidence` (
  `crime_evidence_id` int(11) NOT NULL,
  `fk_crime_report_id` int(11) NOT NULL,
  `evidence_file_name` varchar(100) NOT NULL,
  `evidence_file_type` varchar(50) NOT NULL,
  `evidence_file` varchar(100) NOT NULL,
  `evidence_uploaded_date` date NOT NULL,
  `fk_crime_user_id` int(11) NOT NULL,
  `uploaded_by` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crime_evidence`
--

INSERT INTO `crime_evidence` (`crime_evidence_id`, `fk_crime_report_id`, `evidence_file_name`, `evidence_file_type`, `evidence_file`, `evidence_uploaded_date`, `fk_crime_user_id`, `uploaded_by`) VALUES
(10, 7, 'Shattered Window Photo', 'Image', 'Evidence_inve/20260312_174110.png', '2026-03-12', 5, 'citizen'),
(11, 8, 'Cyber Fraud Forensic Log', 'Pdf', 'Evidence_inve/20260312_175507.pdf', '2026-03-11', 5, 'citizen'),
(12, 9, 'Photo of damaged door lock', 'Image', 'Evidence_inve/20260312_182658.png', '2026-03-06', 6, 'citizen');

-- --------------------------------------------------------

--
-- Table structure for table `crime_law`
--

CREATE TABLE `crime_law` (
  `crime_law_id` int(11) NOT NULL,
  `fk_crime_cat_id` int(11) NOT NULL,
  `crime_law` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crime_law`
--

INSERT INTO `crime_law` (`crime_law_id`, `fk_crime_cat_id`, `crime_law`) VALUES
(2, 3, 'IPC Section 390 and 392 – Punishment may include imprisonment up to 10 years and a fine.'),
(3, 4, 'IPC Sections 351 and 352 – Assault and its punishment under the Indian Penal Code.'),
(4, 5, 'Information Technology Act, 2000 – Section 65 (Tampering with computer source documents), Section 66 (Computer-related offences), Section 66C (Identity theft), and Section 66D (Cheating by personation using computer resources)'),
(5, 6, 'IPC Section 359–369 – Kidnapping and Abduction. Section 363 provides punishment for kidnapping.'),
(6, 7, 'Protection of Women from Domestic Violence Act, 2005 – Provides protection for women against physical, emotional, sexual, and economic abuse within a household.'),
(7, 8, 'IPC Section 425 – Mischief (damage to property). Section 427 provides punishment for causing damage to property.'),
(8, 9, 'Narcotic Drugs and Psychotropic Substances Act, 1985 (NDPS Act) – Punishes illegal possession, production, sale, and trafficking of narcotic drugs.'),
(9, 10, 'IPC Section 300 & IPC Section 302 – Punishment for murder (death penalty or life imprisonment and fine).'),
(10, 11, 'IPC Section 370 – Trafficking of persons.\r\nIPC Section 370A – Exploitation of trafficked persons.'),
(11, 12, 'IPC Section 354A – Sexual harassment.\r\nIPC Section 509 – Word, gesture, or act intended to insult the modesty of a woman.');

-- --------------------------------------------------------

--
-- Table structure for table `crime_reports`
--

CREATE TABLE `crime_reports` (
  `crime_report_id` int(11) NOT NULL,
  `fk_user_id` int(11) NOT NULL,
  `fk_category_id` int(11) NOT NULL,
  `crime_report_title` varchar(100) NOT NULL,
  `crime_description` text NOT NULL,
  `crime_report_location` varchar(50) NOT NULL,
  `crime_report_latitude` decimal(10,7) NOT NULL,
  `crime_report_longitude` decimal(10,7) NOT NULL,
  `crime_report_date` date NOT NULL,
  `crime_report_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crime_reports`
--

INSERT INTO `crime_reports` (`crime_report_id`, `fk_user_id`, `fk_category_id`, `crime_report_title`, `crime_description`, `crime_report_location`, `crime_report_latitude`, `crime_report_longitude`, `crime_report_date`, `crime_report_status`) VALUES
(7, 5, 6, 'Suspected Kidnapping of a Minor', 'A minor child was reported missing from the local area and is suspected to have been taken by an unknown person without the consent of the parents. The incident occurred in the evening and witnesses reported seeing a suspicious individual near the location. Immediate investigation is requested.', 'Njaliakuzhi-Ericade Road, Njaliyakuzhi, Changanass', 9.5178885, 76.5727328, '2026-03-12', 'Closed'),
(8, 5, 5, 'Online Banking Fraud Complaint', 'The victim reported unauthorized transactions from their bank account after clicking a suspicious link received through email. Personal banking details were stolen and used to transfer money without permission. The case is suspected to be an online fraud and requires investigation.', 'Njaliakuzhi-Ericade Road, Pariyaram, Kottayam, Ker', 9.5400659, 76.5839796, '2026-03-11', 'Under Review'),
(9, 6, 7, 'Disturbance reported at neighboring residence', 'At approximately 10:30 PM, loud shouting and the sound of breaking glass were heard coming from the residence. This has been a recurring issue over the past week.', 'Changanassery, Kottayam, Kerala, 686101, India', 9.4432225, 76.5411822, '2026-03-05', 'Under Review');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-11-27 10:14:51.145246'),
(2, 'auth', '0001_initial', '2025-11-27 10:14:58.600036'),
(3, 'admin', '0001_initial', '2025-11-27 10:15:00.644999'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-11-27 10:15:00.682451'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-27 10:15:00.786905'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-11-27 10:15:02.174754'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-11-27 10:15:03.344067'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-11-27 10:15:03.446892'),
(9, 'auth', '0004_alter_user_username_opts', '2025-11-27 10:15:03.499378'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-11-27 10:15:04.244811'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-11-27 10:15:04.277350'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-11-27 10:15:04.344912'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-11-27 10:15:04.471592'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-11-27 10:15:04.588391'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-11-27 10:15:04.765574'),
(16, 'auth', '0011_update_proxy_permissions', '2025-11-27 10:15:04.832451'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-11-27 10:15:05.114120'),
(18, 'sessions', '0001_initial', '2025-11-27 10:15:05.923052');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bpnukju0rrey4j4j9xlp2r1rbxqcazit', 'eyJzZW1haWwiOiJkZXZ1Z29wejA1QGdtYWlsLmNvbSIsInVzZXJfdHlwZSI6ImNpdGl6ZW4ifQ:1wI03R:lEUnqsvUmyvT84KWAYup0B1Pq1d0Qb_b_4HAVrOKF-4', '2026-05-13 08:13:57.355829');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_notes`
--

CREATE TABLE `investigation_notes` (
  `investigation_note_id` int(11) NOT NULL,
  `fk_report_id_notes` int(11) NOT NULL,
  `fk_notes_officer_id` int(11) NOT NULL,
  `investigation_note` text NOT NULL,
  `note_created_date` date NOT NULL,
  `investigation_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `investigation_notes`
--

INSERT INTO `investigation_notes` (`investigation_note_id`, `fk_report_id_notes`, `fk_notes_officer_id`, `investigation_note`, `note_created_date`, `investigation_status`) VALUES
(13, 7, 3, '      Arrived at the scene at Njaliakuzhi. Found signs of forced entry via the back window. Interviewed neighbors for CCTV footage of the \'suspicious individual\' mentioned in the initial report and finally the suspect was caught successfully. ', '2026-03-12', 'Closed'),
(14, 7, 3, '  jghfghfjhv', '2026-03-12', 'Closed');

-- --------------------------------------------------------

--
-- Table structure for table `investigator`
--

CREATE TABLE `investigator` (
  `inv_id` int(11) NOT NULL,
  `inv_full_name` varchar(50) NOT NULL,
  `inv_email` varchar(100) NOT NULL,
  `inv_phone` varchar(10) NOT NULL,
  `inv_address` text NOT NULL,
  `inv_location` varchar(50) NOT NULL,
  `inv_gender` varchar(20) NOT NULL,
  `inv_role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `investigator`
--

INSERT INTO `investigator` (`inv_id`, `inv_full_name`, `inv_email`, `inv_phone`, `inv_address`, `inv_location`, `inv_gender`, `inv_role`) VALUES
(3, 'Krishna Kumar', 'kk12@gmail.com', '8139006451', 'pittapallil house', 'kottayam', 'Male', 'investigator'),
(4, 'Anjali Menon', 'anjali12@gmail.com', '8139006452', 'Panampalli House', 'Changanassery', 'Female', 'investigator');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `user_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user_id`, `username`, `password`, `user_type`, `user_status`) VALUES
(1, 'admin@gmail.com', 'Admin@12', 'admin', 'active'),
(8, 'devugopz05@gmail.com', 'devu@123', 'citizen', 'active'),
(9, 'kk12@gmail.com', 'kk@330616', 'investigator', 'active'),
(10, 'anjali12@gmail.com', 'anjali@330616', 'investigator', 'active'),
(11, 'devugopz@gmail.com', 'amal@330616', 'citizen', 'active'),
(12, 'vyshnavishaji02@gmail.com', 'vyshnavi02@', 'citizen', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_phone` varchar(10) NOT NULL,
  `user_address` text NOT NULL,
  `user_location` varchar(50) NOT NULL,
  `user_gender` varchar(15) NOT NULL,
  `user_role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `full_name`, `user_email`, `user_phone`, `user_address`, `user_location`, `user_gender`, `user_role`) VALUES
(5, 'Devika Mohan', 'devugopz05@gmail.com', '8139006453', 'Maheswari Vilasam', 'Puthupally', 'Female', 'citizen'),
(6, 'Amal John', 'devugopz@gmail.com', '8139006454', 'Puzhavathu House', 'Changanassery', 'Male', 'citizen'),
(7, 'vyshnavi', 'vyshnavishaji02@gmail.com', '8281659438', 'udvhb bhjbjcb basbd', 'kottayam', 'Female', 'citizen');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `case_assignment`
--
ALTER TABLE `case_assignment`
  ADD PRIMARY KEY (`assignment_id`);

--
-- Indexes for table `crime_category`
--
ALTER TABLE `crime_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `crime_evidence`
--
ALTER TABLE `crime_evidence`
  ADD PRIMARY KEY (`crime_evidence_id`);

--
-- Indexes for table `crime_law`
--
ALTER TABLE `crime_law`
  ADD PRIMARY KEY (`crime_law_id`);

--
-- Indexes for table `crime_reports`
--
ALTER TABLE `crime_reports`
  ADD PRIMARY KEY (`crime_report_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `investigation_notes`
--
ALTER TABLE `investigation_notes`
  ADD PRIMARY KEY (`investigation_note_id`);

--
-- Indexes for table `investigator`
--
ALTER TABLE `investigator`
  ADD PRIMARY KEY (`inv_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`) USING BTREE;

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `case_assignment`
--
ALTER TABLE `case_assignment`
  MODIFY `assignment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `crime_category`
--
ALTER TABLE `crime_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `crime_evidence`
--
ALTER TABLE `crime_evidence`
  MODIFY `crime_evidence_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `crime_law`
--
ALTER TABLE `crime_law`
  MODIFY `crime_law_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `crime_reports`
--
ALTER TABLE `crime_reports`
  MODIFY `crime_report_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `investigation_notes`
--
ALTER TABLE `investigation_notes`
  MODIFY `investigation_note_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `investigator`
--
ALTER TABLE `investigator`
  MODIFY `inv_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
