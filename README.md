<!--
  Auto-generated file. Do not edit directly.
  Edit docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="cc-utils">cc-utils</h1>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.1</p>

<h2 id="overview">Overview</h2>
<p>Cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.</p>

<hr />

<p><img src="https://github.com/jcook3701/cc-utils/actions/workflows/black-format.yml/badge.svg" alt="black-format" />
<img src="https://github.com/jcook3701/cc-utils/actions/workflows/ruff-lint.yml/badge.svg" alt="ruff-lint" />
<img src="https://github.com/jcook3701/cc-utils/actions/workflows/tests.yml/badge.svg" alt="tests" />
<img src="https://github.com/jcook3701/cc-utils/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" />
<img src="https://github.com/jcook3701/cc-utils/actions/workflows/yaml-lint.yml/badge.svg" alt="yaml-lint" /></p>

<h2 id="command-examples">Command Examples:</h2>
<h3 id="-cc-utils-add_docs-extract-run-list">🔧 cc-utils (add_docs, extract, run, list)</h3>
<h4 id="add-docs">Add Docs:</h4>
<p><strong>Description:</strong> Add GitHub docs to an existing project using the github-docs-cookiecutter template.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils add-docs <span class="si">$(</span>target_dir<span class="si">)</span>
</code></pre></div>    </div>
  </li>
</ol>

<h4 id="extract">Extract:</h4>
<p><strong>Description:</strong> Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils extract ./python3-cookiecutter  
</code></pre></div>    </div>
  </li>
  <li>
    <p>Modify extracted json to meet you new projects requirements.</p>
  </li>
  <li>Run ccutils extract command:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils extract <span class="se">\</span>
 <span class="nt">--repo</span> git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
 <span class="nt">--branch</span> develop <span class="se">\</span>
 <span class="nt">--output</span> clean_cookiecutter.json  
</code></pre></div>    </div>
  </li>
</ol>

<h4 id="run">Run:</h4>
<p><strong>Description:</strong> Run a cookiecutter template using a pre-supplied JSON configuration file.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils run <span class="si">$(</span>template<span class="si">)</span> <span class="si">$(</span>config<span class="si">)</span>
</code></pre></div></div>

<h4 id="list">List:</h4>
<p><strong>Description:</strong> List available cookiecutter templates under a namespace.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils list
</code></pre></div></div>

<hr />

<h3 id="️-config-cc-config">⚙️ Config (cc-config)</h3>
<p><strong>Description:</strong> cc-utils configuration tools.
<strong>Note:</strong> These are tools that are used to manage the cc-utils configuration file.</p>

<h4 id="sub-commands-show">Sub-commands: (show)</h4>

<h4 id="show">Show:</h4>
<p><strong>Description:</strong></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-config show
</code></pre></div></div>

<hr />

<h3 id="-build-cc-build">🔨 Build (cc-build)</h3>
<p><strong>Description:</strong> Cookiecutter build automation utilities.
<strong>Note:</strong> These commands are intended to be used within project Makefiles as build tools. Examples will assume for use in Makefile.</p>
<h4 id="sub-commands-readme-add-yaml-front-matter">Sub-commands: (readme, add-yaml-front-matter)</h4>

<h4 id="readme">Readme:</h4>
<p><strong>Description:</strong> Generates project readme from projects github-docs jekyll project.  The intention is keep the readme within ./docs/jekyll as the projects single source of truth.<br />
<strong>Note</strong>: Replace with real values.</p>
<div class="language-makefile highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nl">readme</span><span class="o">:</span>
  <span class="err">cc-build</span> <span class="err">readme</span> <span class="err">$(JEKYLL_DIR)</span> <span class="err">./README.md</span> <span class="err">\</span>
	  <span class="err">--tmp-dir</span> <span class="err">$(README_GEN_DIR)</span> <span class="err">--jekyll-cmd</span> <span class="s1">'$(JEKYLL_BUILD_CMD)'</span>
</code></pre></div></div>

