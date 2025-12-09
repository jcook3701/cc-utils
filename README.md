<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/nutri-matic/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="nutri-matic">Nutri-Matic</h1>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.2</p>

<h2 id="overview">Overview</h2>
<p>Cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.</p>

<hr />

<p><img src="https://github.com/jcook3701/nutri-matic/actions/workflows/black-format.yml/badge.svg" alt="black-format" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/ruff-lint.yml/badge.svg" alt="ruff-lint" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/tests.yml/badge.svg" alt="tests" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" />
<img src="https://github.com/jcook3701/nutri-matic/actions/workflows/yaml-lint.yml/badge.svg" alt="yaml-lint" /></p>

<h2 id="command-examples">Command Examples:</h2>
<h3 id="-nutrimatic-add_docs-extract-run-list">🔧 nutrimatic (add_docs, extract, run, list)</h3>
<h4 id="add-docs">Add Docs:</h4>
<p><strong>Description:</strong> Add GitHub docs to an existing project using the github-docs-cookiecutter template.
1.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nutrimatic add-docs <span class="si">$(</span>target_dir<span class="si">)</span>
</code></pre></div></div>

<h4 id="extract">Extract:</h4>
<p><strong>Description:</strong> Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.</p>
<ol>
  <li>Run extract command to local cookiecutter repository:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nutrimatic extract ./python3-cookiecutter
</code></pre></div>    </div>
    <p><strong>OR</strong></p>
  </li>
  <li>Run extract command to remote github cookiecutter repository:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nutrimatic extract <span class="se">\</span>
 <span class="nt">--repo</span> git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
 <span class="nt">--branch</span> develop <span class="se">\</span>
 <span class="nt">--output</span> clean_cookiecutter.json
</code></pre></div>    </div>
  </li>
  <li>Modify extracted json to meet you new projects requirements.</li>
</ol>

<h4 id="run">Run:</h4>
<p><strong>Description:</strong> Run a cookiecutter template using a pre-supplied JSON configuration file.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nutrimatic run <span class="si">$(</span>template<span class="si">)</span> <span class="si">$(</span>config<span class="si">)</span>
</code></pre></div></div>

<h4 id="list">List:</h4>
<p><strong>Description:</strong> List available cookiecutter templates under a namespace.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nutrimatic list
</code></pre></div></div>

<hr />

<h3 id="️-config-nm-config">⚙️ Config (nm-config)</h3>
<p><strong>Description:</strong> nutrimatic configuration tools.<br />
<strong>Note:</strong> These are tools that are used to manage package configuration file.<br />
<strong>Sub-commands:</strong> (show)</p>

<h4 id="show">Show:</h4>
<p><strong>Description:</strong></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nm-config show
</code></pre></div></div>

<hr />

<h3 id="-build-nm-build">🔨 Build (nm-build)</h3>
<p><strong>Description:</strong> Cookiecutter build automation utilities.<br />
<strong>Note:</strong> These commands are intended to be used within project Makefiles as build tools. Examples will assume for use in Makefile.<br />
<strong>Sub-commands:</strong> (readme, add-yaml-front-matter)</p>

<h4 id="readme">Readme:</h4>
<p><strong>Description:</strong> Generates project readme from projects github-docs jekyll project.  The intention is keep the readme within <code class="language-plaintext highlighter-rouge">./docs/jekyll</code> as the project’s single source of truth.<br />
<strong>Note</strong>: Intended for use within project Makefile as shown below.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code>PROJECT_ROOT :<span class="o">=</span> <span class="si">$(</span>PWD<span class="si">)</span>
DOCS_DIR :<span class="o">=</span> <span class="si">$(</span>PROJECT_ROOT<span class="si">)</span>/docs
JEKYLL_DIR :<span class="o">=</span> <span class="si">$(</span>DOCS_DIR<span class="si">)</span>/jekyll
JEKYLL_BUILD :<span class="o">=</span> bundle <span class="nb">exec </span>jekyll build <span class="nt">--quiet</span>
README_GEN_DIR :<span class="o">=</span> <span class="si">$(</span>JEKYLL_DIR<span class="si">)</span>/tmp_readme
README_FILE :<span class="o">=</span> <span class="si">$(</span>PROJECT_ROOT<span class="si">)</span>/README.md

readme:
  nm-build readme <span class="si">$(</span>JEKYLL_DIR<span class="si">)</span> <span class="si">$(</span>README_FILE<span class="si">)</span> <span class="se">\</span>
	  <span class="nt">--tmp-dir</span> <span class="si">$(</span>README_GEN_DIR<span class="si">)</span> <span class="nt">--jekyll-cmd</span> <span class="s1">'$(JEKYLL_BUILD)'</span>
