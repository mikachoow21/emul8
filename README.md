## Emul8 : Micah Weitzman - ESE350 Spring 2020
[`wmicah at seas dot upenn dot edu`](mailto:wmicah@seas.upenn.edu)
### Compilation
Run the following commands to clear logs and old object files, and to create a new `./Executeable` file. 
```shell 
$ make clean 
$ make 
```
### Plaing a Game
To play anyone of the games listed in the `games/` folder, either run the following from the command line: 
```shell 
$./Executable [GAME]
```
Or, you could run `$ ./Executable` and input the game when prompted. 

### Files
```
├── beep.aiff
├── Executable
├── games
│   ├── 15PUZZLE
│   ...
│   └── WIPEOFF
├── LICENSE
├── Makefile
├── obj
│   ├── emul8.o
│   ├── errors.o
│   ├── gamul.o
│   └── handler.o
├── README.md
├── run.sh
├── src
│   ├── emul8.c
│   ├── errors.c
│   ├── errors.h
│   ├── gamul.c
│   ├── gamul.h
│   ├── handler.c
│   ├── handler.h
│   └── state.h
└── test.py
```
### Code Layout 
#### `src/` Directory
Most the main program is containted within the `src/` directory. The main graphics and logic loops, as well as the debugging functions can be found in `emul8.c`. This file initiates the state of the program, as well as the emulated memory arrarys found in the `state` struct.  
The `state` struct is defined in `state.h` and contains a struct with fields contining the 4k program memory, stack pointer, general purpose register, stack, stack pointer, timer register, and delay register. The `state` struct was designed to be portable, so all the various memory registers could be accessed from different files, and passed to the `handler_ptr_array` pointer array.  
The each of the 35 opcode functions are defined in `handler.c`. Each of this functions is passed a `state` struct as well as the optcode itself. Each one of the optcode functions performs its role described in the literature.  
The optcode functions are combined to form a function pointer array, `*handler_ptr_array[]`, defined in `handler.h`. Becuase the most significant hex digit determined the optcode, they all required the same input, and because they took up all values from `0..F` they could be treated like an array of functions, and were implemented as such.  
    In addition to containing the display functionality, `gamul.c` also contians the functions to subtract one from the sound and delay registers when appropriate. 

### Other Files 
`test.py` is a python script written to help with testing specific optcodes. Running: `$ python test.py` output a binary file, `TEST`, which contains a binary of the hex-string `hx` in the file.   
`run.sh` is another script to help automate testing and debugging. It runs `./Execute` with the `TEST` binary file and outputs all of the data to `log.txt` to make inspection easier. 
