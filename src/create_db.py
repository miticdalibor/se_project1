from dwh import Features, engine, Base

Base.metadata.create_all(engine)  # this code line creates the DB with the specified metadata