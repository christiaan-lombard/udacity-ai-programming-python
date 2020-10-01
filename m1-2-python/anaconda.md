# Anaconda

Anaconda is a program to manage (install, upgrade, or uninstall) packages and environments to use with Python.

## Installation

- [Download and install Anaconda](https://www.anaconda.com/products/individual)
- In bash, run `[conda install dir]/Scripts/conda init bash` which will update your .bash_profile adding `eval "$('/d/exe/anaconda3/Scripts/conda.exe' 'shell.bash' 'hook')"`. Move this to .bashrc if .bash_profile is not loaded in your shell.
- Remove conda environment from PS1: `conda config --set changeps1 false`
- [Modify PS1 behaviour](https://stackoverflow.com/questions/42481726/how-to-modify-conda-source-activate-ps1-behavior)
- Add `alias python='winpty python.exe'` to .bashrc

## Conda

- `conda upgrade conda` - Update Conda utility
- `conda upgrade --all` - Update all packages

### Packages

- `conda install {package}` - Install package in current env
  - `conda install {package}={version}` - Install specified version
- `conda remove {package}` - Remove package
- `conda update {package}` - Update package
  - `conda update --all` - Update all packages
- `conda search {search_term}` - Search for a
- `conda list` - List packages in current environment
  - `conda list -n {env_name}` - List packages of other environment

### Environments

- `conda env list` - List environments
- `conda create -n {env_name} [python={version}] [{packages}]` - Create new environment
  - `conda env create -f environment.yaml` - Create environment from file
- `conda env export` - Show current env info and list packages
  - `conda env export > environment.yaml` - Export current env to a file
- `conda env remove -n {env_name}` - Remove an environment