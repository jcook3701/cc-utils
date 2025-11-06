# Makefile
# =========================================
# Project: ccutils
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c

# If V is set to '1' or 'y' on the command line, AT will be empty (verbose).
# Otherwise, AT will contain '@' (quiet by default).
# The '?' is a conditional assignment operator: it only sets V if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif
# --------------------------------------------------
# 📁 Build Directories
# --------------------------------------------------
SRC_DIR := ./src
TEST_DIR := ./tests
DOCS_DIR := ./docs
SPHINX_DIR := $(DOCS_DIR)/sphinx
JEKYLL_DIR := $(DOCS_DIR)/jekyll

SPHINX_BUILD_DIR := $(SPHINX_DIR)/_build/html
JEKYLL_OUTPUT_DIR := $(JEKYLL_DIR)/sphinx
README_GEN_DIR := $(JEKYLL_DIR)/tmp_readme
# --------------------------------------------------
# 🐍 Python / Virtual Environment
# --------------------------------------------------
PYTHON := python3.11
VENV_DIR := .venv
# --------------------------------------------------
# 🐍 Python Dependencies
# --------------------------------------------------
DEPS := .
DEV_DEPS := .[dev]
DEV_DOCS := .[docs]
# --------------------------------------------------
# 🐍️ Python Commands (venv, activate, pip)
# --------------------------------------------------
CREATE_VENV := $(PYTHON) -m venv $(VENV_DIR)
ACTIVATE := source $(VENV_DIR)/bin/activate
PIP := $(ACTIVATE) && $(PYTHON) -m pip
# --------------------------------------------------
# 🧠 Typing (mypy)
# --------------------------------------------------
MYPY := $(ACTIVATE) && $(PYTHON) -m mypy
# --------------------------------------------------
# 🔍 Linting (ruff, yaml)
# --------------------------------------------------
RUFF := $(ACTIVATE) && $(PYTHON) -m ruff
YAMLLINT := $(ACTIVATE) && $(PYTHON) -m yamllint
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
PYTEST := $(ACTIVATE) && $(PYTHON) -m pytest
# --------------------------------------------------
# 📘 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(ACTIVATE) && $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build --quiet
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
# 🏃‍♂️ ccutils command
# --------------------------------------------------
CCUTILS := $(ACTIVATE) && $(PYTHON) -m ccutils.ccutils

# -------------------------------------------------------------------
.PHONY: all venv install ruff-lint-check ruff-lint-fix yaml-lint-check \
	lint-check typecheck test build-docs run-docs readme clean help
# -------------------------------------------------------------------
# Default: run install, lint, typecheck, tests, and docs
# -------------------------------------------------------------------
all: install lint-check typecheck test build-docs readme

# --------------------------------------------------
# Virtual Environment Setup
# --------------------------------------------------
venv:
	$(AT)echo "🔨️ Creating virtual environment..."
	$(AT)$(CREATE_VENV)
	$(AT)echo "✅ Virtual environment created."

install: venv
	$(AT)echo "📦 Installing project dependencies..."
	$(AT)$(PIP) install --upgrade pip
	$(AT)$(PIP) install -e $(DEPS)
	$(AT)$(PIP) install -e $(DEV_DEPS)
	$(AT)$(PIP) install -e $(DEV_DOCS)
	$(AT)echo "✅ Dependencies installed."

# --------------------------------------------------
# Linting (ruff, yaml, jinja2)
# --------------------------------------------------
ruff-lint-check:
	$(AT)echo "🔍 Running ruff linting..."
	$(AT)$(RUFF) check $(SRC_DIR) $(TEST_DIR)

ruff-lint-fix:
	$(AT)echo "🎨 Running ruff lint fixes..."
	$(AT)$(RUFF) check --show-files $(SRC_DIR) $(TEST_DIR)
	$(AT)$(RUFF) check --fix $(SRC_DIR) $(TEST_DIR)

yaml-lint-check:
	$(AT)echo "🔍 Running yamllint..."
	$(AT)$(YAMLLINT) .

lint-check: ruff-lint-check yaml-lint-check

