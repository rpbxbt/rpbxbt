from belonging.model import Community


def test_belonging_score():
    community = Community.from_json('data/sample_data.json')
    assert abs(community.belonging_score() - 0.67) < 0.01
