# Docker Helpers

Collection of Docker commands (and why you might need them) while working on this project’s `DockerFile`.

### Build a local image
Run this from the project root (`d:\GAN_AI\projects\Arabic_research_agent`):
```
docker build -f backend/DockerFile -t pyapp .
```
- `-f backend/DockerFile` tells Docker which file to use.
- `-t pyapp` assigns a friendly tag.
- `.` is the build context (project root), allowing access to `pyproject.toml`.

### Run the container interactively
```
docker run -it pyapp
```
- `-it` allocates an interactive terminal so you can poke around inside the container.
- Useful for quickly verifying dependencies or running manual commands.

### Build an image for Docker Hub
```
docker build -f backend/DockerFile -t abelrahman2922/ai-app-test:latest .
```
- Same build, but tagged with your Docker Hub namespace (`username/repo:tag`).
- `latest` is a conventional default tag; change it when versioning.

### Push to Docker Hub
```
docker push abelrahman2922/ai-app-test:latest
```
- Uploads the previously built/tagged image so others can pull it.
- Requires `docker login` with a Docker Hub account that has access to the repo.

### Serve the project with Python’s HTTP server
```
python -m http.server 8000
```
- Convenience command for hosting static files locally; also what the container runs by default (`CMD`).

### Run the container and expose the server
```
docker run -it -p 4000:8000 pyapp
```
- `-p 4000:8000` maps container port `8000` (where `http.server` listens) to host port `4000`.
- Visit `http://localhost:4000` to see the served files after the container starts.

Keep these snippets handy whenever you rebuild, run, ship, or test the container.



>docker compose run backend /bin/bash


curl http://localhost:12434/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "ai/qwen3:0.6B-F16","messages": [{"role": "user", "content": "Hello, how are you?"}]}'
