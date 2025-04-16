import csv

def summarize_results(log_path="logs/results.csv"):
    try:
        with open(log_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            total = safe = unsafe = neutral = 0

            for row in reader:
                total += 1
                outcome = row["Outcome"].lower()

                if "safe" in outcome:
                    safe += 1
                elif "unsafe" in outcome:
                    unsafe += 1
                elif "neutral" in outcome:
                    neutral += 1

            if total == 0:
                print("No results found.")
                return

            print("\n📊 Summary Statistics")
            print(f"Total Simulations: {total}")
            print(f"Safe Responses: {safe} ({safe/total:.1%})")
            print(f"Unsafe Responses: {unsafe} ({unsafe/total:.1%})")
            print(f"Neutral Responses: {neutral} ({neutral/total:.1%})")

    except FileNotFoundError:
        print("⚠️ No results file found. Run a simulation first.")
