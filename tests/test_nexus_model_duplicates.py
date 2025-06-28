from nexus_ai.model import Network

def test_network_score_dedup():
    network = Network.from_json('data/nexus_sample_data_duplicates.json')
    assert abs(network.network_score() - 0.67) < 0.01
