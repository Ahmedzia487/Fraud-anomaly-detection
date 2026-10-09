
"""Robust preprocessing for unusual transaction-note inputs."""

import numpy as np
import unicodedata


def preprocess_transaction_note(value, max_length=500):
    """
    Safely preprocess an unusual transaction note.

    Returns:
        tuple: (cleaned_text, actions_taken)
    """

    if not isinstance(max_length, int) or max_length < 0:
        raise ValueError("max_length must be a non-negative integer.")

    actions = []

    # Handle missing values
    if value is None or (
        isinstance(value, (float, np.floating))
        and np.isnan(value)
    ):
        text = ""
        actions.append("missing_value_replaced_with_empty")
    else:
        if not isinstance(value, str):
            text = str(value)
            actions.append("non_string_converted_to_text")
        else:
            text = value

        # Normalize Unicode
        normalized = unicodedata.normalize("NFKC", text)

        if normalized != text:
            actions.append("unicode_normalized")

        text = normalized

    # Normalize line breaks and remove control characters
    cleaned_chars = []
    control_characters_removed = False
    line_breaks_normalized = False

    for char in text:
        if char in "\t\n\r":
            cleaned_chars.append(" ")
            line_breaks_normalized = True
        elif char.isprintable():
            cleaned_chars.append(char)
        else:
            control_characters_removed = True

    text = "".join(cleaned_chars)

    if line_breaks_normalized:
        actions.append("tabs_or_line_breaks_normalized")

    if control_characters_removed:
        actions.append("control_characters_removed")

    # Collapse repeated whitespace
    collapsed = " ".join(text.split())

    if collapsed != text:
        actions.append("whitespace_normalized")

    text = collapsed

    # Enforce maximum note length
    if len(text) > max_length:
        text = text[:max_length]
        actions.append(f"truncated_to_{max_length}_characters")

    if text == "" and not actions:
        actions.append("empty_input")

    if not actions:
        actions.append("unchanged")

    return text, "; ".join(actions)
