"""Inspect the installed pack identity."""

from authentication_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:authentication"
print(metadata["origin"]["id"])
