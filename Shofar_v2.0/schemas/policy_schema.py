# -*- coding: utf-8 -*-
"""
Defines the Pydantic schema for validating the structure of human-readable
policy files (e.g., YAML).
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Literal

class PolicyMetadata(BaseModel):
    """Schema for the metadata section of a policy file."""
    policy_id: str
    version: str
    author: str
    description: str

class Rule(BaseModel):
    """Schema for a single rule within a policy."""
    rule_id: str
    effect: Literal['allow', 'deny']
    action: List[str]
    resource: str
    condition: Dict[str, Any] = Field({}, description="Optional conditions for the rule.")

class PolicySchema(BaseModel):
    """
    The formal schema for a complete policy file.
    """
    metadata: PolicyMetadata
    rules: List[Rule]

    class Config:
        """Pydantic configuration."""
        extra = 'forbid' # Forbid any extra fields not defined in the schema

def validate_policy_structure(data: Dict) -> bool:
    """
    Validates a dictionary (from YAML/JSON) against the PolicySchema.
    """
    PolicySchema(**data)
    return True
