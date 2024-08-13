"""Update models and relationships

Revision ID: 7e96ea11fa83
Revises: 170bb079f78e
Create Date: 2024-08-12 16:23:14.991153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e96ea11fa83'
down_revision: Union[str, None] = '170bb079f78e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('chefs_recipe_id_fkey', 'chefs', type_='foreignkey')
    op.drop_column('chefs', 'recipe_id')
    op.add_column('recipes', sa.Column('chef_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipes', 'chefs', ['chef_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'chef_id')
    op.add_column('chefs', sa.Column('recipe_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('chefs_recipe_id_fkey', 'chefs', 'recipes', ['recipe_id'], ['id'])
    # ### end Alembic commands ###
