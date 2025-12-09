# Makefile
# =========================================
# Project: Sphinx documentation for  nutri-matic 🍹
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c

# --------------------------------------------------
# ⚙️ Sphinx Build Settings
# --------------------------------------------------
# You can set these variables from the command line, and also
# from the environment for the first two.
# --------------------------------------------------
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
PUBLISHDIR    ?=

# Define the directories where autosummary generates stub files
STUBDIRS      = api _autosummary_generated
# --------------------------------------------------
.PHONY: all publish-markdown help clean Makefile markdown-gen
all: markdown-gen publish-markdown

markdown-gen: markdown

ifeq ($(PUBLISHDIR),)
publish-markdown:
	@echo "⚠️  Warning: Skipping publish-markdown target because PUBLISHDIR is empty."
else
publish-markdown:
	@echo "🧹 Cleaning Previous published Sphinx artifacts..."
	@rm -rf $(PUBLISHDIR)
	@echo "✅ Finished cleaning old Sphinx artifacts."
	@echo "🚀 Publishing sphinx markdown documentation to $(PUBLISHDIR)..."
	@mkdir -p $(PUBLISHDIR)
	@mv $(BUILDDIR)/markdown/* $(PUBLISHDIR)
	@echo "✅ Finished published markdown documentation to $(PUBLISHDIR)."
endif
# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# --------------------------------------------------
# Custom clean target: removes build artifacts AND generated stub files
# --------------------------------------------------
clean:
	@echo "🧹 Cleaning build artifacts and autosummary stubs..."
	@rm -rf "$(BUILDDIR)" $(STUBDIRS)
	@echo "✅ Clean complete."
# --------------------------------------------------
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# --------------------------------------------------
%: Makefile
	@echo "📚 Running Sphinx Documentation Generator..."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "✅ Sphinx run complete."
# --------------------------------------------------
