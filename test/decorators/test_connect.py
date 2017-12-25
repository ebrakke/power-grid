import unittest
from src.decorators import connect
from vendor.python_redux import create_store, combine_reducers


def state_1_reducer(state=None, action=None):
    if state is None:
        state = 1
    if action is None:
        return state
    return state


def state_2_reducer(state=None, action=None):
    if state is None:
        state = 2
    if action is None:
        return state
    return state


TEST_STORE = create_store(combine_reducers({
    'state1': state_1_reducer,
    'state2': state_2_reducer
}))


class TestConnectDecorator(unittest.TestCase):
    def test_runs_normal_function_if_no_store(self):
        @connect.connect
        def func(a, b, **kwargs):
            return a + b
        self.assertEqual(func(1, 2), 3)

    def test_gets_passed_funcs_in_kwargs_if_store_provided(self):
        connect.initialize(TEST_STORE)

        @connect.connect
        def func(a, b, **kwargs):
            get_state = kwargs.get('get_state')
            dispatch = kwargs.get('dispatch')
            self.assertTrue(hasattr(get_state, '__call__'))
            self.assertTrue(hasattr(dispatch, '__call__'))

        func(1, 2)
    
    def test_can_get_state_from_store(self):
        connect.initialize(TEST_STORE)

        @connect.connect
        def func(**kwargs):
            get_state = kwargs.get('get_state')
            dispatch = kwargs.get('dispatch')
            state = get_state()
            global_state = TEST_STORE['get_state']()
            self.assertEqual(state, global_state)
        
        func()
        


if __name__ == '__main__':
    unittest.main()
