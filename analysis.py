import pandas as pd
import matplotlib.pyplot as plt

def analyze_performance(file_path):
    """
    Analyzes student performance data from a CSV file.
    
    Args:
        file_path (str): Path to the input CSV file.
    """
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

    # 2. Pass Rate by Subject (Score >= 60)
    pass_rate_subject = df[df['Score'] >= 60].groupby('Subject')['Score'].count() / df.groupby('Subject')['Score'].count() * 100
    pass_rate_subject = pass_rate_subject.fillna(0) # Handle cases with 0 pass rate
    print("\n--- Pass Rate by Subject (%) ---")
    print(pass_rate_subject)

    # 3. Top Performing Student (Overall Average)
    avg_score_student = df.groupby('Name')['Score'].mean().sort_values(ascending=False)
    top_student = avg_score_student.head(1)
    print("\n--- Top Performing Student ---")
    print(top_student)

    # 4. Grade Distribution
    bins = [0, 59, 69, 79, 89, 100]
    labels = ['F', 'D', 'C', 'B', 'A']
    df['Grade'] = pd.cut(df['Score'], bins=bins, labels=labels, right=True)
    grade_counts = df['Grade'].value_counts().sort_index(ascending=False)
    print("\n--- Grade Distribution ---")
    print(grade_counts)

    # 5. Correlation between Attendance and Score
    correlation = df['Attendance_Percentage'].corr(df['Score'])
    print(f"\n--- Correlation (Attendance vs Score) ---")
    print(f"Correlation Coefficient: {correlation:.2f}")

    # Visualization: 2x2 Grid
    plt.figure(figsize=(14, 10))

    # 1. Bar Chart: Average Score by Subject
    plt.subplot(2, 2, 1)
    avg_score_subject.plot(kind='bar', color='teal')
    plt.title('Average Score by Subject')
    plt.ylabel('Average Score')
    plt.ylim(0, 100)

    # 2. Bar Chart: Pass Rate by Subject
    plt.subplot(2, 2, 2)
    pass_rate_subject.plot(kind='bar', color='lightgreen')
    plt.title('Pass Rate by Subject (%)')
    plt.ylabel('Pass Rate %')
    plt.ylim(0, 100)

    # 3. Pie Chart: Grade Distribution
    plt.subplot(2, 2, 3)
    grade_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'])
    plt.title('Overall Grade Distribution')
    plt.ylabel('')

    # 4. Scatter Plot: Attendance vs Score
    plt.subplot(2, 2, 4)
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
