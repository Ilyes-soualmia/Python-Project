import json
import pandas as pd
import matplotlib.pyplot as plt

def score_to_exam_analysis():
    # JSON data
    with open("History.json", "r") as f:
        data = json.loads(f.read())

    # Create a pandas DataFrame
    df = pd.DataFrame(data['history'])

    # Calculate average scores per exam
    average_scores = df.groupby('exam')['score'].mean()

    # Extract exams and scores for the chart
    exams = df['exam']
    scores = df['score']

    # Plot the data with enhancements
    # Adjust the figure size for better clarity
    plt.figure(figsize=(15, 8))

    # Plot the bars for individual scores
    plt.bar(exams, scores, color='skyblue', edgecolor='black', label='Scores')

    # Plot the average scores as a line
    plt.plot(average_scores.index, average_scores.values, color='red', marker='o', linestyle='-', linewidth=2, label='Average Score')

    # Add titles and labels
    plt.title('Exam Scores with Averages (12 Exams)', fontsize=18, fontweight='bold')
    plt.xlabel('Exam', fontsize=14)
    plt.ylabel('Score', fontsize=14)

    # Customize ticks
    plt.xticks(rotation=60, fontsize=10, ha='right')
    plt.yticks(fontsize=12)

    # Add gridlines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add values on top of the bars
    for i, score in enumerate(scores):
        plt.text(i, score + 0.5, str(score), ha='center', fontsize=10, color='darkblue')

    # Add legend
    plt.legend(fontsize=12)

    plt.tight_layout()

    # Show the chart
    plt.show()