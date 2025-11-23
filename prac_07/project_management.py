"""
CP1404
Project Management Program
Estimated time: 6 hours
"""

import datetime
from project import Project

MENU = "- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n" \
       "- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit"


def main():
    """Run Project Management program."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    choice = input(MENU + "\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option")

        choice = input(MENU + "\n>>> ").upper()

    save_choice = input("Would you like to save to projects.txt? ").lower()
    if save_choice.startswith('y'):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file into a list of Project objects."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()  # Skip header

    for line in in_file:
        parts = line.strip().split('\t')
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        projects.append(Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4])))

    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    out_file = open(filename, 'w')
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")

    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
            f"{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n")

    out_file.close()
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """Display incomplete and complete projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(" ", project)

    print("Completed projects:")
    for project in complete:
        print(" ", project)


def filter_by_date(projects):
    """Filter projects after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered = [p for p in projects if p.start_date > date]
    filtered.sort(key=lambda p: p.start_date)

    for project in filtered:
        print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, percent))


def update_project(projects):
    """Update existing project."""
    for i, project in enumerate(projects):
        print(i, project)
    choice = int(input("Project choice: "))
    project = projects[choice]

    new_percent = input("New Percentage: ")
    if new_percent != "":
        project.completion_percent = int(new_percent)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
