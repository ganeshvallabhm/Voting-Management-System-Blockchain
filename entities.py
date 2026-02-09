"""
Entities module for Voting Management System
Contains Voter and Candidate classes
"""


class Voter:
    """Represents a voter in the system"""
    
    def __init__(self, voter_id, name):
        """
        Initialize a voter
        
        Args:
            voter_id (str): Unique identifier for the voter
            name (str): Name of the voter
        """
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False
    
    def __str__(self):
        """String representation of voter"""
        return f"Voter ID: {self.voter_id}, Name: {self.name}, Has Voted: {self.has_voted}"


class Candidate:
    """Represents a candidate in the election"""
    
    def __init__(self, candidate_id, name):
        """
        Initialize a candidate
        
        Args:
            candidate_id (str): Unique identifier for the candidate
            name (str): Name of the candidate
        """
        self.candidate_id = candidate_id
        self.name = name
    
    def __str__(self):
        """String representation of candidate"""
        return f"Candidate ID: {self.candidate_id}, Name: {self.name}"
