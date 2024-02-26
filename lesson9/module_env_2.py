import os

import dotenv


if __name__ == '__main__':
    dotenv.load_dotenv(".env")

    postgres_user = os.getenv("POSTGRES_USER")
    print(postgres_user)
