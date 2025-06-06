"""Add is_business_customer and billing_name

Revision ID: a0a402ba59be
Revises: af13a9af270c
Create Date: 2025-05-21 14:43:33.382119

"""

import sqlalchemy as sa
from alembic import op

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "a0a402ba59be"
down_revision = "af13a9af270c"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "checkouts", sa.Column("is_business_customer", sa.Boolean(), nullable=True)
    )
    op.execute(
        "UPDATE checkouts SET is_business_customer = false WHERE is_business_customer IS NULL"
    )
    op.alter_column(
        "checkouts",
        "is_business_customer",
        existing_type=sa.Boolean(),
        nullable=False,
    )
    op.add_column(
        "checkouts", sa.Column("customer_billing_name", sa.String(), nullable=True)
    )
    op.add_column("customers", sa.Column("billing_name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("customers", "billing_name")
    op.drop_column("checkouts", "customer_billing_name")
    op.drop_column("checkouts", "is_business_customer")
    # ### end Alembic commands ###
