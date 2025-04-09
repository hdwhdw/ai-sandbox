from math_utils import round_num

def report_values(vals):
    for v in vals:
        # uses our explicit round_num
        print(f"{v} → {round_num(v, 0)}")

if __name__ == "__main__":
    report_values([1.5, 2.5, 3.5])
