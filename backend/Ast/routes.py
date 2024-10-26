from fastapi import APIRouter, HTTPException

from .models import Rule, CreateRuleRequest,CombineRulesRequest,EvaluateRuleRequest

from .utils import create_rule,combine_rules,ast_from_dict,evaluate_rule



router=APIRouter()


@router.post("/create-rule")
async def create_rule_api(request: CreateRuleRequest):
    """
    example testcase:
    age > 30 AND department = 'Sales' OR salary > 50000"""
    # Check if the rule already exists
    existing_rule = await Rule.filter(name=request.name).first()
    if existing_rule:
        raise HTTPException(status_code=400, detail="Rule with this name already exists")

    # Save the new rule to the database
    rule = await Rule.create(name=request.name, rule_string=request.rule_string)
    node = create_rule(request.rule_string)
    return {"message": "Rule created successfully", "rule_id": node}


@router.post("/combine-rule")
async def combine_rules_api(request: CombineRulesRequest):
    """"
    example textcases:
    {
    "rules": [
        "age > 30 AND department = 'Sales'",
        "salary > 50000 OR experience < 3"
    ]
}

    """
    if not request.rules or len(request.rules) < 2:
        raise HTTPException(status_code=400, detail="At least two rules are required to combine.")

    # Combine the rules into a single AST
    try:
        combined_ast = combine_rules(request.rules)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to combine rules: {str(e)}")

    # Return the combined AST representation (for simplicity, as a string)
    return {"combined_ast": repr(combined_ast)}


@router.post("/evaluate-rule")
async def evaluate_rule_api(request: EvaluateRuleRequest):
    """
    example testcase:
    {
    "ast": {
        "type": "operator",
        "value": "OR",
        "left": {
            "type": "operator",
            "value": "AND",
            "left": {
                "type": "operand",
                "value": "age > 30"
            },
            "right": {
                "type": "operand",
                "value": "department = 'Sales'"
            }
        },
        "right": {
            "type": "operand",
            "value": "salary > 50000"
        }
    },
    "data": {
        "age": 35,
        "department": "Sales",
        "salary": 40000,
        "experience": 3
    }
}
"""
    try:
        # Convert the JSON AST to an ASTNode
        root_node = ast_from_dict(request.ast)
        # Evaluate the rule against the provided data
        result = evaluate_rule(root_node, request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to evaluate rule: {str(e)}")

    # Return the evaluation result
    return {"result": result}

