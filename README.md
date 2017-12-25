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
  step_card: boolean // The card that indicates the start of step three
  type: string // 'light' or 'dark'
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

// This will be private to the user
type Deck: PowerPlant[];

enum Phase {
  PlayerOrder,
  BuyPowerPlants,
  BuyResources,
  BuyGenerators,
  Generate
}

// This is the public game state
class GameState {
  players: Player[];
  current_player: string;
  market: Market;
  player_rank: string[];
  map: Map;
  phase: Phase; // Indicates the phase of the round we are in (1,2,3,4,5)
  step: number; // Indicates the step of the game we are in (1,2,3)
}
```
