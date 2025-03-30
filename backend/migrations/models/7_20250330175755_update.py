from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` DROP FOREIGN KEY `fk_forest_p_forest_u_b22863d0`;
        ALTER TABLE `forest_projects` RENAME COLUMN `leader_id` TO `user_id`;
        ALTER TABLE `forest_projects` ADD CONSTRAINT `fk_forest_p_forest_u_c520ea8d` FOREIGN KEY (`user_id`) REFERENCES `forest_users` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `forest_projects` DROP FOREIGN KEY `fk_forest_p_forest_u_c520ea8d`;
        ALTER TABLE `forest_projects` RENAME COLUMN `user_id` TO `leader_id`;
        ALTER TABLE `forest_projects` ADD CONSTRAINT `fk_forest_p_forest_u_b22863d0` FOREIGN KEY (`leader_id`) REFERENCES `forest_users` (`id`) ON DELETE CASCADE;"""
