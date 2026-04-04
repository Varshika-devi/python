def analyze_log(file):
    errors = 0
    
    with open(file, "r") as f:
        for line in f:
            if "ERROR" in line:
                errors += 1

    print(f"Total errors: {errors}")

if __name__ == "__main__":
    analyze_log("app.log")
