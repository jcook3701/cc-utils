---
title: nutrimatic.hooks.post_gen_logic
layout: default
nav_order: 2
parent: api
---
nutrimatic.hooks.post_gen_logic
=================================

<a id="module-nutrimatic.hooks.post_gen_logic"></a>

nutri-matic Package

### nutrimatic.hooks.post_gen_logic.generate_ansible_dirs()

Generate ansible project directories

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.generate_cliff_changelog_dirs()

Generate changelog project directories

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.generate_docs_templates(context)

Generate one or more documentation templates inside docs/

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.get_make_cmds(context)

Generate one or more documentation templates inside docs/

* **Return type:**
  `list`[`str`]

### nutrimatic.hooks.post_gen_logic.replace_placeholders_in_dir(replacements, path=PosixPath('/home/jcook/Documents/git_repo/nutri-matic/docs/sphinx'))

Walk through every file in the newly generated project directory
and replace placeholders in all files.

* **Return type:**
  `None`

### Modules

| [`ansible`](nutrimatic.hooks.post_gen_logic.ansible.md#module-nutrimatic.hooks.post_gen_logic.ansible)          | nutri-matic Package   |
|-----------------------------------------------------------------------------------------------------------------|-----------------------|
| [`auto_vars`](nutrimatic.hooks.post_gen_logic.auto_vars.md#module-nutrimatic.hooks.post_gen_logic.auto_vars)    | nutri-matic Package   |
| [`changelogs`](nutrimatic.hooks.post_gen_logic.changelogs.md#module-nutrimatic.hooks.post_gen_logic.changelogs) | nutri-matic Package   |
| [`docs`](nutrimatic.hooks.post_gen_logic.docs.md#module-nutrimatic.hooks.post_gen_logic.docs)                   | nutri-matic Package   |
| [`license`](nutrimatic.hooks.post_gen_logic.license.md#module-nutrimatic.hooks.post_gen_logic.license)          | nutri-matic Package   |
| [`make`](nutrimatic.hooks.post_gen_logic.make.md#module-nutrimatic.hooks.post_gen_logic.make)                   | nutri-matic Package   |
