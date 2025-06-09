from nexus_ai.model import Network


def test_network_score():
    network = Network.from_json('data/nexus_sample_data.json')
    assert abs(network.network_score() - 0.67) < 0.01
