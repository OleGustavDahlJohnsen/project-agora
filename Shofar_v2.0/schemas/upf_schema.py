# -*- coding: utf-8 -*-
"""
Defines the Pydantic schema for the Unified Perceptual Field (UPF).
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, List
from datetime import datetime

class PerceptualField(BaseModel):
    """Defines the core fused perception data."""
    primary_entity: Dict[str, Any] = Field(..., description="The main entity of focus in the perception.")
    ambient_audio: Dict[str, Any] = Field(..., description="Characteristics of the ambient soundscape.")
    spatial_awareness: Dict[str, Any] = Field(..., description="Information about the spatial environment.")
    
class UPFSchema(BaseModel):
    """
    The formal schema for a Unified Perceptual Field packet.
    This is the standard data structure for all real-time perception.
    """
    upf_version: str = Field("2.0", description="Version of the UPF schema.")
    packet_id: str = Field(..., description="Unique identifier for this perceptual packet.")
    source_node: str = Field(..., description="The ID of the Shofar node that generated this perception.")
    timestamp_utc: datetime = Field(..., description="The UTC timestamp of when the perception was fused.")
    perceptual_field: PerceptualField
    
    class Config:
        """Pydantic configuration."""
        anystr_strip_whitespace = True
        validate_assignment = True

def validate_upf(data: Dict) -> bool:
    """
    Validates a dictionary against the UPFSchema.

    Returns:
        bool: True if data is valid, raises an exception otherwise.
    """
    UPFSchema(**data)
    return True
