import pytest

from mood_ring import _default_mood_map, Ring

input_1 = {'mood1': 1,
           'mood2': 1,
           'mood3': 1}


def test_ring_output_membership():
    mood_list = _default_mood_map.keys()
    mood_ring = Ring()
    assert str(mood_ring) in mood_list

def test_custom_input_arg():
    mood_list = input_1.keys()
    mood_ring = Ring(input_1)
    assert len(input_1.keys()) == len(input_1.keys())
    for mood in mood_ring.moods_opts:
        assert mood in input_1.keys()

def test_extended_input_key():
    def_len = len(_default_mood_map.keys())
    mood_ring = Ring(extend=input_1)
    ext_len = len(input_1.keys())
    assert len(mood_ring.moods_opts) == def_len + ext_len

def test_input_arg_type():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring('this mood')
    assert 'only accepts a dictionary object' in str(err.value)

def test_input_kw_type():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring(extend='this mood')
    assert 'only accepts a dictionary object' in str(err.value)
