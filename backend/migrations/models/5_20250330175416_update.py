from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_envs` RENAME COLUMN `create_time` TO `create_at`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `create_time` TO `create_at`;
        ALTER TABLE `forest_projects` RENAME COLUMN `create_time` TO `create_at`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_envs` RENAME COLUMN `create_at` TO `create_time`;
        ALTER TABLE `forest_projects` RENAME COLUMN `create_at` TO `create_time`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `create_at` TO `create_time`;"""
