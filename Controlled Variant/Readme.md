# Version 2 (Controlled Replication Tool)

This document describes **Version 2** of the replication tool: a controlled, menu‑driven system designed for **document preservation**, redundancy, and safe replication in environments where files may be at risk of deletion or loss.

Unlike the original automatic daemon, Version 2 provides **full user control**, selective replication, optional encryption, and safe cleanup.

---

## 1. Anti-Censorship Purpose 

In an information‑warfare scenario where documents (e.g., books, research, archives) are being selectively deleted, this daemon can:
Version 2 was created to:

- avoid uncontrolled infinite replication loops  
- give the user **full control** over when and how replication happens  
- allow **selective replication** based on file extensions  
- allow **adjustable replication percentage**  
- provide **optional encryption** of replicas with a generated password  
- allow **safe cleanup** of replicas created by the tool  
- preserve original files at all times  

This version is intended for **document preservation**, redundancy, and controlled replication workflows.

---

## 2. Core Features

### 2.1. Adjustable Replication Percentage

The user can choose how many files to replicate per cycle:

- 10%  
- 25%  
- 50%  
- 75%  
- 100%  
- or any custom value between 1–100%

This allows low‑profile or high‑redundancy replication depending on the situation.

---

### 2.2. File‑Type Selection

The user can define which file extensions should be considered for replication.

Examples:

- `.pdf`, `.epub`, `.docx`  
- `.png`, `.jpg`  
- `.zip`, `.7z`  
- any custom extension  

Only files matching the selected extensions will be replicated.

---

### 2.3. Manual Replication Cycles

Replication only occurs when the user selects:

```
3) Start replication cycle
```

During a cycle:

- the tool scans the current working directory  
- filters files by extension  
- selects X% of them  
- creates timestamped replicas with the tag `__REPLICA__`  
- originals remain untouched  

---

### 2.4. Cleanup of Replicas

The cleanup option removes **only** files created by this tool.

It identifies replicas by the `__REPLICA__` tag.

Original files are never deleted.

---

### 2.5. Encryption of Replicas (with generated password)

The tool includes an optional encryption mode:

- encrypts **only** replica files  
- generates a unique password (Fernet key)  
- saves encrypted versions with `.enc` extension  
- preserves original replicas (no deletion)  
- does not modify original user files  

This allows secure storage of replicated documents.

---

## 3. Menu Structure

```
=== Anti‑Censorship Replicator ===
Current percentage: X%
Extensions: .pdf, .epub, .docx

1) Change replication percentage
2) Change file extensions
3) Start replication cycle
4) Cleanup replicas
5) Encrypt replicas (generate password)
6) Exit
```

---

## 4. Running 

Execute the script:

```bash
python replicator_v2.py
```

The tool will operate inside the **current working directory**, meaning:

- all replicas are created in the folder where the script is executed  
- encryption also happens in that folder  
- cleanup removes replicas from that folder  

---

## 5. Notes

- Originals are **never modified or deleted**.  
- Replicas are clearly marked with `__REPLICA__`.  
- Encryption is optional and reversible with the generated key.  
- The tool is fully interactive and requires user confirmation for all actions.  

---

## 6. Intended Use

Version 2 is designed for:

- document preservation  
- redundancy creation  
- controlled replication workflows  
- safe encryption of replicated files  
- environments where files may be at risk of deletion or loss  

It is **not** an automated daemon and does **not** run indefinitely.

