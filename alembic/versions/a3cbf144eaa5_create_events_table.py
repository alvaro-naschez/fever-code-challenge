"""create events table

Revision ID: a3cbf144eaa5
Revises:
Create Date: 2022-12-19 21:52:05.358481

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "a3cbf144eaa5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=True),
        sa.Column("min_price", sa.Integer(), nullable=True),
        sa.Column("max_price", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("events")
