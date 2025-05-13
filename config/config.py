import os

from dotenv import load_dotenv


class PostgresConfig:
    def __init__(self):
        self._host = None
        self._port = None
        self._user = None
        self._password = None
        self._dbname = None

    @property
    def host(self):
        if not self._host:
            self._host = os.environ["PG_HOST"]
        return self._host

    @property
    def port(self):
        if not self._port:
            self._port = int(os.getenv("PG_PORT", "5432"))
        return self._port

    @property
    def user(self):
        if not self._user:
            self._user = os.environ["PG_USER"]
        return self._user

    @property
    def password(self):
        if not self._password:
            self._password = os.environ["PG_PASSWORD"]
        return self._password

    @property
    def dbname(self):
        if not self._dbname:
            self._dbname = os.environ["PG_DBNAME"]
        return self._dbname

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"


class Config:
    def __init__(self):
        self.db = PostgresConfig()


load_dotenv(override=True)
config = Config()