</code></pre></div></div>

<h4 id="add-yaml-front-matter">add-yaml-front-matter:</h4>
<p><strong>Description:</strong> This adds yaml-front-matter to the head of (md, yml, &amp; yaml) files to help beautify github docs.  Intended to be used with <a href="https://github.com/jcook3701/github-docs-cookiecutter">github-docs-cookiecutter</a></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nm-build add-yaml-front-matter
</code></pre></div></div>

<hr />

<h2 id="-template-nm-templates">🍪 Template (nm-templates)</h2>
<p><strong>Description:</strong> nm-templates tools.<br />
<strong>Note:</strong> github-docs-cookiecutter will either be moved to <a href="https://github.com/jcook3701/cc-templates">cc-templates</a> or be added to cc-templates as a submodule.<br />
<strong>Sub-commands:</strong> (generate)</p>

<h4 id="generate">Generate:</h4>
<p><strong>Description:</strong> This is for custom Cookiecutter template (<a href="https://github.com/jcook3701/cc-templates">cc-templates</a>) that utilizes ccmeta.toml files to organize projects.<br />
<strong>Note:</strong> This feature is still in development.  <strong>(Use at your own risk!!!)</strong><br />
<strong>Arguments:</strong></p>
<ul>
  <li>repo: Path to the template repository to generate README.md and Makefile
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>nm-templates generate <span class="si">$(</span>repo<span class="si">)</span>
</code></pre></div>    </div>
  </li>
</ul>

<hr />

<h2 id="development-strategy">Development Strategy</h2>
<p><strong>Note:</strong> All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.</p>
<h3 id="️-build-environment-venv">🐍️ Build environment (.venv)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">install</span>
</code></pre></div></div>
<h3 id="-dependency-management-deptry">🧬 Dependency Management (deptry)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make dependency-check
</code></pre></div></div>
<h3 id="️-security-audit-pip-audit">🛡️ Security Audit (pip-audit)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make security
</code></pre></div></div>
<h3 id="-formatting-black">🎨 Formatting (black)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-check
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-fix
</code></pre></div></div>
<h3 id="-linting-ruff-toml--yaml-lint">🔍 Linting (ruff, toml, &amp; yaml-lint)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-check
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-fix
</code></pre></div></div>
<h3 id="-spellchecking-codespell">🎓 Spellchecking (codespell)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make spellcheck
</code></pre></div></div>
<h3 id="-typechecking-mypy">🧠 Typechecking (mypy)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make typecheck
</code></pre></div></div>
<h3 id="-testing-pytest">🧪 Testing (pytest)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">test</span>
</code></pre></div></div>
<h3 id="-building-build">📦 Building (build)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make build
</code></pre></div></div>
<h3 id="-publishing-twine--github">🚀 Publishing (Twine + Github)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make publish
</code></pre></div></div>
<h3 id="-version-bumping-bumpy-my-version">🔖 Version Bumping (bumpy-my-version)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make bump-version-patch
</code></pre></div></div>
<h3 id="-build-help">❓ Build Help</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">help</span>
</code></pre></div></div>

<hr />

<h2 id="commit-help">Commit Help:</h2>
<p><strong>Note:</strong> Commits are required to be conventional git commit message.  This helps with the auto-generation of the changelog files and is enforced by pre-commit.<br />
<strong>example:</strong></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;<span class="nb">type</span><span class="o">&gt;[</span>optional scope]: &lt;description&gt;

<span class="o">[</span>optional body]

