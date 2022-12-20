# Import all the models, so that Base has them before being
# imported by Alembic
from fever.db.base_class import Base  # noqa
from fever.models import Event  # noqa
