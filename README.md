# Python Fundamentals

Holberton School, Full-Stack Software Engineer program (Cohort 29).

### Description

A collection of Python projects covering the core building blocks of the language, from how code is executed to how programs handle errors. Each project lives in its own folder with its own README and code.

### Projects

| # | Project | Focus | README |
|---|---|---|---|
| 1 | Interpreter, Scripts and Environments | REPL vs scripts, `pip`, `venv`, dependency isolation | [python_environments](./python_environments/README.md) |
| 2 | Flujo de control | `if`/`elif`/`else`, comparison and Boolean logic, `while` and `for` loops | [python_control_flow](./python_control_flow/README.md) |
| 3 | Functions & Modularity | Functions, `print` vs `return`, imports, `if __name__ == "__main__"` | [python_functions_modularity](./python_functions_modularity/README.md) |
| 4 | Data Structures | Lists, tuples, sets, dictionaries | [data_structures](./data_structures/README.md) |
| 5 | Exception Handling | `try`/`except`/`else`/`finally`, raising exceptions | [python_exception_handling](./python_exception_handling/README.md) |

### Structure

```
python_fundamentals/
├── README.md                       # you are here: index of every project
│
├── python_environments/            # 1. how Python runs and where tools live
│   ├── README.md                   #    REPL vs scripts, pip, venv
│   └── ...                         #    task scripts
│
├── python_control_flow/            # 2. making decisions and repeating actions
│   ├── README.md                   #    if/elif/else, while, for + range()
│   └── ...                         #    task scripts
│
├── python_functions_modularity/    # 3. reusable code across files
│   ├── README.md                   #    functions, print vs return, imports
│   └── ...                         #    task scripts + importable modules
│
├── data_structures/                # 4. choosing the right container
│   ├── README.md                   #    lists, tuples, sets, dicts
│   └── ...                         #    task scripts
│
└── python_exception_handling/      # 5. failing safely
    ├── README.md                   #    try/except/else/finally, raise
    └── ...                         #    task scripts
```

Read top to bottom: each project builds on the one above it.

### Author

[bumble-beed](https://github.com/bumble-beed)