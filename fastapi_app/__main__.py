import uvicorn

uvicorn.run(f"{__package__}.main:app", port=8080, reload=__debug__)