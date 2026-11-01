# Secure Study Planner
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/ChrisPBaconctrl/SecureStudyPlanner/badge)](https://scorecard.dev/viewer/?uri=github.com/ChrisPBaconctrl/SecureStudyPlanner)
A small Python command-line application for organizing study tasks.

## Features

- Add study tasks with a subject and due date
- List saved tasks
- Mark a task as complete
- Store tasks locally in a JSON file

## Requirements

- Python 3.10 or newer
- No third-party packages are required

## Run the application

```bash
python src/study_planner.py
```

The application creates `study_tasks.json` in the current working directory when needed.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## OpenSSF security

The OpenSSF Scorecard badge will be added after the repository is created and scanned:

`<!-- Add the Scorecard badge here after the first scan. -->`

The OpenSSF Best Practices badge will be added after the project profile is completed at
https://www.bestpractices.dev/:

`<!-- Add the Best Practices badge here after receiving its project ID. -->`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.

## Reporting a security issue

See [SECURITY.md](SECURITY.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
