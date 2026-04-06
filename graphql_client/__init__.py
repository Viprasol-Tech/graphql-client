"""
graphql-client - GraphQL client with query builder

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import GraphqlClient, query, process, main

__all__ = ["GraphqlClient", "query", "process", "main"]