# --------------------------------------------------
# Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	$(AT)echo "🧠 Checking types (MyPy)..."
	$(AT)$(MYPY) $(SRC_DIR) $(TEST_DIR)

# --------------------------------------------------
# Testing (pytest)
# --------------------------------------------------
test:
	$(AT)echo "🧪 Running tests with pytest..."
	$(AT)PYTHONPATH=$(PWD)/src $(PYTEST) -v --maxfail=1 --disable-warnings $(TEST_DIR)

# --------------------------------------------------
# Documentation (Sphinx + Jekyll)
# --------------------------------------------------
sphinx:
	$(AT)echo "🔨 Building Sphinx documentation 📘 as Markdown..."
	$(AT)(SPHINX) $(SPHINX_DIR) $(JEKYLL_OUTPUT_DIR)
	$(AT)echo "✅ Sphinx Markdown build complete!"

jekyll:
	$(AT)echo "🔨 Building Jekyll site..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_BUILD)
	$(AT)echo "✅ Full documentation build complete!"

# TODO: Update project to work with sphinx
build-docs: jekyll

run-docs: build-docs
	$(AT)echo "🚀 Starting Jekyll development server..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_SERVE)

readme:
	$(AT)echo "🔨 Building ./README.md 📘 with Jekyll..."
	$(AT)mkdir -p $(README_GEN_DIR)
	$(AT)cp $(JEKYLL_DIR)/_config.yml $(README_GEN_DIR)/_config.yml
	$(AT)cp $(JEKYLL_DIR)/Gemfile $(README_GEN_DIR)/Gemfile
	$(AT)printf "%s\n" "---" \
		"layout: raw" \
		"permalink: /README.md" \
		"---" > $(README_GEN_DIR)/README.md
	$(AT)printf '%s\n' '<!--' \
		'  Auto-generated file. Do not edit directly.' \
		'  Edit $(JEKYLL_DIR)/README.md instead.' \
		'  Run ```make readme``` to regenrate this file' \
		'-->' >> $(README_GEN_DIR)/README.md
	$(AT)cat $(JEKYLL_DIR)/README.md >> $(README_GEN_DIR)/README.md
	$(AT)cd $(README_GEN_DIR) && $(JEKYLL_BUILD)
	$(AT)cp $(README_GEN_DIR)/_site/README.md ./README.md
	$(AT)echo "🧹 Clening README.md build artifacts..."
	$(AT)rm -r $(README_GEN_DIR)
	$(AT)echo "✅ README.md auto generation complete!"

# --------------------------------------------------
# Run ccutils program
# --------------------------------------------------
run:
	$(AT)echo "🏃‍♂️ running ccurtils..."
	$(AT)$(CCUTILS)

# --------------------------------------------------
# Clean artifacts
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Clening build artifacts..."
	$(AT)rm -rf $(SPHINX_DIR)/_build $(JEKYLL_OUTPUT_DIR)
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN)
	$(AT)rm -rf build dist *.egg-info
	$(AT)find $(SRC_DIR) $(TEST_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	$(AT)-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	$(AT)echo "🧹 Finished cleaning build artifacts..."

# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	$(AT)echo "📦 ccutils Makefile"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make venv                   Create virtual environment"
	$(AT)echo "  make install                Install dependencies"
	$(AT)echo "  make ruff-lint-check        Run Ruff linter"
	$(AT)echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff"
	$(AT)echo "  make yaml-lint-check        Run YAML linter"
	$(AT)echo "  make lint-check             Run all project linters (ruff, & yaml)"
	$(AT)echo "  make typecheck              Run Mypy type checking"
	$(AT)echo "  make test                   Run Pytest suite"
	$(AT)echo "  make build-docs             Build Sphinx + Jekyll documentation"
	$(AT)echo "  make run-docs               Preview Jekyll documentation"
	$(AT)echo "  make readme                 Uses Jekyll $(JEKYLL_DIR)/README.md for readme generation"
	$(AT)echo "  make run                    Run ccutils.py"
	$(AT)echo "  make clean                  Clean build artifacts"
	$(AT)echo "  make all                    Run lint, typecheck, test, and docs"
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
