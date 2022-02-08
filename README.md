
# template_repo

### Using these files
- You should be able to change all info to your project by simply replacing all
mentions of "template_repo" to "your_project_name", where "your_project_name"
is the top level module directory name.
- There are both GitHub and GitLab ci/cd files. Use as needed.
   - Notice that you need to change links in the README file for them to work. 
- License should be [changed appropriately](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
- If you think something should be changed/is not right, please make an issue.
- The versioning layout as described in `template_repo/_version.py` was originally made by Paul Mueller.


<!-- Please change these links to your repo, you can usually find them
in the repo settings -->
[![pipeline status]()]()
[![coverage report]()]()


<!-- Short description of what this repo is for -->
This repository contains the default folder, file and code structures to be
used by anyone.


## Installing template_repo

This section is only for users. If you are a developer and want to contribute
to template_repo, you have to clone the repository and install in editable
mode (see below).

Depending on how you set up your GitHub/Lab, one of those
commands will work (should be using ssh!):

```bash
pip install template_repo@git+ssh://<GIT_URL_TO_YOUR_REPO>.git@X.Y.Z
pip install template_repo@git+https://<GIT_URL_TO_YOUR_REPO>.git@X.Y.Z
```

where ``X.Y.Z`` is the version of the package you are interested in.
For example to install `template_repo==0.0.1` via SSH
(works if you have two-factor authentication enabled), run:

```bash
pip install template_repo@git+ssh://<GIT_URL_TO_YOUR_REPO>.git@0.0.1
```

and https:

```bash
pip install template_repo@git+https://<GIT_URL_TO_YOUR_REPO>.git@0.0.1
```


Windows users please note that this might only work with git bash, depending on
permissions.

To **upgrade** to a new version, use the ``--upgrade`` argument:

```bash
pip install --upgrade template_repo@git+ssh://<GIT_URL_TO_YOUR_REPO>.git@0.0.2
```
and https:

```bash
pip install --upgrade template_repo@git+https://<GIT_URL_TO_YOUR_REPO>.git@0.0.2
```

## For Developers

Activate your virtual environment and install this repo in editable mode,
i.e. in the root of the repository, run:

```bash
pip install -e .
```

### Testing

First install the testing requirements:

```bash
pip install -r tests/requirements.txt
```

Then run the tests with `pytest`:

```
pytest tests
```

and lint your code with flake8:

```bash
flake8 template_repo tests
```

## Releasing New Versions

1. Create a new tag:

```bash
git tag -a "0.1.0" -m "new release"  
git push --tags origin
```

At this point, users will be able to install this package with the description
provided at the top of this readme.

2. Create a distribution package e.g. ``template_repo_XYZ.tar.gz`` with:

```bash
python setup.py sdist
```

3. Give the ``.tar.gz`` file to users and tell them to pip-install it with:

```bash
pip install template_repo_XYZ.tar.gz
```
