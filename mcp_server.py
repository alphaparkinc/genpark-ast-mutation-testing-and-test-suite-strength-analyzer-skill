"""MCP server for AST Mutation Testing Analyzer."""
import sys
import json
from client import ASTMutationTestingAnalyzer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "generate_ast_mutations",
                "description": "Mutates AST comparison and arithmetic nodes to evaluate test suite edge-case strength",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "source_code": {"type": "string"}
                    },
                    "required": ["source_code"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "generate_ast_mutations":
            code = params.get("arguments", {}).get("source_code", "")
            res = ASTMutationTestingAnalyzer.generate_mutations(code)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
