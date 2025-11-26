# Makefile
# =========================================
# Project: cc-utils
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c

# If V is set to '1' or 'y' on the command line,
# AT will be empty (verbose).  Otherwise, AT will
# contain '@' (quiet by default).  The '?' is a
# conditional assignment operator: it only sets V
# if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif
# Detect if we are running inside GitHub Actions CI.
# GitHub sets the environment variable GITHUB_ACTIONS=true in workflows.
# We set CI=1 if running in GitHub Actions, otherwise CI=0 for local runs.
ifeq ($(GITHUB_ACTIONS),true)
CI := 1
else
CI := 0
endif

# Define a reusable CI-safe runner
define run_ci_safe =
( $1 || [ "$(CI)" != "1" ] )
endef
# --------------------------------------------------
# ⚙️ Build Settings
# --------------------------------------------------
PACKAGE_NAME := "cc-utils"
PACKAGE_AUTHOR := "Jared Cook"
PACKAGE_VERSION := "0.1.1"
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
PYTHON_CMD := python3.11
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
CREATE_VENV := $(PYTHON_CMD) -m venv $(VENV_DIR)
ACTIVATE := source $(VENV_DIR)/bin/activate
PYTHON := $(ACTIVATE) && $(PYTHON_CMD)
PIP := $(PYTHON) -m pip
# --------------------------------------------------
# 🧠 Typing (mypy)
# --------------------------------------------------
MYPY := $(PYTHON) -m mypy
# --------------------------------------------------
# 🔍 Linting (ruff, yaml)
# --------------------------------------------------
RUFF := $(PYTHON) -m ruff
YAMLLINT := $(PYTHON) -m yamllint
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
BLACK := $(PYTHON) -m black
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
PYTEST := $(PYTHON) -m pytest
COVERAGE := $(ACTIVATE) && coverage run -m pytest
# --------------------------------------------------
# 📘 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build --quiet
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
BUMPVERSION := bump-my-version bump --verbose
# Patch types:
MAJOR := major
MINOR := minor
PATCH := patch
# --------------------------------------------------
# 📦 Build (build)
# --------------------------------------------------
BUILD := $(PYTHON) -m build
# --------------------------------------------------
# 🚀 Publishing (twine)
# --------------------------------------------------
TWINE := $(PYTHON) -m twine
# Repos:
PYPI := upload dist/*
TESTPYPI := upload --repository testpypi --verbose dist/*
# --------------------------------------------------
# 🏃‍♂️ cc-utils command
# --------------------------------------------------
CCUTILS := $(PYTHON) -m ccutils
# -------------------------------------------------------------------
.PHONY: all venv install black-formatter-check black-formatter-fix format-check format-fix \
	ruff-lint-check ruff-lint-fix yaml-lint-check lint-check lint-fix \
	typecheck test sphinx jekyll jekyll-serve build-docs run-docs readme \
	build publish clean help
# -------------------------------------------------------------------
# Default: run install, lint, typecheck, tests, and build-docs
# -------------------------------------------------------------------
all: clean install lint-check typecheck test build-docs readme
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
# Formating (black)
# --------------------------------------------------
black-formatter-check:
	$(AT)echo "🔍 Running black formatter style check..."
	$(AT)$(call run_ci_safe, $(BLACK) --check $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Finished formatting check of Python code with Black!"
	
black-formatter-fix:
	$(AT)echo "🎨 Running black formatter fixes..."
	$(AT)$(BLACK) $(SRC_DIR) $(TESTS_DIR)
	$(AT)echo "✅ Finished formatting Python code with Black!"

format-check: black-formatter-check
format-fix: black-formatter-fix
# --------------------------------------------------
# Linting (ruff, yaml)
# --------------------------------------------------
ruff-lint-check:
	$(AT)echo "🔍 Running ruff linting..."
	$(AT)$(RUFF) check $(SRC_DIR) $(TEST_DIR)
	$(AT)echo "✅ Python lint check complete!"

ruff-lint-fix:
	$(AT)echo "🎨 Running ruff lint fixes..."
	$(AT)$(RUFF) check --show-files $(SRC_DIR) $(TEST_DIR)
	$(AT)$(RUFF) check --fix $(SRC_DIR) $(TEST_DIR)
	$(AT)echo "✅ Python lint fix complete!"

yaml-lint-check:
	$(AT)echo "🔍 Running yamllint..."
	$(AT)$(YAMLLINT) .
	$(AT)echo "✅ Yaml lint check complete!"

lint-check: ruff-lint-check yaml-lint-check
lint-fix: ruff-lint-fix
# --------------------------------------------------
# Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	$(AT)echo "🧠 Checking types (MyPy)..."
	$(AT)$(call run_ci_safe, $(MYPY) $(SRC_DIR) $(TEST_DIR))
	$(AT)echo "✅ Python typecheck complete!"
# --------------------------------------------------
# Testing (pytest)
# --------------------------------------------------
test:
	$(AT)echo "🧪 Running tests with pytest..."
	$(AT)$(call run_ci_safe, $(PYTEST) $(TEST_DIR))
	$(AT)echo "✅ Python tests complete!"
# --------------------------------------------------
# Documentation (Sphinx + Jekyll)
# --------------------------------------------------
sphinx:
	$(AT)echo "🧹 Clening Sphinx build artifacts..."
	$(AT)rm -rf $(JEKYLL_OUTPUT_DIR)
	$(AT)echo "🔨 Building Sphinx documentation 📘 as Markdown..."
	$(AT)$(SPHINX) $(SPHINX_DIR) $(JEKYLL_OUTPUT_DIR)
	$(AT)echo "✅ Sphinx Markdown build complete!"

jekyll:
	$(AT)echo "🔨 Building Jekyll site 🌐..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_BUILD)
	$(AT)echo "✅ Full documentation build complete!"

jekyll-serve:
	$(AT)echo "🚀 Starting Jekyll development server 🌐..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_SERVE)

build-docs: sphinx jekyll
run-docs: jekyll-serve

readme:
	$(AT)$(CCUTILS) build readme $(JEKYLL_DIR) ./README.md \
		--tmp-dir $(README_GEN_DIR) --jekyll-cmd '$(JEKYLL_BUILD)'

# DEPRECATED: DON'T USE!!! #
old-readme:
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
# bump version of program
# --------------------------------------------------
# TODO: Also create a git tag of current version.
bump-version-patch:
	$(AT)echo "🔖 Updating $(PACKAGE_NAME) version from $(VERSION)..."
	$(AT)$(BUMPVERSION) $(PATCH)
	$(AT)echo "✅ $(PACKAGE_NAME) version udpate complete!"
# --------------------------------------------------
# Build program
# --------------------------------------------------
build:
	$(AT)echo "📦 Packing $(PACKAGE_NAME)..."
	$(AT)$(BUILD)
	$(AT)echo "✅ $(PACKAGE_NAME) packaging complete!"
# --------------------------------------------------
# Publish program (test.pypi & pypi)
# --------------------------------------------------
publish-test:
	$(AT)echo "🚀 Publishing $(PACKAGE_NAME) to testpypi..."
	$(AT)$(TWINE) $(TESTPYPI)
	$(AT)echo "✅ $(PACKAGE_NAME) upload complete!"

publish:
	$(AT)echo "🚀 Publishing $(PACKAGE_NAME) to pypi..."
	$(AT)$(TWINE) $(PYPI)
	$(AT)echo "✅ $(PACKAGE_NAME) upload complete!"
# --------------------------------------------------
# Clean artifacts
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Clening build artifacts..."
	$(AT)rm -rf $(SPHINX_DIR)/_build
	$(AT)$(call run_ci_safe, cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN))
	$(AT)rm -rf build dist *.egg-info
	$(AT)find $(SRC_DIR) $(TEST_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	$(AT)rm -rf $(VENV_DIR)
	$(AT)echo "🧹 Finished cleaning build artifacts..."
# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	$(AT)echo "📦 $(PACKAGE_NAME) Makefile"
	$(AT)echo "   author: $(PACKAGE_AUTHOR)"
	$(AT)echo "   version: $(PACKAGE_VERSION)"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make venv                   Create virtual environment"
	$(AT)echo "  make install                Install dependencies"
	$(AT)echo "  make format-check           Run all project formatter checks (black)"
	$(AT)echo "  make format-fix             Run all project formatter autofixes (black)"
	$(AT)echo "  make ruff-lint-check        Run Ruff linter"
	$(AT)echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff"
	$(AT)echo "  make yaml-lint-check        Run YAML linter"
	$(AT)echo "  make lint-check             Run all project linters (ruff, & yaml)"
	$(AT)echo "  make lint-fix               Run all project linter autofixes (ruff)"
	$(AT)echo "  make typecheck              Run Mypy type checking"
	$(AT)echo "  make test                   Run Pytest suite"
	$(AT)echo "  make build-docs             Build Sphinx + Jekyll documentation"
	$(AT)echo "  make run-docs               Preview Jekyll documentation"
	$(AT)echo "  make readme                 Uses Jekyll $(JEKYLL_DIR)/README.md for readme generation"
	$(AT)echo "  make run                    Run cc-utils.py"
	$(AT)echo "  make clean                  Clean build artifacts"
	$(AT)echo "  make all                    Run lint, typecheck, test, and docs"
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
