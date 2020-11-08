import pytest
from spelling import spellChecker


spellChecker_cases = [
    ([['hello']], 1),
    ([['Hello', '0494']], .5),
    ([['0495']], 0),
    ([['Hello'], ['string']], 1),
    ([[['hello']], ['hello']], 1)
]


@pytest.mark.parametrize("wordList,correctness", spellChecker_cases)
def test_spellChecker(wordList, correctness):
    assert spellChecker(wordList) == correctness
