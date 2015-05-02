"""add world snapshot entity

Revision ID: 2e291a86762
Revises: 316430cf0b7
Create Date: 2015-05-01 22:27:53.128304

"""

# revision identifiers, used by Alembic.
revision = '2e291a86762'
down_revision = '316430cf0b7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worldsnapshots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('map_thumbnail_url', sa.Text(), nullable=True),
    sa.Column('map_image_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worldsnapshots_timestamp'), 'worldsnapshots', ['timestamp'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worldsnapshots_timestamp'), table_name='worldsnapshots')
    op.drop_table('worldsnapshots')
    ### end Alembic commands ###
