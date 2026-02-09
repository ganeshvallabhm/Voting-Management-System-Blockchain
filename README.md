# Voting Management System

A simple, menu-driven Voting Management System using basic Blockchain concepts for academic purposes.

## Description

This project implements a console-based voting system where votes are stored in a blockchain. Each vote is recorded as a block in the chain, ensuring data integrity through cryptographic hashing (SHA-256). The system prevents double voting and maintains a tamper-resistant record of all votes.

## Features

- **Admin Functions:**
  - Add candidates to the election
  - Add voters to the system
  
- **Voting:**
  - Cast votes (one vote per voter)
  - Automatic blockchain recording
  
- **Blockchain:**
  - Genesis block initialization
  - SHA-256 hashing for each block
  - Block validation
  - Chain integrity verification
  
- **Input Validation:**
  - Prevents duplicate voter IDs
  - Prevents duplicate candidate IDs
  - Prevents double voting
  
- **Viewing:**
  - Display all candidates
  - Display all voters
  - View entire blockchain
  - Validate blockchain integrity

## Requirements

- Python 3.x (64-bit)
- No external dependencies (uses only Python standard library)

## How to Run

1. Open a terminal/command prompt
2. Navigate to the CRYPTO folder
3. Run the following command:

```bash
py main.py
```

## Project Structure

```
CRYPTO/
├── main.py          # Main menu-driven application
├── blockchain.py    # Block and Blockchain classes
├── entities.py      # Voter and Candidate classes
└── README.md        # This file
```

## Usage Example

1. Start the application
2. Add candidates using option 1
3. Add voters using option 2
4. Cast votes using option 3
5. View blockchain using option 4
6. Validate blockchain using option 5
7. Exit using option 8

## Technical Details

- **Hashing Algorithm:** SHA-256
- **Block Structure:**** Index, Voter ID, Candidate ID, Timestamp, Previous Hash, Current Hash
- **Validation:** Checks hash integrity and previous hash links

## Notes

- This is an academic assignment
- Code uses only Python standard libraries
- Simple and readable implementation
- No external dependencies required
