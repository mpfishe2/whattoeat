def loadEnvVariables():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    OPEN_AI_API_KEY = os.getenv("OPEN_API_KEY")
    return OPEN_AI_API_KEY