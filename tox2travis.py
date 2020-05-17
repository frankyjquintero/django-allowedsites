from tox.config import parseconfig

file = open(".travis.yml", "w")
base_python = {
    "py26": "2.6",
    "py27": "2.7",
    "py33": "3.3",
    "py34": "3.4",
    "py35": "3.5",
    "py36": "3.6",
    "py37": "3.7",
    "py38": "3.8",
}
env_configs = parseconfig(None, 'tox').envconfigs

file.write("dist: xenial" + "\r")
file.write("language: python" + "\r")
file.write("matrix:" + "\r")
file.write("  include:" + "\r")

env_allow_failures = []

for env in env_configs:
    file.write("    - python: %s" % base_python[env[0:4]] + "\r")
    file.write("      env: TOX_ENV=%s" % env + "\r")
    if 'master' in env:
        env_allow_failures.append(env)

file.write("  allow_failures:" + "\r")
for env in env_allow_failures:
    file.write("     - env: TOX_ENV=%s" % env + "\r")


file.write("install:" + "\r")
file.write(" - pip install tox" + "\r")
file.write("script:" + "\r")
file.write(" - tox -e $TOX_ENV" + "\r")
file.close()
