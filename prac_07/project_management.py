"""
Project Management
Estimate: 60 minutes
Actual:   55 minutes
"""

import datetime

from prac_07.project import Project

DEFAULT_FILE = "prac_07/projects.txt"


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")

    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")

    choice = ""
    while choice != "q":
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice != "q":
            print("Invalid choice")

    save_choice = input(f"Would you like to save to {DEFAULT_FILE}? ").lower()
    if save_choice.startswith("y"):
        save_projects(DEFAULT_FILE, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a tab-delimited file and return a list of Project objects."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()  # Consume header
    for line in in_file:
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        projects.append(Project(name, start_date, priority, cost_estimate,
                                completion_percentage))
    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save a list of Project objects to a tab-delimited file."""
    out_file = open(filename, 'w')
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(f"{project.name}\t"
                       f"{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t"
                       f"{project.cost_estimate}\t"
                       f"{project.completion_percentage}\n")
    out_file.close()


def display_projects(projects):
    """Display incomplete and completed projects, each group sorted by priority."""
    incomplete = []
    completed = []
    for project in projects:
        if project.is_completed():
            completed.append(project)
        else:
            incomplete.append(project)
    incomplete.sort()
    completed.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after a user-entered date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = []
    for project in projects:
        if project.start_date >= filter_date:
            filtered.append(project)
    filtered.sort(key=Project.get_start_date)
    for project in filtered:
        print(project)


def add_project(projects):
    """Prompt the user for details and add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate,
                            completion_percentage))


def update_project(projects):
    """Let the user choose a project and update its completion % and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()
