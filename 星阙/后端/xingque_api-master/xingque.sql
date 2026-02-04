CREATE TABLE `xq_user` (
                           `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
                           `avatar` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '头像',
                           `name` varchar(20) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '姓名',
                           `birthday` char(8) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '生日',
                           `province_id` int NOT NULL DEFAULT '0' COMMENT '省份id',
                           `city_id` int NOT NULL COMMENT '城市id',
                           `district_id` int NOT NULL DEFAULT '0' COMMENT '行政区id',
                           `wx_openid` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '微信openid',
                           `wx_unionid` varchar(100) COLLATE utf8mb4_general_ci NOT NULL COMMENT '微信unionid',
                           `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 正常 2 禁用 -1 删除',
                           `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
                           `modified_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
                           PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户表';

CREATE TABLE `xq_user_config` (
                                  `id` int unsigned NOT NULL AUTO_INCREMENT,
                                  `user_id` int unsigned NOT NULL COMMENT '用户id',
                                  `apparent_solar_time` tinyint(1) NOT NULL DEFAULT '0' COMMENT '真太阳时 1 开 2 关',
                                  `qimen_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '奇门定局 1 拆补  2 置润',
                                  `liuren_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '六壬排盘 1 三宫  2 横排',
                                  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 正常 2 禁用 -1 删除',
                                  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
                                  `modified_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
                                  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户配置表';

CREATE TABLE `xq_user_suggest` (
                                   `id` int unsigned NOT NULL AUTO_INCREMENT,
                                   `user_id` int unsigned NOT NULL COMMENT '用户id',
                                   `content` varchar(500) COLLATE utf8mb4_general_ci NOT NULL COMMENT '意见内容',
                                   `images` json NOT NULL COMMENT '图片url',
                                   `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 正常 2 禁用 -1 删除',
                                   `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
                                   `modified_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
                                   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户意见反馈表';

CREATE TABLE `xq_user_trigram_book` (
                                        `id` int unsigned NOT NULL AUTO_INCREMENT,
                                        `user_id` int unsigned NOT NULL COMMENT '用户id',
                                        `name` varchar(20) COLLATE utf8mb4_general_ci NOT NULL COMMENT '姓名',
                                        `sex` tinyint(1) NOT NULL COMMENT '1 男 2 女',
                                        `birthday` char(8) COLLATE utf8mb4_general_ci NOT NULL COMMENT '生日 20220101',
                                        `residence_province_id` int NOT NULL COMMENT '现居住省id',
                                        `residence_city_id` int NOT NULL COMMENT '现居住市id',
                                        `residence_district_id` int NOT NULL COMMENT '现居住区id',
                                        `birth_province_id` int NOT NULL COMMENT '出生省id',
                                        `birth_city_id` int NOT NULL COMMENT '出生城市id',
                                        `birth_district_id` int NOT NULL COMMENT '出生区id',
                                        `relation` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '与本人的关系',
                                        `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 正常 2 禁用 -1 删除',
                                        `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
                                        `modified_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
                                        PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户起卦簿表';

CREATE TABLE `xq_user_trigram_record` (
                                          `id` int unsigned NOT NULL AUTO_INCREMENT,
                                          `user_id` int unsigned NOT NULL COMMENT '用户id',
                                          `input` json DEFAULT NULL COMMENT '用户输入信息',
                                          `output` json DEFAULT NULL COMMENT '输出结果信息',
                                          `extras` json DEFAULT NULL COMMENT '其他配置',
                                          `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 正常 2 禁用 -1 删除',
                                          `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
                                          `modified_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
                                          PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户起卦记录表';