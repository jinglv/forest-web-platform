from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `forest_projects` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '项目id',
    `name` VARCHAR(50) NOT NULL COMMENT '项目名称',
    `description` LONGTEXT NOT NULL COMMENT '项目描述',
    `create_time` DATETIME(6) NOT NULL COMMENT '创建日期' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `leader_id` INT NOT NULL COMMENT '项目负责人',
    CONSTRAINT `fk_forest_p_forest_u_b22863d0` FOREIGN KEY (`leader_id`) REFERENCES `forest_users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='项目表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `forest_projects`;"""
