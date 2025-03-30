from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_users` RENAME COLUMN `updated_at` TO `updated_time`;
        ALTER TABLE `forest_users` RENAME COLUMN `created_at` TO `created_time`;
        ALTER TABLE `forest_envs` RENAME COLUMN `create_at` TO `create_time`;
        ALTER TABLE `forest_envs` RENAME COLUMN `updated_at` TO `updated_time`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `create_at` TO `create_time`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `updated_at` TO `updated_time`;
        ALTER TABLE `forest_projects` RENAME COLUMN `create_at` TO `create_time`;
        ALTER TABLE `forest_projects` RENAME COLUMN `updated_at` TO `updated_time`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_envs` RENAME COLUMN `updated_time` TO `updated_at`;
        ALTER TABLE `forest_envs` RENAME COLUMN `create_time` TO `create_at`;
        ALTER TABLE `forest_users` RENAME COLUMN `updated_time` TO `updated_at`;
        ALTER TABLE `forest_users` RENAME COLUMN `created_time` TO `created_at`;
        ALTER TABLE `forest_projects` RENAME COLUMN `updated_time` TO `updated_at`;
        ALTER TABLE `forest_projects` RENAME COLUMN `create_time` TO `create_at`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `updated_time` TO `updated_at`;
        ALTER TABLE `forest_project_module` RENAME COLUMN `create_time` TO `create_at`;"""
