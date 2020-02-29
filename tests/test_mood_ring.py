#import sys
#sys.path.append('..')
import mood_ring as mr

def test_ring_output_membership():
    mood_list = [item[0] for item in mr.mood_map]
    mood_ring = mr.Ring()
    assert str(mood_ring) in mood_list
