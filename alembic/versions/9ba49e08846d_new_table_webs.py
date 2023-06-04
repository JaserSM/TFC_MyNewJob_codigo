"""new table webs

Revision ID: 9ba49e08846d
Revises: af28b7a1927d
Create Date: 2023-05-01 20:06:30.424196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba49e08846d'
down_revision = 'af28b7a1927d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('job_offer', sa.Column('web', sa.Integer(), nullable=True))
    op.create_foreign_key('job_offer_web_id_fkey', 'job_offer', 'web', ['web'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('job_offer_web_id_fkey', 'job_offer', type_='foreignkey')
    op.drop_column('job_offer', 'web')
    op.drop_table('web')
    # ### end Alembic commands ###