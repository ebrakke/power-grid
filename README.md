## Powergrid

### Setup environment

This is to be run on a Python 3 environment  
To install the required packages, run: `python3 -m pip install -r requirements.txt`

### To run the server

`python3 main.py`

### To run all tests

`python3 test.py`

### To run a specific test file

`python3 test.py suite [test_module] [test_class]`  
For example: to run the board reducers tests, you would type  
`python3 test.py suite reducers TestBoardReducer`

## Game state objects

Here are some of the objects we will have in the

```typescript
class Player {
  id: string;
  money: number;
  power_plants: PowerPlant[];
}

class PowerPlant {
  cost: number;
  resource_type: string[];
  resource_cost: number;
  current_resources: number;
  type: string; // 'light', 'dark' 'step'
}

class Market {
  current: PowerPlant[];
  futures: PowerPlant[];
}

class Map {
  cities: City[];
  link_costs: LinkCosts;
}

class City {
  color: string;
  name: string;
  generators: {
    1: string;
    2: string;
    3: string
  }
}

class ConnectionCost {

}

// This will be private to the user
type Deck: Card[];

class ResourceBank {
  coal: number;
  oil: number;
  gas: number;
  uranium: number;
}

// This is the public game state
class GameState {
  players: Player[];
  market: Market;
  map: Map;
  game: {
    current_player: string;
    player_rank: string;
    phase: number;
    step: number;
    current_bid: {
      card: Card;
      amount: number;
      player_id: string;
      passed: string[];
    };
    bought_or_passed: string[]
  };
  resources: {
    max_resource_bank: ResourceBank[];
    current_resource_bank: ResourceBank[];
  }
}
```
