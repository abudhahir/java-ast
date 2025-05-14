import os
import sys
from tree_sitter import Language, Parser

# Path to build the language library
tree_sitter_lib_path = os.path.join(os.path.dirname(__file__), 'build', 'my-languages.so')

def build_language_library():
    """
    Build the tree-sitter language library for Java if it doesn't exist.
    """
    if not os.path.exists(tree_sitter_lib_path):
        Language.build_library(
            # Store the library in the `build` directory
            tree_sitter_lib_path,
            # Include the Java grammar
            [
                os.path.join(os.path.dirname(__file__), 'tree-sitter-java')
            ]
        )

def load_java_parser():
    """
    Load the Java parser from the built language library.
    """
    build_language_library()
    JAVA_LANGUAGE = Language(tree_sitter_lib_path, 'java')
    parser = Parser()
    parser.set_language(JAVA_LANGUAGE)
    return parser

def find_java_files(root_dir):
    """
    Recursively find all .java files in the given directory.
    """
    java_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                java_files.append(os.path.join(dirpath, filename))
    return java_files

def ast_to_dict(node, source_code):
    """
    Recursively convert a tree-sitter node to a dictionary for easier inspection/serialization.
    """
    result = {
        'type': node.type,
        'start_point': node.start_point,
        'end_point': node.end_point,
        'children': [ast_to_dict(child, source_code) for child in node.children]
    }
    if node.child_count == 0:
        result['text'] = source_code[node.start_byte:node.end_byte].decode('utf-8')
    return result

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_java_codebase>")
        sys.exit(1)
    codebase_dir = sys.argv[1]
    parser = load_java_parser()
    java_files = find_java_files(codebase_dir)
    print(f"Found {len(java_files)} Java files.")
    for java_file in java_files:
        with open(java_file, 'rb') as f:
            source_code = f.read()
        tree = parser.parse(source_code)
        ast = ast_to_dict(tree.root_node, source_code)
        print(f"AST for {java_file}:")
        print(ast)  # You may want to pretty-print or serialize this as JSON

if __name__ == "__main__":
    main()
