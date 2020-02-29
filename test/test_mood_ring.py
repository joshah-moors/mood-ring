from mood_ring import mood_map, Ring

def test_ring_output_membership():
    mood_list = [item[0] for item in mood_map]
    mood_ring = Ring()
    assert str(mood_ring) in mood_list
