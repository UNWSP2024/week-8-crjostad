def Enter_courses():
    courses = {}
    while True:
        course_id = input("Enter the course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter the course name: ")
        courses[course_id] = course_name
    return courses

def display_courses_by_subject(courses, subject):
    print(f"Courses for subject '{subject}':")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")

def main():
    courses = Enter_courses()
    subject = input("Enter the subject to search for : ")
    display_courses_by_subject(courses, subject)

if __name__ == "__main__":
    main()
