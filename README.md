# Warfare Replication Daemon

## Overview

This script implements a continuous replication daemon designed for hostile or adversarial digital environments.
In a warfare context, the tool behaves as a resource‑pressure mechanism: it continuously duplicates files inside a directory tree, creating operational noise, redundancy, and storage pressure.

This behavior can be used in scenarios where:

- an environment is compromised

- an operator wants to disrupt file‑level stability

- replication pressure is used as part of a defensive or adversarial posture

This tool is high‑risk and must only be executed in controlled, isolated systems.
## ⚠️ Usage Warning

Running this daemon will:

1. replicate files indefinitely

2. consume disk space extremely quickly

3. degrade system performance

4. create thousands of timestamped copies

5. be difficult to stop without manual intervention

This script must not be used on:

- production systems

- shared machines

- systems you do not fully control

- environments where uncontrolled replication is unsafe

You are fully responsible for any operational impact.

**How It Works:**

- The daemon starts in the current working directory.

- It walks all subdirectories.

- For every file (except .py and .txt), it creates a timestamped copy.

- Each loop iteration is a cycle.

- The loop is infinite.

    The process stops only when the user presses Ctrl+C.

## Warfare Context

In digital warfare scenarios, uncontrolled replication can:

- overwhelm storage

- create operational noise

- complicate cleanup

- increase system load

- interfere with hostile attempts to maintain order

This script is intentionally aggressive and unbounded, reflecting a warfare‑grade behavior pattern.

## Running
```bash

   python daemon.py

Stop with:

   Ctrl + C
