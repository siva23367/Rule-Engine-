import unittest
from .utils import create_rule
class TestCreateRule(unittest.TestCase):
    def test_single_and_condition(self):
        # Rule: "age > 30 AND department = 'Sales'"
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)

        # Expected AST:
        #        AND
        #       /   \
        #  age > 30  department = 'Sales'
        
        self.assertEqual(ast.type, 'operator')
        self.assertEqual(ast.value, 'AND')
        self.assertEqual(ast.left.type, 'operand')
        self.assertEqual(ast.left.value, 'age > 30')
        self.assertEqual(ast.right.type, 'operand')
        self.assertEqual(ast.right.value, "department = 'Sales'")

    def test_single_or_condition(self):
        # Rule: "salary > 50000 OR experience < 3"
        rule_string = "salary > 50000 OR experience < 3"
        ast = create_rule(rule_string)

        # Expected AST:
        #       OR
        #      /   \
        # salary > 50000  experience < 3
        
        self.assertEqual(ast.type, 'operator')
        self.assertEqual(ast.value, 'OR')
        self.assertEqual(ast.left.type, 'operand')
        self.assertEqual(ast.left.value, 'salary > 50000')
        self.assertEqual(ast.right.type, 'operand')
        self.assertEqual(ast.right.value, 'experience < 3')

    def test_combined_and_or_condition(self):
        # Rule: "age > 30 AND department = 'Sales' OR salary > 50000"
        rule_string = "age > 30 AND department = 'Sales' OR salary > 50000"
        ast = create_rule(rule_string)

        # Expected AST:
        #         OR
        #        /   \
        #      AND   salary > 50000
        #     /   \
        # age > 30  department = 'Sales'
        
        self.assertEqual(ast.type, 'operator')
        self.assertEqual(ast.value, 'OR')
        self.assertEqual(ast.left.type, 'operator')
        self.assertEqual(ast.left.value, 'AND')
        self.assertEqual(ast.left.left.type, 'operand')
        self.assertEqual(ast.left.left.value, 'age > 30')
        self.assertEqual(ast.left.right.type, 'operand')
        self.assertEqual(ast.left.right.value, "department = 'Sales'")
        self.assertEqual(ast.right.type, 'operand')
        self.assertEqual(ast.right.value, 'salary > 50000')





if __name__ == "__main__":
    unittest.main()
