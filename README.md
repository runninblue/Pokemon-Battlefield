# Pokemon Battlefield

Welcome to Pokemon Battlefield, a client/server application that simulates Pokemon battles.

### Prerequisites
- Git
- Node.js (version 20.10.0)
- npm (version 10.2.5)
- Python (version 3.12.1)
- pip (version 23.3.2)

## Installation
   Clone the repository:
```
   git clone https://github.com/runninblue/Pokemon-Battlefield.git
```

## Server (Node.js) Initialization
1. Navigate to the server directory:
```shell
    cd Pokemon-Battlefield/server
```

2. Install dependencies:
```shell
    npm install
```

### Usage
1. Start the server:
```shell
    npm start
```
    
   Alternatively, start the server by executing:
```shell
    node ./src/server.js
```

2. The server will run at http://localhost:5000

## Client (Python) Initialization
1. From root navigate to the client directory:
```shell
    cd client/pokemon_battlefield
```

2. Install libraries from requirements.txt:
```shell
    pip install -r requirements.txt
```

### Usage
1. Run the client script:
```shell
    python main.py
```

   Alternatively provide the Pokemon names as arguments, for example:
```shell
    python main.py raichu caterpie
```

2. Follow any prompts to initiate Pokemon battles.
