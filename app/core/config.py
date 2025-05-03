from sqlmodel import create_engine, SQLModel

# create a file called "logs.db" in the current folder
DATABASE_URL = "sqlite:///./logs.db"

# Creates the database engine (connection)
# echo=True = print all SQL queries in the terminal for debugging
engine = create_engine(DATABASE_URL, echo=True)

# creates all database tables defined as SQLModel classes
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)