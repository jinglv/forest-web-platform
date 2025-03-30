from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` ALTER COLUMN `description` SET DEFAULT '';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` ALTER COLUMN `description` DROP DEFAULT;"""
