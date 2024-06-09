# #!/usr/bin/env python
# # App versioned with #3 from
# # https://packaging.python.org/guides/single-sourcing-package-version/
# from setuptools import find_packages, setup

# app_name = 'app'
# app_path = './app'
# version = {}

# with open(f'{app_path}/version.py') as fp:
#     exec(fp.read(), version)

# with open('README.md') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

# extras = {
#     'dev': open(f'{app_path}/requirements-dev.txt').read().splitlines(),
#     'test': ['pytest'],
#     # 'opt': ['oapackage', 'pqkmeans'],
#     # 'doc': open('docs/requirements.txt').read().splitlines(),
#     # 'experimental': ['asap3', 'dftpy']
# }

# setup(
#     name = app_name,
#     version = version["__version__"],
#     description = (''),
#     long_description = readme,
#     long_description_content_type = 'text/markdown',
#     url = 'https://github.com/qte77/ML-HF-WnB',
#     author = 'qte77',
#     license = license,
#     packages = [app_name] + [app_name + '.' + pkg for pkg in find_packages(app_name)],
#     zip_safe = False,
#     install_requires = f'{app_path}/requirements.txt',
#     extras_require = extras,
#     # entry_points = {
#     #     "app": [
#     #         "app=app.app",
#     #     ]
#     # },
# )

# if __name__ == '__main__':
#     setup()
