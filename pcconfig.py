import pynecone as pc


config = pc.Config(
    app_name="aboutpage",
    api_url="0.0.0.0:3006",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
