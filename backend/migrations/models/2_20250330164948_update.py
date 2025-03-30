from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `forest_envs` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '环境id',
    `global_variable` JSON COMMENT '全局变量',
    `name` VARCHAR(50) NOT NULL COMMENT '测试环境名称',
    `host` VARCHAR(50) NOT NULL COMMENT '测试环境的host地址',
    `create_time` DATETIME(6) NOT NULL COMMENT '创建日期' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `project_id` INT NOT NULL COMMENT '所属项目',
    CONSTRAINT `fk_forest_e_forest_p_a5ad8e25` FOREIGN KEY (`project_id`) REFERENCES `forest_projects` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='环境表';
        CREATE TABLE IF NOT EXISTS `forest_project_module` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '模块id',
    `name` VARCHAR(50) NOT NULL COMMENT '模块名称',
    `create_time` DATETIME(6) NOT NULL COMMENT '创建日期' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `project_id` INT NOT NULL COMMENT '所属项目',
    CONSTRAINT `fk_forest_p_forest_p_5bf47856` FOREIGN KEY (`project_id`) REFERENCES `forest_projects` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='功能模块表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `forest_project_module`;
        DROP TABLE IF EXISTS `forest_envs`;"""
