# Roadmap for implementation

## MVP Details 
### Summary of Status: 
My MVP retrieves and displays all earthquakes from 1 hour of program start time. There is also a unit-tested sliding average algorithm. 

### Completed Work
Set up Steps 
- Create Github repo and Make public for review and source control 
    - Create this doc
    - Create Works Cited
    - Create Dirs for data 
- Get Weather API Account Set up
    - Collect Sample Data to test with
- Create Works Cited 

- Evaluate and Transfer Provided Code (S) <br />
    [D] for Weather API <br />
    [D] for Earthquake <br />
    [D] for algo unit test <br />
[D] Write Sliding Average Algorithm <br />
[D] Incorporate Sliding Algo Unit Tests<br />
[D] Take basic user input for n and API Key (not hard coded) <br />
- Set up API Infrastructure (M)
    [D] For Weather (S)<br />
    [D] For Earthquake <br />
[D] Implement Data Structure for earthquake 
    - Store Name, Temp, timestamp, <br />

## Remaining Work for next Iteration

Hook up the Sliding Temperature Algorithm to the Main program [S]

Enable Constant Updates
- Add Web Hook or other mechanism to allow program to run until cancelled [M-L]
- Ensure the List of Earthquakes is updated regularly with every new entry [S]

Create simple Diagrams for Design elements [S]
- Sequence Diagram for API Interactions 
- Class diagram for the Earthquake data 
- Sliding average algorithm 

Improve Testing [M]
- Add Unit Tests for each of the Functions of the Main app
- Account for more edge cases 

Validate Input [S]
 
Refine Installation process for people who download it [M]

Quality and Robustness Considerations [M]
- Ensure Const Correctness for inputs to functions 
- Optimize for Scalabiltiy 



# Key for Estimates 
S = Small, 10 mins <br />
M = Med, 30 mins <br />
L = Large, 45-60mins or significant ramp up necessary <br />
[D] = Done, otherwise not done
