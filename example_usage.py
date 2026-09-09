"""Example usage for Hungarian Munkres Assignment Skill."""
from client import HungarianMunkres

def main():
    print("Executing Hungarian Munkres Assignment Algorithm...")
    cost_mat = [
        [10.0, 19.0, 8.0],
        [10.0, 1.0, 12.0],
        [13.0, 16.0, 9.0]
    ]
    hungarian = HungarianMunkres(cost_mat, maximize=False)
    res = hungarian.solve()
    print("Result:", res)
    assert res["total_cost"] == 20.0, f"Expected 20.0, got {res['total_cost']}"
    assert len(res["assignments"]) == 3
    print("Hungarian Munkres Assignment verified successfully!")

if __name__ == "__main__":
    main()
