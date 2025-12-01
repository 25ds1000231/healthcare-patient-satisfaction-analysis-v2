# analysis/healthcare_analysis.py
# Author email (for verification): 25ds1000231@ds.study.iitm.ac.in

import os
import pandas as pd
import matplotlib.pyplot as plt

INDUSTRY_TARGET = 4.5

def main():
    # Ensure we are using the correct path
    data_path = os.path.join("data", "patient_satisfaction_2024.csv")

    df = pd.read_csv(data_path)
    df["patient_satisfaction_score"] = df["patient_satisfaction_score"].astype(float)

    avg_score = df["patient_satisfaction_score"].mean()

    print("=== Patient Satisfaction - 2024 Summary ===")
    print(df)
    print(f"\nAverage patient satisfaction score (2024): {avg_score:.2f}")
    print(f"Industry benchmark target: {INDUSTRY_TARGET:.2f}")
    print(f"Gap vs. target: {avg_score - INDUSTRY_TARGET:.2f}")

    df["above_target"] = df["patient_satisfaction_score"] >= INDUSTRY_TARGET
    print("\nQuarters vs target:")
    print(df[["quarter", "patient_satisfaction_score", "above_target"]])

    os.makedirs("figures", exist_ok=True)

    # Line plot
    plt.figure(figsize=(8, 5))
    plt.plot(df["quarter"], df["patient_satisfaction_score"], marker="o", label="2024 score")
    plt.axhline(INDUSTRY_TARGET, color="red", linestyle="--", label=f"Target {INDUSTRY_TARGET}")
    plt.title("2024 Quarterly Patient Satisfaction vs Industry Target")
    plt.xlabel("Quarter")
    plt.ylabel("Patient Satisfaction Score")
    plt.ylim(0, max(df["patient_satisfaction_score"].max(), INDUSTRY_TARGET) + 1)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join("figures", "patient_satisfaction_trend.png"))
    plt.close()

    # Bar plot
    plt.figure(figsize=(8, 5))
    plt.bar(df["quarter"], df["patient_satisfaction_score"], label="2024 score")
    plt.axhline(INDUSTRY_TARGET, color="red", linestyle="--", label=f"Target {INDUSTRY_TARGET}")
    plt.title("Quarterly Patient Satisfaction Scores (2024)")
    plt.xlabel("Quarter")
    plt.ylabel("Patient Satisfaction Score")
    plt.ylim(0, max(df["patient_satisfaction_score"].max(), INDUSTRY_TARGET) + 1)
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join("figures", "patient_satisfaction_bars.png"))
    plt.close()

if __name__ == "__main__":
    main()
