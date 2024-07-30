"""
Git snapshotting tool
"""
from .lethe import (
    snap as snap,
    snap_ref as snap_ref,
    snap_tree as snap_tree,
    find_merge_base as find_merge_base,
    deref_symref as deref_symref,
    update_ref as update_ref,
    commit_tree as commit_tree,
    get_tree as get_tree,
    get_commit as get_commit,
    get_obj as get_obj,
    shorten_hash as shorten_hash,
    get_root as get_root,
    get_latest_commit as get_latest_commit,
    push_ref as push_ref,
    fetch_ref as fetch_ref,
    )

from .endpoints import main as main

__author__ = 'Jan Petykeiwicz'
__version__ = '0.13'
