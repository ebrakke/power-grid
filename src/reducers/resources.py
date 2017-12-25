"""Reducers for the resources part of the state"""
import json
import os.path
from copy import deepcopy
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
INITIAL_RESOURCES = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/initial_resources.json')).read())
MAX_RESOURCES = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/max_resources.json')).read())

INITIAL_STATE = dict(
    current_resource_bank=deepcopy(INITIAL_RESOURCES),
    max_resource_bank=deepcopy(MAX_RESOURCES)
)


def get_available_bucket(state, resource_type):
    """Get the bucket to take the next resource from
       returns :: index of bucket to take from, or -1 if no resources are there"""
    buckets_with_resources = [i for (i, bucket) in enumerate(
        state['current_resource_bank']) if bucket.get(resource_type) > 0]
    return buckets_with_resources[0] if buckets_with_resources else -1


def get_first_non_filled_bucket(state, resource_type):
    """Get the first bucket that should be refilled
       returns :: index of the bucket to refill or -1 if all are full"""
    non_full_buckets = [i for (i, bucket) in enumerate(state['current_resource_bank']) if bucket.get(
        resource_type) < state['max_resource_bank'][i][resource_type]]
    return non_full_buckets[-1] if non_full_buckets else -1


def resources(state=None, action=None):
    if state is None:
        state = deepcopy(INITIAL_STATE)
    if action is None:
        return state
    action_type = action.get('type')
    if action_type == 'TAKE_RESOURCE':
        idx = get_available_bucket(state, action.get('resource_type'))
        if idx == -1:
            return state  # Can't take a resouce that's not there
        new_state = deepcopy(state)
        new_state['current_resource_bank'][idx][action.get('resource_type')] -= 1
        return new_state

    if action_type == 'REPLENISH_RESOURCE':
        idx = get_first_non_filled_bucket(
            state, action.get('resource_type'))
        if idx == -1:
            return state  # Can't replenish if everything is full
        new_state = deepcopy(state)
        new_state['current_resource_bank'][idx][action.get('resource_type')] += 1
        return new_state

    return state
