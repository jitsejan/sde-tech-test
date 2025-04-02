from dagster import ConfigurableResource
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

class PostgresResource(ConfigurableResource):
    user: str
    password: str
    host: str
    port: int
    database: str

    def get_engine(self):
        return create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )
