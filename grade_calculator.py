def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 45:
        return "D"
    else:
        return "F"

def main():
    print("===== Student Grade Calculator =====")

    subjects = int(input("Enter number of subjects: "))

    if subjects <= 0:
        print("Invalid number of subjects!")
        return

    marks = []
    for i in range(subjects):
        score = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(score)

    total = sum(marks)
    percentage = total / subjects

    grade = calculate_grade(percentage)

    print("\n----- Result -----")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    # save to file
    with open("sample_output.txt", "w") as f:
        f.write("===== Student Grade Calculator Result =====\n")
        f.write(f"Total Marks: {total}\n")
        f.write(f"Percentage: {percentage:.2f}%\n")
        f.write(f"Grade: {grade}\n")

    print("\nResult saved to sample_output.txt")

if __name__ == "__main__":
    main()