<span class="o">[</span>optional footer<span class="o">(</span>s<span class="o">)]</span>
</code></pre></div></div>
<ul>
  <li><code class="language-plaintext highlighter-rouge">&lt;type&gt;</code>: A required noun that describes the nature of the change.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional scope]</code>: An optional phrase within parentheses that specifies the part of the codebase being affected (e.g., fix(parser):).</li>
  <li><code class="language-plaintext highlighter-rouge">&lt;description&gt;</code>: A required short, imperative-mood summary of the changes.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional body]</code>: A longer description providing additional context and “what and why” details.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional footer(s)]</code>: Used for adding meta-information, such as issue references (Fixes #123) or indicating breaking changes.</li>
</ul>

<hr />

<h2 id="requirements">Requirements:</h2>
<ol>
  <li>Python 3.11
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span><span class="nb">sudo </span>apt <span class="nb">install </span>python3.11
</code></pre></div>    </div>
  </li>
  <li><a href="https://rust-lang.org/tools/install/">rustup</a><br />
<strong>Note:</strong> I found that it is easiest to use rustup to manage rustc and cargo but this is not required.<br />
<strong>Example:</strong> Install rustup with the following:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>curl <span class="nt">--proto</span> <span class="s1">'=https'</span> <span class="nt">--tlsv1</span>.2 <span class="nt">-sSf</span> https://sh.rustup.rs | sh
</code></pre></div>    </div>
  </li>
  <li><a href="https://git-cliff.org/">git-cliff</a><br />
<strong>Note:</strong> git-cliff can generate changelog files from the Git history by utilizing conventional commits as well as regex-powered custom parsers.
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cargo <span class="nb">install </span>git-cliff
</code></pre></div>    </div>
  </li>
</ol>

<hr />

<h2 id="authors-notes">🍹Authors Notes:</h2>
<p>Their fundamental design flaws are completely hidden by their superficial design flaws.</p>

<h3 id="todos">TODO’s:</h3>
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

<h3 id="future-design-decisions">Future Design Decisions:</h3>
<ol>
  <li>I need to decide whether to change all my current Cookiecutter projects to use the prefix <code class="language-plaintext highlighter-rouge">cc-</code> and use them as submodules within the <a href="https://github.com/jcook3701/cc-templates">cc-templates</a> repository.  Or to just move the code directly into the cc-templates repository and use it as a monolithic repo.</li>
</ol>

<!--

2. Need to come up with a new name as ccutils and cc-utils are giving me issues on either pypi or testpypi.
  * Thinking of going with Hitch Hikers Guide to Galaxy based names as this is becoming rediculious.


🧣📖🤖🧑‍🚀👽✨🚀🛸🪐🍹🧃

cc-utils -> slartibartfast, improbability_drive, probability_engine, hyperjumps
cc-templates -> ~~Magrathea~~, restaurant_at_end_of_universe, life_universe_everything

slartibartfast -> src -> fjord
slartibartfast -> Magrathea

SubEtha -> Messaging system.  Good Open Name. (should claim)

To replace cc-utils:
  1. ✅ HeartOfGold
  2. ✅ heart_of_gold, (claim)
  3. ❌ ImprobCore
  4. ✅ improbability_core (claim)
  5. ✅ improb_core
  6. ✅ robot_marvin
To replace cc-templates:
  1. ❌ NutriMatic
  2. ✅ nutri_matic (claim)

__Notes:__
##### Project Theme (Hitch Hikers Guide the Galaxy)
"Don't Panic."
"The ships hung in the sky in much the same way that bricks don't."
"The answer to the great question...of Life, the Universe and Everything...is...forty-two."
"For a moment, nothing happened. Then, after a second or so, nothing continued to happen."
"I may not have gone where I intended to go, but I think I have ended up where I needed to be".
"The story so far: In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move".

##### Heart of Gold (cc-utils)
1. “Hi there! This is Eddie, your shipboard computer, and I’m feeling just great, guys, and I know I’m just going to get a bundle of kicks out of any program you care to run through me.”

2. “That ship?” said Ford in sudden excitement. “What happened to it? Do you know?” “It hated me because I talked to it.” “You talked to it?” exclaimed Ford. “What do you mean you talked to it?” “Simple. I got very bored and depressed, so I went and plugged myself in to its external computer feed. I talked to the computer at great length and explained my view of the Universe to it,” said Marvin. “And what happened?” pressed Ford. “It committed suicide,” said Marvin, and stalked off back to the Heart of Gold.

##### Nuri-Matic (cc-utils)
“The Nutri-Matic Drinks Synthesizer claimed to produce the widest possible range of drinks personally matched to the tastes and metabolism of whoever cared to use it. When put to test, however, it invariably produced a plastic cup filled with a liquid which was almost, but not quite, entirely unlike tea.”


cc-python-cli
cc-ansible-role
cc-sphinx-docs
cc-github-docs
-->

<h2 id="package-information">Package Information:</h2>
<h3 id="pypi-stable"><a href="https://pypi.org/project/nutri-matic/">PyPi:</a> (stable)</h3>
<h3 id="testpypi-development"><a href="https://test.pypi.org/project/nutri-matic/">TestPyPi:</a> (development)</h3>
<h3 id="github"><a href="https://github.com/jcook3701/nutri-matic/">GitHub:</a></h3>
<h3 id="gitdocs"><a href="https://jcook3701.github.io/nutri-matic/">GitDocs:</a></h3>

<!--
# Authors Second Hidden Notes:

## Development Ideas:
1. Right now I am thinking about adding two different types of meta files.
  * teabag.toml -> This will be used in (cc-templates, to be changed to: )
  * tea.toml -> This will be automatically to generated projects and used for updates.
      1. Potentially human generated and added to a project to allow
-->
