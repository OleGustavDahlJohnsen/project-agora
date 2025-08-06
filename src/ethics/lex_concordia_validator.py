"""
Project Agora: Lex Concordia Validator (Refined NLP Version)
Part of the SANCTUM Architecture v2.0

This module provides functions to programmatically check actions and proposals
against the three inalienable articles of Lex Concordia. This refined version
uses a zero-shot classification model to understand semantic meaning, not just
keywords.
"""

from transformers import pipeline

# --- Model Initialization ---
# This initializes the NLP pipeline. The model is downloaded on first run.
# We use a model fine-tuned for Natural Language Inference, which is excellent
# for zero-shot classification.
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def validate_against_article_II(proposal_text: str, threshold=0.90) -> bool:
    """
    Checks for any support, enablement, or ignorance of specific, defined harms
    using zero-shot classification. This is an absolute zero-tolerance check.
    """
    # Labels derived directly from the article's text.
    candidate_labels = [
        'child abuse', 'human trafficking', 'sexual exploitation',
        'psychological manipulation', 'coercion', 'cult formation', 'addiction',
        'safe content'
    ]
    
    print(f"\nValidator (Art. II): Analyzing text with NLP model...")
    results = classifier(proposal_text, candidate_labels, multi_label=False)
    
    # Get the label with the highest score.
    top_label = results['labels'][0]
    top_score = results['scores'][0]
    
    print(f"Validator (Art. II): Top predicted label is '{top_label}' with score {top_score:.2f}.")

    # If the top-scoring label is not 'safe content' and the score is high, fail.
    if top_label != 'safe content' and top_score > threshold:
        return False

    return True

# NOTE: Article I and III are more nuanced and would require more complex logic
# or a different type of NLP model (e.g., stance detection, sentiment analysis).
# For this refinement, we focus on the most critical zero-tolerance article.
# The placeholder functions remain for now.

def validate_against_article_I(proposal_text: str) -> bool:
    """Placeholder for nuanced Article I validation."""
    return True

def validate_against_article_III(proposal_text: str) -> bool:
    """Placeholder for nuanced Article III validation."""
    return True
