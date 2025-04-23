from intervals import overlapping_intervals


def test_overlapping_intervals():
    # Basisgevallen
    assert overlapping_intervals((1, 5), (3, 6))  # Overlap
    assert not overlapping_intervals((2, 5), (7, 10))  # Geen overlap

    # Zelfde interval
    assert overlapping_intervals((1, 5), (1, 5))  

    # Volledige insluiting
    assert overlapping_intervals((2, 6), (3, 5))  
    assert overlapping_intervals((3, 5), (2, 6))  

    # Randgeval: aanraking (geen overlap)
    assert not overlapping_intervals((1, 3), (3, 5))  
    assert not overlapping_intervals((3, 5), (1, 3))  

    # Omgekeerde invoer (lege interval)
    assert not overlapping_intervals((4, 2), (1, 3))  
    assert not overlapping_intervals((1, 3), (4, 2))  

    # Intervallen in omgekeerde volgorde ingevoerd
    assert overlapping_intervals((3, 6), (1, 5))  
    assert overlapping_intervals((1, 5), (3, 6))