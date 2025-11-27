---
title: ccutils.models.metadata
layout: default
nav_order: 2
parent: api
---
ccutils.models.metadata
=======================

<a id="module-ccutils.models.metadata"></a>

cc-utils Package

### Classes

| [`Metadata`](#ccutils.models.metadata.Metadata)(\*[, version, author, license])   | metadata type.   |
|-----------------------------------------------------------------------------------|------------------|

### *class* ccutils.models.metadata.Metadata(, version: str = '', author: str = '', license: str = '')

Bases: `BaseModel`

metadata type.

#### version

(str).

* **Type:**
  str

#### author

(str).

* **Type:**
  str

#### license

(str).

* **Type:**
  str

#### copyright

(str).

#### version *: str*

#### author *: str*

#### license *: str*

#### *property* copyright *: str*

#### *classmethod* from_package(package_name: str = 'cc-utils') → [Metadata](#ccutils.models.metadata.Metadata)

Create Metadata from the installed package metadata.

Falls back to defaults if the package is not found.
