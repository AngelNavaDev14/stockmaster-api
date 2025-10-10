from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Esta es la URL de conexión a tu base de datos PostgreSQL.
# Formato: "postgresql://usuario:contraseña@host/nombre_db"
SQLALCHEMY_DATABASE_URL = "postgresql://angel_dev:brasiljr08@localhost/stockmaster_db"

# 2. El "motor" de SQLAlchemy que se conectará a la base de datos.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. La "sesión". Cada vez que necesitemos hablar con la BD, abriremos una de estas.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Una clase base que nuestros modelos de la base de datos heredarán.
Base = declarative_base()