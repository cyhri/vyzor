# VYZOR Architecture

## Overview

VYZOR is designed around a simple idea:

Keep the experiment engine independent from the platform it runs on.

Instead of building separate tools for Windows, Linux, Docker, and Kubernetes, VYZOR uses a shared execution engine with platform-specific adapters. This keeps experiments reusable while allowing new targets to be added without changing the core architecture.

---

## Design Goals

- Modular
- Cross-platform
- Extensible
- Easy to maintain
- Designed for production-quality architecture

---

## High-Level Architecture

```text
                 CLI / API
                     │
             Configuration
                     │
              Chaos Engine
                     │
        ┌────────────┼────────────┐
        │            │            │
    Windows       Linux      Containers
                                 │
                     Docker / Kubernetes
                     │
              Experiment Modules
                     │
          Reporting & Telemetry
```

---

## Supported Targets

| Target     | Status  |
|------------|---------|
| Windows    | Planned |
| Linux      | Planned |
| Docker     | Planned |
| Kubernetes | Planned |

---

## Core Components

### Chaos Engine

Coordinates experiment execution.

### Targets

Provides platform-specific implementations while exposing a common interface.

### Experiments

Contains individual resilience experiments.

### Reporting

Generates structured reports after execution.

### Telemetry

Collects execution metrics.

### CLI

Primary command-line interface.

### API

Future REST interface for automation and integrations.