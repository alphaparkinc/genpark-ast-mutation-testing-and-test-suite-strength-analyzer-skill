"""Example usage for AST Mutation Testing Analyzer."""
from client import ASTMutationTestingAnalyzer

if __name__ == "__main__":
    code = "def check(a, b): return a >= 10 and b + 2 > 5"
    res = ASTMutationTestingAnalyzer.generate_mutations(code)
    print("Mutations Generated:", res["total_mutations_generated"])
