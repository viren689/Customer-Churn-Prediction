# Student Grade Calculator

def calculate_grade(marks):
    """Returns grade and encouraging message based on marks."""

    if marks >= 90:
        return "A", "Excellent! Outstanding performance! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! Keep learning. 😊"
    elif marks >= 60:
        return "D", "Keep practicing! You're improving! 💪"
    else:
        return "F", "Don't give up. Study harder! 📚"


print("===================================")
print("    STUDENT GRADE CALCULATOR")
print("===================================")

# Get student name
student_name = input("Enter student name: ")

# Validate marks
while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n========== RESULT ==========")
print(f"Student Name : {student_name.upper()}")
print(f"Marks        : {marks}/100")
print(f"Grade        : {grade}")
print(f"Message      : {message}")
print("============================")
