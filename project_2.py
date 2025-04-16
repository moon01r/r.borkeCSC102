admitted = []
not_admitted = []
def admission_checker(name, dept, jamb_score, credits, passed_interview):
    if dept == "computer science":
        if jamb_score >= 250 and credits >= 5 and passed_interview == "y":
            admitted.append((name, dept))
        else:
            not_admitted.append((name, dept))

    elif dept == "mass communication":
        if jamb_score >= 230 and credits >= 5 and passed_interview == "y":
            admitted.append((name, dept))
        else:
            not_admitted.append(name, dept)

    else:
        print(f"Uknown department {dept}")
        not_admitted.append((name, dept))

while True:
    name = input("Candidate name: ")
    dept = input("Candidate department: ").lower()
    jamb_score = int(input("Jamb score: "))
    credits = int(input("Number of credits: "))
    passed_interview = input("Passed interview (y/n): ").lower()

    admission_checker(name, dept, jamb_score, credits, passed_interview)

    more = input("Want to check for more candidates?(yes/no): ").strip().lower()
    if more != 'yes':
        break 

    print("\nAdmitted Candidates")
    for candidate in admitted:
        print(candidate)

    print("\nNot Admitted Candidates")
    for candidates in not_admitted:
        print(candidate)