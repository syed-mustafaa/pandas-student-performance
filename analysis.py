import pandas as pd
import matplotlib.pyplot as plt

def analyze_performance(file_path):
    print(f"Loading data from {file_path}...")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # 1. Average Score by Subject
    avg_score_subject = df.groupby('Subject')['Score'].mean().sort_values(ascending=False)
    print("\n--- Average Score by Subject ---")
    print(avg_score_subject)

    # 2. Top Performing Student (Overall Average)
    avg_score_student = df.groupby('Name')['Score'].mean().sort_values(ascending=False)
    top_student = avg_score_student.head(1)
    print("\n--- Top Performing Student ---")
    print(top_student)

    # 3. Correlation between Attendance and Score
    correlation = df['Attendance_Percentage'].corr(df['Score'])
    print(f"\n--- Correlation (Attendance vs Score) ---")
    print(f"Correlation Coefficient: {correlation:.2f}")

    # Visualization
    plt.figure(figsize=(12, 5))

    # Bar Chart: Average Score by Subject
    plt.subplot(1, 2, 1)
    avg_score_subject.plot(kind='bar', color='teal')
    plt.title('Average Score by Subject')
    plt.ylabel('Average Score')
    plt.ylim(0, 100)

    # Scatter Plot: Attendance vs Score
    plt.subplot(1, 2, 2)
    plt.scatter(df['Attendance_Percentage'], df['Score'], color='crimson')
    plt.title(f'Attendance vs Score (Corr: {correlation:.2f})')
    plt.xlabel('Attendance %')
    plt.ylabel('Score')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('performance_report.png')
    print("\nReport saved as 'performance_report.png'")

if __name__ == "__main__":
    analyze_performance('student_data.csv')
