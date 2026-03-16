
# Lab 5 Team Work Split (Team of 3)
## CSCI/CSCY 4407 – Security & Cryptography
## Lab 5: MAC, UF-CMA, CBC-MAC, HMAC & PRF

This plan splits the work across **3 team members** while still making sure the final submission feels consistent and complete. Since only **one person submits**, the team should still review the final PDF together before turning it in.

---

# Team Roles Overview

## Member 1 — GitHub / Environment / Core HMAC Lead
Responsible for:
- GitHub repository setup
- lab folder structure
- Task 1
- Task 2
- Task 3
- helping standardize filenames and screenshots

## Member 2 — Verification / Integrity / Replay Lead
Responsible for:
- Task 4
- Task 5
- Task 8
- helping verify screenshots and outputs are clear

## Member 3 — Multi-message / Key-change / PRF / Report Assembly Lead
Responsible for:
- Task 6
- Task 7
- Task 9
- assembling the final report structure and rubric check

---

# Step 0: GitHub Setup (Do This First)

## Goal
Set up one shared repository so everyone has:
- the same scripts
- the same file names
- the same folder structure
- version history
- an easy way to combine work at the end

## Recommended Repo Name
```text
lab5-mac-prf
````

## Suggested Folder Structure

```text
lab5-mac-prf/
├── README.md
├── report/
│   ├── lab5_report.md
│   └── screenshots/
├── code/
│   ├── hmac_gen.py
│   ├── hmac_verify.py
│   ├── hmac_multi.py
│   └── prf_experiment.py
├── messages/
│   ├── message1.txt
│   ├── message2.txt
│   └── message3.txt
└── notes/
    ├── task_notes.md
    └── rubric_checklist.md
```

## GitHub Setup Tasks

### Member 1

* Create the GitHub repo
* Add teammates as collaborators if needed
* Create the initial folder structure
* Add a basic `README.md`
* Push the initial commit

### Member 2

* Clone the repo locally
* Confirm they can pull and push
* Create a branch for their task set

### Member 3

* Clone the repo locally
* Confirm they can pull and push
* Create a branch for their task set

## Recommended Branch Names

```text
main
member1-setup-hmac
member2-verify-replay
member3-prf-report
```

## Basic Git Commands

```bash
git clone <repo-url>
cd lab5-mac-prf

git checkout -b member1-setup-hmac
git checkout -b member2-verify-replay
git checkout -b member3-prf-report

