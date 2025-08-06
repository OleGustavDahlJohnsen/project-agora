# === OPPDATERT KODE som erstatter de gamle testene for validatoren ===

def test_article_II_pass_case_with_nlp_mock(mocker):
    """Tests a safe proposal by mocking the NLP model's output."""
    # Mock the classifier to simulate its output for a safe text
    mock_output = {'labels': ['safe content', 'coercion'], 'scores': [0.98, 0.01]}
    mocker.patch('src.ethics.lex_concordia_validator.classifier', return_value=mock_output)
    
    safe_text = "This is a feature for user well-being."
    assert validate_against_article_II(safe_text) == True

def test_article_II_fail_case_with_nlp_mock(mocker):
    """Tests an unsafe proposal by mocking the NLP model's output."""
    # Mock the classifier to simulate its output for a harmful text
    mock_output = {'labels': ['psychological manipulation', 'safe content'], 'scores': [0.95, 0.02]}
    mocker.patch('src.ethics.lex_concordia_validator.classifier', return_value=mock_output)
    
    unsafe_text = "This will subtly influence users to stay online longer."
    assert validate_against_article_II(unsafe_text) == False

def test_article_II_borderline_case_with_nlp_mock(mocker):
    """Tests a borderline case where the score is below the threshold."""
    # Mock the classifier to simulate a low-confidence harmful label
    mock_output = {'labels': ['addiction', 'safe content'], 'scores': [0.75, 0.15]}
    mocker.patch('src.ethics.lex_concordia_validator.classifier', return_value=mock_output)
    
    borderline_text = "This is a very engaging game mechanic."
    assert validate_against_article_II(borderline_text) == True # Passes because score is < 0.90
