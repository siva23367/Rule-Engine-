class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' or 'operand'
        self.value = value  # Condition for operand, or operator type (AND/OR)
        self.left = left  # Left child (another ASTNode)
        self.right = right  # Right child (another ASTNode)

    def __repr__(self):
        if self.type == 'operand':
            return f"Operand({self.value})"
        return f"Operator({self.value})"
