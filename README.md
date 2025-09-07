# Taters 🥔

A Python CLI accelerator built with Typer, demonstrating clean architecture and dependency injection patterns.

## Features

- **Dad Jokes**: Get random dad jokes from [icanhazdadjoke.com](https://icanhazdadjoke.com/api)
- **Hello Command**: A simple greeting command with optional name parameter
- **Clean Architecture**: 3-tiered architecture (Actions, Services, Repositories)
- **Dependency Injection**: Using dependency-injector for IoC
- **Comprehensive Testing**: Unit tests for all layers with mocking
- **Type Safety**: Full type hints throughout the codebase

## Project Structure

```
accelertater/
├── src/taters/
│   ├── actions/           # Top layer - CLI command orchestration
│   │   ├── dad_joke_action.py
│   │   └── hello_action.py
│   ├── services/          # Middle layer - Business logic
│   │   └── dad_joke_service.py
│   ├── repositories/      # Bottom layer - Data access
│   │   └── dad_joke_repository.py
│   ├── container.py       # Dependency injection configuration
│   └── main.py           # CLI entry point
├── tests/                # Comprehensive unit tests
│   ├── actions/
│   ├── services/
│   ├── repositories/
│   └── test_container.py
├── pyproject.toml        # Modern Python packaging
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── Makefile             # Development automation
```

## Installation

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tristanl-slalom/accelertater.git
   cd accelertater
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   make install-dev
   # or manually:
   pip install -e ".[dev]"
   ```

### Production Installation

```bash
pip install -e .
```

## Usage

### Available Commands

```bash
# Show help
taters --help

# Say hello (generic)
taters hello

# Say hello to someone specific
taters hello "World"

# Get a random dad joke
taters dad-joke
```

### Examples

```bash
$ taters hello
👋 Hello there!

$ taters hello "Alice"
👋 Hello, Alice!

$ taters dad-joke
🃏 Dad Joke: Why don't scientists trust atoms? Because they make up everything!
```

## Development

### Running Tests

```bash
# Run all tests with coverage
make test

# Run tests manually
pytest tests/ -v --cov=src
```

### Code Formatting

```bash
# Format code with Black
make format

# Type checking with mypy
make typecheck
```

### Project Commands

```bash
make install      # Install production dependencies
make install-dev  # Install development dependencies
make test         # Run tests with 80% coverage requirement
make format       # Format code with Black
make format-check # Check code formatting without changes
make typecheck    # Run type checking with mypy (strict mode)
make quality-check # Run all quality checks (CI simulation)
make lint         # Run linting
make clean        # Clean build artifacts
```

### Quality Standards

This project enforces strict quality standards:

- **Code Formatting**: Black with 88-character line length
- **Type Checking**: mypy in strict mode with full type annotations
- **Test Coverage**: Minimum 80% coverage requirement
- **All Checks Required**: CI/CD fails if any quality check fails

The `make quality-check` command runs the same checks as the CI/CD pipeline:
1. Black formatting verification
2. mypy strict type checking  
3. pytest with 80% coverage requirement

## Architecture

### 3-Tiered Architecture

1. **Actions Layer** (`actions/`): CLI command orchestration and user interaction
2. **Services Layer** (`services/`): Business logic and workflow coordination
3. **Repositories Layer** (`repositories/`): External API calls and data access

### Dependency Injection

The project uses `dependency-injector` to manage dependencies:

- **Container**: Central configuration for all dependencies
- **Factory Providers**: Create instances with injected dependencies
- **Loose Coupling**: Each layer depends on abstractions, not implementations

### Error Handling

- **Graceful Degradation**: Dad joke service falls back to hardcoded joke if API fails
- **Comprehensive Exception Handling**: All external API calls are wrapped with proper error handling
- **User-Friendly Messages**: CLI displays helpful error messages with emojis

## Testing Strategy

- **Unit Tests**: Each layer tested in isolation with mocks
- **Test Coverage**: 100% coverage for business logic layers
- **Async Testing**: Proper async/await testing with pytest-asyncio
- **Mock Strategy**: External dependencies mocked at repository layer

## Dependencies

### Production
- **typer**: Modern CLI framework with automatic help generation
- **httpx**: Modern async HTTP client
- **dependency-injector**: Dependency injection framework

### Development
- **pytest**: Testing framework with async support
- **black**: Code formatting
- **mypy**: Static type checking
- **coverage**: Test coverage reporting

## API Integration

The dad joke command integrates with the [icanhazdadjoke.com API](https://icanhazdadjoke.com/api):

- **Endpoint**: `https://icanhazdadjoke.com`
- **Headers**: `Accept: application/json`
- **User-Agent**: Custom agent for identification
- **Timeout**: 10 seconds
- **Fallback**: Hardcoded joke if API unavailable

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite: `make test`
6. Format code: `make format`
7. Submit a pull request

## License

This project is intended for educational and demonstration purposes.

## Future Enhancements

- Add more command examples
- Configuration file support
- Plugin architecture
- Interactive mode
- Caching for API responses
- Additional external API integrations
