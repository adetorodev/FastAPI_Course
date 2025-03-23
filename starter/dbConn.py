from sqlmodel import create_engine

sqlite_file_name = "databse.db"
db_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(db_url, connect_args=connect_args)