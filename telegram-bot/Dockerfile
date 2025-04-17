# Use Python 3.11 image as base
FROM python:3.11-slim

# Set environment variables
ENV POETRY_VERSION=1.9.0

# Install Poetry (for dependency management)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Create and set working directory
WORKDIR /app

# Copy the poetry configuration and lock file into the container
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry install --no-root --no-dev  # --no-root to not install the current project as a package

# Copy the rest of the project files into the container
COPY . /app

# Set the default command to run the bot
CMD ["poetry", "run", "python", "src/bot/main.py"]