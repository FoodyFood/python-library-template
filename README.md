# Python Library Template

This doesn't do much on it's own, it's a reference for myself for future
<br>

## Description

Once you build this, it will create a dist folder. 

If you pip install the whl file from there you can `import mylibrary` in  other projects to use it's functions.

Of course this doesn't do very much as I said, its just a template I can expand upon for future libraries I need to build.


## Development Environment Setup

As a developer you will need to be able to run the build command in the [Makefile](./makefile). This command will build a whl file that can be distributed and installed using pip.

Bash:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:
```
python -m venv .venv
source .\.venv\scripts\activate
pip install -r requirements.txt
```
<br>



