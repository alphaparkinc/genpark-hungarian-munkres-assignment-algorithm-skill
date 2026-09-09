"""MCP Server for Hungarian Munkres Assignment Skill."""
import json
import sys
from client import HungarianMunkres

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "solve_assignment",
                            "description": "Solve optimal bipartite matching assignment via Hungarian Munkres algorithm",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "cost_matrix": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "maximize": {"type": "boolean"}
                                },
                                "required": ["cost_matrix"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                solver = HungarianMunkres(args["cost_matrix"], maximize=args.get("maximize", False))
                output = solver.solve()
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(output)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
