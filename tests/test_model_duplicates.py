from belonging.model import Community

def test_belonging_score_dedup():
    community = Community.from_json('data/sample_data_duplicates.json')
    assert abs(community.belonging_score() - 0.67) < 0.01
