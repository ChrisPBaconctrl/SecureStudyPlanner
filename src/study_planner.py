"""A tiny local command-line study planner."""

import json
from pathlib import Path

DATA_FILE = Path("study_tasks.json")


def load_tasks(path=DATA_FILE):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("The task file must contain a JSON list.")
    return data


def save_tasks(tasks, path=DATA_FILE):
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, subject, description, due_date):
    if not subject.strip():
        raise ValueError("Subject cannot be empty.")
    if not description.strip():
        raise ValueError("Description cannot be empty.")
    if not due_date.strip():
        raise ValueError("Due date cannot be empty.")

    task = {
        "subject": subject.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return task


def main():
    tasks = load_tasks()
    print("Secure Study Planner")
    print("--------------------")
    print(f"You have {len(tasks)} saved task(s).")


if __name__ == "__main__":
    main()
