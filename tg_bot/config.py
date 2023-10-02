from environs import Env

env = Env()
env.read_env()


class Settings:
    POSTGRES_USER = env.str('POSTGRES_USER', 'admin')
    POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD', 'admin')
    POSTGRES_DB = env.str('POSTGRES_DB', 'db')
    POSTGRES_HOST = env.str('POSTGRES_HOST', 'localhost')

    BOT_TOKEN = env.str('BOT_TOKEN')

    JWT_SECRET = env.str('JWT_SECRET')
    ALGORITHM = env.str('ALGORITHM' )

settings = Settings()
