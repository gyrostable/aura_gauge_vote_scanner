# constants.py

SNAPSHOT_SUBGRAPH_URL = "https://hub.snapshot.org/graphql"

# Query to fetch votes for a specific proposal
VOTES_QUERY = """
query ($proposalId: String!) {
  votes (
    first: 1000
    skip: 0
    where: {
      proposal: $proposalId
    }
    orderBy: "created",
    orderDirection: desc
  ) {
    id
    voter
    vp
    vp_by_strategy
    vp_state
    created
    proposal {
      id
    }
    choice
    space {
      id
    }
  }
}
"""

# Query to fetch details of a specific proposal
PROPOSAL_QUERY = """
query ($proposalId: String!) {
  proposal(id: $proposalId) {
    id
    title
    body
    choices
    start
    end
    snapshot
    state
    author
    created
    scores
    scores_by_strategy
    scores_total
    scores_updated
    plugins
    network
    strategies {
      name
      network
      params
    }
    space {
      id
      name
    }
  }
}
"""
