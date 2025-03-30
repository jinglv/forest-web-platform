from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` MODIFY COLUMN `description` VARCHAR(255) NOT NULL COMMENT '项目描述';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` MODIFY COLUMN `description` LONGTEXT NOT NULL COMMENT '项目描述';"""
