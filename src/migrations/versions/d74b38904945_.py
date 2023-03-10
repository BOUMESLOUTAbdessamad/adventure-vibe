"""empty message

Revision ID: d74b38904945
Revises: 
Create Date: 2023-01-29 22:59:54.750067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74b38904945'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('email_verified', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('family_name', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('given_name', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('identities', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('locale', sa.String(length=4), nullable=False))
        batch_op.add_column(sa.Column('nickname', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('picture', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.String(length=255), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['user_id'])
        batch_op.drop_column('fullname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fullname', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_id')
        batch_op.drop_column('picture')
        batch_op.drop_column('nickname')
        batch_op.drop_column('locale')
        batch_op.drop_column('identities')
        batch_op.drop_column('given_name')
        batch_op.drop_column('family_name')
        batch_op.drop_column('email_verified')
        batch_op.drop_column('email')
        batch_op.drop_column('created_at')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