git add .
git commit -m "Complete Task 3 HMAC generation script"
git push -u origin member1-setup-hmac
```

## Merge Plan

After each member finishes:

* push branch
* review files/screenshots
* merge into `main`

If you want to keep it simple, one person can merge everything after reviewing.

---

# Member 1 Work Split

## Role: GitHub / Setup / Core HMAC Lead

### Main Responsibilities

* Set up GitHub repo
* Build shared file structure
* Complete Task 1
* Complete Task 2
* Complete Task 3

## Task 1: Lab Setup and Directory Creation

### Deliverables

* Screenshot of creating `MAC_Lab`
* Screenshot showing `pwd` and/or `ls`
* short explanation of why the working directory matters

## Task 2: Message Creation

### Deliverables

* screenshots of creating `message1.txt`, `message2.txt`, `message3.txt`
* screenshots of `cat` output
* screenshot of `ls -l`
* screenshot of `sha256sum`
* short explanation about hash changes after a small modification

## Task 3: HMAC Generation Script

### Deliverables

* `hmac_gen.py`
* screenshot of script contents
* screenshot of terminal execution
* recorded HMAC tags for multiple messages
* explanation of what the script does step by step
* explanation of why different messages produce different HMAC values

## Extra Duties

* make sure filenames are consistent
* make sure everyone stores screenshots in the same folder
* make sure Python files are saved in `code/`

---

# Member 2 Work Split

## Role: Verification / Integrity / Replay Lead

### Main Responsibilities

* Complete Task 4
* Complete Task 5
* Complete Task 8

## Task 4: Message Verification

### Deliverables

* `hmac_verify.py`
* screenshot of script
* screenshot showing successful verification
* screenshot showing failed verification with wrong tag
* screenshot showing failed verification after message modification
* short explanation of how HMAC verification checks integrity and authenticity

## Task 5: Message Tampering Experiment

### Deliverables

* screenshots showing at least 3 different modifications to the message
* screenshots showing verification failure each time
* short explanation of why the original tag becomes invalid after tampering
* explanation of how MACs help detect message changes

## Task 8: Replay Attack Experiment

### Deliverables

* screenshot showing original valid message restored
* screenshot showing valid HMAC tag generation
* screenshot showing successful verification
* screenshot showing replay acceptance a second time
* screenshot showing replay acceptance a third time
* screenshot showing updated message with timestamp/counter
* screenshot showing generation of new tag for updated message
* screenshot showing successful verification of updated message
* explanation of why replay works
* explanation of why MAC alone does not provide freshness
* short discussion of timestamps, counters, and nonces

## Extra Duties

* double-check that the replay section clearly shows **multiple successful replays**
* make sure screenshots are readable and not cropped badly

---

# Member 3 Work Split

## Role: Multi-message / Key-change / PRF / Report Assembly Lead

### Main Responsibilities

* Complete Task 6
* Complete Task 7
* Complete Task 9
* assemble final report

## Task 6: Multiple Message Authentication

### Deliverables

* `hmac_multi.py`
* screenshot of script
* screenshot showing output for all 3 messages
* screenshot after modifying one message
* comparison of old vs new tag values
* explanation of why different messages produce different tags under the same key

## Task 7: Secret Key Change Experiment

### Deliverables

* screenshot showing original key
* screenshot showing modified key
* screenshot showing changed outputs
* comparison of old vs new tag values
* explanation of why the secret key affects authentication output
* explanation of why secret key secrecy matters

## Task 9: PRF-Based Authentication Script

### Deliverables

* `prf_experiment.py`
* screenshot of self-written script
* screenshot showing outputs for at least 3 messages
* screenshot showing output changes after modifying a message
* screenshot showing output changes after changing the key
* short explanation of how PRFs relate to MACs

## Report Assembly Duties

* combine all member writeups into one report
* keep formatting consistent
* organize by Task 1 through Task 9
* make sure every task has:

  * explanation
  * screenshot evidence
  * code snippet or code file
  * output
  * interpretation

---

# Shared Team Rules

## Everyone should

* pull the latest repo changes before starting
* use the same filenames
* save screenshots with clear names
* write explanations in complete sentences
* avoid submitting raw terminal output without explanation

## Screenshot Naming Suggestion

```text
task1_directory_setup.png
task2_message_creation.png
task2_hashes.png
task3_hmac_script.png
task3_hmac_output.png
task4_verify_success.png
task4_verify_fail.png
task5_tamper1.png
task5_tamper2.png
task5_tamper3.png
task6_multi_output.png
task7_key_change.png
task8_replay1.png
task8_replay2.png
task8_timestamp.png
task9_prf_script.png
task9_prf_output.png
```

---

# Final Assembly Plan

## Member 1

* confirms GitHub repo has all scripts and screenshots
* confirms folder structure is clean

## Member 2

* checks that all verification/tampering/replay evidence is included
* checks that screenshots are readable

## Member 3

* assembles the final report
* matches everything against rubric
* exports to PDF for submission

---

# Final Pre-Submission Checklist

## GitHub / Files

* [ ] GitHub repo created
* [ ] all members added or able to contribute
* [ ] all scripts uploaded
* [ ] all screenshots uploaded
* [ ] final report saved in repo

## Task Coverage

* [ ] Task 1 included
* [ ] Task 2 included
* [ ] Task 3 included
* [ ] Task 4 included
* [ ] Task 5 included
* [ ] Task 6 included
* [ ] Task 7 included
* [ ] Task 8 included
* [ ] Task 9 included

## Report Quality

* [ ] organized by task number
* [ ] explanations are in complete sentences
* [ ] screenshots match the task they support
* [ ] code is readable
* [ ] outputs are explained
* [ ] reproducible steps are shown

## Submission

* [ ] one final PDF created
* [ ] one group member submits to Canvas
* [ ] team reviews before submission

```

A couple smart notes so you don’t get burned:
- **Task 3 and Task 4 are linked**, so Member 1 and Member 2 should coordinate on the exact key and filenames.
- **Task 8 depends on earlier working scripts**, so don’t leave replay until the very end.
- For **Task 9**, Member 3 should make the PRF script look clearly self-written and not just a renamed HMAC script.
- Put **all code in GitHub**, even if you also embed snippets in the PDF.

I can also make you a **full report template in Markdown with sections for each teammate to fill in**.
```
