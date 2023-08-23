# Virtual Env #

- These are very import when we want to work in an isolated environment without affecting the other/global
  environments.
- You could have multiple projects which are dependent on say fast api but each project needs a different version of
  fast api. If you upgrade the version globally, it might break other applications/projects. Instead, we can create
  multiple virtual environments and install respective versions of fast api inside them and can work without affecting
  other projects.

```bash
  python3 -m pip install virtualenv

```

- Once **virtualenv** is installed, we can create the virtual environment using below command

```bash
  virtualenv your_project_name
```

- Now activate the virtual environment using:

```bash
  source your_project_name/bin/activate
```

Now we can start working in this project. Installation of any pip package will have scope to this environment.

- To get out of virtual environment, simply type **deactivate**.