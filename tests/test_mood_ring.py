import pytest

from mood_ring import _default_mood_map, Ring

dict_input_1 = {'mood1': 1,
                'mood2': 1,
                'mood3': 1}

list_input_1 = ['mood3', 'mood4', 'mood5', 'mood6']


def test_ring_output_membership():
    mood_list = _default_mood_map.keys()
    mood_ring = Ring()
    assert str(mood_ring) in mood_list

def test_custom_dict_input():
    mood_list = dict_input_1.keys()
    mood_ring = Ring(dict_input_1)
    assert len(mood_ring.mood_opts) == len(dict_input_1.keys())
    for mood in mood_ring.mood_opts:
        assert mood in dict_input_1.keys()

def test_custom_list_input():
    mood_ring = Ring(list_input_1)
    assert len(mood_ring.mood_opts) == len(list_input_1)
    for mood in mood_ring.mood_opts:
        assert mood in list_input_1
    assert mood_ring.mood_probs == tuple([1 for m in list_input_1])

def test_extended_input_dict():
    def_len = len(_default_mood_map.keys())
    mood_ring = Ring(extend=dict_input_1)
    ext_len = len(dict_input_1.keys())
    assert len(mood_ring.mood_opts) == def_len + ext_len

def test_custom_list_input_list_extend():
    mood_ring = Ring(dict_input_1, extend=list_input_1)
    opt_set = set(list(dict_input_1.keys()) + list_input_1)
    assert len(mood_ring.mood_opts) == len(opt_set)
    for mood in mood_ring.mood_opts:
        assert mood in opt_set

def test_input_arg_type_str():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring('this mood')
    assert 'only accepts list/dict objects' in str(err.value)

def test_input_kw_type_str():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring(extend='this mood')
    assert 'only accepts list/dict objects' in str(err.value)

def test_input_arg_type_int():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring(1)
    assert 'only accepts list/dict objects' in str(err.value)

def test_input_kw_type_int():
    with pytest.raises(TypeError) as err:
        mood_ring = Ring(extend=1)
    assert 'only accepts list/dict objects' in str(err.value)
