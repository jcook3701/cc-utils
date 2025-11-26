<!--
  Auto-generated file. Do not edit directly.
  Edit docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="cc-utils">cc-utils</h1>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.1</p>

<h2 id="overview">Overview</h2>
<p>Cookiecutter utilities for jcook3701’s cookiecuter templates.</p>

<hr />

<h2 id="usage-commands">Usage (Commands)</h2>
<h3 id="add-docs">Add Docs</h3>
<p><strong>Description:</strong> Add GitHub docs to an existing project using the github-docs-cookiecutter template.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils add-docs <span class="nt">--help</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="extract">Extract</h3>
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

<h3 id="run">Run</h3>
<p><strong>Description:</strong> Run a cookiecutter template using a pre-supplied JSON configuration file.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils run <span class="nt">--help</span>
</code></pre></div></div>

<h3 id="list">List</h3>
<p><strong>Description:</strong> List available cookiecutter templates under a namespace.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-utils list <span class="nt">--help</span>
</code></pre></div></div>

<hr />

<h3 id="config-cc-config">Config (cc-config)</h3>
<p><strong>Description:</strong> cc-utils configuration tools.</p>

<h4 id="sub-commands-show">Sub-commands: (show)</h4>

<h4 id="show">Show</h4>
<p><strong>Description:</strong></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-config show
</code></pre></div></div>

<hr />

<h3 id="build-cc-build">Build (cc-build)</h3>
<p><strong>Description:</strong> Cookiecutter build automation utilities.</p>

<h4 id="sub-commands-readme-add-yaml-front-matter">Sub-commands: (readme, add-yaml-front-matter)</h4>

<h4 id="readme">Readme</h4>
<p><strong>Note</strong>: Replace with real values.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-build readme <span class="si">$(</span>JEKYLL_DIR<span class="si">)</span> ./README.md <span class="se">\</span>
		<span class="nt">--tmp-dir</span> <span class="si">$(</span>README_GEN_DIR<span class="si">)</span> <span class="nt">--jekyll-cmd</span> <span class="s1">'$(JEKYLL_BUILD_CMD)'</span>
</code></pre></div></div>

<hr />

<h2 id="template-cc-templates">Template (cc-templates)</h2>
<p><strong>Description:</strong> cc-templates tools.</p>

<h4 id="sub-commands-readme-add-yaml-front-matter-1">Sub-commands: (readme, add-yaml-front-matter)</h4>

<h4 id="generate">Generate:</h4>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cc-templates generate
</code></pre></div></div>

<hr />

<h2 id="development">Development</h2>
<h3 id="build-environment-venv">Build environment (.venv)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">install</span>  
</code></pre></div></div>
<h3 id="linting-ruff--yaml-lint">Linting (ruff &amp; yaml-lint)</h3>
<p>2.</p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-check  
</code></pre></div></div>
<h3 id="typechecking-mypy">Typechecking (mypy)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make typecheck  
</code></pre></div></div>
<h3 id="testing-pytest">Testing (pytest)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">test</span>  
</code></pre></div></div>
<h3 id="building-build">Building (build)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make build
</code></pre></div></div>
<h3 id="publishing-twine">Publishing (Twine)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make pubish
</code></pre></div></div>
<h3 id="build-help">Build Help</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">help</span>  
</code></pre></div></div>
<h2 id="usage">Usage</h2>
<ol>
  <li>Source environment created by <code class="language-plaintext highlighter-rouge">make install</code>.
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span><span class="nb">source</span> .venv  
</code></pre></div>    </div>
  </li>
</ol>

<hr />

<h3 id="authors-notes">Authors Notes:</h3>

<h3 id="future-ideas-todos">Future Ideas (TODOs):</h3>
<ol>
  <li>cc-templates/ccindex.toml
    <ul>
      <li>create/update this file using the individual ccmeta.toml files in cc-templates</li>
    </ul>
  </li>
</ol>

<h2 id="packages">Packages</h2>
<h3 id="pypi-stabale">PyPi (stabale)</h3>

<h3 id="testpypi-development">TestPyPi (development)</h3>
<p>https://test.pypi.org/project/cc-utils/</p>
