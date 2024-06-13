# data_fetcher.py

from constants import SNAPSHOT_SUBGRAPH_URL, VOTES_QUERY, PROPOSAL_QUERY
from utils import fetch_graphql_data


def fetch_votes(proposal_id):
    variables = {"proposalId": proposal_id}
    result = fetch_graphql_data(SNAPSHOT_SUBGRAPH_URL, VOTES_QUERY, variables)
    if result:
        return result['data']['votes']
    return None


def fetch_proposal(proposal_id):
    variables = {"proposalId": proposal_id}
    result = fetch_graphql_data(SNAPSHOT_SUBGRAPH_URL, PROPOSAL_QUERY, variables)
    if result:
        return result['data']['proposal']
    return None
