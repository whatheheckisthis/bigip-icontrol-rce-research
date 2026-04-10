from fastapi import FastAPI

app = FastAPI(title="Fixture iControl surface")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "bind": "127.0.0.1 only"}
