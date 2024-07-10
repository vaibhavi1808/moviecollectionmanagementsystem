def calculate_collection (rating):
    """
    Calculates collection based on rating.
    Args:
        rating (float): rating score of a moviecollection1.
    Returns:
        str: collection (A, B, C, D, F) based on the rating.
    """
    if rating>= 5:
        return 'silver hit'
    elif rating >= 8:
        return 'golden hit'
    elif rating == 10:
        return 'max hit'
    else:
        return 'poor hit'
    

    def calculate_average_percentage():
Calculates the average total percentage of students from the CSV data.
data pd.read_csv('data/students.csv')
if data.empty:
print("No student data found.")
return
total_percentage = data['total_percentage'].mean print(f"Average Percentage: {total_percentage:.2f}%")
def generate_report():
Generates a report showing the count of students and average total percentage grouped by city from the CSV data.
data = pd.read_csv('data/students.csv')
if data.empty:
print("No student data found.")
return
report = data.groupby('city').agg({
'name': 'count',
'total_percentage': 'mean'
}).reset_index()
report.columns = ['City', 'Number of Students', 'Average Percentage']
print("Report:")
print(report.to_string(index=False))
if
name == main":
calculate_average_percentage()
generate_report()
