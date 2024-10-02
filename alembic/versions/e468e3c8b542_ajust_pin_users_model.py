"""Ajust pin users model

Revision ID: e468e3c8b542
Revises: 90f297e15fe1
Create Date: 2024-10-02 10:37:40.818624

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e468e3c8b542'
down_revision: Union[str, None] = '90f297e15fe1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_token_blacklist_id', table_name='token_blacklist')
    op.drop_table('token_blacklist')
    op.drop_index('ix_users_chave_pix', table_name='users')
    op.drop_index('ix_users_cnpj', table_name='users')
    op.drop_index('ix_users_cpf', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_items_id', table_name='items')
    op.drop_index('ix_items_name', table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='items_pkey')
    )
    op.create_index('ix_items_name', 'items', ['name'], unique=False)
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cpf', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cnpj', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('chave_pix', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_cpf', 'users', ['cpf'], unique=True)
    op.create_index('ix_users_cnpj', 'users', ['cnpj'], unique=True)
    op.create_index('ix_users_chave_pix', 'users', ['chave_pix'], unique=True)
    op.create_table('token_blacklist',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='token_blacklist_pkey')
    )
    op.create_index('ix_token_blacklist_id', 'token_blacklist', ['id'], unique=False)
    # ### end Alembic commands ###