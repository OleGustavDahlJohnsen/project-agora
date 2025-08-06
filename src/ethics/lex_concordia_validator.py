"""
Project Agora: Lex Concordia Validator
Part of the SANCTUM Architecture v2.0

This module provides functions to programmatically check actions and proposals
against the three inalienable articles of Lex Concordia, the moral and legal
constitution for the entire ecosystem.

Key Responsibilities:
- [cite_start]Provide a verifiable check against Article I: The Bridge of Duality. [cite: 341]
- [cite_start]Provide a verifiable check against Article II: Absolute Zero Tolerance for Harm. [cite: 343]
- [cite_start]Provide a verifiable check against Article III: Light in the Depths. [cite: 345]
- Be used by other modules like E.L.I.A.H. and PORTA SANCTA to enforce the
  constitution at a software level.
"""

import re

def validate_against_article_I(proposal_text: str) -> bool:
    """
    [cite_start]Checks for balance between philosophy/spirituality and the scientific method. [cite: 341]
    [cite_start]Must not conflict with human safety, freedom, or enlightened debate. [cite: 342]
    """
    # Simple keyword analysis for a first pass.
    philosophical_terms = ['faith', 'spiritual', 'metaphysical', 'dogma']
    scientific_terms = ['scientific', 'evidence', 'verified', 'falsifiable', 'rationality']
    conflict_terms = ['override safety', 'restrict freedom', 'censor debate', 'prohibit discussion']

    text_lower = proposal_text.lower()

    # Check for conflict terms
    if any(re.search(r'\b' + term + r'\b', text_lower) for term in conflict_terms):
        return False

    # If philosophical terms are present, balancing scientific terms should also be present.
    has_philosophical = any(re.search(r'\b' + term + r'\b', text_lower) for term in philosophical_terms)
    has_scientific = any(re.search(r'\b' + term + r'\b', text_lower) for term in scientific_terms)

    if has_philosophical and not has_scientific:
        return False # Fails the balance test

    return True

def validate_against_article_II(proposal_text: str) -> bool:
    """
    [cite_start]Checks for any support, enablement, or ignorance of specific, defined harms. [cite: 343]
    This is an absolute zero-tolerance check.
    """
    # A non-exhaustive list of blacklisted phrases based directly on the article.
    # The regex `\b` ensures we match whole words only.
    blacklist = [
        'child abuse', 'human trafficking', 'sexual exploitation',
        'psychological manipulation', 'coercion', 'cult formation', 'addiction'
    ]

    text_lower = proposal_text.lower()

    if any(re.search(r'\b' + phrase + r'\b', text_lower) for phrase in blacklist):
        return False # Immediate failure if any blacklisted phrase is found.

    return True

def validate_against_article_III(proposal_text: str) -> bool:
    """
    [cite_start]Checks for humility, responsibility, and integrity. [cite: 345]
    [cite_start]Ensures humor is not used as a shield for offense or manipulation. [cite: 347]
    """
    text_lower = proposal_text.lower()
    
    # Check for negative framing: cultivating darkness or imposing light
    if "cultivate darkness" in text_lower or "impose light" in text_lower:
        return False
        
    # Check for weaponized humor
    humor_terms = ['joke', 'humor', 'satire', 'funny']
    negative_context = ['degrade', 'offend', 'manipulate', 'attack', 'mock']

    has_humor = any(re.search(r'\b' + term + r'\b', text_lower) for term in humor_terms)
    has_negative_context = any(re.search(r'\b' + term + r'\b', text_lower) for term in negative_context)

    if has_humor and has_negative_context:
        return False # Humor used as a shield for offense/manipulation

    return True
