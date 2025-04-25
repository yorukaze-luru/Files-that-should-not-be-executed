# Files-that-should-not-be-executed

This repository contains two Python scripts designed for specific purposes:

1. **File Copier and Executor**  
   Copies a Python script with a randomly generated name and executes it.  
   Example scripts include dynamically named file creation and execution functionality.

2. **Stop Script**  
   Stops running Python scripts using system commands without requiring additional libraries.

---

## Features

- **File Copier and Executor**:  
  - Safely copies a file with a unique random name using UUID.  
  - Executes the copied Python script.

- **Stop Script**:  
  - Terminates Python processes without relying on third-party libraries.  
  - Designed for UNIX-based systems.

---

## Prerequisites

- Python 3.x installed
- UNIX-based system (for `stop.py` functionality)
- Ensure the original script (`original_script.py`) is available for copying.

---

## Usage

### File Copier and Executor
1. Place your Python script (`original_script.py`) in the same directory.
2. Run `copier.py`:
   ```bash
   python copier.py
