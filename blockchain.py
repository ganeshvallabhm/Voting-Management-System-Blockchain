"""
Blockchain module for Voting Management System
Contains Block and Blockchain classes using SHA-256 hashing
"""

import hashlib
from datetime import datetime


class Block:
    """Represents a single block in the blockchain"""
    
    def __init__(self, index, voter_id, candidate_id, previous_hash):
        """
        Initialize a block
        
        Args:
            index (int): Position of block in chain
            voter_id (str): ID of the voter who cast the vote
            candidate_id (str): ID of the candidate voted for
            previous_hash (str): Hash of the previous block
        """
        self.index = index
        self.voter_id = voter_id
        self.candidate_id = candidate_id
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Calculate SHA-256 hash of the block
        
        Returns:
            str: Hexadecimal hash string
        """
        # Create a string representation of block data
        block_string = f"{self.index}{self.voter_id}{self.candidate_id}{self.timestamp}{self.previous_hash}"
        # Calculate SHA-256 hash
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __str__(self):
        """String representation of block"""
        return (f"Block {self.index}\n"
                f"  Voter ID: {self.voter_id}\n"
                f"  Candidate ID: {self.candidate_id}\n"
                f"  Timestamp: {self.timestamp}\n"
                f"  Previous Hash: {self.previous_hash}\n"
                f"  Hash: {self.hash}\n")


class Blockchain:
    """Represents the blockchain for storing votes"""
    
    def __init__(self):
        """Initialize blockchain with genesis block"""
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """
        Create the first block (genesis block) in the chain
        
        Returns:
            Block: The genesis block
        """
        return Block(0, "GENESIS", "GENESIS", "0")
    
    def add_block(self, voter_id, candidate_id):
        """
        Add a new block (vote) to the blockchain
        
        Args:
            voter_id (str): ID of the voter
            candidate_id (str): ID of the candidate voted for
        
        Returns:
            Block: The newly created block
        """
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            voter_id=voter_id,
            candidate_id=candidate_id,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)
        return new_block
    
    def print_chain(self):
        """Print all blocks in the blockchain"""
        print("\n" + "="*60)
        print("BLOCKCHAIN")
        print("="*60)
        for block in self.chain:
            print(block)
            print("-"*60)
        print()
    
    def validate_chain(self):
        """
        Validate the integrity of the blockchain
        
        Returns:
            tuple: (is_valid: bool, error_message: str)
        """
        # Check if chain is empty
        if len(self.chain) == 0:
            return False, "Blockchain is empty"
        
        # Validate genesis block
        genesis = self.chain[0]
        if genesis.index != 0 or genesis.previous_hash != "0":
            return False, "Invalid genesis block"
        
        # Validate each block
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False, f"Block {current_block.index} has invalid hash"
            
            # Check if previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False, f"Block {current_block.index} has invalid previous hash"
        
        return True, "Blockchain is valid"
