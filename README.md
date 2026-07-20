# VYZOR
![License](https://img.shields.io/badge/License-MIT-green.svg)

*Build resilient systems by intentionally breaking them.*
> Cross-platform framework for resilience testing and chaos engineering.

VYZOR is an open-source framework for running controlled resilience experiments across different execution environments. It is designed to help evaluate how systems behave under stress while keeping the architecture modular, extensible, and easy to build upon.

The long-term goal is to provide a single framework capable of targeting Windows, Linux, Docker, and Kubernetes through a common experiment engine.

> **Status:** 🚧 Early Development

---

# Why VYZOR?

Most chaos engineering tools are tightly coupled to a specific platform or infrastructure.

VYZOR is being built around a different idea:

- one experiment engine
- multiple execution targets
- reusable architecture
- consistent reporting

Instead of rewriting experiments for every environment, the framework aims to provide a common abstraction layer that can be extended as new targets are added.

---

# Planned Features

- Cross-platform architecture
- Configuration-driven execution
- Modular experiment engine
- Plugin support
- Structured logging
- Experiment reporting
- Windows support
- Linux support
- Docker support
- Kubernetes support

---

# Project Structure

```text
src/
└── vyzor/
    ├── api/
    ├── cli/
    ├── config/
    ├── core/
    ├── engine/
    ├── experiments/
    ├── plugins/
    ├── reporting/
    ├── targets/
    ├── telemetry/
    └── utils/
```

---

# Technology Stack

| Technology | Purpose                  |
|------------|--------------------------|
| Python     | Core framework           |
| Docker     | Container experiments    |
| Kubernetes | Cluster experiments      |
| FastAPI    | REST API                 |
| Typer      | Command-line interface   |
| PyYAML     | Configuration management |

---

## Project Goals

VYZOR is built with the following goals:

- Keep experiments platform-independent.
- Make new execution targets easy to implement.
- Encourage modular design.
- Provide consistent reporting across environments.

Built with curiosity, one commit at a time.
---

# Current Progress

- Repository initialized
- Development environment
- Project architecture
- Documentation

Current focus:

- Configuration System
- Logging
- Target abstraction layer

---

# Roadmap

See [ROADMAP.md](ROADMAP.md) for the complete development roadmap.

---

# Architecture

Architecture details are documented in [ARCHITECTURE.md](ARCHITECTURE.md).

---

# Contributing

Contributions, suggestions, and discussions are always welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

---

> Installation instructions will be available in a future release.

This project is licensed under the MIT License.