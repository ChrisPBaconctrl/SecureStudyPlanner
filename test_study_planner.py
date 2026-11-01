import tempfile
import unittest
from pathlib import Path

from src.study_planner import add_task, load_tasks, save_tasks


class StudyPlannerTests(unittest.TestCase):
    def test_add_task_creates_incomplete_task(self):
        tasks = []
        task = add_task(tasks, "Chemistry", "Review bonding", "2026-11-05")
        self.assertEqual(task["subject"], "Chemistry")
        self.assertFalse(task["completed"])
        self.assertEqual(len(tasks), 1)

    def test_add_task_rejects_blank_subject(self):
        with self.assertRaises(ValueError):
            add_task([], " ", "Review bonding", "2026-11-05")

    def test_save_and_load_tasks(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.json"
            original = [{"subject": "Biology", "completed": False}]
            save_tasks(original, path)
            self.assertEqual(load_tasks(path), original)


if __name__ == "__main__":
    unittest.main()
