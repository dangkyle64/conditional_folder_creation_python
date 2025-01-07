# Conditional Folder Creation

Python script examples displaying brute force delete_on_empty and potential usage on on_demand for folder creation. 

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Install Dependencies](#install-dependencies)
- [Usage](#usage)


## Installation

Clone the repository:
   ```bash
   git clone https://github.com/dangkyle64/conditional_folder_creation_python
   ```

### Requirements
- Python 3.x

### Usage

Normal folder creation function using os library 
```python
import os 

os.mkdirs('path/to/folder', exist_ok = boolean)
```

Removal of empty folders using os library 
```python
import os 

os.rmdir('path/to/folder')
```
Check if folder exists 
```python
import os 

os.path.exists('path/to/folder')
```