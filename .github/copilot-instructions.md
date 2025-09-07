# Python CLI Accelerator - GitHub Copilot Instructions

## Framework & Architecture

### Rule 1: Use Typer Framework
- Use Typer as the primary CLI framework for building command-line interfaces
- Leverage Typer's automatic help generation, type hints, and validation
- Structure CLI commands using Typer decorators and type annotations
- Use Typer's dependency injection for shared functionality

### Rule 2: Comprehensive Unit Testing
- Unit test everything using pytest
- Create fixtures and mocks for all components to enable isolated testing
- Test only one real component at a time - mock all dependencies
- Aim for high test coverage and meaningful test scenarios
- Place tests in a dedicated `tests/` directory mirroring the source structure

### Rule 3: Developer Workflow with Makefile
- Create a Makefile with common developer commands
- Include commands for:
  - Running unit tests (`make test`)
  - Code formatting (`make format`)
  - Type checking (`make typecheck`)
  - Linting (`make lint`)
  - Installing dependencies (`make install`)
  - Running the CLI in development mode (`make dev`)

### Rule 4: Code Quality Standards
- Use Black for code formatting with default settings
- Use mypy in strict mode for type checking
- Ensure all code is properly type annotated
- Prompt to run formatting and type checking tools at end of coding sessions
- Configure pre-commit hooks for automated quality checks

### Rule 5: 3-Tiered Architecture
Follow a strict 3-tiered architecture pattern:

#### Tier 1: Main/CLI Layer (`main.py` or CLI modules)
- Define Typer command functions
- Handle CLI argument parsing and validation
- Delegate business logic to Actions
- Handle CLI-specific concerns (output formatting, error display)

#### Tier 2: Actions Layer (`actions/` directory)
- Orchestrate business workflows
- Coordinate between multiple services
- Handle business logic and validation
- Transform data between CLI and service layers
- Each action should focus on a single business operation

#### Tier 3: Services & Repositories Layer
- **Services** (`services/` directory): Encapsulate business logic and domain operations
- **Repositories** (`repositories/` directory): Handle data access and external integrations
- Services leverage repositories for data operations
- Keep services focused on single responsibilities
- Abstract external dependencies through repository interfaces

## File Structure Guidelines

```
project/
├── src/
│   ├── main.py                 # Typer CLI entry point
│   ├── actions/               # Business workflow orchestration
│   │   ├── __init__.py
│   │   └── example_action.py
│   ├── services/              # Business logic layer
│   │   ├── __init__.py
│   │   └── example_service.py
│   └── repositories/          # Data access layer
│       ├── __init__.py
│       └── example_repository.py
├── tests/                     # Mirror source structure
│   ├── test_main.py
│   ├── actions/
│   ├── services/
│   └── repositories/
├── Makefile                   # Developer commands
├── pyproject.toml            # Project configuration
└── requirements.txt          # Dependencies
```

## Dependency Flow

```
CLI/Main → Actions → Services → Repositories
```

- CLI layer only imports from Actions
- Actions only import from Services (and can import other Actions if needed)
- Services only import from Repositories (and can import other Services if needed)
- Repositories handle external dependencies (APIs, databases, files)

## Testing Strategy

- Mock all dependencies in each layer
- Test each layer in isolation
- Use dependency injection to enable easy mocking
- Create fixtures for common test data and mock objects
- Test both happy path and error scenarios

## Code Quality Reminders

At the end of each coding session, run:
1. `make format` - Format code with Black
2. `make typecheck` - Run mypy strict type checking
3. `make test` - Run full test suite
4. `make lint` - Run additional linting if configured

### Rule 6: CLI Application Name and Installation
- The CLI application name is **'Taters'**
- After running `make install`, the CLI should be available as `taters` command in the terminal
- All sub-commands should be accessed via `taters <sub-command>` pattern
- Example: If creating a Dad Joke command, it should be run as `taters dad-joke`
- Configure the entry point in `pyproject.toml` to map `taters` to the main CLI function
- Use kebab-case for multi-word sub-command names

### Rule 7: Dependency Injection with Container
- Use the `dependency-injector` library (https://python-dependency-injector.ets-labs.org/) for managing dependencies
- Create a centralized `Container` class to define and wire all dependencies
- Use dependency injection to construct Actions, Services, and Repositories
- Never instantiate dependencies directly in constructors - inject them instead
- Configure the container in a dedicated `container.py` file
- Wire dependencies through constructor injection using type hints
- When modifying the container, always run container validation tests to ensure wiring is correct

#### Container Structure Guidelines:
```python
# container.py
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

class Container(containers.DeclarativeContainer):
    # Configuration
    config = providers.Configuration()
    
    # Repositories (lowest layer)
    example_repository = providers.Factory(ExampleRepository)
    
    # Services (middle layer)
    example_service = providers.Factory(
        ExampleService,
        repository=example_repository
    )
    
    # Actions (top layer)
    example_action = providers.Factory(
        ExampleAction,
        service=example_service
    )
```

#### Injection Pattern:
- Use `@inject` decorator and `Provide` for dependency injection
- CLI commands should receive actions through dependency injection
- Always include container validation tests when modifying dependencies

## Additional Guidelines

- Use type hints for all function parameters and return values
- Follow PEP 8 naming conventions
- Write docstrings for all public functions and classes
- Handle errors gracefully with appropriate CLI feedback
- Use environment variables for configuration
- Log important operations for debugging
