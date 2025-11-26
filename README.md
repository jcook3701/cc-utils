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

<h2 id="usage-commands">Usage (Commands)</h2>
<h3 id="add-docs">Add Docs</h3>
<p><strong>Description:</strong> Add GitHub docs to an existing project using the github-docs-cookiecutter template.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code></code></pre></div>    </div>
  </li>
</ol>

<h3 id="extract">Extract</h3>
<p><strong>Description:</strong> Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>ccutils extract ./python3-cookiecutter  
</code></pre></div>    </div>
  </li>
  <li>
    <p>Modify extracted json to meet you new projects requirements.</p>
  </li>
  <li>Run ccutils extract command:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>ccutils extract <span class="se">\</span>
 <span class="nt">--repo</span> git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
 <span class="nt">--branch</span> develop <span class="se">\</span>
 <span class="nt">--output</span> clean_cookiecutter.json  
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="run">Run</h3>
<p><strong>Description:</strong> Run a cookiecutter template using a pre-supplied JSON configuration file.</p>
<ol>
  <li>
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code></code></pre></div>    </div>
  </li>
</ol>

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