<h4 id="add-yaml-front-matter">add-yaml-front-matter:</h4>
<p><strong>Description:</strong> This adds yaml-front-matter to the head of (md, yml, &amp; yaml) files to help beautify github docs.  Intended to be used with <a href="https://github.com/jcook3701/github-docs-cookiecutter">github-docs-cookiecutter</a><br />
<strong>Note:</strong> github-docs-cookiecutter will either be moved to <a href="https://github.com/jcook3701/cc-templates">cc-templates</a> or be added to cc-templates as a submodule.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-templates add-yaml-front-matter
</code></pre></div></div>

<hr />

<h2 id="-template-cc-templates">🍪 Template (cc-templates)</h2>
<p><strong>Description:</strong> cc-templates tools.
<strong>Note:</strong></p>
<h4 id="sub-commands-generate">Sub-commands: (generate)</h4>

<h4 id="generate">Generate:</h4>
<p><strong>Description:</strong> This is for custom Cookiecutter template (<a href="https://github.com/jcook3701/cc-templates">cc-templates</a>) that utilizes ccmeta.toml files to organize projects.
<strong>Note:</strong> This feature is still in development.  <strong>(Use at your own risk!!!)</strong>
<strong>Arguments:</strong></p>
<ul>
  <li>repo: Path to the template repository to generate README.md and Makefile
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-templates generate <span class="si">$(</span>repo<span class="si">)</span>
</code></pre></div>    </div>
  </li>
</ul>

<hr />

<h2 id="development-strategy">Development Strategy</h2>
<p><strong>Note:</strong> All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.</p>
<h3 id="️-build-environment-venv">🐍️ Build environment (.venv)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">install</span>  
</code></pre></div></div>
<h3 id="-linting-ruff--yaml-lint">🔍 Linting (ruff &amp; yaml-lint)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-check  
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-fix  
</code></pre></div></div>
<h3 id="-formatting-black">🎨 Formatting (black)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-check
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-fix
</code></pre></div></div>
<h3 id="-typechecking-mypy">🧠 Typechecking (mypy)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make typecheck  
</code></pre></div></div>
<h3 id="-testing-pytest">🧪 Testing (pytest)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">test</span>  
</code></pre></div></div>
<h3 id="-version-bumping-bumpy-my-version">🔖 Version Bumping (bumpy-my-version)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make bump-version-patch
</code></pre></div></div>
<h3 id="-building-build">📦 Building (build)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make build
</code></pre></div></div>
<h3 id="-publishing-twine">🚀 Publishing (Twine)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make pubish
</code></pre></div></div>
<h3 id="build-help">Build Help</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">help</span>  
</code></pre></div></div>

<hr />

<h2 id="authors-notes">Authors Notes:</h2>
<h3 id="future-ideas-todos">Future Ideas (TODO’s):</h3>
<ol>
  <li>cc-templates/ccindex.toml
    <ul>
      <li>create/update this file using the individual ccmeta.toml files in cc-templates</li>
    </ul>
  </li>
  <li>Finish updating this.readme with command usage.</li>
  <li>Readme <code class="language-plaintext highlighter-rouge">make readme</code> should end up being a ci/cd process to ensure it is always up to date.</li>
  <li>Thinking about adding a ci/cd process for version bumping.  To create a git tag.</li>
</ol>

<h3 id="future-design-decisions">Future Design Decisions</h3>
<ol>
  <li>I need to decide whether to change all my current Cookiecutter projects to use the prefix <code class="language-plaintext highlighter-rouge">cc-</code> and use them as submodules within the <a href="https://github.com/jcook3701/cc-templates">cc-templates</a> repository.  Or to just move the code directly into the cc-templates repository and use it as a monolithic repo.</li>
</ol>

<h2 id="packages">Packages</h2>
<h3 id="pypi-stable">PyPi (stable)</h3>

<h3 id="testpypi-development">TestPyPi (development)</h3>
<p>https://test.pypi.org/project/cc-utils/</p>
