"""add many-to-many tables

Revision ID: 442c174e05a9
Revises: 
Create Date: 2026-07-16 10:16:00.769153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '442c174e05a9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if not inspector.has_table('association_table'):
        op.create_table(
            'association_table',
            sa.Column('commande_id', sa.Integer(), nullable=False),
            sa.Column('produit_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['commande_id'], ['commandes.id']),
            sa.ForeignKeyConstraint(['produit_id'], ['produits.id']),
            sa.PrimaryKeyConstraint('commande_id', 'produit_id')
        )

    if not inspector.has_table('produit_menu_association'):
        op.create_table(
            'produit_menu_association',
            sa.Column('menu_id', sa.Integer(), nullable=False),
            sa.Column('produit_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['menu_id'], ['menus.id']),
            sa.ForeignKeyConstraint(['produit_id'], ['produits.id']),
            sa.PrimaryKeyConstraint('menu_id', 'produit_id')
        )

    produit_columns = {col['name'] for col in inspector.get_columns('produits')}
    # SQLite does not support dropping constraints directly; batch mode recreates the table safely.
    if 'commande_id' in produit_columns or 'menu_id' in produit_columns:
        with op.batch_alter_table('produits', schema=None) as batch_op:
            if 'commande_id' in produit_columns:
                batch_op.drop_column('commande_id')
            if 'menu_id' in produit_columns:
                batch_op.drop_column('menu_id')


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    produit_columns = {col['name'] for col in inspector.get_columns('produits')}
    needs_commande_id = 'commande_id' not in produit_columns
    needs_menu_id = 'menu_id' not in produit_columns

    if needs_commande_id or needs_menu_id:
        with op.batch_alter_table('produits', schema=None) as batch_op:
            if needs_commande_id:
                batch_op.add_column(sa.Column('commande_id', sa.Integer(), nullable=True))
            if needs_menu_id:
                batch_op.add_column(sa.Column('menu_id', sa.Integer(), nullable=True))
            if needs_commande_id:
                batch_op.create_foreign_key(
                    'fk_produits_commande_id_commandes',
                    'commandes',
                    ['commande_id'],
                    ['id']
                )
            if needs_menu_id:
                batch_op.create_foreign_key(
                    'fk_produits_menu_id_menus',
                    'menus',
                    ['menu_id'],
                    ['id']
                )

    if inspector.has_table('produit_menu_association'):
        op.drop_table('produit_menu_association')
    if inspector.has_table('association_table'):
        op.drop_table('association_table')
