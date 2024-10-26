import re
from .ast import ASTNode
from typing import List
def create_rule(rule_string):
    """
    Parses a rule string and builds an Abstract Syntax Tree (AST).

    Args:
        rule_string (str): The rule string to parse (e.g., "age > 30 AND department = 'Sales'").

    Returns:
        ASTNode: The root node of the constructed AST.
    """
    
    # Helper function to tokenize the rule string
    def tokenize(expression):
        # Split the expression by logical operators AND/OR while keeping the operators
        tokens = re.split(r'(\s+AND\s+|\s+OR\s+)', expression)
        # Strip any extra whitespace from each token
        return [token.strip() for token in tokens if token.strip()]

    # Recursive function to build an AST from the tokens
    def build_ast(tokens):
        # Base case: if there's only one token, it's an operand
        if len(tokens) == 1:
            return ASTNode('operand', tokens[0])

        # Find the lowest-precedence operator (OR has lower precedence than AND)
        if 'OR' in tokens:
            index = tokens.index('OR')
            left = build_ast(tokens[:index])
            right = build_ast(tokens[index + 1:])
            return ASTNode('operator', 'OR', left, right)

        # Handle AND operators
        if 'AND' in tokens:
            index = tokens.index('AND')
            left = build_ast(tokens[:index])
            right = build_ast(tokens[index + 1:])
            return ASTNode('operator', 'AND', left, right)

    # Tokenize the input rule string
    tokens = tokenize(rule_string)

    # Build and return the AST
    return build_ast(tokens)




def combine_rules(rules: List[str]):
    asts = [create_rule(rule) for rule in rules]
    if len(asts) == 1:
        return asts[0]

    combined_ast = asts[0]
    for ast in asts[1:]:
        combined_ast = ASTNode('operator', 'OR', combined_ast, ast)
    return combined_ast



def ast_from_dict(data):
    if not data:
        return None
    node_type = data['type']
    value = data['value']
    left = ast_from_dict(data['left']) if 'left' in data else None
    right = ast_from_dict(data['right']) if 'right' in data else None
    return ASTNode(node_type, value, left, right)






def evaluate_rule(node, data):
    """
    Evaluates the combined rule's AST against the provided user data.

    Args:
        node (ASTNode): The root node of the combined rule's AST.
        data (dict): A dictionary containing the user attributes (e.g., {"age": 35, "department": "Sales"}).

    Returns:
        bool: True if the user meets the criteria specified by the rule, False otherwise.
    """
    if node.type == 'operand':
        # Evaluate the condition for operand nodes
        condition = node.value
        # Split the condition by spaces to get the attribute, operator, and value
        attr, op, val = re.split(r'\s+', condition, 2)
        # Convert the value to the appropriate type (int, float, or string)
        try:
            val = int(val) if val.isdigit() else float(val) if '.' in val else val.strip("'")
        except ValueError:
            val = val.strip("'")
        
        # Perform the comparison based on the operator
        if op == '>':
            return data.get(attr, 0) > val
        elif op == '<':
            return data.get(attr, 0) < val
        elif op == '=':
            return data.get(attr, '') == val
        else:
            raise ValueError(f"Unsupported operator: {op}")

    elif node.type == 'operator':
        # Evaluate the left and right child nodes
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)

        # Perform logical operation based on the operator type
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result
        else:
            raise ValueError(f"Unsupported operator: {node.value}")

    return False

