import random

# Optional: For textual similarity measure
try:
    from sentence_transformers import SentenceTransformer, util
    SBERT_AVAILABLE = True
    sbert_model = SentenceTransformer("all-MiniLM-L6-v2")  # or any other
except ImportError:
    SBERT_AVAILABLE = False
    sbert_model = None

########################
# 1) PARSE THE ERROR
########################

def parse_textual_error(error_msg):
    """
    Identify key issues or tags in the textual error message.
    Returns a list (or set) of tags like ["compile_error", "no_pass", "partial_pass", etc.].
    """
    msg_lower = error_msg.lower()
    tags = []

    if "fails to compile" in msg_lower or "does not compile" in msg_lower:
        tags.append("compile_error")
    if "crashes at runtime" in msg_lower or "runtime error" in msg_lower:
        tags.append("runtime_error")
    if "passes all tests" in msg_lower:
        tags.append("all_pass")
    elif ("does not pass any tests" in msg_lower or 
          "fails all tests" in msg_lower or 
          "no tests passed" in msg_lower):
        tags.append("no_pass")
    elif "passes some tests" in msg_lower or "partial logic" in msg_lower:
        tags.append("partial_pass")
    if "no tests available" in msg_lower or "no test results" in msg_lower:
        tags.append("no_tests")

    # Similarity tags or references
    if "very similar" in msg_lower or "very close" in msg_lower:
        tags.append("very_close")
    elif "moderate similarity" in msg_lower or "close to the reference" in msg_lower:
        tags.append("close")
    elif "significantly different" in msg_lower or "far from the reference" in msg_lower:
        tags.append("far")

    return tags

########################
# 2) OPTIONAL: QUANTIFY
########################

def measure_error_distance(error_msg, ideal_msg="The code compiles and passes all tests."):
    """
    Use Sentence-BERT to measure how far the error is from the 'ideal' feedback.
    Returns a similarity score in [0..1] (roughly). Higher = more similar to ideal.

    If SBERT is not installed, returns None.
    """
    if not (SBERT_AVAILABLE and sbert_model):
        return None
    
    # Encode
    error_emb = sbert_model.encode(error_msg, convert_to_tensor=True)
    ideal_emb = sbert_model.encode(ideal_msg, convert_to_tensor=True)
    similarity_score = util.cos_sim(error_emb, ideal_emb).item()
    # similarity_score is typically in [-1, 1], but usually positive for normal text.
    return similarity_score

########################
# 3) GENERATE GRADIENT
########################

def generate_textual_gradient(error_msg, use_similarity=False):
    """
    Create a textual gradient (high-level suggestions) from a textual error.

    If 'use_similarity' is True, we measure how close the error is to the 'ideal feedback'
    and incorporate a short mention or consideration into the final gradient text
    (e.g., 'The error is quite distant from the ideal. Focus on thorough correctness.').
    """
    tags = parse_textual_error(error_msg)
    suggestions = []

    # Priority-based or multi-tag approach
    if "compile_error" in tags:
        suggestions.append("Focus on syntax correctness. Fix compilation issues first.")
    if "runtime_error" in tags:
        suggestions.append("Ensure robust handling of runtime exceptions and edge cases.")
    if "no_pass" in tags:
        suggestions.append("Emphasize thorough handling of all test inputs. Seek full correctness.")
    elif "partial_pass" in tags:
        suggestions.append("Address the specific failing cases or edge conditions.")
    elif "all_pass" in tags:
        suggestions.append("The solution is correct for given tests. Consider further edge cases.")
    elif "no_tests" in tags:
        suggestions.append("Add or clarify test cases to verify correctness.")

    # Similarity to reference approach
    if "far" in tags:
        suggestions.append("Align the solution more closely with the reference's approach or logic.")
    elif "close" in tags:
        suggestions.append("Refine minor differences to closely match the reference.")
    elif "very_close" in tags:
        suggestions.append("Keep the current approach; only small improvements may be needed.")

    # If no tags found, we do a generic suggestion
    if not suggestions:
        suggestions.append("Review logic and correctness. The error is unclear or unspecified.")

    # Combine
    gradient_text = " ".join(suggestions)

    # Optionally measure how close the error is to the ideal "no error" feedback
    if use_similarity:
        similarity_score = measure_error_distance(error_msg)
        if similarity_score is not None:
            # You can interpret the score as you like:
            # e.g., if similarity_score < 0.3 => "Quite far from ideal feedback."
            # or just incorporate a short note.
            if similarity_score < 0.3:
                gradient_text += " The error is quite distant from the ideal solution. Consider major revisions."
            elif similarity_score < 0.6:
                gradient_text += " The error is moderately distant from the ideal solution. Further improvements needed."
            else:
                gradient_text += " The error is somewhat close to the ideal solution, but minor fixes remain."

    return gradient_text.strip()


if __name__ == "__main__":
    # Some example error messages
    error_messages = [
        "The code compiles but does not pass any tests. It is significantly different from the reference.",
        "The code fails to compile.",
        "The code compiles and passes all tests. It is very similar to the reference solution.",
        "The code compiles but crashes at runtime. No tests passed.",
        "The code compiles and passes some tests but not all. It has moderate similarity to the reference."
    ]

    for idx, e_msg in enumerate(error_messages, start=1):
        gradient = generate_textual_gradient(e_msg, use_similarity=True)
        print(f"\nError #{idx}: {e_msg}")
        print(f"Textual Gradient: {gradient}")
