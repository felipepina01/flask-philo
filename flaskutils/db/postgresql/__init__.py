def syncdb():
    """
    Create tables if they don't exist
    """
    from flaskutils.db.postgresql.schema import Base
    from flaskutils.db.postgresql.orm import BaseModel  # noqa
    from flaskutils.db.postgresql.connection import get_pool

    for conn_name, conn in get_pool().connections.items():
        Base.metadata.create_all(conn.engine)
