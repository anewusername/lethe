"""
Git snapshotting tool
"""
from .lethe import (
    main, snap, snap_ref, snap_tree, find_merge_base, deref_symref,
    update_ref, commit_tree, get_tree, get_commit, get_obj, get_root, get_latest_commit,
    shorten_hash, _run,
    )

from .VERSION import __version__

__author__ = 'Jan Petykeiwicz'
