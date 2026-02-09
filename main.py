"""
Main module for Voting Management System
Menu-driven console application
"""

from blockchain import Blockchain
from entities import Voter, Candidate


def print_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("VOTING MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add Candidate")
    print("2. Add Voter")
    print("3. Cast Vote")
    print("4. View Blockchain")
    print("5. Validate Blockchain")
    print("6. View Candidates")
    print("7. View Voters")
    print("8. Exit")
    print("="*60)


def add_candidate(candidates):
    """
    Add a new candidate to the system
    
    Args:
        candidates (dict): Dictionary of candidates
    
    Returns:
        bool: True if candidate was added, False otherwise
    """
    print("\n--- Add Candidate ---")
    candidate_id = input("Enter Candidate ID: ").strip()
    
    # Validate candidate ID
    if not candidate_id:
        print("Error: Candidate ID cannot be empty!")
        return False
    
    if candidate_id in candidates:
        print(f"Error: Candidate ID '{candidate_id}' already exists!")
        return False
    
    name = input("Enter Candidate Name: ").strip()
    
    # Validate candidate name
    if not name:
        print("Error: Candidate name cannot be empty!")
        return False
    
    candidates[candidate_id] = Candidate(candidate_id, name)
    print(f"Success: Candidate '{name}' (ID: {candidate_id}) added successfully!")
    return True


def add_voter(voters):
    """
    Add a new voter to the system
    
    Args:
        voters (dict): Dictionary of voters
    
    Returns:
        bool: True if voter was added, False otherwise
    """
    print("\n--- Add Voter ---")
    voter_id = input("Enter Voter ID: ").strip()
    
    # Validate voter ID
    if not voter_id:
        print("Error: Voter ID cannot be empty!")
        return False
    
    if voter_id in voters:
        print(f"Error: Voter ID '{voter_id}' already exists!")
        return False
    
    name = input("Enter Voter Name: ").strip()
    
    # Validate voter name
    if not name:
        print("Error: Voter name cannot be empty!")
        return False
    
    voters[voter_id] = Voter(voter_id, name)
    print(f"Success: Voter '{name}' (ID: {voter_id}) added successfully!")
    return True


def cast_vote(blockchain, voters, candidates):
    """
    Allow a voter to cast a vote
    
    Args:
        blockchain (Blockchain): The blockchain instance
        voters (dict): Dictionary of voters
        candidates (dict): Dictionary of candidates
    
    Returns:
        bool: True if vote was cast, False otherwise
    """
    print("\n--- Cast Vote ---")
    voter_id = input("Enter Voter ID: ").strip()
    
    # Validate voter exists
    if voter_id not in voters:
        print(f"Error: Voter ID '{voter_id}' not found!")
        return False
    
    voter = voters[voter_id]
    
    # Check if voter has already voted
    if voter.has_voted:
        print(f"Error: Voter '{voter.name}' (ID: {voter_id}) has already voted!")
        return False
    
    # Display available candidates
    if not candidates:
        print("Error: No candidates available!")
        return False
    
    print("\nAvailable Candidates:")
    for candidate_id, candidate in candidates.items():
        print(f"  {candidate_id}: {candidate.name}")
    
    candidate_id = input("\nEnter Candidate ID to vote for: ").strip()
    
    # Validate candidate exists
    if candidate_id not in candidates:
        print(f"Error: Candidate ID '{candidate_id}' not found!")
        return False
    
    # Add vote to blockchain
    blockchain.add_block(voter_id, candidate_id)
    
    # Mark voter as voted
    voter.has_voted = True
    
    candidate = candidates[candidate_id]
    print(f"\nSuccess: Vote cast by '{voter.name}' for '{candidate.name}' has been recorded!")
    return True


def view_candidates(candidates):
    """Display all candidates"""
    print("\n--- Candidates ---")
    if not candidates:
        print("No candidates registered yet.")
    else:
        for candidate_id, candidate in candidates.items():
            print(f"  {candidate}")
    print()


def view_voters(voters):
    """Display all voters"""
    print("\n--- Voters ---")
    if not voters:
        print("No voters registered yet.")
    else:
        for voter_id, voter in voters.items():
            print(f"  {voter}")
    print()


def validate_blockchain(blockchain):
    """Validate and display blockchain status"""
    print("\n--- Blockchain Validation ---")
    is_valid, message = blockchain.validate_chain()
    if is_valid:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")
    print()


def main():
    """Main function to run the voting management system"""
    # Initialize data structures
    blockchain = Blockchain()
    voters = {}
    candidates = {}
    
    print("Welcome to the Voting Management System!")
    print("Using Blockchain Technology for Secure Voting")
    
    # Main menu loop
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_candidate(candidates)
        
        elif choice == "2":
            add_voter(voters)
        
        elif choice == "3":
            cast_vote(blockchain, voters, candidates)
        
        elif choice == "4":
            blockchain.print_chain()
        
        elif choice == "5":
            validate_blockchain(blockchain)
        
        elif choice == "6":
            view_candidates(candidates)
        
        elif choice == "7":
            view_voters(voters)
        
        elif choice == "8":
            print("\nThank you for using the Voting Management System!")
            print("Exiting...")
            break
        
        else:
            print("\nError: Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
