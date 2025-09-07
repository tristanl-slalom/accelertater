.PHONY: install install-dev test format typecheck lint dev clean

# Install production dependencies
install:
	pip install -e .

# Install development dependencies
install-dev:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

# Run unit tests with strict coverage requirements
test:
	pytest --cov-fail-under=80

# Format code with Black (and check for compliance)
format:
	black src/ tests/

# Check code formatting without making changes
format-check:
	black --check --diff src/ tests/

# Run type checking with mypy in strict mode
typecheck:
	mypy --strict src/

# Run all quality checks (CI simulation)
quality-check: format-check typecheck test
	@echo "✅ All quality checks passed!"

# Run linting (placeholder for additional linters)
lint:
	@echo "Linting complete"

# Run the CLI in development mode
dev:
	python -m taters

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
