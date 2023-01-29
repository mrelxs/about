import pynecone as pc


config = pc.Config(
    app_name="aboutpage",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
