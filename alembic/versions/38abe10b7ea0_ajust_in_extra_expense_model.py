"""Ajust in extra expense model

Revision ID: 38abe10b7ea0
Revises: 3c6f81901fb1
Create Date: 2024-10-11 14:31:59.106477

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '38abe10b7ea0'
down_revision: Union[str, None] = '3c6f81901fb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_hourly_rates_id', table_name='hourly_rates')
    op.drop_table('hourly_rates')
    op.drop_index('ix_extra_expenses_id', table_name='extra_expenses')
    op.drop_table('extra_expenses')
    op.drop_index('ix_payments_id', table_name='payments')
    op.drop_table('payments')
    op.drop_index('ix_token_blacklist_id', table_name='token_blacklist')
    op.drop_table('token_blacklist')
    op.drop_index('ix_users_chave_pix', table_name='users')
    op.drop_index('ix_users_cnpj', table_name='users')
    op.drop_index('ix_users_cpf', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_index('ix_journeys_id', table_name='journeys')
    op.drop_table('journeys')
    op.execute('DROP TABLE users CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journeys',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('start', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('end', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('hours_worked', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('hourly_rate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='journeys_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='journeys_pkey')
    )
    op.create_index('ix_journeys_id', 'journeys', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cpf', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cnpj', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('chave_pix', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('reset_pin', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('reset_pin_expiration', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
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
    op.create_table('payments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='payments_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='payments_pkey')
    )
    op.create_index('ix_payments_id', 'payments', ['id'], unique=False)
    op.create_table('extra_expenses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='extra_expenses_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='extra_expenses_pkey')
    )
    op.create_index('ix_extra_expenses_id', 'extra_expenses', ['id'], unique=False)
    op.create_table('hourly_rates',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('active', 'inactive', 'pending', 'rejected', name='rate_status'), autoincrement=False, nullable=False),
    sa.Column('request_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='hourly_rates_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='hourly_rates_pkey')
    )
    op.create_index('ix_hourly_rates_id', 'hourly_rates', ['id'], unique=False)
    # ### end Alembic commands ###