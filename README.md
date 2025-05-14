# Tree-sitter Java AST Generator

This script parses a Java codebase and generates an Abstract Syntax Tree (AST) for each Java file using [Tree-sitter](https://tree-sitter.github.io/tree-sitter/).

## Setup

1. Clone the Java grammar:

```
git clone https://github.com/tree-sitter/tree-sitter-java.git
```
Place the `tree-sitter-java` folder inside this project directory.

2. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

```
python tree_sitter_java_ast.py <path_to_java_codebase>
```

## Output

The script prints the AST for each Java file. You can modify the script to serialize the ASTs as JSON or process them as needed.
